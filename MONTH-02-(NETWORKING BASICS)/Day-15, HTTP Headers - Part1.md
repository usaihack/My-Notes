# 🌐 Day 15: HTTP Headers - Part 1

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Web](https://img.shields.io/badge/Web-informational?style=for-the-badge)
![HTTP](https://img.shields.io/badge/HTTP-critical?style=for-the-badge)

> _The HTTP Header is the "Label" on the box. It tells the server who you are, what you want, and how to handle the delivery._ 🌐

---

## 📍 1. Host Header: The GPS Coordinator

A single domain (IP address) may host multiple websites on the same physical server. Some are public-facing, while others are "hidden" private admin panels. The **Host** header tells the server exactly which "apartment" in the building you want to visit.

### **The Attack: Host Header Injection**

Imagine a "Forgot Password" flow. When you request a reset, the server generates a link like:

`https://mybank.com/reset?token=abc123`

**The Logic Flaw:** How does the server know to write `mybank.com` in that URL? Often, it just reads the **Host header** you sent and it trusts it blindly.

**The "Dirty Hands" Move:** If you intercept the "forgot password" request and change the Host header to your own evil server, the request looks like this:

HTTP

```
POST /forgot-password HTTP/1.1
Host: evil-hacker.com          <-- You manually changed this!
Content-Type: application/x-www-form-urlencoded

email=victim@gmail.com
```

**The Result:** The real bank server generates a real token, but it builds the link using _your_ host. The victim receives an official email saying:

_Click here to reset: https://evil-hacker.com/reset?token=abc123

The victim clicks it, the secret token is sent to **YOUR** server logs, and you use that token on the real site to take over their account.

---

---

## 🍪 2. Cookie Header: The Identity Card

When you login, the server gives you a unique string (the Cookie) stored in the browser's "cookie bucket." Because servers have "amnesia" and forget who you are the moment a request ends, the browser automatically sends this cookie with **every** future request to prove it's you.

### **The Attack: CSRF (Cross-Site Request Forgery)**

Attackers take advantage of the fact that the browser **automatically** sends cookies. This happens because of developer laziness. For a cookie to be safe, these three "Bodyguards" must be added in the server's response:

- **No `HttpOnly`:** JavaScript can read the cookie. This means an **XSS** attack can steal it.
    
- **No `Secure`:** The cookie travels over plain HTTP (unencrypted). Anyone on your Wi-Fi (like at a café) can "sniff" it using **Wireshark**.
    
- **No `SameSite=Strict`:** This allows **CSRF** attacks. A hacker can trick you into clicking a link that makes your browser send a "Transfer Money" request to your bank, and the browser will automatically attach your login cookie!
    

### **Cookie vs. Token (The Difference)**

- **Cookie:** A string stored in a dedicated browser bucket. It is given by the server upon login and is **automatically** added to requests by the browser.
    
- **Token:** Behaves similarly but is usually stored in **Session Storage** or **Local Storage**. It is NOT sent automatically; JavaScript must add it. This makes tokens safer from CSRF but very easy to steal via **XSS** if security is poor.
    

---

---

## 🔐 3. Authorization Header: The App/API Key

This header is the standard for mobile apps and APIs. It has two main formats:

- **Basic Auth:** It simply encodes your `username:password` in **Base64**.
    
    - _Hacker Note:_ Base64 is NOT encryption. Anyone can decode it in a second.
        
    - `Authorization: Basic dXNlcjpwYXNzd29yZA==`
        
- **Bearer Token (JWT):** A JSON Web Token with three parts: `Header.Payload.Signature`.
    
    - **Header:** Tells the server how to verify the user.
        
    - **Payload:** Contains the real data (User name, role: user, etc).
        
    - **Signature:** This is the "Security Seal." (If the header/payload is changed, the signature becomes invalid).
        

### 🕵️‍♂️ The Vulnerability: JWT Manipulation

What if I change the header to `{"alg": "none"}`? A "dumb" server might be tricked into not using any authentication method at all.

**The Hack:** 
1. Change the role in the payload to `role: admin`. 
2. Change the header to `alg: none`. 
3. Delete the signature entirely. 
4. The final Token becomes `Header.Payload.` (with only two dots and no signature). Boom—you are now an Admin.

If the "none" trick is blocked, hackers use a tool called **Hashcat** to brute-force the Signature if it was generated with a weak secret password.

---

---

## 🏷️ 4. Content-Type: The Label on the Box

This tells the server what kind of data is in the "body" (HTML, JS, JSON, etc.).

### **The Attack: Content-Type Mismatch**

If a server only trusts the "Label" (the header) and doesn't look at the "Contents" (the body), it creates chaos.

**1. CSRF Bypass:** I change the header to `application/json` to trick the server into thinking it's a safe API call, but I send a malicious command in the body:

```
Content-type: application/json

amount=100000&to=hacker_account
```

The server sees the "JSON" label, trusts it blindly, and sends the body straight to the database to be processed.

**2. File Upload Shell:** I try to upload a **PHP Shell Script** (a virus that gives me total control). The server says "No PHP allowed!" **The Move:** I capture the request in **Burp Suite**, change the header to `Content-type: image/jpeg`, and hit send. The server thinks it's a photo, allows it, and now I have "Shell Access" to the entire server.

**Rule:** Never trust the user's label!

---

---

## 📏 5. Content-Length: The Ruler

This determines exactly how long the data is.

```
POST / HTTP/1.1 
Content-Length: 12

Hello World!
```

The server counts exactly 12 characters. When it hits the "!", it closes the connection.

- **The Glitch:** If I say the length is 12 but only send "Hello" (5 characters), the server will sit and **hang**, keeping the connection open forever waiting for the rest.
    

---

---

## 🔄 6. Transfer-Encoding: The Conveyor Belt

This header is used when the user isn't sure how long the data will be (like a live stream or a big file). It sends data in "chunks." It has values like chunk, zipped, compressed etc.

**The Rule:** Unlike Content-Length, which stops at a specific count, Transfer-Encoding only closes the connection when it sees a **lonely `0`** in the body.




> **Note:** In the next class, we will be starting from the attacks of Content-Length and Transfer-Encoding.

---

<div align="center">

**[⬅️ Day 14: HTTP Methods and Status Codes](./Day-14,%20HTTP%20Methods%20and%20Status%20Codes.md) | [🏠 Home](../README.md) | [Day 16: HTTP Headers - Part2 ➡️](./Day-16,%20HTTP%20Headers%20-%20Part2.md)**

</div>
