**Scenario:** An attacker hides a process by naming it something innocent.

**Setup:**

```bash
# Start a process disguised as a system process
bash -c 'exec -a "[kworker/0:1-events]" sleep 9999' &
```

**Tasks:**

1. Run `ps aux` — can you spot the fake process?
2. The real `[kworker]` processes are kernel threads owned by `root`. This fake one is owned by your user. Find it:
    
    ```bash
    ps aux | grep kworker
    ```
    
3. Which one is fake? (Hint: check the USER column)
4. Kill the fake one



### Solution
1. First of all, I ran the above setup command so that a fake process is created: `exec -a '[kworker/0:1-events]' sleep 9999 &`.
   Here is the breakdown of the whole command:
	- `-a` flag means alias. It is used to show the Process with our desired name `kworker` instead of `sleep`.
	- After searching, I found that `kworker` are the vital and essential processes of the kernel which run as `root` so that the system works properly.

2. Then I ran the `ps aux` by grepping the `kworker` processes.
3. I found one `kworker` process was running as `kali` and hence this is the fake process.
4. I killed it using `kill -9 PID`.