# 🌐 Day 9: Domain Name System (DNS)

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![DNS](https://img.shields.io/badge/DNS-informational?style=for-the-badge)

> _The **Domain Name System (DNS)** is a distributed hierarchical system that resolves domain names into IP addresses._ 🌐

---

Humans remember:
`google.com`

Machines understand:
`142.250.190.14`

DNS translates names into numeric IP addresses so computers can communicate.

---

# 🔎 How DNS Resolution Works

Suppose you search for:
`google.com`

Here’s what happens step by step:

## 1️⃣ Client Request

- The **browser** acts as the _client_.
- It passes the request to the **Stub Resolver** (part of the OS DNS client service).

**Flow:**
`Browser` → `OS Stub Resolver`

The stub resolver is part of the operating system, not the browser.

---

## 2️⃣ Local Lookup (Before Internet Query)

The stub resolver checks locally in this order:

1. **Browser DNS Cache**
2. **OS DNS Cache**
3. **Hosts File**
   - Windows: `C:\Windows\System32\drivers\etc\hosts`
   - Linux: `/etc/hosts`

If the IP is found → resolution stops.
If not found → query is forwarded to a **Recursive DNS Server**, such as:

- Google Public DNS (`8.8.8.8`)
- Cloudflare (`1.1.1.1`)
- Or your ISP DNS

---

## 3️⃣ Recursive DNS Server

The first external DNS server contacted is called the:

**Recursive Resolver**
Its job is to fully resolve the domain.

It first checks:

- Its own DNS cache

If found → returns IP.
If not → it begins querying the DNS hierarchy.

---

## 4️⃣ Root DNS Servers

There are **13 named root server systems (A–M)**.
They are globally distributed using Anycast and coordinated by:

- ICANN

When asked:

> “Where is `google.com`?”

The root server replies:

> “I don’t know `google.com`, but here are the name servers for `.com`.”

It returns **NS (Name Server) records for the `.com` TLD**.

---

### 🔹 What is a TLD?

TLD = **Top Level Domain**

Examples:

- `.com`
- `.org`
- `.pk`
- `.io`

It is the last portion of a domain name.

---

### 🔹 Manual Root Query Example

You can manually query a root server:

```bash
nslookup -type=NS com. m.root-servers.net
```

This asks:

> “Who manages the `.com` TLD?”

The root server returns TLD name servers like:

`a.gtld-servers.net`  
`b.gtld-servers.net`  
`...`

---

## 5️⃣ TLD Name Servers (.com Servers)

The recursive resolver contacts one of the `.com` TLD servers and asks:

> “Who is authoritative for `google.com`?”

The TLD server returns the **Authoritative Name Servers** for that domain.

Example:

```bash
nslookup -type=NS chatgpt.com d.gtld-servers.net
```

This shows which servers manage `chatgpt.com`.

---

## 6️⃣ Authoritative Name Servers (Final Step)

Now the recursive resolver asks one of the authoritative servers:

> “What is the A record (IP address) for `google.com`?”

The authoritative server replies with the final IP address.

---

## 7️⃣ Caching and TTL

When the recursive resolver receives the IP:

- It stores it in cache
- For a duration defined by **TTL (Time To Live)**

_Note:_ DNS TTL is different from packet TTL.

Then:

- Stub resolver caches it
- Browser caches it

Future lookups are faster until TTL expires.

---

# 🧠 Final DNS Flow Summary

1. Browser requests `google.com`
2. Stub Resolver checks:
   - Browser cache
   - OS cache
   - Hosts file
3. Stub Resolver queries Recursive DNS Server
4. Recursive Server checks its cache
5. If not found:
   - Queries Root Server
   - Gets TLD (.com) servers
6. Queries TLD Server
   - Gets Authoritative Name Servers
7. Queries Authoritative Server
   - Gets IP address
8. IP returned to Browser
9. All layers cache the result using TTL

---

**Reference Video:** [How DNS works](https://www.youtube.com/watch?v=NiQTs9DbtW4)

<div align="center">

**[⬅️ Day 8: ARP Poisoning with arpspoof](./Day-08,%20ARP%20Poisoning%20with%20arpspoof.md)** | **[Day 10: DNS Record Types and DNS spoofing ➡️](./Day-10,%20DNS%20Record%20Types%20and%20DNS%20spoofing.md)**

</div>
