**Scenario:** Use pipes to extract intelligence from the system.

**Tasks (each must be ONE command using pipes `|`):**

1. List all processes and filter only those owned by `root`
2. Count how many processes are currently running.
3. Find all running services that contain the word "network"
4. Display the contents of `/etc/passwd` and show only lines containing "root"
5. List all files in `/etc` and display only the first 5 results
6. Chain 3 commands: list all processes → filter for "sleep" → count them


### Solution
1. To list all processes and filter them by `root` ownership, run this command: `ps aux | grep root`. But after running this, I realized that this command will filter out all the `root` words even if they are somewhere in the middle of a line and in the actual process output, the USER is the first word means in the first column. So I searched isn't there any way to filter out the USER from the processes output so we see the lines only containing `root` in the start? Then I found this pattern: `ps aux | grep '^root'` . The `^` sign is used to search for the string in the very start of the line. The result was absolutely amazing. In the first command, it showed me 164 lines, while in the second one, it showed me 163 lines which is why the second command is efficient.
2. In processes output, every line represents a single process, so we have to count all the lines in the `ps aux` output: `ps aux | wc -l`. 
   `wc` means word count while the `-l` flag means by line.
   But it will give us one extra line count because the header line will also be included in so we will subtract 1 from the output.
3. To list all the running services having the word network, we can use" `systemctl --type=service --state=running | grep network` 
   But it will show nothing or very few because there might be Network (with capital N) while we are searching for network (with lowercase n). So to avoid case sensitivity, use the `-i` flag which means ignore: `systemctl --type=service --state=running | grep -i network` 
   Always use `-i` even if there is no need. This is my personal recommendation.
4. Now to display the contents of the `/etc/passwd` with the lines containing root:
   `sudo cat /etc/passwd | grep -i root` 
5. For this one, I used `head -5 /etc` but the output said `/etc` is a directory and I realized `head` is used for files. So I searched how to display the first five files only. I found this: `ls /etc | head -5`.
6. To chain three commands: `ps aux | grep sleep | wc -l`