# 📊 Day 7: ARP States & MAC Spoofing

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![ARP States](https://img.shields.io/badge/ARP-States-success?style=for-the-badge)

> _A device needs to maintain the status of its ARP cache to know when a MAC address is reliable, questionable, or dead._ 🕵️‍♂️

---

## 🗂️ ARP Entries

There are two main types of ARP entries:

1. **Dynamic**
2. **Static**

---

### 1. 🔄 Dynamic

The device dynamically learns the MAC address of another device it wants to communicate with. These entries are temporary and expire after some time.

Dynamic entries have different states:

- **INCOMPLETE:**  
  The device knows the IP address but has not yet learned the MAC address.
- **REACHABLE:**  
  The device successfully mapped the MAC address to the IP and can communicate.
- **STALE:**  
  The MAC address is known, but it has not been used recently. It may still be valid, but the device is unsure.
- **DELAY:**  
  Instead of immediately sending a new ARP request, the device tries sending data to the existing MAC address. If communication succeeds, the entry becomes valid again. Otherwise, it proceeds to PROBE.
- **PROBE:**  
  The device sends ARP requests to verify whether the MAC address is still reachable.
- **FAILED:**  
  The device could not confirm the MAC address after multiple attempts. The entry is marked unreachable.

---

### 2. 📌 Static

A static ARP entry is manually configured by mapping an IP address to a MAC address. It does not expire automatically and remains permanent unless manually removed.

---

## 🛠️ Real Hands-On Practice

### 🎭 MAC Spoofing

**Step 1:** Disable the interface

```bash
sudo ip link set eth0 down
```

**Step 2:** Change the MAC address

```bash
sudo ip link set eth0 address XX:XX:XX:XX:XX:XX
```

**Step 3:** Enable the interface again

```bash
sudo ip link set eth0 up
```

---

### ⚠️ What Happens If You Spoof the Router’s MAC?

Spoofing a MAC address does not give unlimited access. If you change your MAC address to match the router’s MAC:

- Other devices still have the router’s real MAC cached in their ARP tables.
- Now two devices on the same network are using the same MAC address.
- The switch becomes confused.

This results in **MAC Flapping**.

---

### 🦅 What is MAC Flapping?

Layer 2 switches maintain a MAC address table that maps:

`MAC Address → Switch Port`

**Example:**

- **Router's MAC** → Port 1
- **Spoofed MAC** → Port 2

When both devices send traffic, the switch keeps updating the table between Port 1 and Port 2 for the same MAC address.

This constant switching of port mappings is called **MAC Flapping**.

---

## ☠️ ARP Poisoning (Man-in-the-Middle)

**ARP Poisoning** (or ARP Spoofing) is an attack where the attacker sends falsified ARP messages over a local area network to link their MAC address with the IP address of a legitimate server or router.

### 🛠️ Steps to Perform ARP Poisoning (As Covered in the Video)

1. **Spoofing the Target:** The attacker sends continuous, forged ARP messages claiming to be the default gateway/router (e.g., `192.168.1.254`).
2. **Victim's Cache Update:** The victim's machine updates its ARP table (`arp -a`). The router's IP is now mapped to the attacker's MAC address (e.g., a Kali machine).
3. **Intercepting Traffic:** The victim visits an unencrypted website (like an `HTTP` login page) and inputs credentials. Believing the attacker is the router, the victim's machine sends all traffic to the attacker.
4. **Capturing Data in Wireshark:** The attacker's Kali machine acts as a Man-in-the-Middle. The attacker filters Wireshark for the web server's IP (`ip.addr == 10.10.10.10`), noticing the destination MAC is their own. They can find the password by filtering for the payload (e.g., `frame contains PWD`).
5. **Automated Extraction:** Alternatively, attackers can use tools like **Ettercap** to quickly parse and extract plaintext user credentials, files, and confidential information from the packet stream.

### 🛡️ Mitigation Strategies

- **Data Encryption:** This attack relies on cleartext protocols (HTTP, FTP, Telnet). Since most internet traffic today is encrypted (HTTPS), this limits the useful data an attacker can extract.
- **Dynamic ARP Inspection (DAI):** Corporate networks can configure DAI on switches to validate ARP packets and block malicious ARP spoofing attacks entirely.

> 🎥 **Reference Video:**
>
> <iframe width="560" height="315" src="https://www.youtube.com/embed/A7nih6SANYs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div align="center">

**[⬅️ Day 6: ARP](./Day-06,%20ARP.md)** | **[Day 8: ARP Poisoning with arpspoof ➡️](./Day-08,%20ARP%20Poisoning%20with%20arpspoof.md)**

</div>
