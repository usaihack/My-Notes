**Scenario:** The logs hold evidence. Learn to read them.

**Tasks:**

1. List all log files: `ls /var/log/`
2. Read the authentication log (records every login/sudo attempt):
    ```bash
    sudo cat /var/log/auth.log | tail -20
    ```
    
3. Find all failed login attempts:
    ```bash
    sudo grep "Failed" /var/log/auth.log
    ```
    
4. Find all successful or unsuccessful `sudo` commands:
    ```bash
    sudo grep "sudo" /var/log/auth.log | grep "COMMAND"
    ```
    
5. Check system messages:  
    ```bash
    sudo cat /var/log/syslog | tail -20
    ```


6.  **Report in `log_analysis.txt`:** What 3 things would you look for in logs if you suspected a breach?


### Solution
1. I listed all the log files using `ls /var/log`
2. I didn't find any `auth.log` files so I searched for it, Why? The answer was that the modern Linux systems has changed the logs storage directory (which you can search for). So I found a solution to install the old log storing files. I ran this command: `sudo apt install rsyslog` (Search what `rsyslog` is?)  Then I listed the log files again and found the auth log files. I did some intentional failed login attempts because the auth log files were new and then ran `sudo cat /var/log/auth.log`. Here, I found all the failed and successful login attempts.
3. To find all the failed login attempts: `sudo grep -i failed /var/log/auth.log`
4. To find all ran commands ( which are ran by users but might be successful or not )" `sudo grep 'sudo' /var/log/auth.log | grep 'COMMAND'`
5. If you want to filter out the exact successful attempts, use the above same command but with a new filter: `sudo grep 'sudo' /var/log/auth.log | grep -i 'session opened'`
6. To check for system logs: `sudo cat /var/log/syslog | tail -25`
   
   
