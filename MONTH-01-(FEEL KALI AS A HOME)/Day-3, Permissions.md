# 🔐 Day 3: File Permissions & Security

![Security](https://img.shields.io/badge/Security-Critical-red?style=for-the-badge&logo=lock)
![Linux](https://img.shields.io/badge/Linux-Admin-success?style=for-the-badge)

> _In Linux, every file is owned by someone. Understanding who can touch your files is the first line of defense._

---

## 👥 The Three Identities

Who are we talking about when we say "Permissions"?

|   Key   | Identity         | Description                                           |
| :-----: | :--------------- | :---------------------------------------------------- |
| **`u`** | **User (Owner)** | The creator of the file. Usually has the most power.  |
| **`g`** | **Group**        | A collection of users (e.g., `developers`, `admins`). |
| **`o`** | **Others**       | Everyone else on the system (The Public).             |

---

## 🚦 The Three Permissions

What can they do?

| Symbol  |   Action    | Description                                        | Numeric Value |
| :-----: | :---------: | :------------------------------------------------- | :-----------: |
| **`r`** |  **Read**   | View file contents / List directory contents.      |     **4**     |
| **`w`** |  **Write**  | Modify file / Create or Delete files in directory. |     **2**     |
| **`x`** | **Execute** | Run file as program / Enter directory.             |     **1**     |

> **💡 Quick Math:**
>
> - `rwx` = 4 + 2 + 1 = **7** (Full Permissions)
> - `rw-` = 4 + 2 = **6** (Read & Write)
> - `r-x` = 4 + 1 = **5** (Read & Execute)

---

## 🛠️ Changing Permissions: `chmod`

The command `chmod` (Change Mode) is used to set these rules.

### 📝 Method 1: Symbolic Mode

Use `+` to add, `-` to remove.

```bash
chmod u+rwx filename
# Gives User (u) Read, Write, and Execute permissions.

chmod g-wx filename
# Removes Write and Execute permissions from Group (g).
```

### 🔢 Method 2: Numeric Mode (The Pro Way)

Set all permissions at once using the sum of values for User, Group, and Others.

```bash
chmod 755 filename
# User (7) = r+w+x (4+2+1)
# Group (5) = r+x   (4+1)
# Others (5)= r+x   (4+1)
```

---

## 📂 Directories vs. Files

Permissions behave slightly differently for folders.

| Permission        | For a File 📄            | For a Directory 📁              |
| :---------------- | :----------------------- | :------------------------------ |
| **Read (`r`)**    | See the content text.    | List files inside (`ls`).       |
| **Write (`w`)**   | Edit the content text.   | Create or Delete files inside.  |
| **Execute (`x`)** | Run as a script/program. | **Enter the directory (`cd`).** |

### ⚠️ The "Bucket" Analogy

> **Why do I need `x` to list files?**
>
> Think of a directory as a **Bucket**.
>
> - **`x` (Execute):** Allows you to _look inside_ or _step into_ the bucket.
> - **`w` (Write):** Allows you to _put things in_ or _take things out_.
>
> **Crucially:** You cannot put things in (`w`) if you cannot even reach inside (`x`).
> _Without `x`, `w` is useless for a directory._

---

<div align="center">

**[⬅️ Day 2: Shortcuts](./Day-2%20Shortcuts%20and%20Basic%20Commands.md)** • **[Day 4: Ownership ➡️](./Day-4,%20Ownerships.md)**

</div>
