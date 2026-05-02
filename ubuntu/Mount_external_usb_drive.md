## Moung external USB SSD drive

* See [Mount/USB](https://help.ubuntu.com/community/Mount/USB)

Type the following:

```bash
sudo fdisk -l
```

Find your device in the list. It is probably something like /dev/sdb1 or /dev/sdc1.

To check the drive and filesystem type:

```bash
sudo lsblk -f
```

Create a new dir for the drive:

```bash
# In this specific example, the T7 stands for Samsung T7 SSD
sudo mkdir /media/T7
```

Mount the drive:

```bash
# the example drive uses the ext4 filesystem
# use the file system of your specific device
sudo mount -t ext4 /dev/sdc1 /media/T7
```

Run the following command to unmount the drive

```bash
sudo umount /dev/sdc1
```

For more information about the tags see [Mount USB](https://help.ubuntu.com/community/Mount/USB#Using_mount).

## Backup home folder to backup drive

```bash
rsync -av --ignore-existing --progress ~/ /mnt/backup_drive/home/your_username
```

## Copy home folder from backup drive

Afte the drive has been mounted:

```bash
rsync -av --ignore-existing --progress /mnt/backup_drive/home/your_username/ ~/
```

Use `--dry-run` option to test the command without actually running it:

```bash
rsync -av --ignore-existing --dry-run --progress /mnt/backup_drive/home/your_username/ ~/
```
### Set Permissions (If Necessary)

```bash
sudo chown -R your_username:your_username ~/
```