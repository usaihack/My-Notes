# ⚡ Day 2: Shortcuts & Basic Commands

![Shortcuts](https://img.shields.io/badge/Productivity-Maximum-orange?style=for-the-badge)
![Linux Skills](https://img.shields.io/badge/Skills-Essential-blue?style=for-the-badge)

> _Mastering shortcuts and core commands is the key to velocity in the terminal. Navigate like a pro!_ 🚀

---

## 🎹 Keyboard Shortcuts

_These shortcuts will save you hours of typing over your career._

| Key Combo              | Action              | Mnemonic                               |
| :--------------------- | :------------------ | :------------------------------------- |
| **`Ctrl + L`**         | **Clear Screen**    | Same as `clear` command (Clean Slate). |
| **`Ctrl + A`**         | **Start of Line**   | **A**lpha (Beginning).                 |
| **`Ctrl + E`**         | **End of Line**     | **E**nd.                               |
| **`Ctrl + K`**         | **Delete to End**   | **K**ill from cursor to end.           |
| **`Ctrl + U`**         | **Delete to Start** | **U**ndo entire line (cut).            |
| **`Ctrl + Shift + T`** | **New Tab**         | **T**ab.                               |
| **`Ctrl + Shift + R`** | **Split Terminal**  | **R**ight? (Maybe right split).        |
| **`Ctrl + Shift + E`** | **Close Split**     | **E**xit split.                        |

---

## 🛠️ Essential Commands

_The bread and butter of Linux navigation and file manipulation._

### 📂 Navigation & Listing

| Command     | Description                                      | Example |
| :---------- | :----------------------------------------------- | :------ |
| **`pwd`**   | **Print Working Directory** - Where am I?        | `pwd`   |
| **`ls`**    | **List** files and folders.                      | `ls`    |
| **`ls -a`** | List **all** (including hidden `.` files).       | `ls -a` |
| **`ls -l`** | List **long** format (permissions, size, owner). | `ls -l` |

### 📁 File & Directory Management

| Command     | Description                           | Power User Tip                                         |
| :---------- | :------------------------------------ | :----------------------------------------------------- |
| **`mkdir`** | **Make Directory**.                   | Use `mkdir -p a/b/c` to create nested folders at once. |
| **`touch`** | Create an empty file.                 | `touch notes.txt`                                      |
| **`cp`**    | **Copy** files usually.               | `cp file.txt backup.txt`                               |
| **`cp -r`** | Copy directories (**Recursive**).     | `cp -r folder/ copy_folder/`                           |
| **`mv`**    | **Move** or **Rename** files/folders. | `mv old.txt new.txt` (Rename)                          |
| **`rm`**    | **Remove** files.                     | `rm junk.txt`                                          |
| **`rm -r`** | Remove directory (**Recursive**).     | `rm -rf dangerous_folder/` (Careful!)                  |

### 📝 Reading & Editing

| Command    | Description                               | Usage                                     |
| :--------- | :---------------------------------------- | :---------------------------------------- |
| **`cat`**  | **Concatenate** and display file content. | `cat file.txt`                            |
| **`head`** | Show first 10 lines.                      | `head large_log.txt`                      |
| **`tail`** | Show last 10 lines.                       | `tail error_log.txt`                      |
| **`less`** | Scroll through large files page by page.  | `less giant_file.txt` (Press `q` to quit) |
| **`nano`** | Simple terminal text editor.              | `nano config.conf`                        |

---

## 🔗 Chaining & Redirection

_Combine commands to build powerful workflows._

### 1. The Pipe `|`

Take the output of the first command and feed it as input to the second.

```bash
ls -la | grep "txt"
# Lists all files, then filters only lines containing "txt"
```

### 2. The Chain `&&`

Run the second command only if the first succeeds.

```bash
mkdir project && cd project
# Creates directory "project" and enters it immediately
```

### 3. Output Redirection `>` & `>>`

```bash
echo "Hello World" > file.txt   # Overwrites file.txt
echo "New Line" >> file.txt     # Appends to file.txt
```

---

<div align="center">

**[⬅️ Day 1: Directories](./Day-1,%20Directories.md)** • **[Day 3: Permissions ➡️](./Day-3,%20Permissions.md)**

</div>
