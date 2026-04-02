# 📧 Day 23: SMTP (Simple Mail Transfer Protocol)

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Email](https://img.shields.io/badge/Email-Service-yellow?style=for-the-badge)
![SMTP](https://img.shields.io/badge/SMTP-Port--25-blueviolet?style=for-the-badge)

> _SMTP is the standard protocol for sending emails across the internet. It ensures that no matter the OS or language, your message reaches its destination._ 📧

---

## 🏗️ 1. What is SMTP?

**Simple Mail Transfer Protocol** is the set of rules used in sending electronic mails. Before 1982, sending emails was extremely difficult due to compatibility issues between different operating systems. Jonathan Postel developed SMTP to resolve these issues and standardize email communication.

---

## ⚙️ 2. How SMTP Works

When you write an email and hit send, your device establishes a connection with your mail server (e.g., Gmail). The server then locates the receiver's server and pushes the mail through.

### 🔄 The Full Mechanism:
1. **Client:** You compose the mail.
2. **Handshake:** Connection established between your device and your mail server.
3. **Transfer:** Your mail is sent to your server.
4. **Routing:** Your server looks for the receiver's mail server.
5. **Push:** Your server sends the mail to the receiver's server.

> [!IMPORTANT]
> - **SMTP is ONLY used for sending emails.**
> - **SMTP usually operates on port 25.**

---

## 📥 3. Mail Downloading Protocols

### 📧 1. POP (Post Office Protocol)
POP (currently POP3) is the legacy method of downloading mail. When a device downloads mail from the server, the server copy is deleted. This means mail only exists on one device and cannot be synced across multiple platforms.

### 🌐 2. IMAP (Internet Message Access Protocol)
IMAP is the modern standard for retrieving mail. It downloads mail without deleting it from the server, allowing for seamless synchronization across all your connected devices. Mail is only removed from the server when you explicitly delete it from one of your devices.

---

<div align="center">

**[⬅️ Day 22: continue SMB Enumeration](./Day-22,%20continue%20SMB%20Enumeration.md) | [🏠 Home](../README.md) | [Day 24: SMTP Security ➡️](./Day-24,%20SMTP%20Security.md)**

</div>
