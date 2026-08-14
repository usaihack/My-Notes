**Scenario:** You receive an alert: "Unknown service `update-helper` detected running as root."


> [!NOTE] For this drill, first create a fake `update-helper.service` (like in Assignment 4.1), then practice responding to it as if you discovered it in the wild.

**Step-by-step response (do each step and document it):**

1. **Identify:** `systemctl status update-helper` — is it real?
2. **Analyze:** What binary does it execute? Check the service file.
3. **Contain:** Stop and disable it immediately.
4. **Investigate:** Check when the service file was created.
5. **Check logs:** Inspect system logs.
6. **Eradicate:** Disable and remove the service file
7. **Recover:** Verify it's gone, scan for any files it created

---

### ***Solution***

***First of all, I created the fake update helper service as I did in Assignment 4.1 and then completed the rest of the Assignment 5.3***

1. On looking its `LoadedBy` section in the `status` output, the path was not as it should be. Because legitimate services are loaded by the `/usr` path like `/usr/lib`, or `/usr/sbin` etc. (You can look at the status of the other legit services to confirm their paths). As it was a different path, it look suspicious to me.
2. Our simulated fake service does not execute any binary. Instead, it executes a simple bash script, which can be found in the `[Service]` section of the service configuration file at the line starting with `ExecStart`.
3. I stopped and disabled it via the commands:
   `sudo systemctl stop update_helper`
   `sudo systemctl disable update_helper`
4. I investigated the file's creation date and time etc. by running the command: `ls -l update_helper.service`
5. I inspected the system logs via: `cat /var/log/syslog`.I viewed all the failed starting fo the service and the successful launch etc.
6. I disabled the service and removed its configuration file:
   `sudo systemctl disable update_helper`
   `sudo rm update_helper.service`
7. The only file it created was `update.log` where the script this service executed was writing the string "Updating" to it after every 3 seconds. So I removed that files also.