# 🕸️ Day 4: Subnetting and CIDR Notation

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Subnetting](https://img.shields.io/badge/Subnetting-CIDR-success?style=for-the-badge)

> _Subnetting is like dividing a large pizza into slices so everyone gets their share without fighting. It's the art of efficient network management._ 🍕

---

## 🛣️ Network vs Router

Prior to moving towards **subnetting** and **CIDR notation**, here are some terms you must know.

A **network** is allocated to you by your ISP (think of it like a street). The **router** is just the gatekeeper of this street.

- Your ISP assigns you a **public IP** with a **prefix** that defines the range of that network.
  - **Example:** `192.168.10.0/24`
  - `/24` tells how many devices can exist in that network.
  - In this case, `/24` means **256** addresses, **254** usable for devices.

- The router is the **gateway**, directing traffic between your devices and the outside world.

---

## 🏠 Network Address

Every network has a **network address**, like the **name of the street**.

- Your ISP’s public IP belongs to a network.
- **Example:** `192.168.10.0/24` -> `.0` is the **Network Address**.
- This is **not assigned to a device**, it simply identifies the network.

---

## 📢 Broadcast Address

Imagine you want to send a wedding invitation to all houses on your street.

- Instead of knocking on every door, you take a **megaphone** and announce it to everyone at once.
- In networking, this megaphone is called the **Broadcast Address**.
- Broadcast is the **last address** in the network range and is used to send a message to all devices in that subnet.

---

## 🔪 Subnetting

Subnetting is like dividing your network into smaller, private blocks.

- **Analogy:** You have 2 cars (seats for 4 each). Your neighbours want to join, but you don’t want everyone crammed into your car.
- You give them their own car. Both cars reach the same destination, but traffic is separated.
- Similarly, subnetting splits a network so devices are grouped separately, traffic is isolated, and management becomes easier.

> **Remember:** Every subnet has its own **Broadcast Address** and **Network Address**.

---

## 📏 CIDR Notation

**Classless Inter-Domain Routing (CIDR)** is a system where we use **IP + Suffix** to describe the size of a network.

For example, your ISP may assign you a Public IP + suffix combination, like `192.168.10.0/24` (`/24` is common in home networks). By this `/24`, we can readily find the **network size**, the **Network Address**, and **Broadcast Address**.

### 🧮 How to Calculate?

**Example 1:** `192.168.10.0/24`

1.  **Calculate Host Bits:** Total bits in an IP = 32. Subtract the CIDR: `32 - 24 = 8`.
2.  **Calculate Total IPs:** `2^8 = 256`. Range is `0-255`.
3.  **Block Size:** 256.
4.  **Network Address:** The first IP -> `192.168.10.0`.
5.  **Broadcast Address:** The last IP -> `192.168.10.255`.
6.  **Usable Hosts:** `256 - 2 = 254` devices.

> **Note:** The first 24 bits are for **Network Identification** and the remaining 8 bits are for **Size**.

---

### 🧠 Tricky Example

**Example 2:** `192.168.50.70/26`

1.  **Calculate Host Bits:** `32 - 26 = 6`.
2.  **Calculate Total IPs:** `2^6 = 64`.
3.  **Block Ranges:**
    - `0 - 63`
    - `64 - 127`
    - `128 - 191`
    - `192 - 255`
4.  **Find the Range:** Where does `70` fall? In the **second range** (`64 - 127`).
5.  **Results:**
    - **Network Address:** `192.168.50.64`
    - **Broadcast Address:** `192.168.50.127`
    - **Usable Hosts:** `64 - 2 = 62`

> _The step of finding the correct block is crucial!_ ⚠️

---

<div align="center">

**[⬅️ Day 3: OSI Model](./Day-03,%20OSI%20Model.md) | [Day 5: Multi-Subnetting and Subnet Masks ➡️](./Day-05,%20Multi%20Subnetting%20and%20Subnet%20Masks.md)**

</div>
