# ⚙️ Day 5: Understanding Linux Processes

![Processes](https://img.shields.io/badge/Processes-Active-critical?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Internal-success?style=for-the-badge)

> _A program is static code. A process is that code in action!_ 🚀

---

## 🧠 Program vs. Process

| Term           | Definition                                   | State                        |
| :------------- | :------------------------------------------- | :--------------------------- |
| **Program** 📄 | An executable file stored on the disk.       | **Passive** (Doing nothing)  |
| **Process** 🏃 | A program currently running in memory (RAM). | **Active** (Executing tasks) |

Every active **Process** has unique identifiers:

1.  **PID:** Process ID (Unique number).
2.  **USER:** Who started it.
3.  **%CPU:** Processor usage.
4.  **%MEM:** Memory usage.
5.  **COMMAND:** The command that started it.

---

## 📚 Key Terminologies

Before we dive into commands, let's clear up some terms:

### 1️⃣ Terminal vs. Shell

- **Terminal:** The window/interface where you type.
- **Shell:** The program interpreting your commands.

### 2️⃣ Foreground vs. Background

- **Foreground:** Interactive processes (occupy your terminal).
- **Background:** Runs silently behind the scenes.

---

## 🕵️‍♂️ Viewing Processes: `ps` & `ps aux`

### 1. Basic View (`ps`)

Shows _only_ processes running in the current shell session.

```bash
ps
# Output shows very few processes (usually just bash and ps itself)
```

### 2. Detailed View (`ps aux`)

The gold standard for viewing system activity.

```bash
ps aux
# Shows ALL processes from ALL users
```

**Flags Breakdown:**

- **`a`**: All users' processes.
- **`u`**: Display user/owner information.
- **`x`**: Include processes not attached to a terminal (background/daemons).

---

## 📊 Monitoring Live: Task Manager Style

Want to see what's creating load in real-time?

### 1. The Classic: `top`

Updates in real-time.

```bash
top
# Press 'q' to quit
```

### 2. The Modern: `htop`

Colorful, interactive, and user-friendly. You can even use your mouse! 🖱️

```bash
htop
# A visual upgrade to top
```

---

## 🔐 Processes & Ownership

Who controls the process?

> **Rule:** You can only kill or manage processes you own (unless you represent the "Bank", i.e., root).

- **`kali` (User):** Can control/kill processes owned by `kali`.
- **`root` (Admin):** Can control **ANY** process.
- **Other Users:** Cannot touch your processes.

---

<div align="center">

**[⬅️ Day 4: File Ownership](./Day-4,%20Ownerships.md)** • **[Day 6: Processes and Signals ➡️](./Day-6,%20Continue%20Processes,%20New%20Topic%20Signals.md)**

</div>
