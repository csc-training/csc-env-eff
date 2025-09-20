---
layout: default
title: Processing many files with HyperQueue
parent: 11. How to speed up jobs
grand_parent: Part 2
nav_order: 2
has_children: false
has_toc: false
permalink: /hands-on/throughput/hyperqueue.html
---

# Using HyperQueue and local disk to process many small files efficiently

> This tutorial is done on **Puhti**, which requires that

- you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
- your account belongs to a project [that has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

## Overview

💬 [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) is a tool for efficient
sub-node task scheduling and well suited for task farming and running
embarrassingly parallel jobs.

💬 In this example, we have more than 4000 files which we want to convert to
another format.

- Each file contains a [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)
  string (an ASCII notation encoding the two-dimensional structure of a
  molecule) which we want to convert into a three-dimensional coordinate
  format.
- The computational cost of each of the conversions is expected to be
  comparable.
- Since the workflow involves many small files, we will also demonstrate the
  usage of the fast local disk to avoid stressing the parallel file system.

### The workflow of this exercise

1. Download the files from Allas.
2. Decompress the files to `$LOCAL_SCRATCH`.
3. Convert each `.smi` file to a three-dimensional `.sdf` molecular file
   format.
4. Archive and compress the output files and move them back to `/scratch`.

## Download the input files

1. Create and enter a suitable scratch directory on Puhti (replace `<project>`
   with your CSC project, e.g. `project_2001234`):

   ```bash
   mkdir -p /scratch/<project>/$USER/hq-example
   cd /scratch/<project>/$USER/hq-example
   ```

2. Download the input files representing molecules initially obtained from the
   [ChEMBL database](https://chembl.gitbook.io/chembl-interface-documentation/downloads):
  
   ```bash
   wget https://a3s.fi/CSC_training/smiles.tar.gz
   ```

## Create a HyperQueue batch script

💬 We will use [Open Babel](https://docs.csc.fi/apps/openbabel/) to convert the
SMILES strings into a three-dimensional `.sdf` coordinate format.

☝🏻 Multiple files can be converted using the batch conversion mode of Open
Babel. For 4000+ files this would, however, take more than an hour.
Submitting each conversion as a separate Slurm job is also a bad idea since
each conversion takes just a few seconds. Running many short jobs will degrade
the performance of the scheduler for all users.

💡 [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) is a program that allows
us to schedule sub-node tasks *within* a Slurm allocation. One can think of
HyperQueue as a "Slurm within a Slurm", or a so-called "meta-scheduler", which
allows us to leverage embarrassing parallelism without overloading Slurm by
looping `srun` or `sbatch` commands.

1. Copy the following script into a file `hq.sh` using, e.g., `nano`:

   ```bash
   #!/bin/bash
   #SBATCH --partition=small
   #SBATCH --account=<project>  # replace <project> with your CSC project, e.g. project_2001234
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=1
   #SBATCH --cpus-per-task=40
   #SBATCH --time=00:10:00
   #SBATCH --gres=nvme:1
 
   module load hyperqueue openbabel
 
   # Specify a location for the HyperQueue server
   export HQ_SERVER_DIR=${PWD}/hq-server-${SLURM_JOB_ID}
   mkdir -p "${HQ_SERVER_DIR}"
 
   # Start the server in the background (&) and wait until it has started
   hq server start &
   until hq job list &>/dev/null ; do sleep 1 ; done
 
   # Start the workers in the background and wait for them to start
   srun --exact --cpu-bind=none --mpi=none hq worker start --cpus=${SLURM_CPUS_PER_TASK} &
   hq worker wait "${SLURM_NTASKS}"
 
   # Extract the input files to the local disk and cd there
   tar -xf smiles.tar.gz -C $LOCAL_SCRATCH
   cd $LOCAL_SCRATCH/smiles
 
   # Submit each Open Babel conversion as a separate HyperQueue job
   for f in *.smi ; do
       hq submit --stdout=none --stderr=none obabel $f -O ${f%.*}.sdf --gen3d best &
   done
 
   # Wait for all jobs to finish, then shut down the workers and server
   hq job wait all
   hq worker stop all
   hq server stop
 
   # Archive and compress the output .sdf files and copy the package back to /scratch
   tar -czf sdf.tar.gz *.sdf
   cp sdf.tar.gz $SLURM_SUBMIT_DIR
   ```

2. As explained by the comments in the script above, HyperQueue works on a
   worker-server-client basis, i.e. a worker is started on each compute node to
   execute commands that the client submitted to the server.
    - This is in principle what Slurm also does, only difference is that you
      need to start the server and workers yourself.
    - In this example, one full Puhti node is reserved for processing the
      files, meaning that 40 conversion commands will be running in parallel.

   ☝🏻 Ideally, the number of sub-tasks should be larger than the amount that
   can fit running on the reserved resources simultaneously to avoid too short
   Slurm jobs.

1. Submit the script with:

   ```bash
   sbatch hq.sh
   ```

2. After a short while, you should notice that a file `sdf.tar.gz` containing
   the output files has appeared in your working directory. How long did it
   take to convert all files?

💡 Tip: If you want to monitor the progress of your HyperQueue jobs/tasks,
just set the location of the HyperQueue server and use the `hq` commands
(see the [official documentation for details](https://it4innovations.github.io/hyperqueue/stable/jobs/jobs/)).
Note that the HQ job/task IDs are not the same as the Slurm job ID!

```bash
module load hyperqueue
export HQ_SERVER_DIR=${PWD}/hq-server-<slurmjobid>
hq job list
hq job info <hqjobid>
hq job progress <hqjobid>
hq task list <hqjobid>
hq task info <hqjobid> <hqtaskid>
```

☝🏻 Remember to load the `hyperqueue` module before running the commands
above from the terminal, otherwise you will get an error message
`-bash: hq: command not found`.

☝🏻 Also note that these commands are available only after your job has
started running.

💬 To get a report of how your jobs/tasks completed and spot possible
failures, you could also run one of these commands in your batch script and
redirect the output to a file before shutting down the server.

## More information

- [HyperQueue page in Docs CSC](https://docs.csc.fi/apps/hyperqueue/)
