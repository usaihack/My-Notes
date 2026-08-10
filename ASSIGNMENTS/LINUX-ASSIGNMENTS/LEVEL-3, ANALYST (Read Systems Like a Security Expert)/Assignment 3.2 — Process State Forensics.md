**Scenario:** You need to analyze what's happening on a live system.

**Tasks:**

1. Run `ps aux` and redirect the output to a file.
2. From that file, answer:
    - How many processes are in state `S` (sleeping)?
    - How many are in state `R` (running)?
    - Are there any zombie processes (`Z`)?
    - How many processes are running as `root`?
3. Create a zombie process (this is advanced but important):
``` bash
bash -c 'sleep 1 & exec sleep 60'
```

Then in another terminal run `ps aux | grep Z` — can you spot it?

 4. **Write down:** Why are zombie processes dangerous? What happens if thousands accumulate?


### Solution
1. I ran the command: `ps aux > ~/system_snapshot.txt`
2. For `S` state processes, I ran the `grep` command: `grep S ~/system_snapshot.txt`
3. For `R` state processes, I ran: `grep R ~/system_snapshot.txt`
4. For `Z` processes, I ran: `grep Z ~/system_snapshot.txt` but there were no Zombie processes.
5. Now, to create a zombie process, I ran: `bash -c 'sleep 1 & exec sleep 60'`
   *Command Breakdown:*
	- `bash -c` creates another shell in the background which runs commands as a string only.
	- When we run `bash -c` , this invisible shell receives a PID because it is also a process. Also, `sleep 1` and `sleep 60` are processes and receive PIDs. The `sleep 60` starts immediately because the `sleep 1` is in the background. 
	- `exec` means to give the PID of the `bash -c` to the `sleep 60` (`exec` is used for this purpose to give one process PID to the other). The `sleep 1` finishes immediately because it is of only 1 sec. As soon as `sleep 1` finishes, it reports to the PID of the `bash -c` to update its state to finished/gone. But on the PID of `bash -c`, there is `sleep 60` which does not know how to read and update the states of child processes and hence, the `sleep 1` goes to Zombie state.
  Then I ran `ps aux | grep Z` and I found a Zombie process there.

6.  *Why are zombie processes dangerous? What happens if thousands accumulate?*
   I asked this question from Gemini, because I didn't know its answer. Here is the explanation:
   In Linux, every process has a PID, even if it is Zombie. But, Linux has a limit of PIDs to exist at a time. Linux often allows 32768 PIDs to exist at a time. As the Zombie processes does not consume CPU or RAM, we may ran out of PIDs if there are thousands of Zombie processes and hence it is not efficient.

