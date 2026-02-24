# ☠️ Day 8: ARP Poisoning with arpspoof

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![ARP Poisoning](https://img.shields.io/badge/ARP-Poisoning-critical?style=for-the-badge)

> _Performing a manual Man-in-the-Middle attack using the command-line tool arpspoof._ 🕵️‍♂️

---

Yesterday, I used `ettercap` for ARP poisoning. It was simple and mostly automated.

But today, I performed the same attack manually using the command-line tool `arpspoof`. Here’s how I did it:

---

## Step 1: Enable IP Forwarding

Before starting, we must enable IP forwarding.

If IP forwarding is disabled, traffic from the victim will reach the attacker and stop there.  
Traffic from the router will also stop at the attacker.

But we want the victim and router to stay connected so they don’t notice anything.  
That’s how we perform a proper MITM attack.

Run:

```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
```

---

## Step 2: Poison the Victim

Split the terminal.

In the first terminal, run:

```bash
sudo arpspoof -i eth0 -t <victim_IP> <router_IP>
```

- `-i` → interface
- `-t` → target

This command tells the victim:

> "Hey, I am the router."

Now, the victim’s ARP table will store our MAC address as the router.

---

## Step 3: Poison the Router

In the second terminal, run the same command but reverse the IPs:

```bash
sudo arpspoof -i eth0 -t <router_IP> <victim_IP>
```

This tells the router:

> "Hey, I am the victim."

---

## Step 4: MITM Achieved

Now you are in the middle.

Open Wireshark and observe the traffic — especially ARP packets.

You will see how trust in ARP makes this attack possible.

---

# How to Prevent ARP Poisoning

Because ARP has no authentication, it can be spoofed easily.

Here are the two main mitigations I learned:

---

## 1️. Static ARP Entries

Instead of dynamically learning MAC addresses, you manually enter them in the ARP table.

This prevents fake ARP replies from changing the mapping.

### On Windows

1. Open Command Prompt as Administrator.
2. View ARP table:
   ```cmd
   arp -a
   ```
3. Add a static entry:

   ```cmd
   arp -s <IP> <MAC>
   ```

   Example:

   ```cmd
   arp -s 192.168.10.7 e9-60-dd-a6-f8-cc
   ```

   **Note:** Windows uses MAC addresses with dashes (`-`).

4. Verify with:

   ```cmd
   arp -a
   ```

   You will now see the entry as **static**.

5. To delete an entry:
   ```cmd
   arp -d <IP>
   ```

---

### On Linux

Add a static ARP entry:

```bash
sudo ip neigh add <IP> lladdr <MAC> dev eth0 nud permanent
```

**Example**:

```bash
sudo ip neigh add 192.168.10.8 lladdr 00:0f:2a:55:1a:7c dev eth0 nud permanent
```

- `eth0` may be different on your system. Check using `ip a`.
- `nud permanent` makes it static.

To delete:

```bash
sudo ip neigh del <IP> dev eth0
```

---

> **Note – Limitations**
>
> Static ARP entries are cleared after reboot.
> This can be solved using a start-up script.
>
> It works fine in small home networks,  
> but it is not scalable for enterprise environments.

---

## 2️. Dynamic ARP Inspection (DAI)

DAI is used in enterprise networks.

It works like this:

- Intercepts ARP packets
- Checks if IP–MAC mapping is valid
- Allows valid packets
- Drops invalid ones

### But how does it know what is valid?

It uses the **DHCP Snooping binding table**.

This table stores trusted information:

- IP address
- MAC address
- Switch port
- VLAN

If an ARP packet does not match this table, it is dropped.

---

ARP was designed for trust.  
Modern networks are not built on trust anymore.

<div align="center">

**[⬅️ Day 7: ARP States](./Day-07,%20ARP%20States.md)**

</div>
