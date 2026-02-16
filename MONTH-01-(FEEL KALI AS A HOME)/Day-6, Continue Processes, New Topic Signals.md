# 🚦 Day 6: Processes & Signals

![Linux](https://img.shields.io/badge/Linux-Signals-success?style=for-the-badge)
![Kali](https://img.shields.io/badge/Kali-Processes-critical?style=for-the-badge)

> _Signals are just signals, not rocket science!_ 📡

---

## 🎯 Today's Practice Task

Here you will learn killing a process, sending it to the background, and bringing it back to the foreground.

### 1️⃣ Creating a Dummy Process

1.  Create a task using `sleep`:

    ```bash
    sleep 100
    ```

    - `sleep` in Kali is used to pause the terminal for a specific time (100 seconds here).
    - It is used here for **Processes** learning.

---

## 💀 Killing the Process

1.  **Pause the Process:** Press `Ctrl + Z` or open a split terminal/new tab.
2.  **Find the PID:**
    ```bash
    ps
    # OR
    ps aux | grep sleep
    ```
    Pick the PID of the `sleep 100` command.
3.  **Kill it:**
    ```bash
    kill PID
    ```
    The process `sleep 100` will be ended completely.
4.  **Force Kill (if needed):**
    If `kill PID` failed, use:
    ```bash
    kill -9 PID
    ```
    The `-9` flag sends a **force kill** signal.

---

## 🔙 Background & Foreground

### Sending to Background

1.  **Pause the process** (as discussed above).
2.  **Find the Job Number:**
    ```bash
    jobs
    ```
    Note the number in square brackets (e.g., `[1]`).
3.  **Send to Background:**
    ```bash
    bg %1
    ```
    _(Replace `1` with your job number. The `%` is mandatory)._

### Bringing to Foreground

1.  **Bring Back:**
    ```bash
    fg %1
    ```

> **Remember:**
>
> - `bg` and `fg` always work in the same terminal where the process was initiated.
> - Some processes (like network scanners) continue counting time when suspended, while others (like text editors) do not.

---

## 📡 What are SIGNALS?

Imagine a worker and a boss. The boss might stop him from working, or say to continue his work. **SIGNAL** is the message, while the **processes** are the workers.

View all signals with:

```bash
kill -l
```

### 🔑 Important Signals

#### 1. SIGINT (2): `Ctrl + C`

- **Interrupt Signal.**
- Usage: Stops a process manually.
- Catchable: Yes (Program can ask "Are you sure?").

#### 2. SIGTERM (15): Request Stop

- **Termination Signal.**
- Usage: A polite request to stop. Default for `kill PID`.
- Catchable: Yes.

**Difference between SIGINT and SIGTERM:**

| Feature           | SIGINT          | SIGTERM         |
| :---------------- | :-------------- | :-------------- |
| **Signal Number** | 2               | 15              |
| **Shortcut**      | `Ctrl + C`      | None            |
| **Source**        | User (Keyboard) | System/Programs |
| **Nature**        | Interrupt       | Polite Stop     |

#### 3. SIGKILL (9): Forced Kill

- **Kill Signal.**
- Usage: Forcefully kills the process. Use sparingly to avoid corruption.
- Catchable: **NO**.

#### 4. SIGSTP (20): Pause (Soft)

- **Stop Signal (Terminal).**
- Usage: `Ctrl + Z`. Pauses/suspends the process.
- Catchable: Yes.

#### 5. SIGSTOP (19): Pause (Hard)

- **Stop Signal.**
- Usage: Pauses process strictly.
- Catchable: **NO**.

**Difference between SIGSTP and SIGSTOP:**

| Feature           | SIGSTP     | SIGSTOP |
| :---------------- | :--------- | :------ |
| **Signal Number** | 20         | 19      |
| **Shortcut**      | `Ctrl + Z` | None    |
| **Catchable**     | Yes        | **No**  |

#### 6. SIGCONT (18): Continue

- **Continue Signal.**
- Usage: Resumes a paused/suspended job.

---

## 📝 Quick Summary of SIGNALS

| Signal      | Code | Shortcut   | Catchable? | Purpose                     |
| :---------- | :--- | :--------- | :--------- | :-------------------------- |
| **SIGINT**  | 2    | `Ctrl + C` | Yes        | Interrupt process (User).   |
| **SIGTERM** | 15   | ---        | Yes        | Polite termination request. |
| **SIGSTOP** | 19   | ---        | **No**     | Strict suspension/freeze.   |
| **SIGSTP**  | 20   | `Ctrl + Z` | Yes        | Suspend/freeze (Terminal).  |
| **SIGCONT** | 18   | ---        | N/A        | Resume a suspended process. |
| **SIGKILL** | 9    | ---        | **No**     | Forcefully kill a process.  |

> **Catchable meaning:** The program can intercept the signal (e.g., "Do you want to save your work?") before closing.

---

## 🛠️ How to use SIGNALS

Format:

```bash
kill -SignalNumber PID
# OR
kill -SignalName PID
```

**Example:**

```bash
kill -9 1234
```

> **IMPORTANT:**
> If you start `sleep 500`, suspend it, and interpret it via `SIGCONT` in a different way, it might resume in the background.

---

<div align="center">

**[⬅️ Day 5: Processes](./Day-5,%20Processes.md)** • **[Day 7: States of Processes ➡️](./Day-07,%20STATES%20of%20Processes.md)**

</div>
