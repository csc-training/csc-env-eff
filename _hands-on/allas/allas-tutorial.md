---
topic: allas
title: Advanced Tutorial - Using Allas (bio-data example)
---

# Using Allas in CSC HPC environment

Before the actual exercise, open a view to the Allas service in your browser using the cPouta WWW-interface.

Open: https://pouta.csc.fi

And login with your account.

From the upper left corner, you find a project selection pop-up menu. If you have several projects available, choose one of them to use in this exercise. 

Then from the menu in left side of the interface, select:

**Object Store -> Containers**

During the exercises, you can use this web interface to get another view to the buckets and objects in Allas.

> Note, that you need to **reload** the view in order to see the changes.


## A. Log in to Puhti

1. Login to puhti.csc.fi and move to your project scratch:

**Linux/mac/MobaXterm**

```bash
ssh yourcscusername@puhti.csc.fi    # replace yourcscusername with your csc user account
```

**Windows/PuTTY**

   **host:** puhti.csc.fi
 
   **login as:** yourcscusername  (replace yourcscusername with your csc user account)


In Puhti check your environment with command:

```bash
csc-workspaces
```
Switch to the scratch directory of your project 

```bash
cd /scratch/project_xxxxxxx  # note! replace xxxxxxx here (and below) with your project number
```
Create your own sub-directory, named with your user account (if this directory does not already exist):

```bash
mkdir yourcscusername      # replace yourcscusername with your user account
```

Move to the directory:

```bash
cd yourcscusername
```

## 2. Download data with curl

Next download the dataset from internet and uncompress it. The dataset contains some pythiun genomes with related BWA indexes.

```bash
curl https://a3s.fi/course_12.11.2019/pythium.tgz > pythium.tgz
ls -ltr
tar zxvf pythium.tgz  
ls -ltr
tree pythium
```

## Using Allas

Open connection to Allas:

```bash
module load allas
allas-conf 
```

💡 It might take a while with `module load allas`. 

If you have several Allas projects available, select the same project as earlier.

### Upload case 1.  rclone

Upload the data from Puhti to Allas with `rclone`:

```bash
rclone -P copyto pythium allas:xxxxxxx_yourcscusername/genomes-rc/     # replace xxxxxxx with your project number and yourcscusername with your user account
```

How long did the data upload took?
What was the transfer rate?
How long would it take to transfer 100 GiB with the same speed?

Then study what you have uploaded to Allas with commands: 

```bash
rclone lsd allas:                                    # use the same bucket as earlier, replacing xxxxxxx with your project number and yourcscusername with your user account
rclone ls allas:xxxxxxx_yourcscusername/genomes-rc/
rclone lsl allas:xxxxxxx_yourcscusername/genomes-rc/
rclone lsf allas:xxxxxxx_yourcscusername/genomes-rc/
```

