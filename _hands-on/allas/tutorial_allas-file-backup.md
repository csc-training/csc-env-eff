---
topic: allas
title: Tutorial - File backup with Allas
---

# Backuping files to Allas from Puhti

**Do these preparations if not done already:**

- Login to puhti.csc.fi and move to scratch.
   - In Puhti check your environment with command:
```text
csc-workspaces
```
   - Switch to the scratch directory of your project 
```text
cd /scratch/project_2004306    # NOTE: Here you can use also your project
```
- Go to directory with files that you want to backup:
```text
cd XXXX
```

**Connect to allas:**

- Open connection to Allas wih these commands:
```text
module load allas
allas-conf 
```
   - If you have several Allas projects available, select the one where you have a bucket where you want the backup to be
- Check how the backup-tool works with command:
```text
allas-backup -h
```
- Create the backup with command:
```text
allas-backup your-file-name      # replace your-file-name
```
- Check what snapshots the backup contains:
```text
allas-backup list
allas-backup list | grep $USER
```
   - Make note of the `snapshot_id` in the first column!
- Check what files your backup contains
```text
allas-backup files <snapshot_id>      # replace the snapshot_id
```
- Restore the files from your backup
```text
allas-backup restore <snapshot_id>      # replace the snapshot_id
```
- If you want to delete your backup use command:
```text
allas-backup delete <snapshot_id>      # replace the snapshot_id
```