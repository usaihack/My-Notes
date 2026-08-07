**Scenario:** Create a directory structure where permissions control the path.

**Setup:**

```bash
mkdir -p ~/maze/room1/room2/room3
echo "FLAG{you_found_the_secret}" > ~/maze/room1/room2/room3/flag.txt
```

**Tasks:**

1. Remove execute permission from `room2`.
2. Try to `cd` into `room2` — what happens? Why?
3. Try to `cat ~/maze/room1/room2/room3/flag.txt` — what happens?
4. Remove read permission from `room1` but keep execute
5. Try to `ls ~/maze/room1` — what happens?
6. Try to `cd ~/maze/room1` — does this work? Why?
7. Restore all permissions and read the flag
8. **Key insight to write down:** What's the difference between `r` and `x` on a directory?



### Solution
1. First of all, I ran the setup commands.
2. To remove the execute permissions from room2: `chmod -x ~/maze/room1/room2`.
3. I tried to `cd` into room2. It denied my entrance because there are no execute permissions at all.
4. I tried to cat the `flag.txt` but the permission denied error happens. This is because there is no `x` permission on room2, we cannot enter it. If we cannot enter room2, we cannot enter room3 and hence we cannot read `flag.txt`
5. I removed the read permissions room1 and kept the execute one: `chmod -r+x ~/maze/room1`
6. `ls` will be denied because there are no read permissions at all.
7. `cd` will work because entrance solely depends on the execute permissions.
8. I restored all the permissions and read the flag: `FLAG{you_found_the_secret}`
9. `r` simply means reading the content of the directory. It is like photographing the directory from a distance which you can and you're allowed. But `x` on directory means to enter it. Without `x`, `w` is not possible.