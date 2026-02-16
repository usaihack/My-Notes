# 📂 Day 1: Linux Directory Structure

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Kali](https://img.shields.io/badge/Kali-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)
![Beginner Friendly](https://img.shields.io/badge/Skill_Level-Beginner-success?style=for-the-badge)

> - Understanding the **Linux File System** is like learning the map of a new city. Everything in Linux is a file, and every file has a place.\*

---

## 🌳 The Linux Directory Tree

In Linux, everything starts from the **Root** (`/`). It's the base of the tree from which all other directories branch out.

```mermaid
graph TD
    Root["/ (Root)"] --> Home["/home"]
    Root --> Etc["/etc"]
    Root --> Var["/var"]
    Root --> Bin["/bin"]
    Root --> Tmp["/tmp"]
    Root --> RootHome["/root"]
    Home --> User["~ (User Home)"]

    style Root fill:#f9f,stroke:#333,stroke-width:2px
    style Home fill:#bbf,stroke:#333
    style Etc fill:#bfb,stroke:#333
```

---

## 🗺️ Key Directories Explained

| Directory           | Symbol  | Description                                                                      |
| :------------------ | :-----: | :------------------------------------------------------------------------------- |
| **Root**            |   `/`   | The starting point of the filesystem. The "God" directory containing everything. |
| **User Home**       | `/home` | Contains personal directories for users (e.g., `/home/usman`).                   |
| **Home Shortcut**   |   `~`   | A quick shortcut to the current user's home (e.g., `cd ~` takes you home).       |
| **Super User Home** | `/root` | The private home directory for the System Administrator (Root user).             |
| **Binaries**        | `/bin`  | The **Toolbox**. Contains essential commands like `ls`, `cp`, `cat`.             |
| **Variables**       | `/var`  | Stores changing data like system logs (`/var/log`).                              |
| **Temporary**       | `/tmp`  | Scratchpad space. Files here are often deleted on reboot.                        |

---

## ⚙️ The Configuration Hub: `/etc`

> 🕵️ **Hacker's Note:** This directory is a goldmine for understanding how a system is configured.

The `/etc` directory acts as the system's **Rule Book**. It controls who can do what, network settings, and startup scripts.

### 🔑 Critical Files in `/etc`

1. **`/etc/passwd`**  
   📝 _List of all users on the system._
2. **`/etc/shadow`**  
   🔐 _Stores hashed passwords (highly sensitive)._
3. **`/etc/sudoers`**  
   🛡️ _The definition of "Who can be Admin". Controls `sudo` privileges._

---

<div align="center">

**[Next Checkpoint: Day 2 - Shortcuts & Commands ➡️](./Day-2%20Shortcuts%20and%20Basic%20Commands.md)**

</div>
