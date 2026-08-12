**Scenario:** Misconfigured permissions = attacker wins.

**Tasks:**

1. Create a "sensitive" script owned by root:
    ```bash
    echo "#!/bin/bash" > /tmp/admin_tool.sh
	echo "echo Secret: The root password hash is here" >>                               /tmp/admin_tool.sh
    sudo chmod 755 /tmp/admin_tool.sh
    sudo chown root:root /tmp/admin_tool.sh
    ```
    
2. As your normal user, can you READ it? Can you EXECUTE it? Can you MODIFY it?
3. Now simulate a misconfiguration:
    ```bash
    sudo chmod 777 /tmp/admin_tool.sh
    ```
    
4. As your normal user, MODIFY the script to add: `echo "HACKED by $(whoami)"`
5. Execute it — you just escalated from modifying a root-owned file!
6. **Fix it:** Set proper permissions (`750`) and proper ownership



### Solution
1. First of all, I created the script file and adjusted its owner and permissions as directed.
2. As a normal user, I fall in others. As others have the read and execute permissions, so I was able to read it.
3. To simulate the misconfiguration, I turned this file to a world-writeable.
4. Then I added the line `echo 'echo Hacked by $(whoami)'`. This will print the current username.
5. As I executed it, It printed me the current username.
6. As it is a vulnerability, so I adjusted the permissions so that no one else can write or execute except root.