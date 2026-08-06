**Scenario:** Take a snapshot of your system.

**Tasks:**

1. Run `ps` — how many processes do you see? Why so few?
2. Run `ps aux` — find the process with the HIGHEST `%MEM` usage. Write down its PID, USER, and COMMAND
3. Open `htop` — sort by CPU usage. Take a mental note of the top 3
4. Start `sleep 300` in your terminal
5. Open a new terminal tab and find the PID of `sleep 300` using `ps aux | grep sleep`
6. Kill it using `kill PID`
7. Verify it's dead by running `ps aux | grep sleep` again


### Solution:
1. On running `ps`, I saw very few processes like two or three. This is because the `ps` shows only the processes originated from the current shell. It does not shows us the background processes or any other foreground processes originated from another shell.
2. I ran `ps aux` and began scrolling for the highest MEM usage process. The scrolling was a headache, so I searched how to sort by MEM usage. I found the `--sort` flag. Here's how to use it:
   `ps aux --sort=-%mem`
   The `-` minus sign is used for descending order. If we remove it, it will show the usage by MEM in ascending order. In order to read the top 10 MEM eating processes, use the `head` command:
   `ps aux --sort=-%mem | head`
   In my case, the PID, USER, and CMD for the highest MEM usage was:
   `PID = 984, USER = root, CMD = usr/lib/xorg/Xorg`
3. Now, I opened `htop` and sorted it by CPU usage (click the CPU to sort it in descending or ascending order).
4. Then I started a process `sleep 300`.
5. In another terminal, I ran `ps aux | grep 'sleep 300'`. I noted its PID.
6. Then I killed the sleep process by `kill PID`
7. By running `ps aux | grep sleep` again, I found it wasn't there and hence it was dead.