---
layout: default
title: Fast disk areas
parent: 8. Working efficiently with data
grand_parent: Part 2
nav_order: 1
has_children: false
has_toc: false
permalink: /hands-on/data-io/tutorial-fastdisks.html
---

# Fast disk areas in CSC's computing environment

> Upon completion of this tutorial, you will be familiar with ideal disk areas
> for I/O-intensive workloads, i.e. frequent read and write operations

## Perform a light-weight pre-processing of data files using fast local disk

💬 You may sometimes come across situations where you have to process a large
number of smaller files, which can cause heavy input/output load on the shared
file system used in CSC's computing environment.

💬 In order to facilitate such heavy I/O operations, CSC provides fast local
disk areas on the login and compute nodes.

1. First login to Puhti using SSH (or by opening a login node shell in the
   Puhti web interface):

   ```bash
   ssh <username>@puhti.csc.fi    # replace <username> with your CSC username, e.g. myname@puhti.csc.fi
   ```

2. Identify the fast local disk areas on the login nodes with the following
   command:

   ```bash
   echo $TMPDIR
   ```

💡 The local disk area on the login nodes is meant for light-weight
pre-processing of data and I/O-intensive tasks such as software compilation.
Actual computations should be submitted to the batch queue from the `/scratch`
disk.

💡 The local disk area on the login nodes are meant for temporary use and
cleaned often, so make sure to move important data to `/scratch` or `/projappl`
once you do not need the fast disk anymore.

☝🏻 Note that a local disk is specific to a particular node, i.e. you cannot
access the local disk of `puhti-login11` from `puhti-login12`.

### Download a tar archive containing thousands of small files and merge the files into one large file using the fast local disk

1. Download a tar file from the **Allas** object storage directly to the local
   disk:
  
   ```bash
   cd $TMPDIR
   wget https://a3s.fi/CSC_training/Individual_files.tar.gz
   ```

2. Unpack the downloaded tar file:

   ```bash
   tar -xavf Individual_files.tar.gz
   cd Individual_files
   ```

3. Merge each small file into a larger one and remove all small files

   ```bash
   find . -name 'individual.fasta*' | xargs cat >> Merged.fasta
   find . -name 'individual.fasta*' | xargs rm
   ```

### Move your pre-processed data to the project-specific `/scratch` area before analysis

💭 Remember: the commands `csc-projects` and `csc-workspaces` reveal
information about your projects.

1. Create your own folder (using the environment variable `$USER`) under a
   project-specific directory on the `/scratch` disk (or skip this step if you
   already created the folder in a previous tutorial).

   ```bash
   mkdir -p /scratch/<project>/$USER/    # replace <project> with your CSC project, e.g. project_2001234
   ```

2. Move your pre-processed data from the previous step (i.e., the
   `Merged.fasta` file) from the fast disk to `/scratch`:

   ```bash
   mv Merged.fasta /scratch/<project>/$USER
   ```

3. You have now successfully moved your data to the `/scratch` area and can
   start performing actual analysis using batch job scripts

## Optional: Fast local disk areas on compute nodes

☝🏻 If you intend to perform heavy computing tasks using a large number of small
files, you have to use the fast local disk areas on the **compute nodes**
instead of the login nodes. The compute nodes are accessed either
[interactively](../../part-1/batch-jobs/interactive.md) or using
[batch jobs](../../part-1/batch-jobs/serial.md).

1. Use the `sinteractive` command to request an interactive session on a
   compute node with 1 GB fast local disk for 10 minutes:

   ```bash
   sinteractive --account <project> --time 00:10:00 --tmp 1    # replace <project> with your CSC project, e.g. project_2001234
   ```

   ☝🏻 Not all compute nodes have fast local disks, meaning that you may have to
   queue for a while before the interactive session starts. You may skip this
   part if you're in a hurry.

2. **In the interactive session**, use the following commands to locate the
   fast local storage areas on that compute node:

   ```bash
   echo $LOCAL_SCRATCH
   echo $TMPDIR
   ```

3. Try the same now in a proper batch job. Create a file called `my_nvme.bash`
   using, for example, the `nano` text editor:

   ```bash
   nano my_nvme.bash
   ```

4. Copy the following batch script there and change `<project>` to the CSC
   project you actually want to use:

   ```bash
   #!/bin/bash
   #SBATCH --account=<project>      # Choose the billing project. Has to be defined!
   #SBATCH --time=00:01:00          # Maximum duration of the job. Upper limit depends on the partition. 
   #SBATCH --partition=small        # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
   #SBATCH --ntasks=1               # Number of tasks. Upper limit depends on partition. For a serial job this should be set 1!
   #SBATCH --gres=nvme:1            # Request fast local disk space. Default unit is GB.

   echo $LOCAL_SCRATCH
   echo $TMPDIR
   ```

5. Submit the batch job with the command:

   ```bash
   sbatch my_nvme.bash
   ```

6. Monitor the progress of your batch job and print the contents of the output
   file when it has completed:

   ```bash
   squeue -u $USER
   cat slurm-<jobid>.out    # replace <jobid> with the actual Slurm job ID
   ```

   ☝🏻 Again, please note that requesting fast local disk space tends to
   increase your queueing time. It is a scarce resource, and should only be
   requested if you really need it. Please ask
   [CSC Service Desk](https://docs.csc.fi/support/contact/) if you're unsure.

   ‼️ If you write important data to the local disk in your interactive session
   or batch job, remember to copy the data back to `/scratch` before the job
   terminates! The local disk is cleaned immediately after your job, and
   salvaging any forgotten files is not possible afterwards.

   💭 Bonus exercise: Try to repeat the
   [first part of this tutorial](#perform-a-light-weight-pre-processing-of-data-files-using-fast-local-disk)
   using a batch job!

## More information

💡 Read more about fast local disk areas in
[Docs CSC](https://docs.csc.fi/computing/disk/#temporary-local-disk-areas).

💡 [Requesting local storage on Puhti](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage).

💡 [Requesting local storage on Mahti](https://docs.csc.fi/computing/running/creating-job-scripts-mahti/#local-storage).
