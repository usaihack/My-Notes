**Scenario:** Attackers often stage stolen data in `/tmp` because it's world-writable.

**Tasks:**

1. Check permissions on `/tmp`.
2. Create a "stolen" file: `echo "credit_card: 4111-1111-1111-1111" > /tmp/.stolen_data`
3. Notice the `.` prefix — it's hidden from normal `ls`
4. **As a defender**, find ALL hidden files in `/tmp`: use your own command.
5. Find files modified in the last 10 minutes in `/tmp`:
    ```bash
    find /tmp -mmin -10 -type f
    ```
    
6. Clean up and **report:** Why is `/tmp` a favorite staging area for attackers?



### Solution
1. I checked the permissions of the `/tmp` directory: `ls -ld /tmp`
2. Then I created a hidden file storing some credit card details.
3. Whenever we use `.` in the start of the file or folder, that file or folder is hidden from the normal `ls` command.
4. To check all the hidden files, we have to filter it them out by the starting `.`: `ls -a /tmp | grep '^.'`
5. To find all the files modified in the last 10 minutes: `find /tmp -mmin -10 -type f`. `-mmin` means the minimum time.
6. `/tmp` is the world-writeable directory in Linux systems and this is intentional because if any program or a service wants to dump their temporary files, they can easily stage it in the `/tmp`. No other directory in Linux is world-writeable. Also, it stores the files on the volatile memory i.e. RAM which automatically clear the logs and that's why, `/tmp` is the favorite staging folder for hackers.