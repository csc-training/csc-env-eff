---
topic: throughput
title: Tutorial - Processing many files with HyperQueue
---

# Using HyperQueue and local disk to process many small files efficiently

> This tutorial requires that

- you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
- your account belongs to a project [that has access to the Puhti
  service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

> This tutorial is done on Puhti

## Overview

💬 [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) is a tool for efficient sub-node
task scheduling and well suited for task farming and running embarrassingly parallel jobs.

💬 In this example, we have a large number of files (4000+) which we want to convert to
another format.

- The files represent SMILES strings (a line notation encoding the two-dimensional
  structure of a molecule) which we want to convert into a three-dimensional coordinate
  format
- The computational cost of each of the conversions is expected to be comparable
- Since the workflow involves many small files, we will utilize the fast local disk to
  avoid stressing the parallel file system

### The workflow of this exercise

1. Download the input files from Allas
2. Decompress the files to `$LOCAL_SCRATCH`
3. Use Open Babel to convert each `.smi` file to a three-dimensional `.sdf` molecular
   file format
4. Archive and compress the output files and move them back to `/scratch`

## Download the input files

1. Create and enter a suitable scratch directory on Puhti (replace `<project>` with your CSC
   project, e.g. `project_2001234`):

```bash
mkdir -p /scratch/<project>/$USER/hq-example
cd /scratch/<project>/$USER/hq-example
```

{:start="2"}
2. Download the input files representing small molecules initially obtained from the
   [ChEMBL database](https://chembl.gitbook.io/chembl-interface-documentation/downloads):
  
```bash
wget https://a3s.fi/CSC_training/smiles.tar.gz
```

## Create a HyperQueue batch script

💬 We will use [Open Babel](https://docs.csc.fi/apps/openbabel/) to convert the SMILES
strings into a three-dimensional `.sdf` coordinate format.

☝🏻 Multiple files can be converted using the batch conversion mode of Open Babel. For
4000+ files this would, however, take more than an hour. Similarly, submitting each
conversion as a separate Slurm job is also a bad idea since each conversion takes
just a few seconds. A large number of short jobs may degrade the performance of the
scheduler for all users.

💡 [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) is a program that allows us to
schedule sub-node tasks *within* a Slurm allocation. One can think of HyperQueue as a
"Slurm within a Slurm", or a so-called "meta-scheduler", which allows us to leverage
embarrassing parallelism without overloading Slurm by looping `srun` or `sbatch` commands.

1. Copy the following script into a file `hq.sh` using, e.g., `nano`:

```bash
#!/bin/bash
#SBATCH --partition=small
#SBATCH --account=<project>
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --time=00:10:00
#SBATCH --mem=1G
#SBATCH --gres=nvme:1

module load hyperqueue openbabel

# Specify a location for the HyperQueue server
export HQ_SERVER_DIR=${PWD}/hq-server-${SLURM_JOB_ID}
mkdir -p "${HQ_SERVER_DIR}"

# Start the server in the background (&) and wait until it has started
hq server start &
until hq job list &>/dev/null ; do sleep 1 ; done

# Start the workers (one per node, in the background) and wait until they have started
srun --exact --cpu-bind=none --mpi=none hq worker start --cpus=${SLURM_CPUS_PER_TASK} &
hq worker wait "${SLURM_NTASKS}"

# Extract the SMILES strings (one string per .smi file) to the local disk and cd there
tar -xf smiles.tar.gz -C $LOCAL_SCRATCH
cd $LOCAL_SCRATCH/smiles

# Use Open Babel for the 3D conversion, each as a separate HyperQueue job
for f in *.smi ; do
    hq submit --stdout=none --stderr=none obabel $f -O ${f%.*}.sdf --gen3d best &
done

# Wait until all jobs have finished, shut down the HyperQueue workers and server
hq job wait all
hq worker stop all
hq server stop

# Compress the output .sdf files and copy the package back to /scratch
tar -czf sdf.tar.gz *.sdf
cp sdf.tar.gz $SLURM_SUBMIT_DIR
```

{:start="2"}
2. As explained by the comments in the script above, HyperQueue works on a
   worker-server-client basis, i.e. a worker is started on each compute node
   which executes commands that the client submitted to the server
    - This is in principle what Slurm also does, only difference is that you
      need to start the server and workers yourself
3. Submit the script with:

```bash
sbatch hq.sh
```

{:start="4"}
4. After the job has finished (should take a couple of minutes), you should notice that a
   file `sdf.tar.gz` containing the output files has appeared in your working directory.
