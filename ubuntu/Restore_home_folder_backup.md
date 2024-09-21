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