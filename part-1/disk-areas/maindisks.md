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
>
> - Familiarize yourself with personal and project-specific disk areas and their quotas on CSC supercomputers.
> - Learn how to share your files, such as software installations and data, to other project members on CSC supercomputers.

💬 Each user of CSC supercomputers (Roihu and LUMI) have access to different disk areas (or directories) for managing their data. Each disk area has its own specific purpose.

💬 Active data files needed for computational simulations and analyses should be stored and shared in directories under `/scratch` while any software installations and binaries should be shared under the `/projappl` directory.

‼️ None of the disk areas on Roihu and LUMI are automatically backed up by CSC. Data that is accidentally deleted by the user or otherwise lost cannot be recovered. It is the user's own responsibility to keep backup copies of any data they want to preserve.

‼️ The `/scratch` disk area on Roihu is periodically cleaned of files that have not been accessed in 180 (default) or 90 (>5 TiB quota) days. See the [Usage policy](../../computing/usage-policy.md#disk-cleaning) page for details.

## Identify your personal and project-specific directories on Roihu supercomputer

1. First login to Roihu using SSH (or by opening a login node shell in the [Roihu web interface](https://www.roihu.csc.fi)):
  
   ```bash
   ssh <username>@roihu-cpu.csc.fi    # replace <username> with your CSC username, e.g. myname@roihu-cpu.csc.fi
   ```

2. Get an overview of your projects and directories by running the following commands on the login node:

   ```bash
   csc-projects
   csc-workspaces
   ```

3. Inspect the output information summarizing your directories, their current quotas and cleanup cycles.
4. Visit your project's `/scratch` directory and list its contents:

   ```bash
   cd /scratch/<project>/   # replace <project> with your CSC project, e.g. project_2001234
   ls
   ```

5. Visit your project's `/projappl` directory and list its contents:

   ```bash
   cd /projappl/<project>/   # replace <project> with your CSC project, e.g. project_2001234
   ls
   ```

💬 These directories can be briefly summarized as follows:

- User-specific directory (i.e. your personal home folder)
  - Your home directory (path stored in environment variable `$HOME`)
  - The default directory when you login to Roihu/LUMI
  - You can store configuration files and other minor data for personal use
- Project-specific directories:
  - The project's `/scratch` and `/projappl` directories
  - Each project has its own `/scratch` disk space where most computational tasks are performed. The `/scratch` area is a temporary space not intended for long-term data storage! Please move inactive data to e.g. [Allas](https://docs.csc.fi/data/Allas/).
  - `/projappl` directory on the other hand is mainly for storing and sharing compiled applications and libraries etc. with other members of the project.

## Sharing binaries and data files

💬 Data transfer between two supercomputers can be done e.g. with `rsync`.

### Download the example files

☝🏻 In this example you will *download* data from [Allas](https://docs.csc.fi/data/Allas/) object storage.

1. Move to your home folder:

   ```bash
   cd
   ```

   💡 If you know the files are large, you should consider downloading them directly to `/scratch`.

2. Download an example program package (`ggplot2_3.3.3_Rprogramme.tar.gz`) and a data file (`Merged.fasta`) from the Allas object storage
  
   ```bash
   wget https://a3s.fi/CSC_training/shared_files.tar.gz
   tar -xavf shared_files.tar.gz
   cd shared_files
   ```

Let's assume that

- `Merged.fasta` is a data file intended for computational use
- `ggplot2_3.3.3_Rprogramme.tar.gz` is a software tool needed for the analysis.

### Move the files to Roihu `/scratch` and `/projappl`

1. Create folders with your username (using environment variable `$USER`) in your project directories under `/scratch` and `/projappl` on Roihu.

   ```bash
   mkdir -p /projappl/<project>/$USER   # replace <project> with your CSC project, e.g. project_2001234
   mkdir -p /scratch/<project>/$USER    # replace <project> with your CSC project, e.g. project_2001234
   ```

2. Copy your `ggplot2_3.3.3_Rprogramme.tar.gz` file to the `/projappl` directory

   ```bash
   cp ggplot2_3.3.3_Rprogramme.tar.gz  /projappl/<project>/$USER/   # replace <project> with your CSC project, e.g. project_2001234
   ```

3. Copy the `Merged.fasta` file to the `/scratch` directory

   ```bash
   cp Merged.fasta /scratch/<project>/$USER/    # replace <project> with your CSC project, e.g. project_2001234
   ```

   - Note that all new files and directories are also fully accessible to other members of the project (including read and write permissions).

4. Set read-only permissions for your project members for the file `Merged.fasta`:

   ```bash
   cd /scratch/<project>/$USER/    # replace <project> with your CSC project, e.g. project_2001234
   chmod g-w Merged.fasta          # g-w means that we "subtract" write permissions for users belong to our group (g), i.e. our project
   ```

### Copying files from Roihu to LUMI (optional, requires a LUMI project)

☝🏻 For this part you must ensure you have forwarded your SSH agent to Roihu, otherwise you will not be able to connect to LUMI.

1. Check if your SSH keys are available on Roihu using command `ssh-add -L`.
2. If true, it will print your public key. Proceed to step 4.
3. If not:
   1. Linux/macOS: Log out and log back in using `ssh -A` option.
   2. Windows: Log out. Toggle option *Allow agent forwarding* found under "Session" -> "SSH" -> "Advanced SSH settings" -> "Expert SSH settings" (MobaXterm) **or** under "Connection" -> "SSH" -> "Auth" (PuTTY) before connecting again.
4. Change to the folder where you have the example files
5. Copy `Merged.fasta` file from Roihu to the `/scratch` drive of LUMI:

   ```bash
   rsync -P Merged.fasta <username>@lumi.csc.fi:/scratch/<project>/$USER/    # replace <username> with your CSC username and <project> with your CSC project, e.g. project_2001234
   ```

6. Copy the `ggplot2_3.3.3_Rprogramme.tar.gz` file from Roihu to the `/projappl` directory on LUMI:

   ```bash
   rsync -P ggplot2_3.3.3_Rprogramme.tar.gz <username>@lumi.csc.fi:/projappl/<project>/$USER/    # replace <username> with your CSC username and <project> with your CSC project, e.g. project_2001234
   ```

## More information

💡 Hint: You can use your folder under `/scratch` for the rest of the tutorials. You can save the path using an [alias](https://www.shell-tips.com/bash/alias/) (with `cd` or `echo`) or somewhere in your notes.

💡 It is sometimes required to export the paths of the `/scratch` or `/projappl` directories in environmental variables (until logout). This can be done with the following commands:

```bash
export PROJAPPL=/projappl/<project>/   # replace <project> with your CSC project, e.g. project_2001234
export SCRATCH=/scratch/<project>/   # replace <project> with your CSC project, e.g. project_2001234
```
