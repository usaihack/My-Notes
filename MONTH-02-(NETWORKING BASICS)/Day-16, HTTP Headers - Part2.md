# 🌐 Day 16: HTTP Headers - Part 2

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Web](https://img.shields.io/badge/Web-informational?style=for-the-badge)
![HTTP](https://img.shields.io/badge/HTTP-critical?style=for-the-badge)

> _Today’s session is a deep dive into advanced headers that hackers use to break into big systems. We focused on the **Request Hijacking** attack that won awards from PortSwigger and worked against giants like **Google** and **Netflix**._ 🌐

---

## 🏗️ 1. Request Smuggling / Hijacking

This is a high-level attack that happens because modern websites use two "guards": a **Frontend Proxy** (outer guard) and a **Backend Server** (inner guard).

### 🕵️‍♂️ The Heist Logic

An attacker sends a request that has **two different rules** for counting data at the same time: `Content-Length` (The Ruler) and `Transfer-Encoding: chunked` (The Conveyor Belt).

HTTP

```
POST / HTTP/1.1
Content-Length: 15
Transfer-Encoding: chunked

0
HELP_ME_HACK
```

- **The Outer Guard (Frontend):** He looks at `Content-Length: 15`. He counts the `0`, the blank lines (The Enter key is also counted as 2 chars i.e. `\r\n` = 2 chars), and the text `HELP_ME_HACK`. That are 15 characters. He says, "Check passed, move along."
    
- **The Inner Guard (Backend):** He looks at `Transfer-Encoding: chunked`. His rulebook says: "When you see a `0`, the request is finished." He finds the `0` and closes the connection.
    
- **The Leftover:** Because the inner guard stopped at the `0`, the text **`HELP_ME_HACK`** is still sitting in the server's memory (the buffer).
    
- **The Hijack:** When a normal user makes a request a split-second later, the server thinks: "I still have some data left from the last guy, let's bind this new request with that leftover data."
    
- **The Result:** The attacker has "smuggled" their command into the next user's session. They can use this to steal that user's cookies or data.
    

---

---

## 🎭 2. User-Agent: The Mask

If the **Host** header lies about "Where are you going?" and the **Cookie** header lies about "Who you are," the **User-Agent** header lies about **"What you are."**

This header tells the server about your OS (Windows/Mac/Linux) and your browser (Chrome/Firefox/Safari) so it can serve the right layout for mobile or desktop.

#### 🕵️‍♂️ The 5 Big "Hacker Lies"

- **Lie #1: Pretending to be Googlebot (The Paywall Bypass):** Google uses robots (crawlers) to scan sites. Some sites let these robots in for free so they appear in search results. A hacker changes their User-Agent to `Googlebot` to read "Premium" articles without paying.
    
- **Lie #2: Finding "Old & Broken" Sites:** Hackers pretend to be using ancient browsers like **Internet Explorer 6 on Windows XP**. Some servers will redirect "old" browsers to a "legacy" version of the site. These old versions are a goldmine because they usually have zero modern security.
    
- **Lie #3: The Mobile Trick:** Hackers pretend to be an iPhone (using F12) to access the mobile site. Often, mobile versions have "lazy" security—for example, a file upload box might not have a strong virus scanner on mobile.
    
- **Lie #4: Targeted Bug Triggering:** A hacker might find a bug that only happens when the server reads the word "Safari." They hide a malicious script inside the User-Agent to make the server crash or give them control.
    
- **Lie #5: WAF/Bot Bypass:** Firewalls block hacking tools like `sqlmap`. If you use it, the firewall sees the name `sqlmap` and blocks you. To fix this, we tell the tool to lie and say its name is `Chrome` instead.
    

---

---

## 👣 3. Referer: The Digital Footprints

This header (historically misspelled) tells the server where you were _just before_ you clicked the link.

### **The Traps:**

1. **Bypassing Trusted Checks:** Some bad admin panels check: "Is the user coming from the login page?" If yes, they let them in. A hacker just manually writes `Referer: https://bank.com/login` to trick the server into thinking they are an "insider."
    
2. **Information Leakage:** If you are on a private page with a secret token in the URL (`reset?token=SECRET_123`) and you click a link to an external site, your browser "tells" that external site your secret token in the Referer header!
    
3. **Open Redirects:** A hacker uses a trusted site to "vouch" for a bad site by using a redirect parameter.
    

---

---

## 🛡️ 4. Origin: The Security Badge

The **Origin** is like the Referer, but it is automatically attached by your browser. You can change your own Origin, but you cannot easily force a _victim's_ browser to lie about it.

#### **The Attack: The "Cat Video" Trap (CSRF)**

Imagine you are logged into your bank. In another tab, you watch a "Funny Cat Video" on a hacker's site.

- **The Trap:** While you watch, the hacker's site sends a hidden request to your bank to transfer money.
    
- **The Browser:** Your smart browser sees the request and attaches `Origin: funny-cats.com`.
    
- **The Choice:** If the bank is smart, it sees the wrong Origin and blocks the transfer. If it's **lazy**, it ignores the Origin, sees your login cookie, and you get hacked.
    

#### **The "CORS" Goldmine:**

Lazy developers often use a wildcard: `Access-Control-Allow-Origin: *`. This means _anyone_ can talk to the server. A hacker can then write a script to reach into the site and read your private messages.

---

---

## 🚀 5. Location: The Teleporter

This is a **Response Header**. It tells your browser: "Hey, the thing you want isn't here. Go there instead."

#### **The "Bad Guy" Hack: Open Redirect**

Hackers look for sites that use a "Redirect Parameter" like `?next=`.

- **The Trap:** Hacker sends a link: `safe-bank.com/login?next=https://evil-phishing-site.com`.
    
- **The Steps:** 1. Victim sees `safe-bank.com` and feels safe.
    
    2. Victim logs in with their real password.
    
    3. The server sees the `next` part and sends back: `Location: https://evil-phishing-site.com`.
    
    4. The victim’s browser **instantly** jumps to the hacker’s fake site.
    
    5. The victim thinks they are still at the bank and enters their credit card info when the fake site asks for it.
    

---

---

## 📊 Summary Table of the 10 Headers

| **#**  | **Header**            | **Type** | **The Hacker's "Dirty" Goal**                                         |
| ------ | --------------------- | -------- | --------------------------------------------------------------------- |
| **1**  | **Host**              | Request  | Find hidden private sites or fake password reset links.               |
| **2**  | **Cookie**            | Both     | **Session Hijacking:** Steal the ID card to log in as the user.       |
| **3**  | **Authorization**     | Request  | **JWT Cracking:** Change roles to "Admin" or crack secrets.           |
| **4**  | **Content-Type**      | Both     | **Bypass Uploads:** Upload a virus but label it as a "Photo."         |
| **5**  | **Content-Length**    | Request  | **Smuggling:** Lie about data size to hide secret commands.           |
| **6**  | **Transfer-Encoding** | Request  | **Smuggling:** Use "chunked" pieces to confuse server guards.         |
| **7**  | **User-Agent**        | Request  | **Masking:** Pretend to be Googlebot or a mobile phone.               |
| **8**  | **Referer**           | Request  | **Trust Bypass:** Lie about where you came from to enter admin areas. |
| **9**  | **Origin**            | Request  | **CSRF:** Exploit lazy servers that don't check the "Badge."          |
| **10** | **Location**          | Response | **Open Redirect:** Teleport victims to a fake phishing site.          |

---

<div align="center">

**[⬅️ Day 15: HTTP Headers - Part1](./Day-15,%20HTTP%20Headers%20-%20Part1.md) | [🏠 Home](../README.md) | [Day 17: HTTP Cookies and Sessions ➡️](./Day-17,%20HTTP%20Cookies%20and%20Sessions.md)**

</div>
