---
topic: disk-areas
title: Exercise - disk-areas main disks
---

# Where to put files in CSC environment?

## Binary and data files to share

Where would you share your files such as programme packages and data files to other project members on the same supercomputer (i.e., on Puhti) as well as on Mahti (i.e, another supercomputer at CSC)?

###  Background

This exercise is aimed at familiarising yourself with main disk areas in Puhti and Mahti supercomputers. Data files needed for computational analysis should be stored and shared in *scratch* directories and any software compilations and binaries should be shared in *proappl* directory. In order to find actual directories use commands such as `csc-workspaces` and `csc-projects`. Data transfer between two supercomputers can be done with many tools including `rsync`. In this example try to avoid using *allas* for data transfer between the supercomputers. You may download an example programme package (i.e.,ggplot2_3.3.3_Rprogramme.tar.gz) and data file (i.e., Merged.fasta) from [**allas** object storage](https://a3s.fi/CSC_training/shared_files.tar.gz)

### Solution

1. First login to Puhti supecomputer using *ssh* command as below:

```bash
ssh yourcscusername@puhti.csc.fi
```
Authenticate using the password associated with CSC user account. Once your login to Puhti is successful, Linux terminal will be opened for command-line interaction in your home directory. 

2. Download example programme package (i.e.,ggplot2_3.3.3_Rprogramme.tar.gz) and data file (i.e, Merged.fasta) from **allas** object storage

```bash
wget https://a3s.fi/CSC_training/shared_files.tar.gz
tar -xavf shared_files.tar.gz
cd shared_files
```

Let's assume that file *Merged.fasta* is data file intended for computational use and *ggplot2_3.3.3_Rprogramme.tar.gz* is a software tool needed for analysis.  You can now share file *Merged.fasta* in scratch folder and *ggplot2_3.3.3_Rprogramme.tar.gz* file in projapple directory.


3. Share your *ggplot2_3.3.3_Rprogramme.tar.gz* file in *projappl* directory

```bash
cp ggplot2_3.3.3_Rprogramme.tar.gz  /projappl/project_xxxx/$USER
````

4. Share *Merged.fasta* file in *scratch* directory
```bash
cp Merged.fasta /scratch/project_xxxx/$USER
```
All new files and directories are also fully accessible for other group members (including read, write and execution permissions). If you want to restrict access from your group members, you can reset the permissions with *chmod* command.

Set read-only permissions for your group members for the file *Merged.fasta*:

```bash
chmod -R g-w Merged.fasta
```
5. sharing files in Mahti supercomputer

you can copy *Merged.fasta* file on puhti to *scratch* drive on Mahti as below:

```bash
rsync -P Merged.fasta yourcscusername@mahti.csc.fi:/scratch/project_xxxx/$USER
```
you can copy *ggplot2_3.3.3_Rprogramme.tar.gz* file on puhti to *projappl* directory on Mahti as below:

```bash
rsync -P ggplot2_3.3.3_Rprogramme.tar.gz yourcscusername@mahti.csc.fi:/projappl/project_xxxx/$USER
```


