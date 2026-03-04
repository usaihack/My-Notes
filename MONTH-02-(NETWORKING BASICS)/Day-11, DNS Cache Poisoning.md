# 🛡️ Day 11: The Kaminsky Attack (DNS Cache Poisoning)

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![DNS](https://img.shields.io/badge/DNS-informational?style=for-the-badge)
![DNS Cache Poisoning](https://img.shields.io/badge/DNS_Cache_Poisoning-critical?style=for-the-badge)

> _In our last session, we talked about local DNS poisoning at the LAN level by targeting a single machine. But today, we’re looking at a **huge attack** that poisons the cache of the **Recursive DNS server**. This leads everyone using that resolver to visit an attacker's site instead of the real one. This is the famous **Kaminsky Attack**._ 🛡️

---

### 🔍 The Core Concept: Kaminsky's Attack

Before 2008, DNS resolvers used a single port (Port 53) for all queries and a 16-bit **Transaction ID**. This meant there were only 65,536 possible IDs to guess. These IDs are used to confirm a reply is true; if the ID of the request and the reply don’t match, the resolver just ignores it.

### 🛑 The Problem

When a resolver asks for an IP (like `google.com`), it opens Port 53. The attacker has a very tiny window—sometimes just a fraction of a second—to guess that ID. If the guess is wrong, the "door" closes until the **TTL** (Time to Live) ends. The attacker is stuck waiting.

### 💡 The Solution (The "Subdomain Flood")

Kaminsky discovered that if we send requests for **fake subdomains**, the port stays open for those specific requests. If one guess fails, we just send another!

- **The Process:** The attacker asks for `fake1.google.com`. The server says, "I don't know this, let me ask the authoritative server."
- **The Logic:** Since subdomains often have different IPs, the resolver makes a separate request for every single one.
- **Infinite Ammo:** If the attacker misses the ID for `fake1.google.com`, they immediately try `fake2.google.com`. The server requests again on Port 53, and the attacker gets a fresh chance. Since we have no scarcity of fake subdomains, we can keep this going until the ID is guessed correctly.

### 🚩 The Control (The Hijack)

Once the attacker wins the race and guesses the ID, they map their malicious IP to that domain. They also add a **fake note** saying:

> _"I am the authority for `google.com`. For any future requests, just ask me."_

The server simply trusts it. **Boom—the server's cache is now poisoned.** It’s a massive attack.

---

### 🛡️ The Fix: Port Randomization

To stop this, engineers began randomizing the **Source Ports**.

- **Before:** Only 65,536 IDs to guess on a fixed port.
- **Now:** The ID (65,536) and the Port (65,536) are both random.
- **The Math:** Total combinations are $65,536 \times 65,536 = 4,294,967,296$.

It would now take weeks for even a supercomputer to guess the correct Port + ID combination!

---

### 📚 Key Terms to Remember

| **Term**       | **My Simple Explanation**                                                                                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zone**       | A part of the internet an organization owns. `google.com` is the big picture; `drive.google.com` is a zone inside it.                                                             |
| **Zone File**  | The actual file where all the records for a domain and its subdomains are kept.                                                                                                   |
| **Sub-Zones**  | If `gemini.google.com` gets "so big" it needs its own management, it becomes a **Delegated Zone**. The main file just points to it and says: "Do not ask me, ask Gemini's files." |
| **Hosts File** | A file on your own OS for popular sites that can override the cache and the server entirely.                                                                                      |

---

<div align="center">

**[⬅️ Day 10: DNS Record Types and DNS spoofing](./Day-10,%20DNS%20Record%20Types%20and%20DNS%20spoofing.md)** | **[Day 12: DNSSEC ➡️](./Day-12,%20DNSSEC.md)**

</div>
