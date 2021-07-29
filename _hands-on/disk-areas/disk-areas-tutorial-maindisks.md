---
topic: disk-areas
title: Tutorial - Main disk areas in CSC supercomputing environment
---

# Where to put files in CSC environment?

> In this tutorial you 
   - Familiarise yourself with personal and project-specific disk areas and their quotas in Puhti and Mahti supercomputers. 
   - See how to share your files such as programme packages and data files to other project members on Puhti as well as on Mahti.

💬 Each user at CSC supercomputer (Puhti or Mahti) have access to different disk areas (or directories) to manage their data in supercomputers. The disk areas have their specific purposes. 

💬 Data files needed for computational analysis should be stored and shared in **scratch** directories and any software compilations and binaries should be shared in **proappl** directory.

## Identify your personal and project-specific directories in Puhti and Mahti supercomputers

1. Get an overview of your projects and directories by using the following commands in login node:
   ```bash
   csc-projects
   csc-workspaces 
   ```
2. Look through the output information about your directories and their current quotas.  
3. Visit your projects **scratch** directory and check out its contents:
   ```bash
   cd /scratch/project_XXXX/   # replace XXXX with your project number
   ls
   ```
4. Visit your projects **projappl** directory and check out its contents:
   ```bash
   cd /projappl/project_XXXX/   # replace XXXX with your project number
   ls
   ```

💬 These directories can be briefly summerised as below:
- User-specific directory (= Personal home folder)
   - Your home directory `$HOME`
   - The default directory when you login to Puhti/Mahti. 
   - You can store configuration files and other minor personal data. 
- Project-specific directories: 
   - The project **scratch** and **projappl** directories. 
   - Each project contains its **scratch** disk space where actual data analysis tasks are performed. **scratch** area is a temporary space.
   - **Projappl** directory on the other hand is mainly for storing and sharing compiled applications and libraries etc. with other members of the project. 

## Binary and data files to share

💬 Data transfer between two supercomputers can be done with many tools including `rsync`. 

### Download the example files

☝🏻 In this example you will download data from [*Allas*](https://docs.csc.fi/data/Allas/), but try still to avoid using *Allas* for data transfer between the supercomputers. 

1. First login to Puhti supecomputer using *SSH*:
   ```bash
   ssh YOURUSERNAME@puhti.csc.fi    # replace YOURUSERNAME
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

### Sharing files from Puhti to Mahti

1. Change to the folder where you have the example files
2. Copy *Merged.fasta* file on puhti to **scratch** drive on Mahti as below:
   ```bash
   rsync -P Merged.fasta YOURUSERNAME@mahti.csc.fi:/scratch/project_XXXX/$USER    # replace XXXX and YOURUSERNAME
   ```
3. Copy *ggplot2_3.3.3_Rprogramme.tar.gz* file on puhti to **projappl** directory on Mahti as below:
   ```bash
   rsync -P ggplot2_3.3.3_Rprogramme.tar.gz YOURUSERNAME@mahti.csc.fi:/projappl/project_XXXX/$USER    # replace XXXX and YOURUSERNAME
   ```

## More information

💡 Hint: You can use your folder in scratch for the rest of the tutorials. Save the path in [alias](https://www.shell-tips.com/bash/alias/) (with `cd`or `echo`) or somewhere in your notes. 

💡 It is sometimes needed to save the paths of project **scratch** or **projappl** directories in an environmental variable (until logout).
- This can be done wiht a following command:
   ```bash
   export PROJAPPL=/projappl/project_XXXX/   # replace XXXX with your project number
   export SCRATCH=/scratch/project_XXXX/   # replace XXXX with your project number
   ```