Check how this looks like in the Pouta web interface. Open browser and go to: [https://pouta.csc.fi/](https://pouta.csc.fi/)

In Pouta interface, go to _object store_ section, list the buckets (which are here called as “Containers”).
Locate your own _xxxxxxx_yourcscusername_ bucket and download one of the uploaded fasta files to your local computer.

💡 You can read more about moving files from [CSC Docs: Copying files using scp](https://docs.csc.fi/data/moving/scp/) and [CSC Docs: Moving data with rclone](https://docs.csc.fi/support/faq/how-to-move-data-between-puhti-and-allas/#move-data-with-rclone)

### Upload case 2. a-put 

Upload the pythium directory from Puhti to Allas using a-commands.

A-put case 1: Store everything in one object:

```bash
 a-put pythium      
 a-list                       # replace xxxxxxx with your project number and yourcscusername with your user account
 a-list xxxxxxx-puhti-SCRATCH
 a-info xxxxxxx-puhti-SCRATCH/yourcscusername/pythium.tar
```
A-put case 2: Each subdirectory (species) as one object:

```bash
 a-put pythium/*
 a-list xxxxxxx-puhti-SCRATCH   # replace xxxxxxx with your project number and yourcscusername with your user account
 a-check pythium/*
 a-info xxxxxxx-puhti-SCRATCH/yourcscusername/pythium/pythium_vexans.tar
```

A-put case 3: Use your own bucket name:

```bash
 a-put pythium/* -b xxxxxxx-yourcscusername-genomes-ap   # replace xxxxxxx with your project number and yourcscusername with your user account
 a-list xxxxxxx-yourcscusername-genomes-ap
```

Can you see the difference between the three _a-put_ commands above?

Study the _xxxxxxx-yourcscusername-genomes-ap_ bucket with commands:

```bash
a-list xxxxxxx-yourcscusername-genomes-ap   # replace xxxxxxx with your project number and yourcscusername with your user account
rclone ls allas:xxxxxxx-yourcscusername-genomes-ap 
```

Why the two commands above list different amount of objects?

Try command:

```bash
a-info xxxxxxx-yourcscusername-genomes-ap/pythium_vexans.tar  # replace xxxxxxx with your project number and yourcscusername with your user account
```

which is actually the same as:

```bash
rclone cat allas:xxxxxxx-yourcscusername-genomes-ap/pythium_vexans.tar_ameta  # replace xxxxxxx with your project number and yourcscusername with your user account
```

Finally try command:

```bash
a-flip pythium/pythium_vexans/pythium_vexans.fasta 
```

Try opening the public link that a-flip produced, with your browser.


## Upload case 3. Allas-backup

Run commands:

```test
allas-backup -help
allas-backup pythium
allas-backup list
```

What did these commands do for your data?

## Exit

The data in pythium directory is now stored in many ways to Allas so we can remove the data from puhti and log out.

```bash
rm -r pythium
exit
```

## Downloading data from Allas to Puhti


1. Login to puhti.csc.fi and move to scratch:

Linux/mac/MobaXterm

```bash
ssh xxxx@puhti.csc.fi   (replace xxxx with your user account )
```

Windows/PuTTY

   host: __puhti.csc.fi__
 
   login as: _xxxx_  (replace xxxx with your CSC account )

In Puhti check you projects with command:

```bash
csc-workspaces
```
Go to your personal scratch directory of your project. 
```bash
cd /scratch/project_yourprojectnumber/xxxx
```
Set up Allas connection
```bash
module load allas
allas-conf 
```
Then run commands
```bash
a-list
rclone lsd allas:

a-list xxxx-genomes-ap
rclone ls allas:xxxx-genomes-ap

a-find pythium_vexans.fasta
a-find -a pythium_vexans.fasta
```

Next download the data in different ways:

## 1. Download with rclone

```bash
mkdir rclone_dir
cd rclone_dir/
```
### example 1: copy everything
```bash 
mkdir all
rclone ls allas:xxxx-genomes-rc 
rclone copyto -P allas:xxxx-genomes-rc all/
ls -l all
```

### example 2:copy a set of objects
```bash
mkdir vexans 
rclone copyto allas:xxxx-genomes-rc/pythium_vexans vexans/
ls -l vexans
```
### example 3: copy just one object
```bash
rclone copyto allas:trng_xxxx-genomes-rc/pythium_vexans/pythium_vexans.fasta  ./vexans.fasta
ls -l
```

## 2. Download with  a-get

Return to your youcscusername directory in Puhti scratch
```bash
cd ..
```
Check that you are in right place:

```bash
pwd
```

The _pwd_ command should print  /scratch/project_projnum/_youcscusername_

Make a new directory 
``text
mkdir a_dir
cd a_dir/
``
create directory _all_ and go there: 
```bash
 mkdir all
 cd all
```
list your default scratch bucket.
```bash
a-list projectnumber-puhti-SCRATCH
a-list projectnumber-puhti-SCRATCH/xxxx
```

Look for file pythium_vexans.fasta in Puhti SCRATCH  bucket:
```bash
a-find pythium_vexans.fasta -b projectnumber-puhti-SCRATCH
```
download the full dataset with command:
```bash 
a-get projectnumber-puhti-SCRATCH/trng_xxxx/pythium.tar.zst
```
And check what you got:
```bash
ls -l
ls -R
```
Now get just one genome dataset:
```
cd ..
a-get projectnumber-puhti-SCRATCH/xxxx/pythium/pythium_vexans.tar.zst
ls -l pythium/
ls -l pythium/pythium_vexans/
```


## 3. Downloading data from allas-backup
Return to your main scratch directory and make a new directory:
```bash
cd ..
mkdir a_backup
cd a_backup/
```
Use the commands below, to find out the ID of the most recent version backup of your pythium directory:
```bash
allas-backup list 
allas-backup list | grep $USER
```
Then use allas-backup restore to download the data:
```bash
allas-backup restore ID-string
ls -l
ls -l pythium
```



