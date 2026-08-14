**Create `~/security_monitor.sh` — a bash script that does:**

```bash
#!/bin/bash
echo "====== SECURITY AUDIT $(date) ======"
echo ""
echo "--- Current User ---"
(write the command)
echo ""
echo "--- Users with Login Shell ---"
(write the command)
echo ""
echo "--- Running Services ---"
(write the command)
echo ""
echo "--- World-Writable Files in /tmp ---"
(write the command)
echo ""
echo "--- Hidden Files in /tmp ---"
(write the command)
echo ""
echo "--- Top 5 CPU Processes ---"
(write the command)
echo ""
echo "--- Recent Auth Failures ---"
(write the command)
echo ""
echo "====== AUDIT COMPLETE ======"
```

**Tasks:**

1. Create this script
2. Make it executable: `chmod 700 ~/security_monitor.sh`
3. Why `700` and not `755`? Write your answer.
4. Run it: `./security_monitor.sh`
5. Read the output — does anything look suspicious?


---

### ***Solution***
1. First of all, I have to complete the script by embedding commands in it. So I created a bash script file: `nano ~/security_monitor.sh` and added the following commands in its placeholders:
``` bash

#!/bin/bash
echo "====== SECURITY AUDIT $(date) ======"
echo ""
echo "--- Current User ---"
whoami
echo ""
echo "--- Users with Login Shell ---"
cat /etc/passwd | grep -E "/bash|/zsh"
echo ""
echo "--- Running Services ---"
systemctl --type=service --state=running
echo ""
echo "--- World-Writable Files in /tmp ---"
find /tmp -type f -perm -o+w 2>/dev/null
echo ""
echo "--- Hidden Files in /tmp ---"
ls -a /tmp | grep "^\."
echo ""
echo "--- Top 5 CPU Processes ---"
ps aux --sort=-%cpu | head -6
echo ""
echo "--- Recent Auth Failures ---"
grep -i Failed /var/log/auth.log
echo ""
echo "====== AUDIT COMPLETE ======"
   
```

2. Then I changed its permissions: `chmod 700 ~/security_monitor.sh`
3. The reason the permissions are `700` because we wants only the owner of the file to execute, and write to it and that's why, we kept it `700`.
4. I ran the script by `bash ~/security_monitor.sh`
5. I read the output and nothing looked suspicious.
   
---
### ***Mistakes I made in the script while writing it***
1. Instead of writing `ls -a` in finding hidden files in `tmp`, I wrote it as `ls -l` accidentally.
2. In top 5 CPU processes, I forgot adding `-` in front of the `%cpu` to sort in descending order. Also, I accidentally read the first 20 lines instead of 5. After correction, I wrote 5, which is again incorrect because the first line of `ps aux` is the title so we have to read first 6 lines in order to achieve the top 5 CPU usage processes.
3. I accidentally wrote the path to `auth.log` as `/var/auth/auth.log`