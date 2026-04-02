# 🔍 Day 22: SMB Enumeration (Continued)

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Exploitation](https://img.shields.io/badge/Exploitation-Success-green?style=for-the-badge)
![SSH](https://img.shields.io/badge/SSH-Access-lightgrey?style=for-the-badge)

> _The hunt continues. From a simple file share to a full system compromise, this session demonstrates the power of persistence and lateral movement._ 🚩

---

## 🔑 3. The SSH Key Discovery

Inside the share, I found a text file mentioning that **John Cactus** has office timings on SSH. I found a hidden directory called `.ssh`.

- **The Vulnerability:** Most directories kicked me out when I tried to `cd` into them, but `.ssh` allowed me in!
    
- **The Prize:** Inside, I found a **public key** (`id_rsa.pub`) and a **private key** (`id_rsa`). I downloaded both.
    

---

---

## 💻 4. Connecting via SSH

After exiting the SMB client, I had to prepare the private key for the connection.

### Step A: Changing Permissions

I ran `chmod 600 id_rsa`.

- **Why?** SSH is very strict. It will not allow you to use a private key if it is "shared openly" (meaning other users on your computer can read it). `600` makes it private to only you.
    

### Step B: The Connection

I used the `-i` flag to tell SSH to use my downloaded private key instead of a password.

**Command:**

`ssh -i id_rsa cactus@[TARGET_IP]`

> **Note:** We always use the **private key** for the connection. The username `cactus` was found inside the public key file earlier.

---

---

## 🚩 The Final Result

**Boom!** The connection was successful. Once inside the server, I found the file, used the `cat` command to read it, and obtained the **FLAG** 🚩.

---

<div align="center">

**[⬅️ Day 21: SMB Enumeration (26,27-March-2026)](./Day-21,%20SMB%20Enumeration%20(26,27-March-2026).md) | [🏠 Home](../README.md) | [Day 23: SMTP ➡️](./Day-23,%20SMTP.md)**

</div>
