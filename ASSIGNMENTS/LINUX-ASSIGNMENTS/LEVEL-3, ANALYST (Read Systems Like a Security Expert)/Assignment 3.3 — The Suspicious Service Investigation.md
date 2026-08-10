**Scenario:** You notice high CPU usage. Investigate.

**Tasks:**

1. Open `htop` and sort by CPU
2. Run this in a separate terminal to simulate a suspicious process:
    
    ```bash
    while true; do echo "mining..." > /dev/null; done &
    ```
    
3. Go back to `htop` — find the process consuming CPU
4. Note its PID, USER, STATE, and COMMAND
5. Kill it from `htop` (press F9, select SIGKILL)
6. Check if it respawns — if it was a service, it might!
7. Now do the same thing but kill it from the command line using `kill -9 PID`
8. **Report:** How would you tell the difference between a legitimate high-CPU process and malware?


### Solution
1. I opened `htop` and clicked the CPU, it will automatically sort in descending order if the arrow is down and vice versa.
2. I pressed `ctrl + shift + R` and it opened another split terminal where I ran the above script:
   `while true; do echo "mining..." > /dev/null; done &`
3. In `htop`, the CPU usage suddenly increased, to full 100%. I noted the PID of the process.
4. In `htop`, I clicked Kill at the bottom (or press F9). In the side panel, I searched for SIGKILL which is number 9 and clicked it to kill that process consuming the highest CPU.
5. I restarted the process and killed it using signal sending.
6. For the question: *How would you tell the difference between a legitimate high-CPU process and malware?* Search or ask Gemini.
   But here's my general understanding that malwares are usually run from the `/tmp` directory, so always validate the process path.