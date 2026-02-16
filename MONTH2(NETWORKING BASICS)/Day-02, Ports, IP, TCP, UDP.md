# 🚪 Day 2: Ports, Protocols, TCP & UDP

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Ports](https://img.shields.io/badge/Ports-TCP%2FUDP-success?style=for-the-badge)

> _A Port is just a door through which different services and your device communicates._ 🚪

---

## 🔌 What is a Port?

Earlier, we talked about NAT and PAT which translates the IPs and Ports.

### Total Number of Ports

Every Port is of **16 bits**, ranges from **0 - 65535**, so there are a total of **65,536** Ports.

There are three ranges of Ports:

| Range             | Name                  | Description                            |
| :---------------- | :-------------------- | :------------------------------------- |
| **0 - 1023**      | **Well-Known**        | Public ones. Used commonly.            |
| **1024 - 49151**  | **Registered**        | Registered ones for specific services. |
| **49152 - 65535** | **Dynamic/Ephemeral** | Those which OS chooses randomly.       |

### How it Works ⚙️

1.  When you open your browser, the OS assigns that connection a random Port from **Dynamic Ports**.
2.  Then **PAT** translates that to a public Port (on the router's side for the internet).
3.  The server then talks to your public Port and all the communication happens here.

> **Example:** You have 3 tabs open. Every tab gets a unique random Port from Dynamic Ports. When you search "Hello", the browser binds a Port (like 443) to the packet. Then it goes through PAT, and the server serves it on Port 443 (HTTPS).

### Common Ports to Know

Of course, you don't have to remember all ports, but here is a list of some Ports you must be familiar with:

|   Port   | Service        |
| :------: | :------------- |
|  **21**  | FTP            |
|  **22**  | SSH            |
|  **23**  | Telnet         |
|  **53**  | DNS            |
|  **80**  | HTTP           |
| **443**  | HTTPS          |
| **445**  | SMB            |
| **3389** | RDP            |
| **139**  | NetBIOS        |
| **3306** | MySQL          |
| **8080** | HTTP Alternate |

---

## 📜 Protocols

We have rules for the English language, like grammar. Imagine if we spoke English without caring about grammar—would anyone understand us?
Similarly, in the realm of the internet, there are rules, like grammar, which are called **Protocols**.
For example, **HTTPS**, **SMTP**, **FTP**, etc., are all protocols.

From a hacker's perspective, here are some of the most important ones:

### 1. IP (Internet Protocol) 🌐

**Internet Protocol (IP)** only cares about the **source** and **destination** IPs.
As we know, data flows over the internet in chunks, and these chunks are called **Packets**.
Every packet usually has two main parts (with a third optional one):

1.  **Packet Header**
2.  **Payload**

**The Packet Header (IP Header):**

Imagine a letter in an envelope. The envelope has sender and receiver addresses. Here, the envelope represents the IP Header.
It has many parts, but here are the most important ones:

1.  **Identification:** Uniquely identifies each packet and can be used for reassembling fragmented packets.
2.  **IP Flags:** Indicates whether a packet is **Fragmented (M)** or **Not (D)**.
3.  **Fragment Offset:** Shows the position of the fragmented part. Like a page number in a book.
4.  **TTL (Time To Live):** Counts "hops" (routers) the packet passes through.
    - _TTL is crucial because without it, undelivered packets could loop endlessly._
    - Examples: 64 (Linux/macOS), 128 (Windows).
5.  **Protocol:** Defines which protocol is being used (e.g., 6 for TCP, 1 for ICMP, 17 for UDP).
6.  **Source & Destination:** The IP addresses of sender and receiver.

### 2. TCP (Transmission Control Protocol) 🤝

There are many protocols, but the most reliable one is **TCP**. TCP is very important from a hacker's perspective.
Before any data is sent, TCP says: _"Let's establish a connection."_ (The 3-way handshake).

**The TCP Header:**

Just like the IP Header, the TCP Header ensures data reaches the correct service.
_Analogy: IP Header = Building Address. TCP Header = Apartment Number._

1.  **Source & Destination Port:** From which port communication started and to which it must go.
2.  **Sequence Number:** TCP breaks data into segments and numbers them.
3.  **Acknowledgement Number:** Tells the sender: _"I received packet X, send the next one."_ (Reliability).
4.  **Flags:**
    - **SYN:** Start of communication.
    - **ACK:** I got your last message.
    - **RST:** Something went wrong (Reset).
    - **FIN:** I’m done (Close).
5.  **Window Size:** Receiver tells sender: _"I can only handle this much data at once."_
6.  **Checksum:** Ensures data integrity.

---

## 🤝 The 3-Way Handshake

When communication starts, TCP first establishes a connection using a 3-way handshake:

1.  **SYN:** Sender says _"Hello, can you hear me?"_
2.  **SYN-ACK:** Server says _"I can hear you. Can we talk?"_
3.  **ACK:** Sender says _"Acknowledged! Let’s begin."_

**Connection States (Scanning Perspective):**

- **Port Open:** Server replied with **SYN-ACK**. (Tools like Nmap mark it open).
- **Port Closed:** Server replies with **RST**.
- **Port Filtered:** No response. (Silence usually means a firewall dropped the packet).

> **What's the difference between IP Identification and TCP Sequence Number?**
>
> - The data is first segmented by TCP, each segment getting a unique **Sequence Number**.
> - When the **IP Header** is added, it becomes a **Packet**. The IP Header gives each packet a unique **Identification**.
> - _Sequence Number_ orders the data stream. _Identification_ helps reassemble fragmented IP packets.

---

<div align="center">

**[⬅️ Day 1: All About IP Addresses](./Day-01,%20All%20about%20IP%20Addresses.md)**

</div>
