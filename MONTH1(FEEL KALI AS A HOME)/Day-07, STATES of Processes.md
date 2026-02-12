# 🔄 Day 7: Process States

![Linux](https://img.shields.io/badge/Linux-States-success?style=for-the-badge)
![Kali](https://img.shields.io/badge/Kali-Core-critical?style=for-the-badge)

> _State is just a snapshot of a process at a moment._ 📸

---

## 🧊 The 4 Main Process States

| State | Name          | Description                                                      |
| :---: | :------------ | :--------------------------------------------------------------- |
| **R** | **Running**   | The process is running or ready to run.                          |
| **S** | **Sleeping**  | Waiting for an event or I/O. (Very common).                      |
| **T** | **Stopped**   | Suspended by a signal like **SIGSTOP** or **SIGSTP** (`Ctrl+Z`). |
| **Z** | **Zombie** 🧟 | Finished execution but still in the process table.               |

> **Zombie Example:** A person has passed away, but their official records still show them as "Alive" because the death certificate hasn't been processed. The record exists, but the entity is gone. ☠️

---

## 🔗 States & Signals

Signals change the state of a process. Here is the relationship:

| SIGNAL      | Effect / New State                |
| :---------- | :-------------------------------- |
| **SIGINT**  | **Gone** (Stopped & Cleared)      |
| **SIGTERM** | **Gone** (Polite Stop)            |
| **SIGSTP**  | **T** (Stopped/Paused)            |
| **SIGSTOP** | **T** (Stopped/Paused)            |
| **SIGCONT** | **R** or **S** (Running/Sleeping) |
| **SIGKILL** | **Gone** (Forced Kill)            |

> **Note:**
>
> - `S+`: **Foreground** Sleeping (Process is running in the foreground).
> - `S`: **Background** Sleeping (Process is running in the background).
> - The `+` sign indicates **Foreground** processes.

---

## 🎮 Practice Scenarios

1.  **Open Terminal:** Open your terminal in Kali.
2.  **Split Terminal:** Use `Ctrl + Shift + R` (or your shortcut).
3.  **Start Process:**
    In the left terminal:
    ```bash
    sleep 500
    ```
4.  **Check State:**
    In the right terminal:
    ```bash
    ps aux | grep "sleep 500"
    ```
    _You should see `S+` (Sleeping + Foreground)._
5.  **Background It:**
    Pause (`Ctrl + Z`) and send to background (`bg`).
6.  **Check State Again:**
    Run the `ps` command again.
    _You will now see `S` (Sleeping, no `+`)._
7.  **Stop It:**
    Send a `SIGSTOP` to the PID.
8.  **Final Check:**
    Check status again. You should see **T** (Stopped).

---

<div align="center">

**[⬅️ Day 6: Processes & Signals](./Day-6,%20...continue%20Processes,%20New%20Topic%20Signals.md)** • **[Day 8: Services ➡️](./Day-08,%20SERVICES.md)**

</div>
