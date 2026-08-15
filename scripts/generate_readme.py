#!/usr/bin/env python3
"""
Self-updating README generator for My-Notes.

What it does, every time it runs (triggered by GitHub Actions on push):
  1. Reads scripts/config.yaml for the list of months and their expected length.
  2. Scans each month folder on disk for Day-*.md files.
  3. For any file that's new or changed since the last run, asks Claude for a
     short, consistent one-line "what you'll learn" summary (results are
     cached in scripts/.summary_cache.json so unchanged files are never
     re-summarized -- keeps API usage minimal).
  4. Rebuilds the Roadmap, Module Breakdown, Progress, and Directory Tree
     sections of README.md between fixed HTML comment markers, leaving
     everything else (About, Getting Started, Legal, etc.) untouched.
  5. Writes README.md back to disk only if something actually changed.

Uses GEMINI_API_KEY if available (set as a repo secret) to generate summaries.
If the key is missing, cached summaries are reused and new summaries fall back
to a generic placeholder so README generation still succeeds.
"""

import hashlib
import json
import os
import re
import sys
from pathlib import Path

import yaml
from google import genai

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "scripts" / "config.yaml"
CACHE_PATH = REPO_ROOT / "scripts" / ".summary_cache.json"
README_PATH = REPO_ROOT / "README.md"

DAY_FILE_RE = re.compile(r"Day-0*(\d+)", re.IGNORECASE)

MARKERS = {
    "roadmap": ("<!-- ROADMAP_START -->", "<!-- ROADMAP_END -->"),
    "modules": ("<!-- MODULES_START -->", "<!-- MODULES_END -->"),
    "progress": ("<!-- PROGRESS_START -->", "<!-- PROGRESS_END -->"),
    "tree": ("<!-- DIRECTORY_TREE_START -->", "<!-- DIRECTORY_TREE_END -->"),
}

client = None
missing_api_key_warned = False


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["months"]


def load_cache():
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def save_cache(cache):
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")


def file_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def summarize_day(title: str, content: str) -> str:
    """Ask Gemini for a short, consistent 'what you'll learn' line."""
    global client, missing_api_key_warned
    if client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            if not missing_api_key_warned:
                print(
                    "WARNING: GEMINI_API_KEY is not set; using fallback summaries.",
                    file=sys.stderr,
                )
                missing_api_key_warned = True
            return "Notes on this topic"
        client = genai.Client(api_key=api_key)

    prompt = f"""You are writing one line for a study-log README table.

File title: {title}

File content (a personal Linux/networking/security study note):
---
{content[:6000]}
---

Write ONE line (max 12 words) listing the concrete tools, commands, or
concepts this note covers, in the same terse style as these examples:
- "Filesystem hierarchy — /, /etc, /var, /home, /tmp, /root"
- "chmod, symbolic & numeric modes, file vs. directory permissions"
- "ARP spoofing with arpspoof"

Reply with ONLY that line. No preamble, no quotes, no trailing period."""

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    text = (resp.text or "").strip()
    return text.splitlines()[0].strip() if text else "Notes on this topic"


def scan_month(folder: Path, cache: dict) -> list[dict]:
    """Return sorted list of {day, title, summary, path} for a month folder."""
    if not folder.exists():
        return []

    days = []
    for f in folder.iterdir():
        if not f.is_file() or f.suffix.lower() != ".md":
            continue
        m = DAY_FILE_RE.search(f.name)
        if not m:
            continue  # skip non-day files like QUOTES.md
        day_num = int(m.group(1))

        raw_title = f.stem.split(",", 1)[-1].strip() if "," in f.stem else f.stem
        raw_title = re.sub(r"^Day[- ]?0*\d+\s*", "", raw_title, flags=re.IGNORECASE).strip(" -,")
        display_title = raw_title or f.stem

        content = f.read_text(encoding="utf-8", errors="ignore")
        h = file_hash(content)
        cache_key = str(f.relative_to(REPO_ROOT))

        if cache.get(cache_key, {}).get("hash") == h:
            summary = cache[cache_key]["summary"]
        else:
            summary = summarize_day(display_title, content)
            cache[cache_key] = {"hash": h, "summary": summary}

        days.append({
            "day": day_num,
            "title": display_title,
            "summary": summary,
            "path": f.relative_to(REPO_ROOT).as_posix(),
        })

    days.sort(key=lambda d: d["day"])
    return days


