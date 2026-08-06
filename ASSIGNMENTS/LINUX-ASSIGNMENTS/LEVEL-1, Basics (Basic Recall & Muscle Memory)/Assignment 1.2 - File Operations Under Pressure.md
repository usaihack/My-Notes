**Scenario:** You need to create an evidence folder structure quickly.

**Tasks:**

1. Create this exact directory structure in ONE chained command (`&&`):

    `~/evidence/
    `├── logs/`
    `├── passwords/`
    `└── screenshots/`
    
2. Create 5 empty files inside `~/evidence/logs/` named `day1.log` through `day5.log`
3. Write "BREACH DETECTED" into `day1.log` (overwrite mode)
4. Append "Attacker IP: 192.168.1.100" to `day1.log`
5. Copy `day1.log` to `~/evidence/passwords/` and rename the copy to `alert.txt` in a single command
6. Display only the LAST line of `alert.txt`
7. Delete the entire `~/evidence/screenshots/` directory

**Verify:** Run `ls -R ~/evidence/` and confirm the structure matches expectations

### Solution:

1. To create a nested folder structure in one command, we can do it in two ways. First is the simple `mkdir` command which we will chain for every folder through `&&` operator:
   `mkdir evidence && mkdir logs && mkdir passwords && mkdir screenshots`.
   But this is the same as creating the folders one by one through terminal. So I searched and found the `-p` flag and the curly braces. Here's how to create the above nested structure:
   `mkdir -p evidence/{logs,passwords,screenshots}`
   - `-p` flag is telling the machine that if this parent directory (evidence) exists, just exit silently, otherwise create it.
   - `{}` are used for creating multiple sub-folders at once without typing the parent directory again and again. One single folder cannot be created through this. The sub-directory names will be separated by commas and ensure there is no space after or before the comma (This is must), otherwise it will throw an error.

2. First of all, I searched how to create multiple files at once which are similar but differ by only a letter or a number like `day1.log` through `day5.log`. I found a small bash script for this. Here's how:
   `touch day{1..5}.log`
   This will automatically creates files from `day1.log` through `day5.log`

3. Now to write to `day1.log`:
   `echo 'BREACH DETECTED > evidence/logs/day1.log` 
4. Appending to file:
   `echo 'Attacker IP: 192.168.1.100' >> evidence/logs/day1.log`
5. Copying and renaming in single command:
   `cp evidence/logs/day1.log ~/evidence/passwords/alert.txt`
6. To display only the last line of `alert.txt`:
   `tail -1 alert.txt` or `tail -n 1 alert.txt`
7. Deleting the sub-directory:
   `rmdir ~/evidence/screenshots`
8. For Verification:
   `ls -R evidence` or `tree evidence`