**Scenario:** You're hired as a junior security analyst. Your first task: audit a Linux machine.

**Create a comprehensive report `full_audit_report.txt` covering:**

1. **User Audit**
    - Total user count
    - Users with shell access
    - Users with `sudo` privileges (check `/etc/sudoers` or `grep sudo /etc/group`)
      
2. **Permission Audit**
    - Permissions on `/etc/passwd`, `/etc/shadow`, `/etc/sudoers`
    - Any world-writable files in critical directories
    - Any files with dangerous permissions (777)
      
3. **Process Audit**
    - Total running processes
    - Processes running as root
    - Any suspicious or unfamiliar processes
    - Any zombie processes
      
4. **Service Audit**
    - All running services
    - Services enabled at boot
    - Any services with suspicious names or descriptions
      
5. **Filesystem Audit**
    - Hidden files in `/tmp`
    - Recently modified files in `/etc` (last 24 hours):
    - Available disk space: `df -h`
      
6. **Log Audit**
    - Last 10 authentication events
    - Any failed login attempts
    - Any `sudo` commands executed today

---

### ***Solution***
1. ***User Audit***
	- I ran `cat /etc/passwd | wc -l` and found there were 59 accounts. These are overall accounts i.e. Service accounts and real users accounts.
	- I ran the command `cat /etc/passwd | grep -E "/bin|/zsh | wc -l` and found there were only 3 accounts having shell access.
	- I checked `sudoers` file and found a `sudo` group which has `ALL(ALL:ALL) All` rules set.
	  
2. ***Permission Audit***
	- I ran `ls -l /etc/sudoers /etc/shadow /etc/passwd` and verified the permissions which were read-only for all the users. Only `/passwd` and `/shadow` can be written by the owner `root`.
	- I ran `find /etc -type f -perm -o+w 2>/dev/null` and found no world-writeable files.
	- I ran the command `sudo find -type f -perm 777` and found no files with critical permissions.

3. ***Process Audit***
	- Total running processes = `ps aux | wc -l` - 1
    - Processes running as root = `ps aux | grep "^root"`
    - Any suspicious or unfamiliar processes = Not Found
    - Any zombie processes = None found

4. ***Service Audit***
	- All running services = `systemctl --type=service --state=running`
    - Services enabled at boot = `systemctl list-unit-files --type=service --state=running`
    - Any services with suspicious names or descriptions = None found

5.  ***Filesystem Audit****
    - Hidden files in `/tmp` = `ls -a | grep "^\."`
    - Recently modified files in `/etc` (last 24 hours): `find /etc -mmin -1 2>/dev/null`. But wait, `-mmin` is used for modified minute, the correct flag to use is `-mtime`. Be careful!!
    - Available disk space: `df -h`

6. ***Log Audit***
    - Last 10 authentication events = `cat /var/log/auth.log | tail -10`
    - Any failed login attempts = `grep -i failed /var/log/auth.log`
    - Any `sudo` commands executed today = `grep sudo /var/log/auth.log | grep COMMAND`