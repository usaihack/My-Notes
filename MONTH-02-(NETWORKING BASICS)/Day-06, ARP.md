# 🔍 Day 6: Address Resolution Protocol (ARP)

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![ARP](https://img.shields.io/badge/ARP-Protocol-success?style=for-the-badge)

> _Think of ARP like a phone book. You know the person's name (IP address), but you need their phone number (MAC address) to actually call them._ 📖

---

**Address Resolution Protocol (ARP)** is used to connect Layer 3 (IP address) to Layer 2 (MAC address) in the OSI model. It works only inside the same local network (LAN) or broadcast domain.

When a device wants to send a packet, it only knows the destination IP address. To actually deliver the frame on the local network, it needs the MAC address of that IP.

### ⚙️ The Process

The process works like this:

1. The device checks its ARP table (stored in memory).
2. If the MAC address for that IP is already stored, it uses it directly.
3. If not, it broadcasts an ARP request:
   > "Who has this IP address? Tell me your MAC."
4. The device that owns that IP replies with its MAC address.
5. The sender stores this mapping (IP → MAC) in its ARP table.
6. The data is then delivered using that MAC address.

You can view your ARP table using:

```bash
arp -a
```

This works on both Windows and Kali Linux.

---

## 🛠️ Mini Practical 1

1. In your Kali VM, type:
   ```bash
   arp -a
   ```
   _You may see only one IP mapped to a MAC address, usually your router._
2. If your VM is using **NAT mode**, switch it to **Bridged mode**.  
   _Bridged mode allows your VM to become a real device on your LAN and communicate directly with other devices._
3. Find the IP address of another device connected to your LAN (for example, your phone).
4. Ping that device:
   ```bash
   ping <device_ip>
   ```
5. Now run:
   ```bash
   arp -a
   ```
   _You will see that the pinged device has been added to your ARP table._

**Conclusion:** This shows how ARP dynamically learns and stores mappings.

---

## ⚠️ Design Flaw in ARP

**ARP has no authentication mechanism.**

When a device receives an ARP reply, it blindly trusts the information and updates its ARP table. It does not verify whether the sender is legitimate.

### 🎭 Example Scenario:

- **Phone IP:** `192.168.20.2`
- **Router IP:** `192.168.20.1`
- **Router MAC:** `AA:AA:AA:AA:AA:AA`

The phone’s ARP table contains:
`192.168.20.1` → `AA:AA:AA:AA:AA:AA`

If an attacker sends a **forged ARP reply** claiming:
`192.168.20.1` → **Attacker's MAC**

The phone will update its ARP table and start sending traffic to the attacker instead of the real router.

This is the foundation of:

- **Man-in-the-Middle (MITM) attacks**
- **Traffic interception**
- **ARP spoofing**

---

## 🛠️ Mini Practical 2

1. Clear the ARP table (Linux):
   ```bash
   sudo ip neigh flush all
   ```
2. Open **Wireshark**.
3. In the display filter, type: `arp`
4. After flushing the ARP table, check it again:
   ```bash
   arp -a
   ```

You will notice that the router entry may appear again even without manual pinging.

**Why does this happen?**

- The system communicates with the router automatically (default gateway).
- Background services trigger ARP requests.
- Routers sometimes send ARP-related traffic.
- Devices may send gratuitous ARP packets.

5. Connect a new phone to the Wi-Fi network.

_You will capture its ARP request in Wireshark as it tries to resolve the gateway._

<div align="center">

**[⬅️ Day 5: Multi-Subnetting and Subnet Masks](./Day-05,%20Multi%20Subnetting%20and%20Subnet%20Masks.md)** | **[Day 7: ARP States ➡️](./Day-07,%20ARP%20States.md)**

</div>
