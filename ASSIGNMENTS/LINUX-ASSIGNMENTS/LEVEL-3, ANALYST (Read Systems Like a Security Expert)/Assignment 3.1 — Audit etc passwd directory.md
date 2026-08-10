**Scenario:** Analyze the user database of your system.

**Tasks:**

1. Read `/etc/passwd` with `cat`
2. Each line has 7 fields separated by `:`. For the `root` line, identify:
    - Username (field 1)
    - UID — User ID (field 3)
    - GID — Group ID (field 4)
    - Home directory (field 6)
    - Default shell (field 7)
3. Count how many user accounts exist.
4. Find all accounts that have `/bin/bash` or `/bin/zsh` as their shell (these are real login accounts).
5. Find all accounts with `/usr/sbin/nologin` or `/bin/false` (these are service accounts — they can't log in)
6. Try to read `/etc/shadow` without `sudo` — what happens?
7. Read it with `sudo` — identify the hash next to your username look like?
8. **Write a report** `user_audit.txt`: How many real users vs service accounts exist? Why do service accounts exist?



### Solution

1. I read the `/etc/passwd` and it listed me a lot of accounts. Some are real human users accounts while most are the service accounts.
2. Each line has exactly seven fields separated by colons. Here's what does each field mean:
	- *Username:* The very first field is the username field.
	  
	- *Password:* The second field is `x` which means the password. I searched why is this password `x` and I found this explanation:
     In past, the real passwords were stored here. But the `/etc/passwd` must be readable by all users and applications which allow hackers to copy passwords easily and that's why, a placeholder `x` is placed which means to look for the password in a different file called `/etc/shadow`.
     
	- *UID:* This is the User ID field. I searched what does the User ID mean and I found this:
     This is the Unique ID through which the system knows the user and its permissions. For `root`, the UID is always 0. For other service accounts, it ranges from 1 to 999. And for regular human users, it is always 1000.
     
	- *GID:* This is the unique ID of the user's primary group. After asking Gemini, I found that in Linux, when a user is created, a default group is also created which is private to that user. The GID is the same as the UID but the group is stored in a different file `/etc/group` while the users are stored in `/etc/passwd`. This GID is attached to the user because in Linux, when you create a new file or folder, the system asks two questions: which user does this belongs to? and to which group does it belongs? To attach answers to these questions automatically to the file or folder, GID and UID are created. For example, if you created a file using `touch test.txt` and then run `ls -l test.txt`, you will see the output like `-rw-rw-r-- 1 kali kali 0 Jul 30 07:49 test.txt`. Look at the `kali kali`, first one is the user while the second one is the group which we didn't add but it was added automatically. This second `kali` is the primary/private group of the user `kali`.
	  
	- [^1]*GECOS:* This field has some information about the user or the service account. It is also called User Information field. It can be left blank. Learn more about GECOS here: [[https://en.wikipedia.org/wiki/Gecos_field]]  
	  
	- *Home Directory:* The user's home directory/private directory where downloads etc are saved.
	  
	- *Default Shell:* When a user logs in, the command line interface which starts immediately is the default shell. For a regular user, it is usually `/bin/bash` or `/bin/zsh`. For other service accounts, it is usually `/usr/sbin/nologin`.


3. To count the total user accounts, run this: `cat /etc/passwd | wc -l`
   
4. To find all accounts having `/bin/bash` or `/bin/zsh` as their default shell:  `grep -E "/bin/bash|/bin/zsh" /etc/passwd`.
   *Note:* `-E` flag means extended. Normal grep will think of the second pipe as a string while with `-E` flag, it will treat the second pipe a logical OR

5. For the service accounts, use the same pattern: `grep -E "/usr/sbin/nologin|/bin/false" /etc/passwd`

6. Without reading it, I will tell you: It will throw a permission denied error because it is a very sensitive file having the hashes of passwords.

7. Now, I read it with `sudo` and it throw me a bunch of usernames with their password hashes.

8. *Why do Service accounts exist?* There are many services in Linux which need root privileges. If we run every service with root privileges, it would be very dangerous because if one service gets compromised, our whole system will get compromised. To solve this security issue, Linux creates different service accounts for different services in order to isolate every service. So if a service gets compromised, only that service account will be affected without affecting our whole system.






[^1]: **GECOS** stands for **General Electric Comprehensive Operating Supervisor**.
	
	### The History
	
	In the 1960s, General Electric built massive mainframe computers that ran an operating system called GECOS. When the early versions of Unix (the ancestor of Linux) were created, they often needed to connect to these giant GECOS mainframes to run print jobs or transfer data.
	
	To make this connection work, the Unix creators added a specific field in the `/etc/passwd` file to store a user's GECOS network login information.
	
	### Why It Still Exists Today
	
	Even though those General Electric mainframes have been obsolete for decades, the structure of the `/etc/passwd` file was permanently set, and the name of the field never changed.
	
	Today, Linux systems no longer use it to connect to mainframes. Instead, it was simply repurposed as a text box to store human-readable information, like a user's full real name, phone number, or office room number.
	
	(By Gemini)
