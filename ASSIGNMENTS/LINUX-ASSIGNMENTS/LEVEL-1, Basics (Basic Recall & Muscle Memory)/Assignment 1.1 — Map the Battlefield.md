**Scenario:** You just landed on an unknown Linux machine. Map it.

**Tasks:**

1. Print your current location in the filesystem
2. Navigate to `/` and list ALL contents (including hidden)
3. For each of these directories, write ONE sentence (in a file called `battlefield_map.txt`) explaining what it stores:
    - `/home`, `/etc`, `/var`, `/bin`, `/tmp`, `/root`
4. Find out which user you are logged in as
5. Find the full path to your home directory using `~`

**Deliverable:** The file `battlefield_map.txt` with your answers. Create it using ONLY terminal commands (`echo >>`)


#### Solution:
1. I navigated to Desktop `cd Desktop` and created a new Folder `mkdir Linux_Practice`
2. Then I created a file `touch battlefield_map.txt`
3. Navigated to /, `cd /` and ran `ls -a`. It listed all of the directories. Here's the one line explanation of each one:
   
| Directory | What it stores?                                                                                                                                                                                                                                                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/home`   | It contains all the users' personal directories on our system.                                                                                                                                                                                                                                                                      |
| `/etc`    | It acts as the rulebook for the current users. It has some important directories:<br>`/etc/passwd` - It is the list of current users our system has with some info<br>`/etc/shadow` - It stores the hashed passwords of the users<br>`/etc/sudoers` - It is the list which contains who can act as an admin. Usually through `sudo` |
| `/var`    | It store the variable/changing data which are stored on non-volatile memory for persistence. It includes `/var/logs`                                                                                                                                                                                                                |
| `/bin`    | It has the binaries of all the tools we run, like `ls, cd, mkdir, cat` etc.                                                                                                                                                                                                                                                         |
| `/tmp`    | It has the temporary files which are stored on the volatile memory and cleaned on reboot.                                                                                                                                                                                                                                           |
| `/root`   | It is the personal directory for the root user.                                                                                                                                                                                                                                                                                     |

4. I created it strictly via terminal commands like `echo` and some other editors like `nano` and `gedit`
   
