#!/usr/bin/env python3
"""
Self-updating README generator for My-Notes.

What it does on every push (via GitHub Actions):
  1. Reads scripts/config.yaml for module configurations.
  2. Scans each month folder on disk for Day-*.md study notes.
  3. Automatically computes status:
     - Previous months with notes are automatically marked 'Complete' when a new month is active.
     - Current highest month with notes is 'In Progress' (or 'Complete' if reaching expected days).
     - Months without notes are marked 'Planned'.
  4. Generates/updates summaries using Google Gemini API (cached in scripts/.summary_cache.json).
  5. Rebuilds Roadmap, Module Breakdown tables, Progress stats, and Directory Tree.
  6. Writes README.md back to disk cleanly.
"""

import hashlib
import json
import os
import re
import sys
from pathlib import Path

import yaml

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


def get_gemini_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        from google import genai
        return genai.Client()
    except Exception as e:
        print(f"Notice: Unable to initialize Gemini client ({e}). Using local extractor fallback.", file=sys.stderr)
        return None


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["months"]


def load_cache():
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(cache):
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")


def file_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def extract_smart_fallback(title: str, content: str) -> str:
    """Intelligent fallback summary generator from file content when API is unavailable."""
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    
    # 1. Look for bold key concepts or bullet points
    concepts = []
    for line in lines:
        if line.startswith("- **") or line.startswith("* **"):
            m = re.match(r"^[-*]\s*\*\*([^*]+)\*\*", line)
            if m:
                concept_name = m.group(1).strip(": ")
                if len(concept_name) < 40:
                    concepts.append(concept_name)
    
    if len(concepts) >= 2:
        return f"{', '.join(concepts[:3])} — core concepts & hands-on application"
    
    # 2. Look for section headers (H2/H3)
    headers = []
    for line in lines:
        if line.startswith("## ") or line.startswith("### "):
            h_text = line.lstrip("#").strip()
            if h_text.lower() not in {"summary", "overview", "introduction", "conclusion", "notes", "assignment"}:
                headers.append(h_text)
    
    if headers:
        return f"{', '.join(headers[:3])} — practical concepts & command analysis"
    
    # 3. Clean sentence fallback
    for line in lines:
        if not line.startswith("#") and not line.startswith("---") and not line.startswith(">") and len(line) > 20:
            clean = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", line)  # remove markdown links
            clean = re.sub(r"[`*_]", "", clean)
            return clean[:90].rstrip(".") + "..."
            
    return f"{title} notes and practical lab exercises"


def summarize_day(client, title: str, content: str) -> str:
    """Ask Gemini for a short, high-impact 'Key Concepts & Hands-on Focus' summary line."""
    if not client:
        return extract_smart_fallback(title, content)
        
    prompt = f"""You are writing a concise summary for an Ethical Hacking & Cybersecurity study portfolio README table.

File Title: {title}

File Content (Hands-on study note):
---
{content[:6000]}
---

Write ONE concise line (max 12 words) summarizing the core tools, commands, protocols, or security concepts covered.
Focus on actionable technical terms. 
Style examples:
- "Filesystem hierarchy, /, /etc, /var, /home, and path navigation"
- "chmod, symbolic & numeric modes, SUID/SGID, and permission auditing"
- "ARP protocol architecture, table inspection, and spoofing with arpspoof"

Reply with ONLY the summary line. No preamble, no quotes, no period."""

    try:
        resp = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        text = (resp.text or "").strip()
        if text:
            first_line = text.splitlines()[0].strip().strip('"\'')
            return first_line
    except Exception as e:
        print(f"Warning: Gemini API call failed ({e}). Falling back to local extractor.", file=sys.stderr)
    
    return extract_smart_fallback(title, content)


