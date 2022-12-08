---
topic: disk-areas
title: Tutorial - Main disk areas in CSC supercomputing environment (essential)
---

# Where to put files in CSC environment?

> In this tutorial you 
   - Familiarise yourself with personal and project-specific disk areas and their quotas in Puhti and Mahti supercomputers. 
   - See how to share your files such as programme packages and data files to other project members on Puhti as well as on Mahti.

💬 Each user at CSC supercomputer (Puhti or Mahti) have access to different disk areas (or directories) to manage their data in supercomputers. The disk areas have their specific purposes. 

💬 Data files needed for computational analysis should be stored and shared in **scratch** directories and any software compilations and binaries should be shared in **proajppl** directory.

## Identify your personal and project-specific directories in Puhti and Mahti supercomputers

1. First login to Puhti supecomputer using *SSH*:
   ```bash
   ssh yourcscusername@puhti.csc.fi    # replace yourcscusername
   ```
2. Get an overview of your projects and directories by using the following commands in login node:
   ```bash
   csc-projects
   csc-workspaces 
   ```
3. Look through the output information about your directories and their current quotas.  
4. Visit your projects **scratch** directory and check out its contents:
   ```bash
   cd /scratch/project_xxxx/   # replace xxxx with your project number
   ls
   ```
5. Visit your projects **projappl** directory and check out its contents:
   ```bash
   cd /projappl/project_xxxx/   # replace xxxx with your project number
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

💬 Data transfer between two supercomputers can be done e.g. with `rsync`. 

### Download the example files

☝🏻 In this example you will download data from [*Allas*](https://docs.csc.fi/data/Allas/), but keep in mind that one should avoid using Allas to do data transfer between two supercomputers.

1. Move to home folder with:
   ```bash
   cd
   ```

💡 If you know the files are large you should consider downloading them straight to **scratch**. 

{:start="2"}
2. Download the example programme package (i.e.,ggplot2_3.3.3_Rprogramme.tar.gz) and data file (i.e, Merged.fasta) from Allas object storage
   ```bash
   wget https://a3s.fi/CSC_training/shared_files.tar.gz
   tar -xavf shared_files.tar.gz
   cd shared_files
   ```

- Let's assume that
    - file *Merged.fasta* is data file intended for computational use
    - file *ggplot2_3.3.3_Rprogramme.tar.gz* is a software tool needed for analysis. 

### Move the files to Puhti scratch and projappl

1. Create folders with your username in your projects **scratch** and **projappl** directories in Puhti.
   ```bash
   mkdir /projappl/project_xxxx/$USER   # replace project_xxxx with course/your project
   mkdir /scratch/project_xxxx/$USER    # replace project_xxxx with course/your project
   ```
2. Share your *ggplot2_3.3.3_Rprogramme.tar.gz* file in *projappl* directory
   ```bash
   cp ggplot2_3.3.3_Rprogramme.tar.gz  /projappl/project_xxxx/$USER/   # replace project_xxxx with course/your project
   ```
3. Share *Merged.fasta* file in *scratch* directory
   ```bash
   cp Merged.fasta /scratch/project_xxxx/$USER/    # replace project_xxxx with course/your project
   ```
- All new files and directories are also fully accessible for other group members (including read, write and execution permissions). 

4. Set read-only permissions for your group members for the file *Merged.fasta*:
   ```bash
   cd /scratch/project_xxxx/$USER/    # replace project_xxxx with course/your project
   chmod -R g-w Merged.fasta
   ```

### Sharing files from Puhti to Mahti

1. Change to the folder where you have the example files
2. Copy *Merged.fasta* file on puhti to **scratch** drive on Mahti as below:
   ```bash
   rsync -P Merged.fasta yourcscusername@mahti.csc.fi:/scratch/project_xxxx/$USER/    # replace project_xxxx with course/your project
   ```
3. Copy *ggplot2_3.3.3_Rprogramme.tar.gz* file on puhti to **projappl** directory on Mahti as below:
   ```bash
   rsync -P ggplot2_3.3.3_Rprogramme.tar.gz yourcscusername@mahti.csc.fi:/projappl/project_xxxx/$USER/    # replace project_xxxx with course/your project
   ```

## More information

💡 Hint: You can use your folder in scratch for the rest of the tutorials. Save the path in [alias](https://www.shell-tips.com/bash/alias/) (with `cd`or `echo`) or somewhere in your notes. 

💡 It is sometimes needed to save the paths of project **scratch** or **projappl** directories in an environmental variable (until logout).
- This can be done wiht a following command:
   ```bash
   export PROJAPPL=/projappl/project_xxxx/   # replace xxxx with your project number
   export SCRATCH=/scratch/project_xxxx/   # replace xxxx with your project number
   ```

