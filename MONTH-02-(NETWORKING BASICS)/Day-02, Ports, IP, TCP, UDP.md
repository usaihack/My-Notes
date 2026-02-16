# 🔌 Day 2: Ports, IP, TCP, UDP

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Ports](https://img.shields.io/badge/Ports-TCP%2FUDP-success?style=for-the-badge)

> _A Port is just a door through which different services and your device communicates. Earlier, we talked about NAT and PAT which translates the IPs and Ports._ 🚪

---

## 🚪 Ports

Every Port is of **16 bits**, ranges from `0` to `65535`, so there are a total of **65536** Ports.

### 📊 Port Ranges

| Port Type      |      Range      | Usage                                   |
| :------------- | :-------------: | :-------------------------------------- |
| **Well-Known** |   `0 - 1023`    | Public ones. Used commonly.             |
| **Registered** | `1024 - 49151`  | Registered ones, for specific Services. |
| **Dynamic**    | `49152 - 65535` | Those which OS chooses randomly.        |

> _But what's the real explanation? How is it done?_ 🤔

Here's how:

1.  When you open your browser, OS assigns that connection (a single tab may contain dozens of connections) a random Port from **Dynamic Ports**.
2.  Then **PAT** translates that to a public Port.
3.  The server then talks to your public Port and all the communication happens here.

**Example:**
You have 3 tabs open in a browser. Every tab will be assigned a unique random Port from Dynamic Ports by your OS. When you make a search, for instance, "Hello", the browser itself binds Port like `443` to the packet. Then it goes through PAT, and the server serves it on Port `443` (HTTPS).

---

## 📋 Common Ports

Of course, you don't have to remember all these ports, but here is the list of some Ports you must be familiar with:

|   Port   | Service      | Description                       |
| :------: | :----------- | :-------------------------------- |
|  **21**  | **FTP**      | File Transfer Protocol            |
|  **22**  | **SSH**      | Secure Shell (Secure Login)       |
|  **23**  | **Telnet**   | Unsecure Text Communications      |
|  **53**  | **DNS**      | Domain Name System                |
|  **80**  | **HTTP**     | HyperText Transfer Protocol       |
| **443**  | **HTTPS**    | HTTP Secure                       |
| **445**  | **SMB**      | Server Message Block              |
| **3389** | **RDP**      | Remote Desktop Protocol           |
| **139**  | **NetBIOS**  | Network Basic Input/Output System |
| **3306** | **MySQL**    | Database Server                   |
| **8080** | **HTTP-Alt** | Alternative HTTP Port             |

---

## 📜 Protocols

> _We have rules for the English language, like grammar. Imagine if we spoke English without caring about grammar—would anyone understand us?_ 🗣️
>
> _Similarly, in the realm of the internet, there are rules, like grammar, which are called **Protocols**._ 📜

**Examples:** `HTTPS`, `SMTP`, `FTP`, etc.

---

## 📦 Internet Protocol (IP)

> _From a hacker's perspective, this is important._ 🕵️

**Internet Protocol (IP)** only cares about the **source** and **destination** IPs.
As we know, data flows over the internet in chunks, and these chunks are called **packets**.
Every packet usually has two main parts (with a third optional one):

1.  **Packet Header**
2.  **Payload**

### 🏷️ Packet Header (IP Header)

Also called the _IP Header_. Imagine a letter in an envelope. The envelope has sender and receiver addresses. Here, the envelope represents the IP Header.

**Important Fields:**

1.  **Identification:** Uniquely identifies each packet. Used for reassembling fragmented packets.
2.  **IP Flags:** Indicates whether a packet is fragmented (**M**) or not (**D**).
3.  **Fragment Offset:** Shows the position of the fragmented part. Like a page number in a book (page 10 comes after page 9).
4.  **TTL (Time To Live):** Tells us whether the packet successfully reached its destination.
    **Full Explanation of TTL:** Despite its name, TTL does not measure real time, it counts **"hops"** or cycles instead. Here’s what happens:
    - Every packet is assigned a TTL, usually **64** on Linux/macOS and **128** on Windows.
    - The packet leaves your router and travels through multiple routers to reach its destination (it does not go through every router on the internet).
    - Each router the packet passes through **subtracts 1** from the TTL.
    - If the packet reaches its destination before TTL reaches zero, it is successfully delivered.
    - If TTL reaches **0** before the packet reaches its destination, the router **discards** the packet and sends a **"TTL Expired"** message back to the sender.
    - _TTL is crucial_ because without it, undelivered packets could loop endlessly, increasing traffic and making the network inefficient.

5.  **Protocol:** Defines which protocol is used (e.g., 6 for TCP, 17 for UDP).
6.  **Source and Destination:** The IP addresses of sender and receiver.

---

## 🤝 TCP (Transmission Control Protocol)

There are many protocols, but **TCP** is the most reliable.
Before any data is sent, TCP says: _"Let's establish a connection."_

### 🧠 TCP Header

Just like the _IP Header_, the TCP Header ensures data reaches the correct service.

- **IP Header** = Building Address 🏢
- **TCP Header** = Apartment Number 🚪

**Important Fields:**

1.  **Source & Destination Port:** Where the comms started and where it's going.
2.  **Sequence Number:** Number given to each data segment to keep order.
3.  **Acknowledgement Number:** Tells the sender: _"I received packet X, send the next one."_ (Reliability).
4.  **Flags:**
    - **SYN:** Start connection.
    - **ACK:** Acknowledge message.
    - **RST:** Reset connection (something went wrong).
    - **FIN:** Finish/Close connection.
5.  **Window Size:** Flow control. Receiver says _"I can only handle this much data."_
6.  **Checksum:** Ensures data integrity.

### 👋 3-Way Handshake

1.  **SYN:** "Hello, can you hear me?" (Sender)
2.  **SYN-ACK:** "I can hear you. Can we talk?" (Server)
3.  **ACK:** "Acknowledged! Let's begin." (Sender)

**Connection States:**

- **Open:** Server sends `SYN-ACK`.
- **Closed:** Server sends `RST`.
- **Filtered:** No response (Firewall dropped it).

> **What's the difference between IP Header's ID and TCP Header's Sequence number?** 🤔
>
> The **IP Header** gives the _packet_ a unique ID. **TCP** segments the _data_ and gives it a Sequence Number.

---

## 🚀 UDP (User Datagram Protocol)

**UDP** is used where **speed/optimization** matters more than reliability.

> _Imagine you’re standing on a mountain and shout "HELLOOOOO!"_ 🏔️

You don’t:

- Check if someone is listening.
- Wait for confirmation.
- Ask "Did you hear me?".
- Care if the wind distorts your voice.

**You just shout. That’s UDP.**

### ⚠️ Why is UDP tricky?

UDP is **silent**.

- **Open Port:** Service receives packet, might not respond.
- **Filtered Port:** Firewall drops packet, no response.
- **Closed Port:** System sends ICMP "Port Unreachable".

Because open and filtered ports both look like "silence", tools like `nmap` often have to wait or retry, making UDP scanning slower and less reliable.

---

<div align="center">

**[⬅️ Day 1: All About IP Addresses](./Day-01,%20All%20about%20IP%20Addresses.md)**

</div>
