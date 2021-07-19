---
topic: allas
title: Tutorial - File backup with Allas
---

# Backuping files to Allas from Puhti

**Do these preparations if not done already:**

- Login to puhti.csc.fi and move to scratch.
   - In Puhti check your environment with command:
```bash
csc-workspaces
```
   - Switch to the scratch directory of your project 
```bash
cd /scratch/project_2004306    # NOTE: Here you can use also your project
```
- Go to directory with files that you want to backup:
```bash
cd XXXX
```

**Connect to allas:**

- Open connection to Allas wih these commands:
```bash
module load allas
allas-conf 
```
   - If you have several Allas projects available, select the one where you have a bucket where you want the backup to be
- Check how the backup-tool works with command:
```bash
allas-backup -h
```
- Create the backup with command:
```bash
allas-backup your-file-name      # replace your-file-name
```
- Check what snapshots the backup contains:
```bash
allas-backup list
allas-backup list | grep $USER
```
   - Make note of the `snapshot_id` in the first column!
- Check what files your backup contains
```bash
allas-backup files <snapshot_id>      # replace the snapshot_id
```
- Restore the files from your backup
```bash
allas-backup restore <snapshot_id>      # replace the snapshot_id
```
- If you want to delete your backup use command:
```bash
allas-backup delete <snapshot_id>      # replace the snapshot_id
```