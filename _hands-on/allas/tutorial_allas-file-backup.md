---
topic: allas
title: Tutorial - File backup with Allas
---

# Backuping files to Allas from Puhti

### Preparations (if not done already)

1. Login to puhti.csc.fi
2. In Puhti check your environment with command:
   ```bash
   csc-workspaces
   ```
3. Switch to the scratch directory of your project 
   ```bash
   cd /scratch/project_2004306    # NOTE: Here you can use also your project
   ```
4. Create your own sub-directory:
   ```bash
   mkdir YOURCSCUSERNAME      # replace YOURCSCUSERNAME
   cd YOURCSCUSERNAME
   ```

### Connecting to allas

1. Open connection to Allas wih these commands:
   ```bash
   module load allas
   allas-conf 
   ```
2. If you have several Allas projects available, select the one where you have a bucket where you want the backup to be.
3. Check how the backup-tool works with command:
   ```bash
   allas-backup -h
   ```
4. Create the backup with command:
   ```bash
   allas-backup your-file-name      # replace your-file-name
   ```
5. Check what snapshots the backup contains:
   ```bash
   allas-backup list
   allas-backup list | grep $USER
   ```
   - Make note of the `snapshot_id` in the first column!
6. Check what files your backup contains
   ```bash
   allas-backup files <snapshot_id>      # replace the snapshot_id
   ```
7. Restore the files from your backup
   ```bash
   allas-backup restore <snapshot_id>      # replace the snapshot_id
   ```
8. If you want to delete your backup use command:
   ```bash
   allas-backup delete <snapshot_id>      # replace the snapshot_id
   ```