---
layout: default
title: Using Allas with bio data
parent: 7. Allas
grand_parent: Part 1
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/allas/allas-tutorial.html
---

# Using Allas in CSC's HPC environment

Before the actual exercise, open a view to the Allas service in your browser using the Puhti web interface.

1. Go to <https://www.puhti.csc.fi> and login with your account.
2. Configure an Allas S3 connection using the _Cloud storage configuration_ tool.
   - You need to first authenticate by providing your CSC password.
   - If you have several projects available, choose one that you want to use in this exercise.
3. Once you've configured a connection, select `s3allas-project_<id>` from the _Files_ dropdown menu in the top navigation bar. Replace `<id>` with the number of the project you chose to use (e.g. 2001234).
4. During the exercise, you can use this web interface to get another view to the buckets and objects in Allas.

## 1. Login to Puhti

1. Login to Puhti (open a login node shell if using the web interface):

```bash
ssh <username>@puhti.csc.fi    # replace <username> with your CSC username
```

{:style="counter-reset:step-counter 1"}
2. In Puhti, check your environment with the command:

```bash
csc-workspaces
```

{:style="counter-reset:step-counter 2"}
3. Move to the `/scratch` directory of your project

```bash
cd /scratch/<project>  # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 3"}
4. Create your own subdirectory named with your username:

```bash
mkdir -p $USER
```

{:style="counter-reset:step-counter 4"}
5. Move to the directory:

```bash
cd $USER
```

## 2. Download data with `wget`

1. Next, download a dataset and uncompress it
   - The dataset contains some pythium genomes with related BWA indexes

```bash
wget https://a3s.fi/course_12.11.2019/pythium.tgz
tar -xzvf pythium.tgz  
tree pythium
```

## 3. Using Allas

1. Open a connection to Allas:

```bash
module load allas
allas-conf 
```

{:style="counter-reset:step-counter 1"}
2. If you have several Allas projects available, select the same project as earlier

### Upload case 1: `rclone`

1. Upload the data from Puhti to Allas with `rclone`:

```bash
rclone -P copyto pythium allas:$USER-genomes-rc/
```

- How long did the data upload take?
- What was the transfer rate?
- How long would it take to transfer 100 GiB assuming the same speed?

{:style="counter-reset:step-counter 1"}
2. Study what you have uploaded to Allas with the commands:

```bash
rclone lsd allas:
rclone ls allas:$USER-genomes-rc/
rclone lsl allas:$USER-genomes-rc/
rclone lsf allas:$USER-genomes-rc/
```

{:style="counter-reset:step-counter 2"}
3. Check how this looks like in the Puhti web interface. Open a browser and go to <https://www.puhti.csc.fi/>
4. In the Puhti web interface, go to the _Files_ app and select `s3allas-project_<id>` to list the buckets of your project (replace `<id>` as needed).
5. Locate your own `$USER-genomes-rc` bucket and download one of the uploaded fasta files to your local computer

💡 You can read more about moving files at Docs CSC: [Copying files using scp](https://docs.csc.fi/data/moving/scp/) and [Moving data with rclone](https://docs.csc.fi/support/faq/how-to-move-data-between-puhti-and-allas/#move-data-with-rclone)

### Upload case 2: `a-put`

1. Upload the pythium directory from Puhti to Allas using a-commands
2. Case 1: Store everything as a single object (replace `<project number>` with your CSC project number, e.g. 2001234):

```bash
a-put pythium      
a-list
a-list <project number>-puhti-SCRATCH
a-info <project number>-puhti-SCRATCH/$USER/pythium.tar
```

{:style="counter-reset:step-counter 2"}
3. Case 2: Each subdirectory (species) as a separate object (replace `<project number>` with your CSC project number, e.g. 2001234):

```bash
a-put pythium/*
a-list <project number>-puhti-SCRATCH 
a-check pythium/*
a-info <project number>-puhti-SCRATCH/$USER/pythium/pythium_vexans.tar
```

{:style="counter-reset:step-counter 3"}
4. Case 3: Use a custom bucket name (replace `<project number>` with your project number, e.g. 2001234):

```bash
a-put pythium/* -b <project number>-$USER-genomes-ap
a-list <project number>-$USER-genomes-ap
```

{:style="counter-reset:step-counter 4"}
5. Can you see the difference between the three `a-put` commands above?
6. Study the `<project number>-$USER-genomes-ap` bucket with commands:

```bash
a-list <project number>-$USER-genomes-ap
rclone ls allas:<project number>-$USER-genomes-ap 
```

{:style="counter-reset:step-counter 6"}
7. Why do the two commands above list a different amount of objects?
8. Try the command (replace `<project number>` with your project number, e.g. 2001234):

```bash
a-info <project number>-$USER-genomes-ap/pythium_vexans.tar
```

{:style="counter-reset:step-counter 8"}
9. This command is actually the same as:

```bash
rclone cat allas:<project number>-$USER-genomes-ap/pythium_vexans.tar_ameta
```

{:style="counter-reset:step-counter 9"}
10. Finally, try the command:

```bash
a-flip pythium/pythium_vexans/pythium_vexans.fasta 
```

{:style="counter-reset:step-counter 10"}
11. Try opening the public link that `a-flip` produced with your browser

### Upload case 3: `allas-backup`

1. Run the commands:

```test
allas-backup -help
allas-backup pythium
allas-backup list
```

{:style="counter-reset:step-counter 1"}
2. What did these commands do to your data?

## 4. Exit

1. The data in the `pythium` directory is now stored in many ways in Allas, so we can remove the data from Puhti and log out:

```bash
rm -r pythium
exit
```

## 5. Downloading data from Allas to Puhti

1. Login to Puhti and move to your personal directory in your project's `/scratch`:

```bash
ssh <username>@puhti.csc.fi   # replace <username> with your CSC username
cd /scratch/<project>/$USER   # replace `<project>` with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 1"}
2. In Puhti, check you projects with the command:

```bash
csc-workspaces
```

{:style="counter-reset:step-counter 2"}
3. Set up the Allas connection:

```bash
module load allas
allas-conf 
```

{:style="counter-reset:step-counter 3"}
4. Then run the commands (we will use the same bucket that was created earlier):

```bash
a-list
rclone lsd allas:
# replace <project number> with your project number, e.g. 2001234
a-list <project number>-$USER-genomes-ap
rclone ls allas:<project number>-$USER-genomes-ap
a-find pythium_vexans.fasta
a-find -a pythium_vexans.fasta
```

{:style="counter-reset:step-counter 4"}
5. Next, download the data in different ways:

### 1. Download with `rclone`

```bash
mkdir rclone_dir
cd rclone_dir/
```

1. Copy everything:

```bash
mkdir all
rclone ls allas:<project number>-$USER-genomes-ap
rclone copyto -P allas:<project number>-$USER-genomes-ap all/
ls all
```

{:style="counter-reset:step-counter 1"}
2. Copy a set of objects:

```bash
mkdir vexans 
rclone copyto allas:$USER-genomes-rc/pythium_vexans vexans/
ls vexans
```

{:style="counter-reset:step-counter 2"}
3. Copy just one object:

```bash
rclone copyto allas:$USER-genomes-rc/pythium_vexans/pythium_vexans.fasta ./vexans.fasta
ls
```

## 2. Download with `a-get`

1. Return to your `$USER` directory under your project's `/scratch` on Puhti (The `pwd` command should print `/scratch/<project/$USER`):

```bash
cd ..
pwd
```

{:style="counter-reset:step-counter 1"}
2. Make a new directory:

```bash
mkdir a_dir
cd a_dir/
```

{:style="counter-reset:step-counter 2"}
3. Create a directory `all` and move there:

```bash
mkdir all
cd all
```

{:style="counter-reset:step-counter 3"}
4. List your default `SCRATCH` bucket (replace `<project number>` with your project number, e.g. 2001234):

```bash
a-list <project number>-puhti-SCRATCH
a-list <project number>-puhti-SCRATCH/$USER
```

{:style="counter-reset:step-counter 4"}
5. Look for the file `pythium_vexans.fasta` in your Puhti `SCRATCH` bucket:

```bash
a-find pythium_vexans.fasta -b <project number>-puhti-SCRATCH    # replace <project number> with your project number, e.g. 2001234
```

{:style="counter-reset:step-counter 5"}
6. Download the full dataset with command:

```bash
a-get <project number>-puhti-SCRATCH/$USER/pythium.tar   # replace <project number> with your project number, e.g. 2001234
```

{:style="counter-reset:step-counter 6"}
7. Check what you got:

```bash
ls -l
ls -R
```

{:style="counter-reset:step-counter 7"}
8. Now, download just a single genome dataset:

```bash
cd ..
a-get <project number>-puhti-SCRATCH/$USER/pythium/pythium_vexans.tar   # replace <project number> with your project number, e.g. 2001234
ls -l pythium/
ls -l pythium/pythium_vexans/
```

## 3. Downloading data from `allas-backup`

1. Return to your main scratch directory and make a new directory:

```bash
cd ..
mkdir a_backup
cd a_backup/
```

{:style="counter-reset:step-counter 1"}
2. Use the commands below to find out the ID of the most recent backup version of your pythium directory:

```bash
allas-backup list 
allas-backup list | grep $USER
```

{:style="counter-reset:step-counter 2"}
3. Use `allas-backup restore` to download the data:

```bash
allas-backup restore <id string>   # replace <id string> with the ID of your backup snapshot
ls -l
ls -l pythium
```
