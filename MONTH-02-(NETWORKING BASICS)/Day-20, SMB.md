# 📁 Day 20: SMB (Server Message Block)

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Windows](https://img.shields.io/badge/Windows-Service-blue?style=for-the-badge)
![SMB](https://img.shields.io/badge/SMB-File--Sharing-orange?style=for-the-badge)

> _SMB is the "Digital Delivery Truck" of the network. It’s how computers share files, printers, and serial ports within a LAN._ 📁

---

## 🏗️ 1. Introduction to SMB

The **Server Message Block (SMB)** is a client-server communication protocol used for sharing access to files, printers, and serial ports on a network.

- **Primary Use:** Shared folders (copy/paste) and printers within a Local Area Network (LAN).
    
- **Origin:** Originally developed by IBM in the 1980s; later acquired and evolved by Microsoft.
    
- **Network Ports:**
    
    - **Legacy:** Used NetBIOS ports **137, 138, 139**.
        
    - **Modern (Direct):** Uses **Port 445** (Standard).
        
    - **Advanced:** Uses **Port 443** only when using **SMB over QUIC** (for secure internet access).
        
---
---

## 📜 2. Version History & Security

|**Version**|**Released With**|**Security Status**|
|---|---|---|
|**SMB 1.0**|Windows 2000 / XP|**Critical Risk.** No encryption. Vulnerable to **WannaCry**.|
|**SMB 2.x**|Windows Vista / 7|Faster, more efficient, and introduced basic signing.|
|**SMB 3.x**|Windows 8 / 10 / 11|**Secure.** Supports **End-to-End Encryption**.|

---

---

## 🤝 3. The Connection Mechanism (The 4-Phase Handshake)

A standard SMB connection is established through a request-response cycle.

#### ***Phase 1: Negotiation (The Handshake)***

- **Negotiate Protocol Request:** The client sends a list of its supported SMB versions (e.g., 1.0, 2.1, 3.1.1).
    
- **Negotiate Protocol Response:** The server selects the highest version both machines have in common.
    

#### ***Phase 2: Session Setup (The ID Check)***

- **Session Setup Request:** The client sends credentials (usually an **NTLM hash** or **Kerberos ticket**).
    
- **Session Setup Response:** The server validates the ID against its database. If successful, it issues a **Session ID** (the "Visitor Badge") for all future requests.
    

#### ***Phase 3: Tree Connect (The Access Key)***

- **Tree Connect Request:** The client asks for a specific folder path (e.g., `\\Server\Shared_Videos`) using its Session ID.
    
- **Tree Connect Response:** The server checks folder permissions. If allowed, it grants a **Tree ID** (the "Room Key" for that specific folder).
    

#### ***Phase 4: Operations (The Actual Work)***

- **Create/Open/Delete:** Requests to manipulate files or directories.
    
- **Read/Write:** Transferring the actual data within the files.
    
- **Response:** The server confirms the action was completed or sends the requested data.
    

---

---

## ⚖️ 4. SMB vs. SSH: Key Differences

|**Feature**|**SMB**|**SSH**|
|---|---|---|
|**Primary Goal**|**File Sharing:** Moving data like a delivery truck.|**Remote Access:** Controlling a PC like a driver.|
|**Scope**|Optimized for LAN (Internal networks).|Built for LAN and the Public Internet.|
|**Interface**|Usually accessed via File Explorer (GUI).|Accessed via Terminal/Command Line (CLI).|
|**Power**|Can read/write files.|Can run system-level commands and take full control|

---

<div align="center">

**[⬅️ Day 19: HTTP2 and HTTP3 Advance Concepts](./Day-19,%20HTTP2%20and%20HTTP3%20Advance%20Concepts.md) | [🏠 Home](../README.md) | [Day 21: SMB Enumeration (26,27-March-2026) ➡️](./Day-21,%20SMB%20Enumeration%20(26,27-March-2026).md)**

</div>
