# 🔐 Day 24: SMTP Security

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Protocol-red?style=for-the-badge)
![DNS](https://img.shields.io/badge/DNS-MX--Record-orange?style=for-the-badge)

> _Sending an email is one thing; ensuring it’s authentic and secure is another. SMTP security protocols like SPF, DKIM, and DMARC are the "Triple Guard" of your inbox._ 🛡️

---

## 📍 1. MX Records (Mail Exchange)

We previously discussed MX records in the DNS chapter. They deal specifically with incoming mail. If I send an email from my Gmail to `company@store.com`, my SMTP server asks the DNS: "Where is `store.com`?" The DNS server looks up the MX records for `store.com` to find its specific SMTP server and deliver the mail. 



---

## 🛡️ 2. Email Security Layers

### 📋 1. SPF (Sender Policy Framework)
SPF is a list in your DNS settings that specifies: "Only these IPs or servers are authorized to send mail on my behalf."

**How it works (Step-by-Step):**
1. You send an email to `friend@yahoo.com` from `usman@gmail.com`.
2. The email arrives at the Yahoo SMTP server.
3. Yahoo asks: "Is this really from `gmail.com`?"
4. Yahoo checks the DNS records for `gmail.com` and finds the SPF record.
5. If the sending server matches the SPF list, the mail is delivered; otherwise, it’s flagged or deleted.

> **Who manages SPF?** 
> For standard services like `@gmail.com`, Google manages the SPF record. If you own your own domain (e.g., `@yourname.com`), you must define your own SPF record in your DNS settings.


### 🔏 2. DKIM (DomainKeys Identified Mail)
Similar to **DNSSEC**, DKIM adds a digital signature to every email you send. It acts as a "Digital Wax Seal" that can only be verified using your public key. If the signature doesn't match, the mail has been tampered with.


### 🚦 3. DMARC
The final hurdle for hackers. If SPF or DKIM fails, DMARC tells the receiving server exactly what to do (e.g., "Reject the mail" or "Send to Spam").


---

## 🔐 4. Encryption (TLS)
Without **TLS (Transport Layer Security)**, email travels as plain text. Adding TLS creates a secure tunnel, ensuring that any intercepted data appears as scrambled, unreadable gibberish.

> **Note:** We will dedicate a separate session to TLS in the future.

---

<div align="center">

**[⬅️ Day 23: SMTP](./Day-23,%20SMTP.md) | [🏠 Home](../README.md) | [Day 25: ...continue SMTP ➡️](./Day-25,%20...continue%20SMTP.md)**

</div>
