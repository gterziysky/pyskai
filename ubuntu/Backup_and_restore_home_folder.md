### Backup

Mount the external drive.

```bash
# find the external drive and its file system
sudo lsblk -f
# create a mount folder (replace /backup with a desired name)
sudo mkdir /media/backup
# mount the file system
 sudo mount -t ext4 /dev/sdb /media/backup
```

[Backup](https://unix.stackexchange.com/a/43608) the user's home folder.

```bash
# Use -a for archive mode.
# This includes the -recursive flag, but it does more than that in that it preserves
# attributes, links, xattr, etc.
sudo cp -a /home/my_home /media/backup/my_home
```

The name for the backup for the home folder can be derived from the motherboard brand and type. For [Pro WS WRX80E-SAGE SE WIFI](https://www.asus.com/us/motherboards-components/motherboards/workstation/pro-ws-wrx80e-sage-se-wifi/techspec/) it can be for example  `/media/backup/asus_swrx80`.

## Change ownership of all files that belong to a specific group

To change the ownership of all files that belong to a specific group in Ubuntu, you can also use the `find` command combined with `chown`. Here’s how to do it:

### 1. Identify the Specific Group
Determine the group whose files you want to change.

### 2. Use the `find` Command
You can use the following command:

```bash
sudo find /path/to/directory -group old_group -exec chown new_user:new_group {} +
```

### Example
If you want to change all files owned by the group `old_group` in the `/home/example` directory to the user `new_user` and the group `new_group`, you would run:

```bash
sudo find /home/example -group old_group -exec chown new_user:new_group {} +
```

### Explanation:
- `sudo`: Runs the command with superuser privileges.
- `find /path/to/directory`: Specifies the directory to search. You can use `/` for the entire filesystem, but be cautious.
- `-group old_group`: Matches files that belong to `old_group`.
- `-exec chown new_user:new_group {}`: Executes the `chown` command on each found file, changing the ownership to `new_user` and `new_group`.
- `+`: This allows `find` to pass multiple files to `chown` at once for efficiency.

### 3. Verify Ownership Change
After running the command, you can verify the ownership change using:

```bash
ls -l /path/to/directory
```

### Summary
This method allows you to efficiently change the ownership of all files belonging to a specific group. If you have any further questions or need more help, feel free to ask!