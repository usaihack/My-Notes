# 🔍 Day 21: SMB Enumeration

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![TryHackMe](https://img.shields.io/badge/TryHackMe-Lab-red?style=for-the-badge)
![SMB](https://img.shields.io/badge/SMB-Enumeration-orange?style=for-the-badge)

> _Enumeration is the key to the kingdom. In this lab, we dive deep into the SMB protocol to discover hidden shares, users, and potential entry points._ 🛡️

---

## 🛠️ 1. Initial Reconnaissance: `enum4linux`

The first step was running a full scan using `enum4linux` to see what the target machine was hiding.

**Command Structure:** `enum4linux [OPTIONS] [IP]`

### 📊 Common `enum4linux` Flags

|**Tag**|**Function**|
|---|---|
|**-U**|Get userlist|
|**-M**|Get machine list|
|**-N**|Get namelist dump (different from -U and -M)|
|**-S**|Get sharelist|
|**-P**|Get password policy information|
|**-G**|Get group and member list|
|**-a**|**All of the above** (full basic enumeration)|

**My Action:** I ran `enum4linux -a 10.113.134.237` and found these key details:

- **Machine Name:** Found under "`Nbtstat Information`" (e.g., `POLOSMB`).
    
- **Workgroup:** A named group of users sharing files on the network.
    
- **OS Information:** Details about the target's operating system version.
    
- **Share Enumeration:** This showed the shared files/folders. Finding a "Disk" label here is a goldmine.
    

---

---

## 📂 2. Accessing the Share: `smbclient`

To enter the shared folders, we need a client. Linux uses `smbclient`. You need the IP, the Share name, a Username, and the Port.

**Basic Syntax:**

`smbclient //[IP]/[SHARE] -U [USERNAME] -p [PORT]`

**My Action in THM:**

I connected successfully without a password using:

`smbclient //10.113.134.237/profiles -U cactus -p 445`

### 🔍 Understanding File Attributes

Inside the share, I noticed letters next to the files. These are important:

- **D:** Directory (Folder).
    
- **H:** Hidden (Usually starts with a `.`).
    
- **DH:** A Hidden Directory (Like a secret room).
    

---

---

> **Note:** This exploration is continued in the next session.

---

<div align="center">

**[⬅️ Day 20: SMB](./Day-20,%20SMB.md) | [🏠 Home](../README.md) | [Day 22: continue SMB Enumeration ➡️](./Day-22,%20continue%20SMB%20Enumeration.md)**

</div>
