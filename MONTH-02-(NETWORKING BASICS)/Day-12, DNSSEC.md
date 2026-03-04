# 🛡️ Day 12: DNSSEC

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![DNS](https://img.shields.io/badge/DNS-informational?style=for-the-badge)
![DNSSEC](https://img.shields.io/badge/DNSSEC-critical?style=for-the-badge)

> _**Domain Name System Security Extensions (DNSSEC)** is a security system created to add **digital signatures** to DNS entries. It ensures that the "phone book of the internet" cannot be forged by hackers._ 🛡️

---

## **What is DNSSEC?**

### **How does it work?**

To understand DNSSEC, think of **Wax Seals** used on ancient royal letters.

When you search for a website, a DNS request is made to find the IP address of that domain.

- **Example:** `example.com` $\rightarrow$ `10.10.10.10`

An attacker might try to alter this mapping to send you to a fake site:

- **Attack:** `example.com` $\rightarrow$ `2.2.2.2` (A malicious server)

To prevent this, DNSSEC uses **Asymmetric Encryption**. Every domain owner has a **Private Key** (kept secret) and a **Public Key** (shared with everyone). The DNS mapping is signed using that Private Key to create a digital signature called an **RRSIG** (Resource Record Signature).

---

### **DNS Replies: Before vs. After DNSSEC**

| **Before DNSSEC (Unsecured)**             | **After DNSSEC (Secured)**                |
| ----------------------------------------- | ----------------------------------------- |
| `example.com` $\rightarrow$ `10.10.10.10` | `example.com` $\rightarrow$ `10.10.10.10` |
|                                           | **RRSIG (Signature):** `AB23JKD432K`      |

---

### **The Authentication Process**

In a modern secure DNS reply, the information is "wax sealed."

1. **The Stamp:** The Private Key is the secret "stamp" held by the domain owner.
2. **The Public Key:** The **DNSKEY** (Public Key) is sent along with the DNS reply.
3. **The Algorithm:** A code is included to tell the computer which mathematical "recipe" (like RSA) was used.
4. **The Verification:** The computer takes the **IP Address** + the **DNSKEY** and performs the algorithm.
5. **The Match:** The result is compared to the **RRSIG**.
   - **If it matches:** The reply is valid and the website opens.
   - **If it doesn't match:** The reply is discarded as a fake.

---

### **How does the computer know the DNSKEY is real?**

A hacker could send a fake Public Key, too. To prevent this, the computer uses a system called the **Chain of Trust**.

#### **The Three Phases of the Chain:**

- **Phase 1: The DNSKEY (The Employee)**
  Every DNS reply (e.g., for `google.com`) carries its own **DNSKEY**. The Recursive Server (the validator) asks: _"How do I know this key is real?"_ The reply says: _"Don't ask me, ask my parent!"_
- **Phase 2: The DS Record (The Manager)**
  The Recursive Server then asks the "Parent" of `google.com`, which is the manager of the `.com` extension. This manager holds a **DS Record** (Delegation Signer). The Manager says: _"I guarantee this key is real; I am the manager of the .com realm."_ \*
- **Phase 3: The Root (The CEO)**
  The Recursive Server then goes to the "Big Boss" of the entire internet: **The Root**. The Root replies: _"I am the CEO. I vouch for the .com manager. If I say trust them, trust them."_
  **The Conclusion:** The Chain stops at the **Root** (managed by **ICANN**). Because your computer already has the Root's "ID badge" saved in its memory, it trusts the CEO, who trusts the Manager, who trusts the Website. This complete link is the **Chain of Trust**.

---

<div align="center">

**[⬅️ Day 11: DNS Cache Poisoning](./Day-11,%20DNS%20Cache%20Poisoning.md)**

</div>
