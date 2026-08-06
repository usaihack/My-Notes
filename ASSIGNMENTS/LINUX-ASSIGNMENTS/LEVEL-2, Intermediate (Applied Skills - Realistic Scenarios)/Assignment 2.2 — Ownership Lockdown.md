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
5. Try to `cat top_secret.txt` as a different user (use `sudo -u nobody cat ~/classified/top_secret.txt`) — what happens?
6. Change the owner of `top_secret.txt` to `root`
7. Now try to read it as your normal user — what happens and why?

**Write your observations in `~/classified/access_log.txt`**