---
topic: disk-areas
title: Advanced tutorial - Where to put files in CSC environment?
---

# Where to put files in CSC environment?

> In this tutorial you familiarise yourself with main disk areas in Puhti and Mahti supercomputers. 
> See how to share your files such as programme packages and data files to other project members on the same supercomputer (i.e., on Puhti) as well as on Mahti (i.e, another supercomputer at CSC)

💬 Data files needed for computational analysis should be stored and shared in **scratch** directories and any software compilations and binaries should be shared in **proappl** directory.

## Binary and data files to share

💬 In order to find actual directories use commands such as `csc-workspaces` and `csc-projects`.  
💬 Data transfer between two supercomputers can be done with many tools including `rsync`. 

### Download the example files

☝🏻 In this example you will download data from [*Allas*](https://docs.csc.fi/data/Allas/), but try still to avoid using *Allas* for data transfer between the supercomputers. 

1. First login to Puhti supecomputer using *SSH*:
```bash
ssh YOURUSERNAME@puhti.csc.fi
```

2. Download example programme package (i.e.,ggplot2_3.3.3_Rprogramme.tar.gz) and data file (i.e, Merged.fasta) from **allas** object storage
```bash
wget https://a3s.fi/CSC_training/shared_files.tar.gz
tar -xavf shared_files.tar.gz
cd shared_files
```
- Let's assume that 
   - file *Merged.fasta* is data file intended for computational use
   - file *ggplot2_3.3.3_Rprogramme.tar.gz* is a software tool needed for analysis. 

### Move the files to Puhti scratch and projappl

3. Share your *ggplot2_3.3.3_Rprogramme.tar.gz* file in *projappl* directory
```bash
cp ggplot2_3.3.3_Rprogramme.tar.gz  /projappl/project_XXXX/$USER   # replace XXXX
```
4. Share *Merged.fasta* file in *scratch* directory
```bash
cp Merged.fasta /scratch/project_XXXX/$USER    # replace XXXX
```
- All new files and directories are also fully accessible for other group members (including read, write and execution permissions). 

5. Set read-only permissions for your group members for the file *Merged.fasta*:
```bash
cd /scratch/project_XXXX/$USER    # replace XXXX
chmod -R g-w Merged.fasta
```


#### Sharing files from Puhti to Mahti

1. Change to the folder where you have the example files
2. Copy *Merged.fasta* file on puhti to **scratch** drive on Mahti as below:
```bash
rsync -P Merged.fasta YOURUSERNAME@mahti.csc.fi:/scratch/project_XXXX/$USER    # replace XXXX and YOURUSERNAME
```
3. Copy *ggplot2_3.3.3_Rprogramme.tar.gz* file on puhti to **projappl** directory on Mahti as below:
```bash
rsync -P ggplot2_3.3.3_Rprogramme.tar.gz YOURUSERNAME@mahti.csc.fi:/projappl/project_XXXX/$USER    # replace XXXX and YOURUSERNAME
```