def scan_month(client, folder: Path, cache: dict) -> list[dict]:
    """Return sorted list of {day, title, summary, path} for a month folder."""
    if not folder.exists():
        return []

    days = []
    for f in folder.iterdir():
        if not f.is_file() or f.suffix.lower() != ".md":
            continue
        m = DAY_FILE_RE.search(f.name)
        if not m:
            continue
        day_num = int(m.group(1))

        raw_title = f.stem.split(",", 1)[-1].strip() if "," in f.stem else f.stem
        raw_title = re.sub(r"^Day[- ]?0*\d+\s*", "", raw_title, flags=re.IGNORECASE).strip(" -,")
        display_title = raw_title or f.stem

        content = f.read_text(encoding="utf-8", errors="ignore")
        h = file_hash(content)
        cache_key = str(f.relative_to(REPO_ROOT))

        if cache.get(cache_key, {}).get("hash") == h and "summary" in cache[cache_key]:
            summary = cache[cache_key]["summary"]
        else:
            summary = summarize_day(client, display_title, content)
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
    return f"[{text}]({encoded})"


def build_sections(config, cache, client):
    month_scans = []
    for m in config:
        folder = REPO_ROOT / m["folder"]
        days = scan_month(client, folder, cache)
        month_scans.append({**m, "days": days})

    # Find highest month number that has notes
    months_with_notes = [m["number"] for m in month_scans if m["days"]]
    max_active_month_num = max(months_with_notes) if months_with_notes else 0

    module_data = []
    for m in month_scans:
        num = m["number"]
        days_count = len(m["days"])
        target_days = m["expected_days"]

        if not m["days"]:
            status = "Planned"
        elif num < max_active_month_num:
            # Any lower month with notes is automatically marked Complete when a newer month starts!
            status = "Complete"
        elif num == max_active_month_num:
            if days_count >= target_days:
                status = "Complete"
            else:
                status = "Active"
        else:
            status = "Planned"

        module_data.append({**m, "status": status})

    # ---- Roadmap table ----
    status_icon = {"Complete": "✅ Complete", "Active": "🔄 In Progress", "Planned": "📋 Planned"}
    roadmap_lines = ["| # | Module | Status | Notes Logged |", "|---|--------|:------:|:------------:|"]
    for m in module_data:
        logged = f"{len(m['days'])} days" if m['days'] else "-"
        roadmap_lines.append(f"| {m['number']:02d} | {m['title']} | {status_icon[m['status']]} | {logged} |")
    roadmap = "\n".join(roadmap_lines)

    # ---- Module breakdown ----
    breakdown_parts = []
    active_or_complete = [m for m in module_data if m["status"] != "Planned"]
    planned = [m for m in module_data if m["status"] == "Planned"]

    for i, m in enumerate(active_or_complete):
        open_attr = " open" if m["status"] == "Active" or i == len(active_or_complete) - 1 else ""
        lines = [
            f"<details{open_attr}>",
            f"<summary><strong>Month {m['number']:02d} — {m['title']}</strong> "
            f"({status_icon[m['status']]} · {len(m['days'])} Days Logged)</summary>",
            "",
            "| Day | Topic | Key Concepts & Hands-on Focus |",
            "|:---:|-------|-------------------------------|",
        ]
        for d in m["days"]:
            link = md_link(d["title"], d["path"])
            lines.append(f"| Day {d['day']:02d} | {link} | {d['summary']} |")
        lines.append("")
        lines.append("</details>")
        breakdown_parts.append("\n".join(lines))

    if planned:
        lines = [
            "<details>",
            "<summary><strong>Upcoming Curriculum Modules (Months 03–18)</strong></summary>",
            "",
            "| Month | Focus Area | Status |",
            "|:-----:|-----------|:------:|",
        ]
        for m in planned:
            lines.append(f"| {m['number']:02d} | {m['title']} | 📋 Planned |")
        lines += ["", "</details>"]
        breakdown_parts.append("\n".join(lines))

    modules_section = "\n\n".join(breakdown_parts)

    # ---- Progress table ----
    total_days = sum(len(m["days"]) for m in module_data)
    total_modules_completed = sum(1 for m in module_data if m["status"] == "Complete")
    prog_lines = [
        "| Metric | Count | Details |",
        "|--------|:-----:|---------|",
        f"| **Modules Completed** | `{total_modules_completed} / {len(module_data)}` | Full monthly study blocks finished |",
        f"| **Total Study Notes** | `{total_days}` | Structured Markdown notes with terminal logs |",
        f"| **Current Focus Module** | `Month {max_active_month_num:02d}` | Active focus domain |",
    ]
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
    client = get_gemini_client()

    roadmap, modules_section, progress_section = build_sections(config, cache, client)
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
