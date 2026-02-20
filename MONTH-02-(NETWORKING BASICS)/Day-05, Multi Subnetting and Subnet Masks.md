# 🔢 Day 5: Multi-Subnetting and Subnet Masks

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Subnetting](https://img.shields.io/badge/Subnetting-Masks-success?style=for-the-badge)

> _Think of a Large Company with different departments: HR, Sales, and IT. Subnetting is how we give each department its own secure floor while keeping everyone in the same building._ 🏢

---

## 🏗️ Multi-Subnetting

In **Day 4**, we learned how to find the _usable host range_, _network address_, and _broadcast address_ for a single network. Today, we will scale up and find these values for **multiple subnets** within a larger network.

### 📜 The Golden Table

Before we dive in, you must memorize (or bookmark) this relationship between CIDR, hosts, and subnets:

| **CIDR** | **Total IP Addresses** | **Number of subnets** |
| :------- | :--------------------- | :-------------------- |
| **/24**  | 256                    | 1                     |
| **/25**  | 128                    | 2                     |
| **/26**  | 64                     | 4                     |
| **/27**  | 32                     | 8                     |
| **/28**  | 16                     | 16                    |

> **Rule of Thumb:** As you move down, the total number of IPs is halved, while the number of subnets doubles (1 → 2 → 4 → 8 → 16).

---

## 🧮 Example 1: Dividing into 4 Subnets

**Goal:** Divide `192.168.10.0/24` into **4 subnets**.

### 🛠️ Solution:

1.  **Identify New CIDR:** Look at the table. To get **4 subnets**, we need a **/26** CIDR.
2.  **Determine Host Size:** A **/26** network has **64 total hosts**.
    - **Total IPs:** 64
    - **Usable Hosts:** `64 - 2 = 62` (excluding Network and Broadcast addresses).
3.  **Create the Blocks:** Start from zero and add blocks of 64:
    - `0, 64, 128, 192` (Next would be 256, which is out of range).
4.  **The Subnet Table:**

| **Range**     | **Network Address** | **Broadcast Address** | **Usable Range**                     |
| :------------ | :------------------ | :-------------------- | :----------------------------------- |
| **0 - 63**    | `192.168.10.0`      | `192.168.10.63`       | `192.168.10.1` to `192.168.10.62`    |
| **64 - 127**  | `192.168.10.64`     | `192.168.10.127`      | `192.168.10.65` to `192.168.10.126`  |
| **128 - 191** | `192.168.10.128`    | `192.168.10.191`      | `192.168.10.129` to `192.168.10.190` |
| **192 - 255** | `192.168.10.192`    | `192.168.10.255`      | `192.168.10.193` to `192.168.10.254` |

---

## 🧮 Example 2: Dividing into 8 Subnets

**Goal:** Divide the same network into **8 subnets**.

### 🛠️ Solution:

1.  **Identify New CIDR:** For 8 subnets, the table points to **/27**.
2.  **Determine Host Size:** A **/27** CIDR provides **32 hosts** per subnet.
3.  **The Subnet Table:**

| **Hosts Range** | **Network Address** | **Broadcast Address** | **Usable Hosts** |
| :-------------- | :------------------ | :-------------------- | :--------------- |
| **0 - 31**      | `192.168.10.0`      | `192.168.10.31`       | `.1` to `.30`    |
| **32 - 63**     | `192.168.10.32`     | `192.168.10.63`       | `.33` to `.62`   |
| **64 - 95**     | `192.168.10.64`     | `192.168.10.95`       | `.65` to `.94`   |
| **96 - 127**    | `192.168.10.96`     | `192.168.10.127`      | `.97` to `.126`  |
| **128 - 159**   | `192.168.10.128`    | `192.168.10.159`      | `.129` to `.158` |
| **160 - 191**   | `192.168.10.160`    | `192.168.10.191`      | `.161` to `.190` |
| **192 - 223**   | `192.168.10.192`    | `192.168.10.223`      | `.193` to `.222` |
| **224 - 255**   | `192.168.10.224`    | `192.168.10.255`      | `.225` to `.254` |

> **💡 Pro Tip:** If a message is destined for a device in the same subnet, the sender "shouts" (broadcasts) it. If it’s for another subnet, it sends it to the **Router** for delivery.

---

## 🎭 Subnet Mask

A **Subnet Mask** is a 32-bit number used to distinguish the **Network** part from the **Host** part of an IP address.

Computers don't "see" IPs the way we do; they only understand binary. To make it human-friendly, engineers created Subnet Masks as an intermediary—think of it as a high-level language for networking.

### 🧮 Finding a Subnet Mask

To find a subnet mask, we count bits from **left to right in descending order** (starting with all `1s`).

#### **Example 1: Basic Mask**

Find the Subnet Mask for `192.168.10.0/24`.

1.  Think of the IP as a house with **4 rooms** (octets). Each room has **8 switches** (bits).
2.  Distribute the CIDR `/24` into the rooms.
    - Room 1: 8 switches (All ON)
    - Room 2: 8 switches (All ON)
    - Room 3: 8 switches (All ON) -> Total 24.
    - Room 4: 8 switches (All OFF).
3.  **Binary Form:** `11111111.11111111.11111111.00000000`
4.  **Conversion:** A room with all `1s` equals **255**. All `0s` equals **0**.
    - **Result:** `255.255.255.0`

---

#### **Example 2: Intermediate Mask**

Find the Subnet Mask for `10.1.1.50/29`.

1.  First 3 octets get 8 bits each (24 bits total, all `1s`).
2.  The remaining 5 bits (29 - 24 = 5) go into the 4th octet.
3.  **Switch Values:** `128, 64, 32, 16, 8, 4, 2, 1`.
4.  Turn ON the first 5 switches: `128 + 64 + 32 + 16 + 8 = 248`.
5.  **Result:** `255.255.255.248`

---

#### **Example 3: Tricky Mask**

Find the Subnet Mask for `172.16.0.0/20`.

1.  First 2 octets are full (16 bits total).
2.  The remaining 4 bits (20 - 16 = 4) go into the **3rd octet**.
3.  The **4th octet** remains empty (`0`).
4.  Turn ON the first 4 switches in the 3rd octet: `128 + 64 + 32 + 16 = 240`.
5.  **Result:** `255.255.240.0`

---

**_The boring and confusing stuff finally ended!_ 😁🤣**

<div align="center">

**[⬅️ Day 4: Subnetting and CIDR](./Day-04,%20Subnetting%20and%20CIDR.md)**

</div>
