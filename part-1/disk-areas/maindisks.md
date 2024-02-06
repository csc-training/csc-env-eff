---
layout: default
title: Main disk areas
parent: 3. Disk areas
grand_parent: Part 1
nav_order: 1
has_children: false
has_toc: false
permalink: /hands-on/disk-areas/disk-areas-tutorial-maindisks.html
---

# Where to store files in CSC's computing environment?

> In this tutorial you
   - Familiarize yourself with personal and project-specific disk areas and their quotas on CSC supercomputers.
   - Learn how to share your files, such as software installations and data, to other project members on CSC supercomputers.

💬 Each user of CSC supercomputers (Puhti and Mahti) have access to different disk areas (or directories) for managing their data. Each disk area has its own specific purpose.

💬 Active data files needed for computational simulations and analyses should be stored and shared in directories under `/scratch` while any software installations and binaries should be shared under the `/projappl` directory.

## Identify your personal and project-specific directories on Puhti and Mahti supercomputers

1. First login to Puhti using SSH (or by opening a login node shell in the [Puhti web interface](https://www.puhti.csc.fi)):
  
```bash
ssh <username>@puhti.csc.fi    # replace <username> with your CSC username, e.g. myname@puhti.csc.fi
```

{:style="counter-reset:step-counter 1"}
2. Get an overview of your projects and directories by running the following commands on the login node:

```bash
csc-projects
csc-workspaces
```

{:style="counter-reset:step-counter 2"}
3. Inspect the output information summarizing your directories and their current quotas.
4. Visit your project's `/scratch` directory and list its contents:

```bash
cd /scratch/<project>/   # replace <project> with your CSC project, e.g. project_2001234
ls
```

{:style="counter-reset:step-counter 4"}
5. Visit your project's `/projappl` directory and list its contents:

```bash
cd /projappl/<project>/   # replace <project> with your CSC project, e.g. project_2001234
ls
```

💬 These directories can be briefly summarized as follows:

- User-specific directory (i.e. your personal home folder)
   - Your home directory (path stored in environment variable `$HOME`)
   - The default directory when you login to Puhti/Mahti
   - You can store configuration files and other minor data for personal use
- Project-specific directories:
   - The project's `/scratch` and `/projappl` directories
   - Each project has its own `/scratch` disk space where most computational tasks are performed. The `/scratch` area is a temporary space not intended for long-term data storage! Please move inactive data to e.g. [Allas](https://docs.csc.fi/data/Allas/).
   - `/projappl` directory on the other hand is mainly for storing and sharing compiled applications and libraries etc. with other members of the project.

## Sharing binaries and data files

💬 Data transfer between two supercomputers can be done e.g. with `rsync`.

### Download the example files

☝🏻 In this example you will *download* data from [Allas](https://docs.csc.fi/data/Allas/) object storage, but keep in mind that one should avoid using Allas to do data transfer between Puhti and Mahti.

1. Move to your home folder:

```bash
cd
```

💡 If you know the files are large, you should consider downloading them directly to `/scratch`.

{:style="counter-reset:step-counter 1"}
2. Download an example program package (`ggplot2_3.3.3_Rprogramme.tar.gz`) and a data file (`Merged.fasta`) from the Allas object storage
  
```bash
wget https://a3s.fi/CSC_training/shared_files.tar.gz
tar -xavf shared_files.tar.gz
cd shared_files
```

Let's assume that

- `Merged.fasta` is a data file intended for computational use
- `ggplot2_3.3.3_Rprogramme.tar.gz` is a software tool needed for the analysis.

### Move the files to Puhti `/scratch` and `/projappl`

1. Create folders with your username (using environment variable `$USER`) in your project directories under `/scratch` and `/projappl` on Puhti.

```bash
mkdir -p /projappl/<project>/$USER   # replace <project> with your CSC project, e.g. project_2001234
mkdir -p /scratch/<project>/$USER    # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 1"}
2. Copy your `ggplot2_3.3.3_Rprogramme.tar.gz` file to the `/projappl` directory

```bash
cp ggplot2_3.3.3_Rprogramme.tar.gz  /projappl/<project>/$USER/   # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 2"}
3. Copy the `Merged.fasta` file to the `/scratch` directory

```bash
cp Merged.fasta /scratch/<project>/$USER/    # replace <project> with your CSC project, e.g. project_2001234
```

- Note that all new files and directories are also fully accessible to other members of the project (including read and write permissions).

{:style="counter-reset:step-counter 3"}
4. Set read-only permissions for your project members for the file `Merged.fasta`:

```bash
cd /scratch/<project>/$USER/    # replace <project> with your CSC project, e.g. project_2001234
chmod g-w Merged.fasta          # g-w means that we "subtract" write permissions for users belong to our group (g), i.e. our project
```

### Copying files from Puhti to Mahti (it is an optional task as it needs Mahti access)

1. Change to the folder where you have the example files
2. Copy `Merged.fasta` file from Puhti to the `/scratch` drive of Mahti:

```bash
rsync -P Merged.fasta <username>@mahti.csc.fi:/scratch/<project>/$USER/    # replace <username> with your CSC username and <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 2"}
3. Copy the `ggplot2_3.3.3_Rprogramme.tar.gz` file from Puhti to the `/projappl` directory on Mahti:

```bash
rsync -P ggplot2_3.3.3_Rprogramme.tar.gz <username>@mahti.csc.fi:/projappl/<project>/$USER/    # replace <username> with your CSC username and <project> with your CSC project, e.g. project_2001234
```

## More information

💡 Hint: You can use your folder under `/scratch` for the rest of the tutorials. You can save the path using an [alias](https://www.shell-tips.com/bash/alias/) (with `cd` or `echo`) or somewhere in your notes.

💡 It is sometimes required to export the paths of the `/scratch` or `/projappl` directories in environmental variables (until logout). This can be done with the following commands:

```bash
export PROJAPPL=/projappl/<project>/   # replace <project> with your CSC project, e.g. project_2001234
export SCRATCH=/scratch/<project>/   # replace <project> with your CSC project, e.g. project_2001234
```
