**Scenario:** You have 3 sensitive files that need different access levels.

**Setup:**

``` bash

mkdir ~/classified

touch ~/classified/public_notice.txt

touch ~/classified/internal_memo.txt

touch ~/classified/top_secret.txt

echo "Company picnic on Friday!" > ~/classified/public_notice.txt

echo "Q3 revenue: $2.4M" > ~/classified/internal_memo.txt

echo "Root password: hunter2" > ~/classified/top_secret.txt
```

**Tasks:**

1. Set `public_notice.txt` → everyone can read, only owner can write.
2. Set `internal_memo.txt` → owner can read/write, group can read only, others get NOTHING
3. Set `top_secret.txt` → ONLY the owner can read. Nobody else. Not even read.
4. Verify all three with `ls -l`
5. Try to `cat top_secret.txt` as a different user - what happens?
6. Change the owner of `top_secret.txt` to `root`
7. Now try to read it as your normal user — what happens and why?


### Solution
1. First of all, I ran the above commands to set up a simulated scenario.
2. Then I created a file `touch public_notice.txt` and set its permissions as `chmod 644 public_notice.txt`.
3. Then I created another file `touch internal_memo.txt` and set its permissions as `chmod 640 internal_memo.txt`.
4. I created third file `touch top_secret.txt` and set its permissions to `chmod 400 top_secret.txt`.
5. Verified the permission of all the three files through `ls -l public_notice.txt internal_memo.txt top_secret.txt`.
6. I searched that how to `cat` a file as a different user and found the `-u` flag. I ran this command: `sudo -u nobody cat top_secret.txt`
   Here, `nobody` is an actual user on our system, otherwise it will throw an error. While I ran that command, it says `permission denied` which is obvious because only the current user (which is `kali` in my case) can read it.
7. Now, I ran `sudo chown root top_secret.txt` to change the owner to `root`.
8. And then `cat` it without `sudo` which shows me a permission denied error because the owner is `root` now.