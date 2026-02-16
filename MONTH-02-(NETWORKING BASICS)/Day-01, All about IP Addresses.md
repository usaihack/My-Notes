# 🌐 Day 1: All About IP Addresses

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![IP](https://img.shields.io/badge/IP-Address-success?style=for-the-badge)

> _Imagine a courier is delivering you a parcel. He may ask for your street no and house number. To ensure the order reaches exactly at your doorstep, you must give your street and house number._ 📦

---

## 🏠 What is an IP Address?

In terms of networking, this street or house number is called the **Internet Protocol (IP)**.
By this, the courier identifies you to deliver your parcel. Similarly, the server will find your device by its IP address to find you on the internet.

> _But wait, I sugar-coated it. It is not as simple as that!_ 😁😁

---

## 🔢 IPv4 Structure

An IP has two types, **IPv4** and **IPv6**. Here, we will talk about **IPv4** for now.

An IPv4 address looks like this:

```bash
192.16.10.9
```

1.  Every decimal part is an **Octet**.
2.  Every decimal is exactly of **one byte** (8 bits).
3.  IPv4 has a total of **32 bits**.
4.  Every decimal ranges from **0-255**.

---

## 📊 IP Classes

IPv4 has three general classes for common usage. Their ranges are given below:

| Class | Range                            |
| :---: | :------------------------------- |
| **A** | `0.0.0.0` to `127.255.255.255`   |
| **B** | `128.0.0.0` to `191.255.255.255` |
| **C** | `192.0.0.0` to `223.255.255.255` |

> **Note:** Class D and Class E exist, but they are not exposed to the internet. They are for special use cases.

---

## 🌍 Public vs Private IPs

There exist a total of roughly **4.3 billion** IPv4 addresses, but the humans on Earth are about **8 billion**, and every human has more than one device.
To assign every device a unique IP, we face a huge shortage. To avoid this, engineers made two types for IP assigning: **Private** and **Public** IPs.

### 🔒 Private IP

The IP assigned to a device **within the LAN** is a Private IP.

- **Example:** Devices connected to your home Wi-Fi router will have a Private IP which only the router knows.

Private IP is always changing for your device.

- If you connect now, your Private IP might be `192.168.125.1`.
- When you disconnect and connect again, it might be `192.178.12.12`.

**Classes of Private IPs:**

| Class | Range                              | Usage                                   |
| :---: | :--------------------------------- | :-------------------------------------- |
| **A** | `10.0.0.0` to `10.255.255.255`     | Used by large million-dollar companies. |
| **B** | `172.16.0.0` to `172.31.255.255`   | Used by medium-sized organizations.     |
| **C** | `192.168.0.0` to `192.168.255.255` | Used in homes.                          |

### 🌐 Public IP

The IP assigned to the router **over the internet** is a Public IP.

- **Example:** Your ISP will assign an IP to your router on lease to communicate over the internet. This leased IP is Public IP.

So, if your private IP matches another over the internet (which is possible), it doesn't affect your connection because your Public IP is different.

> **Is Public IP permanent for a router over the internet?**
>
> **No**, it changes but very slowly, or it depends on the ISP. For example, if you buy a monthly package, your router's IP might be the same for the whole month, or it may change when you restart the router or after the ISP's maintenance work.
> Some public IPs may be permanent but for an extra cost (Static IP).

---

## 🔄 DHCP & NAT

Now, you might also be thinking, how do our devices get a Private IP? The answer is **DHCP**.

### 🤖 DHCP (Dynamic Host Configuration Protocol)

DHCP is a service that gives a device a **Private IP**.

1.  When you connect to a network, your device sends a **DHCP Discovery** message for available IPs.
2.  The DHCP server replies with an **offer** of an available IP.
3.  The device then sends a **DHCP Request**.
4.  The DHCP server **assigns** that IP to the device.

> **Remember:** In LANs, the router acts as a DHCP server, while in WANs, there is a dedicated DHCP server.

### 🎭 NAT (Network Address Translation)

NAT is a method for transforming **Private IPs** to **Public ones**.

**Example:**

- Router Public IP: `23.45.33.1`
- Phone Private IP: `192.168.4.4`
- Laptop Private IP: `192.168.3.1`

Now, the router's NAT service translates these Private IP addresses to `23.45.33.1` when you make a request on the internet.

---

## 📍 PAT (Port Address Translation)

You might ask: _If every private IP address is translated to the same public IP in the same LAN through NAT, then how does the incoming data know which device made the request?_

**Answer:**
When you make a search, the router doesn't simply do NAT (translate Private IP to Public). Instead, it creates a table using **PAT**.
This table contains the Private IP along with the port, and the translated IP and port.

| Device       | Private IP & Port    | Translated IP & Port |
| :----------- | :------------------- | :------------------- |
| **Device 1** | `192.168.123.1:5000` | `32.192.3.1:3000`    |
| **Device 2** | `192.168.34.3:5500`  | `32.192.3.1:3001`    |
| **Device 3** | `192.168.3.1:5000`   | `32.192.3.1:3002`    |

So, in this way, ports are also translated, and the data goes to the exact location.

> **Difference between NAT and PAT:**
> NAT is an **IP translator**. PAT is an **IP + Port translator**.
> _In most LANs, what we call NAT is actually PAT._

---

<div align="center">

**[Day 2: Ports, IP, TCP, UDP ➡️](./Day-02,%20Ports,%20IP,%20TCP,%20UDP.md)**

</div>
