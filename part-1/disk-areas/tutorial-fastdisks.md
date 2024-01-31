---
layout: default
title: Fast disk areas
parent: 3. Disk areas
grand_parent: Part 1
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/disk-areas/disk-areas-tutorial-fastdisks.html
---

# Fast disk areas in CSC's computing environment

> Upon completion of this tutorial, you will be familiar with ideal disk areas for I/O intensive workloads, i.e. frequent read and write operations

## Perform a light-weight pre-processing of data files using fast local disk

💬 You may sometimes come across situations where you have to process a large number of smaller files, which can cause heavy input/output load on the shared file system used in CSC's computing environment.

💬 In order to facilitate such heavy I/O operations, CSC provides fast local disk areas on the login and compute nodes (excluding Mahti CPU nodes).

1. Identify the fast local disk areas on the login nodes with the following command:

```bash
echo $TMPDIR
```

💡 The local disk area on the login nodes is meant for light-weight pre-processing of data and I/O intensive tasks such as software compilation. Actual computations should be submitted to the batch queue from the `/scratch` disk.

💡 The local disk area on the login nodes are meant for temporary use and cleaned often, so make sure to move important data to `/scratch` or `/projappl` once you do not need the fast disk anymore. Note that e local disk is specific to a particular node, i.e. you cannot access the local disk of `puhti-login11` from `puhti-login12`.

### Download a tar archive containing thousands of small files and merge the files into one large file using the fast local disk

1. Download a tar file from the **Allas** object storage directly to the local disk:
  
```bash
cd $TMPDIR           
wget https://a3s.fi/CSC_training/Individual_files.tar.gz
```

{:style="counter-reset:step-counter 1"}
2. Unpack the downloaded tar file:

```bash
tar -xavf Individual_files.tar.gz
cd Individual_files
```

{:style="counter-reset:step-counter 2"}
3. Merge each small file into a larger one and remove all small files

```bash
find . -name 'individual.fasta*' | xargs cat >> Merged.fasta
find . -name 'individual.fasta*' | xargs rm
```

☝🏻 If you intend to perform heavy computing tasks using a large number of small files, you have to use the fast local disk areas on the *compute nodes* instead of the login nodes. The compute nodes are accessed either [interactively](https://docs.csc.fi/computing/running/interactive-usage/) or using [batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-puhti).

- **In an interactive session**, use the following commands to show the local storage area on that compute node (only on Puhti):

```bash
echo $LOCAL_SCRATCH
echo $TMPDIR
```

- When using batch jobs, use the environment variable `$LOCAL_SCRATCH` in your [batch job scripts](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage) to access the local storage on that node (only on Puhti).

### Move your pre-processed data to the project-specific `/scratch` area before analysis

💭 Remember: the commands `csc-projects` and `csc-workspaces` reveal information about your projects.

1. Create your own folder (using the environment variable `$USER`) under a project-specific directory on the `/scratch` disk (or skip this step if you already created the folder in a previous tutorial).

```bash
mkdir -p /scratch/<project>/$USER/    # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 1"}
2. Move your pre-processed data from the previous step (i.e., the `Merged.fasta` file) from the fast disk to `/scratch`:

```bash
mv Merged.fasta /scratch/<project>/$USER
```

{:style="counter-reset:step-counter 2"}
3. You have now successfully moved your data to the `/scratch` area and can start performing actual analysis using batch job scripts

- More about batch jobs in later tutorials.

## More information

💡 Hint: You can use your folder under `/scratch` for the rest of the tutorials. You can save the path using an [alias](https://www.shell-tips.com/bash/alias/) (with `cd` or `echo`) or somewhere in your notes.

💡 It is sometimes required to export the paths of the `/scratch` or `/projappl` directories in environmental variables (until logout). This can be done with the following commands:

```bash
export PROJAPPL=/projappl/<project>/   # replace <project> with your CSC project, e.g. project_2001234
export SCRATCH=/scratch/<project>/   # replace <project> with your CSC project, e.g. project_2001234
```
