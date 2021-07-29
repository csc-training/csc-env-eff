---
topic: disk-areas
title: Tutorial - Fast disk areas in CSC supercomputing environment
---

# Fast disk areas in CSC supercomputing environment

> Upon completion of this tutorial, you will get familiar with ideal disk areas for large I/O operations (=reading and writing operations)

## Perform a light-weight pre-processing on data files using fast I/O local disks

💬 You sometimes come across situations where you have to handle an uncommonly large number of smaller files that can cause heavy input/output load on supercomputing environment. 

💬 In order to facilitate such heavy I/O operations, CSC provides fast local disk areas in login and compute nodes.

1. Identify fast local disk areas in login nodes with the following command:
   ```bash
   echo $TMPDIR
   ```

💡 This local disk area in login nodes is meant for some light-weight preprocessing of data before you start actual analysis on **scratch** drive. 

### Download a tar file containing thousands of small files and merge the files into one big file in the local storage disks

1. Download tar file from *Allas* object storage by typing:
   ```bash 
   cd $TMPDIR           
   wget https://a3s.fi/CSC_training/Individual_files.tar.gz
   ```
2. Unpack the downloaded tar file by typing:
   ```bash
   tar -xavf Individual_files.tar.gz
   cd Individual_files
   ```
3. Merge all those small files into one file and remove all small files
   ```bash
   find . -name 'individual.fasta*' | xargs cat  >> Merged.fasta
   find . -name 'individual.fasta*' | xargs rm
   ```

☝🏻 If you are going to perform heavy-weight computing tasks on those larger number of smaller files, you have to use *local storage areas* in **compute nodes** instaad og login nodes
- The compute nodes are accessed either [interactively](https://docs.csc.fi/computing/running/interactive-usage/) or using [batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-puhti).
   - In the interactive jobs, use the following commands to find out a local storage area in that compute node (only in Puhti):
   ```bash
   [cscaccount@r07c50 ~]$ echo $LOCAL_SCRATCH
   /run/nvme/job_6891674/data
   [cscaccount@r07c50 ~]$ echo $TMPDIR
   /run/nvme/job_6891674/tmp
   ```
   - When using batch job, use the environment variable $LOCAL_SCRATCH in your [batch job scripts](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage) to access the local storage on that node (only in Puhti).

### Move your pre-processed data to a project-specific scratch area before analysis

💭 Remember: commands `csc-projects` and `csc-workspaces` reveal information of your projects. 

1. Create your own folder (using environment variable $USER) into a project-specific directory on **scratch** area.
   ```bash
   mkdir /scratch/project_XXXX/$USER   # replace XXXX
   ```
2. Move your pre-processed data from earlier step (i.e., Merged.fasta file):
   ```bash
   mv Merged.fasta /scratch/project_xxx/$USER
   ```
3. You have now successfully moved your data to scratch area and can start performing actual analysis using batch job scripts 
- More about batch jobs in a later tutorials.

## More information

💡 Hint: You can use your folder in scratch for the rest of the tutorials. Save the path in [alias](https://www.shell-tips.com/bash/alias/) (with `cd`or `echo`) or somewhere in your notes. 

💡 It is sometimes needed to save the paths of project **scratch** or **projappl** directories in an environmental variable (until logout).
- This can be done wiht a following command:
   ```bash
   export PROJAPPL=/projappl/project_XXXX/   # replace XXXX with your project number
   export SCRATCH=/scratch/project_XXXX/   # replace XXXX with your project number
   ```