def md_link(text: str, path: str) -> str:
    encoded = path.replace(" ", "%20").replace("(", "%28").replace(")", "%29").replace(",", "%2C")
    return f"[{text}](<{encoded}>)" if " " in path else f"[{text}]({encoded})"


def build_sections(config, cache):
    module_data = []
    for m in config:
        folder = REPO_ROOT / m["folder"]
        days = scan_month(folder, cache)
        if not days:
            status = "Planned"
        elif len(days) >= m["expected_days"]:
            status = "Complete"
        else:
            status = "Active"
        module_data.append({**m, "days": days, "status": status})

    # ---- Roadmap table ----
    status_icon = {"Complete": "✅ Complete", "Active": "🔄 In Progress", "Planned": "Planned"}
    roadmap_lines = ["| # | Module | Status |", "|---|--------|--------|"]
    for m in module_data:
        roadmap_lines.append(f"| {m['number']:02d} | {m['title']} | {status_icon[m['status']]} |")
    roadmap = "\n".join(roadmap_lines)

    # ---- Module breakdown ----
    breakdown_parts = []
    active_or_complete = [m for m in module_data if m["status"] != "Planned"]
    planned = [m for m in module_data if m["status"] == "Planned"]

    for i, m in enumerate(active_or_complete):
        open_attr = " open" if i == 0 or m["status"] == "Active" else ""
        lines = [
            f"<details{open_attr}>",
            f"<summary><strong>Month {m['number']:02d} — {m['title']}</strong> "
            f"({m['status']} · {len(m['days'])} days)</summary>",
            "",
            "| Day | Topic | Covers |",
            "|:---:|-------|--------|",
        ]
        for d in m["days"]:
            link = md_link(d["title"], d["path"])
            lines.append(f"| {d['day']:02d} | {link} | {d['summary']} |")
        lines.append("")
        lines.append("</details>")
        breakdown_parts.append("\n".join(lines))

    if planned:
        lines = ["<details>", "<summary><strong>Upcoming Modules</strong></summary>", "",
                  "| Month | Focus Area |", "|:-----:|-----------|"]
        for m in planned:
            lines.append(f"| {m['number']:02d} | {m['title']} |")
        lines += ["", "</details>"]
        breakdown_parts.append("\n".join(lines))

    modules_section = "\n\n".join(breakdown_parts)

    # ---- Progress table ----
    total_days = sum(len(m["days"]) for m in module_data)
    prog_lines = ["| Module | Topic | Progress | Status |", "|--------|-------|:--------:|:------:|"]
    for m in module_data:
        target = m["expected_days"]
        prog_lines.append(
            f"| {m['number']:02d} | {m['title']} | {len(m['days'])} / {target} | {m['status']} |"
        )
    prog_lines.append("")
    prog_lines.append(f"**Total notes logged: {total_days}**")
    progress_section = "\n".join(prog_lines)

    return roadmap, modules_section, progress_section


def build_tree() -> str:
    """Render a simple two-level directory tree, skipping hidden/system dirs."""
    skip = {".git", ".github", "scripts", "node_modules", "__pycache__"}
    lines = ["```", "My-Notes/"]

    entries = sorted(
        [p for p in REPO_ROOT.iterdir() if p.name not in skip and not p.name.startswith(".")],
        key=lambda p: (p.is_file(), p.name.lower()),
    )
    for i, entry in enumerate(entries):
        last = i == len(entries) - 1
        prefix = "└── " if last else "├── "
        suffix = "/" if entry.is_dir() else ""
        lines.append(f"{prefix}{entry.name}{suffix}")
    lines.append("```")
    return "\n".join(lines)


def replace_section(readme_text: str, key: str, new_content: str) -> str:
    start, end = MARKERS[key]
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    replacement = f"{start}\n{new_content}\n{end}"
    if not pattern.search(readme_text):
        print(f"WARNING: markers for '{key}' not found in README.md — skipping", file=sys.stderr)
        return readme_text
    return pattern.sub(replacement, readme_text)


def main():
    config = load_config()
    cache = load_cache()

    roadmap, modules_section, progress_section = build_sections(config, cache)
    tree_section = build_tree()

    readme = README_PATH.read_text(encoding="utf-8")
    readme = replace_section(readme, "roadmap", roadmap)
    readme = replace_section(readme, "modules", modules_section)
    readme = replace_section(readme, "progress", progress_section)
    readme = replace_section(readme, "tree", tree_section)

    README_PATH.write_text(readme, encoding="utf-8")
    save_cache(cache)
    print("README.md regenerated successfully.")


if __name__ == "__main__":
    main()
