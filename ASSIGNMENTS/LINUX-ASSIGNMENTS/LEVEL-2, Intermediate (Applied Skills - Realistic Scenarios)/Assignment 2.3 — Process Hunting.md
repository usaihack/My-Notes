**Scenario:** Three suspicious processes are running. Find and eliminate them in the correct order.

**Setup (run in 3 separate terminals or use `&`):**

```bash
sleep 1000 &
sleep 2000 &
sleep 3000 &
```

**Tasks:**

1. List all your running jobs using `jobs`
2. Find all three sleep processes.
3. Send `SIGSTOP` to the first one — verify its state becomes `T`
4. Send `SIGTERM` to the second one — verify it's gone
5. Send `SIGCONT` to the first one — what state is it now?
6. Force kill the third one using `SIGKILL` — verify it's gone
7. Clean up: kill all remaining sleep processes


### Solution
1. First, I ran the above three commands in the same terminal and started three sleep processes in the background (`&` is used to start the processes in the background).
2. I ran `jobs` and it listed me all the current processes originated from the current shell with their PIDs and job numbers.
3. Then I ran the command `ps aux | grep sleep` and found all the processes were running.
4. Then I ran the command `kill -SIGSTOP PID` to send a SIGSTOP signal to the first `sleep 1000` job to freeze it and then ran the `ps aux | grep sleep` again and verified the state was `T`.
5. I sent a SIGTERM signal to the `sleep 2000` job: `kill -15 PID`, verified it was dead.
6. Again to the `sleep 1000`, I sent a SIGCONT signal: `kill -18 PID`, verified it started again.
7. I killed the third process i.e. `sleep 3000` forcefully by sending it a SIGKILL signal: `kill -9 PID`. Verified it was gone.
8. Then I killed all the running or freeze processes.