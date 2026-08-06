**Scenario:** You found these permission strings during a security audit. Decode them WITHOUT running any commands.

**Write your answers in a file called `permission_audit.txt`:**

1. `-rwxr-xr--` → Who can read? Who can write? Who can execute?
2. `drwx------` → What type is this? Can group members enter it?
3. `-rw-rw-r--` → Convert this to numeric (three-digit) form
4. What does `chmod 644 secret.txt` actually set?
5. What does `chmod 000 secret.txt` do? Why would a hacker do this?
6. A directory has permissions `rw-` for the owner. Can the owner create files inside it? **Why or why not?** (This tests the Day 3 concept in Month1 you noted about `w` needing `x`)


### Solution:
1. First I created the file by `gedit permission_audit.txt` ( `gedit` is easy to use)
2. `-rwxr-xr--` The first `-` means the permissions are for a file. Here, `u, g, o` all can read. Only user can write and execute.
3. `drwx------` This is a directory. No, group members cannot enter this.
4. `-rw-rw-r--` 664
5. `chmod 644 secret.txt` sets `-rw-rw-r-` permissions for that file.
6. `chmod 000 secret.txt` will set the permissions of the file to `----------` having no permissions  for none of the users at all. A hacker would do this so only root owner can access the file.
7. If the owner has no `x` permission, then he is not able to enter the folder because entering a folder means executing it. Now, if he cannot enter it, he will then not be able to create or delete files inside it because of that bucket analogy we gave in Month1 Kali Basics.