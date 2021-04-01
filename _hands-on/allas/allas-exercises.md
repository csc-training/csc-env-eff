---
topic: allas
title: Tutorial - Using Allas in CSC HPC environment
---

# Using Allas in CSC HPC environment

Before the actual exercise, open the view to the Allas service in your browser using the cPouta WWW-interface.

Open: https://pouta.csc.fi

And login with your account.

From the upper left corner, you find a project selection pop-up menu. If you have several projects available, select the
training project: **project_2002389**

Then from the menu in left side of the interface, select:

**Object Store -> Containers**

During the exercises, you can use this interface to get another view to the buckets and objects in Allas.

> Note, that you need to **reload** the view in order to see the changes.


## A. Log in Puhti and use scratch

1. Login to puhti.csc.fi and move to scratch:

**Linux/mac/MobaXterm**
```text
ssh XXXX@puhti.csc.fi   (replace XXXX with your csc user account)
```

**Windows/PuTTY**

   **host:** puhti.csc.fi
 
   **login as:** XXXX  (replace XXXX with your csc user account)


In Puhti check your environment with command:
```text
csc-workspaces
```
Switch to the scratch directory of your project 
```text
cd /scratch/project_2002389  # note! replace the text here (and below) with your project
```
And create your own sub-directory, named after your training account (if this directory does not yet exist):
```text
mkdir XXXX 
```
(replace XXXX with your user account)

move to the directory.
```text
cd XXXX
```

## 2. Download data with curl
Next download a dataset from internet and uncompress it. The dataset contains some pythiun genomes with related BWA indexes.

```text
curl https://a3s.fi/course_12.11.2019/pythium.tgz > pythium.tgz
ls -ltr
tar zxvf pythium.tgz  
ls -ltr
tree pythium
```

## Using Allas

Open connection to Allas:
```text
module load allas
allas-conf 
```
If you have several Allas projects available, select the training project we are currently using.

### Upload case 1.  rclone

Upload the data from Puhti to Allas with `rclone`. Use the command below (replace XXXX with your user account):
```text
rclone -P copyto pythium allas:xxxx-genomes-rc/
```
How long did the data upload took?
What was the transfer rate?
How long would it take to transfer 100 GB with the same speed?

Then study what you have uploaded to Allas with commands: 
```text
rclone lsd allas:
rclone ls allas:xxxx-genomes-rc/
rclone lsl allas:xxxx-genomes-rc/
rclone lsf allas:xxxx-genomes-rc/
```

Check how this looks like in the Pouta web interface. Open browser and go to: [https://pouta.csc.fi/](https://pouta.csc.fi/)

In Pouta interface, go to _object store_ section, list the buckets (which are here called as “Containers”).
Locate your own _xxxx-genomes-rc_ directory and download one of the uploaded fasta files to your local computer.

### Upload case 2. a-put 

Upload the pythium directory from Puhti to Allas using following commands
(replace XXXX with your user account)

A-put case 1: Store everything in one object:
```text
 a-put pythium
 a-list
 a-list projectnumber-puhti-SCRATCH
 a-info projectnumber-puhti-SCRATCH/xxxx/pythium.tar.zst
```
A-put case 2: Each subdirectory (species) as one object:
```text
 a-put pythium/*
 a-list 2002389-puhti-SCRATCH/trng_xxxx
 a-check pythium/*
 a-info 2002389-puhti SCRATCH/training027/pythium/pythium_vexans.tar.zst 
```
A-put case 3: Use your own bucket name
```text
 a-put pythium/* -b xxxx-genomes-ap
 a-list xxxx-genomes-ap
```

A-put case 4: Upload files without compression.
```text 
a-put --nc  pythium/pythium_vexans/bwaindex/* -b XXXX_ap_vexans_bwa
a-list XXXX_ap_vexans_bwa
```
Can you see the difference between the four _a-put_ commands above?

Study the _xxxx-genomes-ap_ bucket with commands
```text
a-list xxxx-genomes-ap
rclone ls allas:xxxx-genomes-ap
```
Why the two commands above list different amount of objects?

Try command:
```text
a-info xxxx-genomes-ap/pythium_vexans.tar.zst
```
which is actually the same as:
```text
rclone cat allas:xxxx-genomes-ap/pythium_vexans.tar.zst_ameta
```

Finally try command:
```text
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
```text
rm -r pythium
exit
```
## Downloading data from Allas to Puhti


1. Login to puhti.csc.fi and move to scratch:

Linux/mac/MobaXterm
```text
ssh xxxx@puhti.csc.fi   (replace xxxx with your user account )
```

Windows/PuTTY

   host: __puhti.csc.fi__
 
   login as: _xxxx_  (replace xxxx with your CSC account )

In Puhti check you projects with command:

```text
csc-workspaces
```
Go to your personal scratch directory of your project. 
```text
cd /scratch/project_yourprojectnumber/xxxx
```
Set up Allas connection
```text
module load allas
allas-conf 
```
Then run commands
```text
a-list
rclone lsd allas:

a-list xxxx-genomes-ap
rclone ls allas:xxxx-genomes-ap

a-find pythium_vexans.fasta
a-find -a pythium_vexans.fasta
```

Next download the data in different ways:

## 1. Download with rclone

```text
mkdir rclone_dir
cd rclone_dir/
```
### example 1: copy everything
```text 
mkdir all
rclone ls allas:xxxx-genomes-rc 
rclone copyto -P allas:xxxx-genomes-rc all/
ls -l all
```

### example 2:copy a set of objects
```text
mkdir vexans 
rclone copyto allas:xxxx-genomes-rc/pythium_vexans vexans/
ls -l vexans
```
### example 3: copy just one object
```text
rclone copyto allas:trng_xxxx-genomes-rc/pythium_vexans/pythium_vexans.fasta  ./vexans.fasta
ls -l
```

## 2. Download with  a-get

Return to your XXXX directory in Puhti scratch
```text
cd ..
```
Check that you are in right place:

```text
pwd
```

The _pwd_ command should print  /scratch/project_projnum/_XXXX_

Make a new directory 
``text
mkdir a_dir
cd a_dir/
``
create directory _all_ and go there: 
```text
 mkdir all
 cd all
```
list your default scratch bucket.
```text
a-list projectnumber-puhti-SCRATCH
a-list projectnumber-puhti-SCRATCH/xxxx
```

Look for file pythium_vexans.fasta in Puhti SCRATCH  bucket:
```text
a-find pythium_vexans.fasta -b projectnumber-puhti-SCRATCH
```
download the full dataset with command:
```text 
a-get projectnumber-puhti-SCRATCH/trng_xxxx/pythium.tar.zst
```
And check what you got:
```text
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
```text
cd ..
mkdir a_backup
cd a_backup/
```
Use the commands below, to find out the ID of the most recent version backup of your pythium directory:
```text
allas-backup list 
allas-backup list | grep $USER
```
Then use allas-backup restore to download the data:
```text
allas-backup restore ID-string
ls -l
la -l pythium
```



