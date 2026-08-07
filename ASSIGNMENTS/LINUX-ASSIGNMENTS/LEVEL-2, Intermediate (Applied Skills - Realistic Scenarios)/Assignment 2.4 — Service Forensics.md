**Scenario:** You suspect someone enabled a dangerous service to start at boot.

**Tasks:**

1. List all running services
2. Check if `ssh` is **enabled**. If enabled, disable it and then verify.
3. Question: If you found an unknown service called `cryptominer.service` running as root and enabled at boot, what exact 3 commands would you run to neutralize it?



### Solution
1. I listed all the running services using the command: `systemctl --type=service --state=running`
2. I verified the `ssh` was not enabled: `systemctl is-enabled shh`.
3. I will run the following three commands to neutralize it:
   - `sudo systemctl stop cryptominer.service`
   - `sudo systemctl disable cryptominer.service`
   - `sudo systemctl mask cryptominer.service`
     
     The `mask` is new to me so I asked Gemini what does it mean:
     The `mask` points the service file to a new location which is `/dev/null`. So when anyone or any program wants to start the service again, the service file will points to the `/dev/null`, which is an absolutely empty file in Linux, resulting in a silent scenario without starting the service.
