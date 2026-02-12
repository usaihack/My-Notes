# 🛠️ Day 8: Linux Services

![Linux](https://img.shields.io/badge/Linux-Services-blue?style=for-the-badge)
![Systemd](https://img.shields.io/badge/Manager-Systemd-orange?style=for-the-badge)

> _Services are the silent workers of your operating system._ 👷‍♂️

---

## 🆚 Service vs. Process

A **Service** is essentially a process that runs in the background, often starting automatically at boot.

| Feature      | Service 🛠️          | Process 🏃          |
| :----------- | :------------------ | :------------------ |
| **Start**    | Automatic or Manual | Manual (User)       |
| **Mode**     | Background (Daemon) | Foreground (mostly) |
| **Lifespan** | Long-running        | Often short-lived   |
| **Example**  | `ssh`, `apache2`    | `ls`, `cd`, `cat`   |

> **Note:** In Kali, **`systemd`** is the manager that controls these services.

---

## 🕹️ Essential Service Commands

Manage your services using `systemctl`.

### 1. Check Status

```bash
systemctl status ssh
```

_Look for `Active: active (running)` to confirm it's working._

### 2. Start a Service

```bash
sudo systemctl start ssh
```

_Starts the service immediately._

### 3. Stop a Service

```bash
sudo systemctl stop ssh
```

_Stops the service immediately._

### 4. Enable at Boot

```bash
sudo systemctl enable ssh
```

_Ensures the service starts automatically when you turn on the computer._

### 5. Disable at Boot

```bash
sudo systemctl disable ssh
```

_Prevents the service from starting automatically._

### 6. Restart

```bash
sudo systemctl restart ssh
```

_Stops and then starts the service (useful for applying config changes)._

### 7. List Running Services

```bash
systemctl --type=service --state=running
```

---

## ⚠️ Why Services Matter?

Understanding services is critical for security:

- **Target:** Hackers often target services rather than simple processes.
- **Persistence:** Malware often installs itself as a service to run continuously in the background using misleading names to hide.
- **Privilege:** If a vulnerable service runs as `root`, compromising it gives the attacker **full** control. 👻

---

<div align="center">

**[⬅️ Day 7: Process States](./Day-07,%20STATES%20of%20Processes.md)** • **[🏠 Back to Home](./README.md)**

</div>
