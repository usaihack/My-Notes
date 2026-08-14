**Create a file `hardening_checklist.md` and complete each task:**

1. Verify `/etc/shadow` is readable only by `root` (what permission number?)
2. Verify `/etc/passwd` is readable by all but writable only by `root`
3. Check that NO files in `/etc` have `777` permissions
4. List all services running as `root` - are any unnecessary?
5. Disable any services you don't need (document which ones)
6. Verify no world-writable files exist in `/etc` or `/bin`
7. Check `/tmp` for hidden files and suspicious scripts
8. Review the last 50 lines of `/var/log/auth.log` for anomalies
9. Verify your user is in the `sudoers` file properly
10. Document all users with `/bin/bash` shell access


---

### Solution
1. First of all, I ran `ls -l /etc/shadow`. I verified it was readable only by `root`. But I also remember that it should be at least readable by the group `shadow` also. By looking at its permissions, it was readable by `shadow`. The correct permission number for `/etc/passwd` should be `640`. (If you don't understand why the permission should be `640` and not `600`, then look at the assignment 3.5).
   
2. I looked at the output of the above command and verified it was only writeable by the `root`. Notice that question asks that file is readable by all, but for tighter security, I disabled, even read for others.
   
3. I ran the following command: `find /etc -perm 777 -type f 2>/dev/null`. The output showed me nothing and hence, there is no world-writeable files in my `/etc` directory.
   
4. After searching a lot, I found that there is no dedicated command or even a trick to show us the services running as root. Here's its explanation why?
   In Linux, almost all the services run as root (starts as root) but after that, Privilege Dropping happens. The service which started as root now changes its user to a different one like `www-data` or `postgres`. This is because to avoid any bad guy entry. This is intentional and for safety purposes. Just if you want to see the running services, run: `systemctl --type=service --state=running` or, services are also background processes, so if you wanna see the `root` processes, run: `ps aux | grep "^root"`. Always remember, `root` only starts the services, it runs as their own restricted user after that.
   
5. After listing all the running services, I had 21 services running. I gave them to [^1]Gemini to tell me which ones are not important for us. I found that `ModemManager.service` (which is used to scan mobile broadband for connectivity, but as we are in a VM, we don't need it) and `colord.service` (which is used by professional photographers and graphic designers to print their exact colors as they captured or created) are completely useless for us. So I stopped and disabled them both. 
   
6. To verify there is no world-writeable file in `/etc` and `/bin`, I ran this command: 
   `find /bin /etc -type f -perm -o+w 2>/dev/null`. The output was empty and hence there are no world-writeable files directories.

7. I listed the hidden files with `ls -a /tmp | grep "^\."` . But I wanted to find the hidden files through `find` and after asking Gemini, I found that find has a name flag also: `find /tmp -type f -name ".*" 2>/dev/null`. To find all the executables in the `/tmp`, run this: `find /tmp -type f -executable 2>/dev/null`. 
   *Search:* What is the difference between `"^\.` and `".*"`.

8. I ran the command: `cat /var/log/auth/.log | tail -50`. I didn't found any anomalies.

9. I have verified all the users in the `/etc/sudoers`. There were two users, one is the default `root` and the other was the `sudo` group which has the `%` in the start.

10. To list all the users with `/bash` or `/zsh` shell access, I ran this command: `sudo cat /etc/passwd | grep -E "/bash|/zsh`. It listed me very few users which is normal.

---

[^1]: ***Be Careful*** about sharing your data with AI tools. This is the first learning of Cybersecurity not to share your data with anyone even if it is not sensitive. But I shared with Gemini and this is safe because I am running a Virtual Machine and also, this is not a server which will reveal my sensitive data like IPs etc. This is safe to share because it only contains the service name, its description and its state.
