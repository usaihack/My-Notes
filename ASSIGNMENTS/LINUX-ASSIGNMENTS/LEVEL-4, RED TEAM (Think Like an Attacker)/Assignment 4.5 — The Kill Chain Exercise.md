**Scenario:** Execute a mini kill chain using ONLY what you've learned in Month 1.

**Complete these steps in order and document each:**

1. **Recon:** List all users, list all running services, check who you are
2. **Foothold:** Create a hidden file in `/tmp`, place a script that writes "connected" to a log every 5 seconds
3. **Persistence:** Make it survive by turning it into a service (like Assignment 4.1)
4. **Privilege Check:** What user is the service running as? Can you make it run as root?
5. **Cover Tracks:** What log files would record your actions? (`/var/log/auth.log`, `/var/log/syslog`)
6. **Cleanup:** Remove everything — service, script, directory, and verify no traces remain



### Solution
1. In Reconnaissance, I ran listed all the users by `grep -E 'bash|zsh /etc/passwd`. Then I checked who I am? I am `kali`.
2. I created a hidden file in `/tmp`: `nano .hidden.sh` and placed a simple script inside it, which is only bash script I know: 
``` bash
   #!/bin/bash
   while true; do echo "Hacked" >> /tmp/.hidden.log; sleep 5; done
```
I logged the output to a hidden `.hidden.log` file also. Then I added `x` permissions to the user with `chmod u+x /tmp/.hidden.sh` and then executed it by `bash /tmp/.hidden.sh &` and started it in the background. Then killed it after some time and then viewed the log file which has the `Hacked` appended to it multiple times.

3. To make the above script a persistent service, I created a service file: `sudo nano /etc/systemd/system/hidden.service` and added the following persistent service configuration template:
``` bash
[Unit]
Description=Network Monitor

[Service]
ExecStart=/tmp/.hidden.sh
Restart=always

[Install]
WantedBy=multi-user.target
```
Then I ran the following commands which I know what do they mean:
```bash
sudo systemctl daemon-reload

sudo systemctl start hidden.service

sudo systemctl enable hidden.service
```
Then I verified its status and it was running. The log file was constantly updating.

4. I didn't know how to check which user the service is running as? Because Linux does not have a specific command for it. So I searched the Internet and found a very best command for this:
   `systemctl show hidden.service -p User`.
   Its output will show `User=<something>`. If the `<something>` is blank, it means the process is running as root. If it is something else, then it is running as another user.
   When I checked my fake service, I found it was running as root.
   
   Now that how to change the user of a process, we cannot change it directly like through `chown` etc. Instead, we have to edit the service configuration file and explicitly add the User. You can do it by two ways but I did it by the first method:
```bash
# First
sudo nano /etc/systemd/system/hidden.service

# Second Method
sudo systemctl edit hidden.service
# But remember, in this second method, you have to add the lines at the very top and do not add the hash symbol '#' in the start of the line
   
```
Then I ran the `daemon-reload`. But on checking the status of the service, It showed me permission denied to the `/tmp/.hidden.log` file. This was because the owner of the log file was root while the service was running as `kali` now. So I changed the owner of the log file to kali and then the issue resolved.

5. For this, I checked both of the files. Because the `auth.log` records the authentication and authorization whether they are failed or successful, and we used `sudo` a lot, so this file also logged my authentication behavior. `syslog` usually records system logs like running processes and services. As we are running a service, that's why it gets recorded in `syslog`.
   So, Both of the files will record our actions.
6. I deleted and cleaned everything related to our assignment.