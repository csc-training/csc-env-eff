---
layout: default
title: File backup with Allas
parent: 7. Allas
grand_parent: Part 1
nav_order: 2
has_children: false
has_toc: false
permalink: /hands-on/allas/tutorial_allas-file-backup.html
---


# Backing up files to Allas from Puhti

## Preparations (if not done already)

1. Login to `puhti.csc.fi` (open a login node shell if using the web interface)
2. In Puhti, check your environment with the command:

```bash
csc-workspaces
```

{:style="counter-reset:step-counter 2"}
3. Switch to the `/scratch` directory of your project

```bash
cd /scratch/<project>    # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 3"}
4. Create your own subdirectory named as your username (tip! your username is automatically stored in the environment variable `$USER`):

```bash
mkdir -p $USER
cd $USER
```

## Connecting to Allas

1. Open a connection to Allas wih these commands:

```bash
module load allas
allas-conf 
```

💡 It might take a while to run `module load allas`.

{:style="counter-reset:step-counter 1"}
2. If you have several projects with the Allas service available, select the one where you want to perform the backup.
3. Check how the `allas-backup` tool works with the command:

```bash
allas-backup -h
```

{:style="counter-reset:step-counter 3"}
4. Create a backup snapshot with the command:

```bash
allas-backup <filename>    # replace <filename> with the name of the file that you want to backup
```

{:style="counter-reset:step-counter 4"}
5. Check what snapshots the backup contains:

```bash
allas-backup list
allas-backup list | grep $USER
```

- Make note of the snapshot `ID` in the first column!

{:style="counter-reset:step-counter 5"}
6. Check what files your backup contains:

```bash
allas-backup files <snapshot_id>      # replace the <snapshot_id>
```

{:style="counter-reset:step-counter 6"}
7. Restore the files from your backup to Puhti:

```bash
allas-backup restore <snapshot_id>      # replace the <snapshot_id>
```

{:style="counter-reset:step-counter 7"}
8. If you want to delete your backup, use command:

```bash
allas-backup delete <snapshot_id>      # replace the <snapshot_id>
```
