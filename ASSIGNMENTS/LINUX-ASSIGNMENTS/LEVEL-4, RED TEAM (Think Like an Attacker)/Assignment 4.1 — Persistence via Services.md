**Scenario:** Understand how attackers install persistent backdoors as services.

**Tasks:**

1. Create a fake "malware" script:
    ```bash
    echo '#!/bin/bash' > /tmp/backdoor.sh
    echo 'while true; do echo "I am alive" >> /tmp/backdoor.log; sleep 10; done' >>      /tmp/backdoor.sh
    chmod +x /tmp/backdoor.sh
    ```
    
2. Create a `systemd` service file:
    ```bash
    sudo nano /etc/systemd/system/backdoor.service
    ```
    
    Contents of the `backdoor.service` file: 
    ``` bash
    [Unit]
    Description=System Health Monitor
    
    [Service]
    ExecStart=/tmp/backdoor.sh
    Restart=always
    
    [Install]
    WantedBy=multi-user.target
    ```


4. Start and enable it:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start backdoor
    sudo systemctl enable backdoor
    ```
    
5. Check it's running: `systemctl status backdoor`
6. Check the log: `cat /tmp/backdoor.log`
7. Now **play defender** — find and remove it:
    ```bash
    sudo systemctl stop backdoor
    sudo systemctl disable backdoor
    sudo rm /etc/systemd/system/backdoor.service
    sudo systemctl daemon-reload
    rm /tmp/backdoor.sh /tmp/backdoor.log
    ```



### Solution
1. First of all, I created the fake malware script so that we can simulate our red team assignment. This script will print `I am alive` every 10 seconds in the `backdoor.log` file forever. (notice `while true` infinite loop).
2. Attackers always installs malware as a service. So we also have to create a service for which we should create a service file in `/etc/systemd/system/backdoor.service`. Usually, attackers name their service file in a disguising way so to trick the user in believing it is a legit service file. But it is for learning purposes only. Don't worry, we will make its description in a disguising way.
3. Now, let's look at the contents of a service file:
``` bash
    [Unit]
    Description=System Health Monitor
    
    [Service]
    ExecStart=/tmp/backdoor.sh
    Restart=always
    
    [Install]
    WantedBy=multi-user.target
```
- The brackets `[]` called *section headers* in a service file. The system manager `systemd` is very strict about it and you cannot define your own section headers, these are pre built.
- The service file content is not any programming language as it does not have any logic or loops etc. So you don't have to master it like a programming language. You will often copy-paste other service files and modify them to make your own service file. These contents are just configurations you are telling the `systemd` manager to do this and that. But you have to know about the above basic configurations:
	- `[Unit]` is the header where we describe what the service is.
	- `[Service]` is the main section of the service file where you tell the manager which file to run and how to run.
	- `[Install]` means when to run the service, like immediately after booting etc.
- Now, look at the `Description`. How it is written fake to disguise users:` 'System Health Monitor'`.
- `ExecStart` means to execute the specified file. `Restart=always` means to make the script a Zombie. In a game, when you kill a Zombie, it stands again no matter how many time you kill it, it will stands again. In the same, we make the script a Zombie to start again and again even if it is killed by some signals or due to any error.
- `WantedBy` will make the service persistent. `multi-user.target` is the state where the system is completely woke up and is ready to login. It means to make the service persistent and start it automatically when the system is in the state of `multi-user.target`.

4. Now, reload all the services by: `sudo systemctl daemon-reload`. `Daemon` means the service in simple language. But why are we reloading the services? It is because we have added a new service. The `systemd` will not see it until we restart it and that's why, we reload the services. Then `start` the service and `enable` it. 
5. I checked its status and it was running.
6. Then I checked the log file after some intervals and the `I am alive` was increasing.
7. Now, to play the defender, I listed all the running services and found the `backdoor` service listed there. So I stopped it, disabled it, removed the fake service file, removed the script and the log file and then I ran the `daemon-reload` again so that the `systemd` can see that the service has been removed.