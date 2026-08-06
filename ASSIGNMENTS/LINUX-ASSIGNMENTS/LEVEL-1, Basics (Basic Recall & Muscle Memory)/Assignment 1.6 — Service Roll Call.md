**Tasks:**

1. Check if `ssh` service is running.
2. List ALL currently running services
3. Start the `ssh` service, verify it's running, then stop it.
4. Answer in a file `service_notes.txt`:
    - What is the difference between `start` and `enable`?
    - Why do hackers prefer to install malware as a service instead of a process?
    - If a service runs as `root`, why is that a "jackpot" for hackers?


### Solution:

1. I ran the command `systemctl status ssh` and it was not running.
2. I ran the command `systemctl --type=service --state=running` and it listed me 21 running services.
3. I ran the command `sudo systemctl start ssh` and then checked its status, it was running. Then I stopped it by using the command `sudo systemctl stop ssh`, verified its status again.
4. I created a file `service_notes.txt` ad answered the following questions in it:
   - `start` will start the service instantly while `enable` will make the service persistent by starting it automatically when the kali boots.
   - A service is a background process which can be faked by its name to look a legit service. It is persistent and can be start in the background automatically at the boot. Services usually run as root so it is easy to take root privileges. Service is not tied to a specific user, it is tied to the OS. On the other hand, Process is started by a user manually through terminal. It has least privileges than a service and it often dies instantly or with a restart and user has to start it again. That's why, for persistence, hackers install malware as a Service.
   - If a Service runs as `root`, it has the all the privileges an attacker wants. With it, an attacker can execute the malicious code without the system sanitizing it. The hacker will have an ultimate power which is why it is a jackpot for them.