# 🌐 Day 3: OSI Model

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![OSI](https://img.shields.io/badge/OSI-Model-success?style=for-the-badge)

> _The OSI Model is the blueprint of the internet. It breaks down the complex process of communication into 7 digestible layers._ 🗺️

---

## 🏛️ What is the OSI Model?

The **Open Systems Interconnection (OSI)** model is a conceptual framework used to understand network interactions. It explains how data moves between two devices.

> **Note:** It is a theoretical model which physically does not exist as a single entity. The real-world implementation is the **TCP/IP Model**.

It has **seven layers**, traditionally counted from **Bottom (Physical)** to **Top (Application)**.

---

## 🔽 The 7 Layers (Top to Bottom)

In reality, data flow starts from the Application layer (Layer 7) when you send data, and goes down to the Physical layer (Layer 1).

### 7️⃣ Application Layer

**"The Interface"**

When you open a browser (Chrome) or use an app (WhatsApp), you are interacting with this layer. It ensures the application knows how to communicate with the network. This is where the human is talking to the networks through an application interface.

- **Protocols:** HTTP, HTTPS, FTP, DNS, SMTP.

### 6️⃣ Presentation Layer

**"The Translator"**

This layer ensures that data is in a usable format. It handles encryption, compression, and translation. Think of it as the designer and stylist of the data.

- **Functions:**
  - **Encryption/Decryption:** SSL/TLS.
  - **Compression:** Reducing data size.
  - **Formatting:** Converting data formats (e.g., ASCII, JPEG).

### 5️⃣ Session Layer

**"The Manager"**

This layer establishes, maintains, and terminates connections (sessions).

- **Example:** When you call a person, the call is first established, maintained while you talk, and closed when you hang up. Similarly, when you log in to a web page, a session is established to keep you logged in. It keeps your connection alive until you kill it.

### 4️⃣ Transport Layer

**"The Courier"**

The most critical layer for delivery. It decides _how_ much data to send and ensures it arrives. Here, either TCP or UDP header (depending on your connection) is added to the data segments.

- **Protocols:** TCP, UDP.
- **Function:** End-to-end communication, segmentation, flow control.

### 3️⃣ Network Layer

**"The Navigator"**

The segments are given **IP Headers** to make **Packets**. This layer handles **Routing** and finds the best path for data to reach its destination across different networks.

- **Function:** Logical addressing (IP Headers) and path determination.

### 2️⃣ Data Link Layer

**"The Local Delivery"**

This is where the packets search for the destination IP's **MAC Address** within the destination LAN to deliver the data packets. Each hop (like your router -> ISP -> server) gets a new MAC header for the next segment.

- **Function:** Physical addressing, error detection.

### 1️⃣ Physical Layer

**"The Hardware"**

These are the real data pulses, regardless of the IP, TCP, or UDP headers. It involves the physical electric pulses of the data moving through cables or air.

- **Key Idea:**
  - **MAC Address** changes at each hop.
  - **IP Address** stays the same end-to-end.
  - **Physical Layer** is like the road the data travels on.

---

## ⚔️ Attacks per Layer

To understand security, you must know what hits where.

| Layer | Name             | Common Attacks                                           |
| :---: | :--------------- | :------------------------------------------------------- |
| **7** | **Application**  | Phishing, HTTP Floods, SQL Injection, XSS, DNS Poisoning |
| **6** | **Presentation** | SSL Stripping, Malformed Encoding                        |
| **5** | **Session**      | Session Hijacking, Man-in-the-Middle (MITM)              |
| **4** | **Transport**    | TCP SYN Flood, UDP Flood, Port Scanning                  |
| **3** | **Network**      | IP Spoofing, Ping of Death, ICMP Flood, Route Injection  |
| **2** | **Data Link**    | ARP Spoofing, MAC Flooding, VLAN Hopping                 |
| **1** | **Physical**     | Wiretapping, Jamming, Physical Tampering                 |

---

<div align="center">

**[⬅️ Day 2: Ports, IP, TCP, UDP](./Day-02,%20Ports,%20IP,%20TCP,%20UDP.md)**

</div>
