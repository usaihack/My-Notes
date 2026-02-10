**I was busy from 16 January to 4 February, but I am back today 😉😉**

Permissions means who can do what to a file or directory.

Who means users and what means the permissions.

**Users:**

| Key | Meaning      |
| :-- | :----------- |
| u   | user (owner) |
| g   | group        |
| o   | others       |

**Permissions:**

| Key | Meaning |
| :-- | :------ |
| r   | read    |
| w   | write   |
| x   | execute |

These Permissions also have numeric values:

| Key | Value |
| :-- | :---- |
| r   | 4     |
| w   | 2     |
| x   | 1     |

**How to change permissions??**

### _For files_

We use a tool called `chmod` for changing permissions. Here's how:

1. First of all, to know the permissions of a file, use this command:
   `ls -l filename`
   This will list a string like this: `rw-r-xr-x`
   The first three characters are always for user, second three are for group, and last three are for others.
   Here, user has reading and writing permissions only, group and others both have reading and executing permissions. Very dangerous 😭😁🤣.

2. Use this for changing permissions:
   `chmod u+rwx filename`
   `+` is used for adding permissions. Here, `u`, the user will have reading, writing, and executing permissions now.

   `chmod g-wx filename`
   `-` is used to remove permissions. group has now only reading permission as writing and executing permissions have been removed.

3. For numeric method, we add the values of permissions. For example:
   `chmod 755 filename`
   First digit is for user, second is for group, third is for others. `7` is obtained by adding all the values of u, g, and o (4 + 2 + 1 = 7). Similarly 5 and 5 (4 + 1 = 5).
   Now, user has all permissions, while group and others have only reading and executing permissions.

### _For Directories:_

1. To know permissions of a directory, use `ls -ld directoryName`
2. Here, the permissions meaning changes a little bit:

| Key | Meaning                 |
| :-- | :---------------------- |
| r   | listing files           |
| w   | creating/deleting files |
| x   | entering directory      |

3. The rest of the method is same and changes permissions by `chmod` as we did for files.
4. Remember that for directories, if you want to add or delete a file (`w`), the executing permission `x` is must. Otherwise it will neither delete nor create (means write).

   ##### But why??

   Because a directory is only a bucket which stores names only. So to remove or add some elements in that bucket, you must enter the bucket first 😉 and only then can you delete or add something.

   So remember, without `x`, `w` is useless.

### _Important!!_

- execute for a file means it can be run as a program.
- execute for a folder means we can enter it.
- `chmod +x folder/file` means to add `x` to all users. For example, if initial permissions are `rw-r--r--`, then after `chmod +x folder/file`, the permissions will be `rwxr-xr-x`. `x` is used as an example. you can use any or use combined. You can use `-` also.
