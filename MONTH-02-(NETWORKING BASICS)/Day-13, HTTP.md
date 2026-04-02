# 🌐 Day 13: HTTP

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Web](https://img.shields.io/badge/Web-informational?style=for-the-badge)
![HTTP](https://img.shields.io/badge/HTTP-critical?style=for-the-badge)

> _**HTTP (HyperText Transfer Protocol)** is the language of the web. It is a "Request-Response" protocol._ 🌐

---

## 1. What is HTTP?

- **Real-Life Example:** Think of a waiter in a restaurant. You (the **Client**) ask for a menu (the **Request**). The waiter (the **Protocol**) takes that request to the kitchen (the **Server**) and brings back your food (the **Response**).

> **Hacker Insight:** HTTP is **plain text**. If you are on an unencrypted Wi-Fi, a hacker using a tool like _Wireshark_ can read your HTTP requests exactly like reading a text message.

---

## 2. HTTP vs. HTTPS

| **Feature**       | **HTTP (Insecure)**           | **HTTPS (Secure)**                                    |
| ----------------- | ----------------------------- | ----------------------------------------------------- |
| **Encryption**    | None. Data is "in the clear." | Encrypted via **TLS/SSL**.                            |
| **Port**          | 80                            | 443                                                   |
| **Hacker's View** | Easy to "sniff" passwords.    | Must use advanced "Man-in-the-Middle" (MITM) attacks. |

---

## 3. Client vs. Server

- **The Client:** This is **you**. Your Browser (Chrome/Firefox), your mobile app, or even a Python script. The Client always _starts_ the conversation.
- **The Server:** A powerful computer (running software like Apache or Nginx) that sits and waits for requests. It holds the "goods"—databases, files, and private user data.

---

## 4. Request vs. Response

This is the heartbeat of the web. Every single "click" triggers this cycle.

### A. The Request (What you send)

HTTP

```
GET /profile.php HTTP/1.1
Host: socialmedia.com
User-Agent: Mozilla/5.0
Cookie: session_id=abc123xyz
```

- **The Verb (GET):** "Give me this file."
- **The Path (/profile.php):** Where the file is located.
- **HTTP Version**
- **Headers:** Extra info (like "I am using a phone" or "Here is my login cookie").

### B. The Response (What you get back)

HTTP

```
HTTP/1.1 200 OK
Content-Type: text/html

<html><body>Welcome, Usman!</body></html>
```

- **HTTP Version**
- **Status Code (200 OK):** "I found it, here you go!"
- **Status Message:** OK in above example.
- **Body:** The actual HTML code the browser turns into a website.

---

## 5. The "Stateless" Concept (The Amnesia Problem)

HTTP is **stateless**. This means the server has a memory of exactly **0 seconds**. It doesn't know that the person who just asked for `profile.php` is the same person who logged in 5 seconds ago.

- **How we fix it:** **Cookies.**
- **Hacker Example:** When you log in, the server gives you a "Session ID" cookie. It’s like a wristband at a concert. You show the wristband (cookie) with every request so the server knows it's still you.
- **The Attack:** If a hacker steals your cookie, they **become you** without ever needing your password.

---

## 6. What happens when you type a URL?

(Example: `https://google.com`)

1. **DNS Lookup:** Your computer turns "google.com" into an IP address (e.g., `142.250.190.46`). **Hacker trick:** DNS Spoofing can send you to a fake IP.
2. **The Handshake:** Your computer establishes a TCP connection (the "Hello" phase).
3. **The Request:** Your browser sends the HTTP GET request.
4. **Processing:** The server checks its database.
5. **The Response:** The server sends back the HTML/CSS/JS.
6. **Rendering:** Your browser paints the pretty website on your screen.

---

## 🛠️ Practical 1: "The Developer's Eye"

**Task:** See the "text" behind the beauty.

1. Open any website in **Chrome**.
2. Right-click anywhere and click **Inspect**.
3. Go to the **Network** tab.
4. **Refresh the page.**
5. Click on the first item in the list (usually the name of the website).
6. Look at **Headers**. You are now seeing the raw Request and Response.

---

<div align="center">

**[⬅️ Day 12: DNSSEC](./Day-12,%20DNSSEC.md) | [🏠 Home](../README.md) | [Day 14: HTTP Methods and Status Codes ➡️](./Day-14,%20HTTP%20Methods%20and%20Status%20Codes.md)**

</div>
