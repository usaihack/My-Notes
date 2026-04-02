# 🌐 Day 14: HTTP Methods, Tools, and Status Codes

![Networking](https://img.shields.io/badge/Networking-Basics-blue?style=for-the-badge)
![Web](https://img.shields.io/badge/Web-informational?style=for-the-badge)
![HTTP](https://img.shields.io/badge/HTTP-critical?style=for-the-badge)

> _Now that we understand the basics of Requests and Responses, it is time to decode every part of that "text conversation."_ 🌐

## 1. HTTP Methods (The "Verbs")

The first line of an HTTP request starts with a **Method**. This tells the server what action you want to take.

### 🟢 The "Big Two" (Common Traffic)

- **GET:** Used to **retrieve** data. You send your information inside the **URL** (the Header).
- **POST:** Used to **send** data. You hide your information (like usernames and passwords) inside the **Request Body**.

### 🔴 The "Dangerous" Methods (Admin Tools)

- **PUT:** Used to **upload** a file to a specific URL.
  - **Hacker Insight:** If a developer leaves this open, a hacker can upload a "Malicious Script" (a Web Shell) to get full control of the server.
  - _Note:_ If the file already exists, it is replaced. If not, it is created.
- **DELETE:** Used to **remove** data from a specific URL.
  - **Hacker Insight:** If misconfigured, a hacker can delete important files or admin accounts to create chaos.
- **PATCH:** While **PUT** replaces the whole file, **PATCH** only replaces a small part of it.

### 🔍 For Reconnaissance (Information Gathering)

- **HEAD:** It is identical to **GET**, but the server's response contains **only the headers** and no body content.
  - **Hacker Insight:** It is great for "Stealth Recon." You can check if a file exists without downloading it, which might help you stay hidden from server logs.
- **OPTIONS:** Used to ask the server, "Which methods do you allow?"
  - **Hacker Insight:** If the server says it allows **PUT** or **DELETE**, you have found a potential way in.

---

---

## 2. Practical: Burp Suite (The Hacker's Interface)

When you first open **Burp Suite (Community Edition)**, it looks like a sci-fi dashboard. For now, we only care about the **Proxy Tab**.

### The Main Parts:

1. **The Dashboard:** Shows what Burp is finding (you can ignore this for now).
2. **The Proxy Tab:** The heart of the tool.
   - **Intercept Sub-tab:** Used to "catch" requests in mid-air.
   - **HTTP History Sub-tab:** A list of every request your browser has made.

3. **The Repeater Tab:** Used to take a caught request and "repeat" it manually to see what breaks.

### 🛠️ Step 1: Setting Up the "Hacker Browser"

1. Open Burp Suite.
2. Go to **Proxy** -> **Intercept**.
3. Click **"Open Browser."** (Use Burp’s built-in browser; it’s much easier!)

### 🚦 Step 2: Your First "Interception"

1. In the Burp Browser, go to `example.com`.
2. In Burp, make sure **"Intercept is ON."**
3. Refresh the browser page.
4. **BOOM.** The browser freezes. Burp has caught the request!

### 🕵️‍♂️ Step 3: Manipulating Live Data

Look at the text in the Intercept window. You can actually edit it!

1. Find the `User-Agent` line.
2. Delete it and type: `User-Agent: HACKER-USMAN`.
3. Click the **"Forward"** button.
4. The browser finishes loading, but you just sent a custom message the server wasn't expecting.

---

---

## 3. HTTP Status Codes (The Feedback)

These are 3-digit numbers the server sends back to tell you what happened. They are divided into 5 families:

### ✅ 2xx Family (Success)

- **200 OK:** "Everything is fine, come in."
- **201 Created:** "Your file or user (via PUT/POST) was created successfully."
- **204 No Content:** "The request worked, but I have no data to send back."

### ↪️ 3xx Family (Redirection)

- **301 Moved Permanently:** "The old URL is gone forever."
- **302 Found (Temporary Redirect):** The **Hacker's Favorite**.
  - _Example:_ If your `OR 1=1` trick works, the server often sends a **302** to the `/dashboard`.

### ⚠️ 4xx Family (Client Error)

- **400 Bad Request:** "Your syntax is wrong."
- **401 Unauthorized:** "I know who you are, but you don't have the key. Log in!"
- **403 Forbidden:** "I know who you are, but you are NOT allowed here."
- **404 Not Found:** "The page does not exist."
- **405 Method Not Allowed:** "You tried a method (like DELETE) that is blocked."

### 🔥 5xx Family (Server Error)

- **500 Internal Server Error:** "The server's code crashed."
- **502 / 503:** "The server is overloaded or the backend is down."
- **504 Gateway Timeout:** "The server took too long to answer."

---

<div align="center">

**[⬅️ Day 13: HTTP](./Day-13,%20HTTP.md) | [🏠 Home](../README.md) | [Day 15: HTTP Headers - Part1 ➡️](./Day-15,%20HTTP%20Headers%20-%20Part1.md)**

</div>
