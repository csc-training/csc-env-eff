---
layout: default
title: Running Gaussian with HyperQueue
parent: 11. How to speed up jobs
grand_parent: Part 2
nav_order: 4
has_children: false
has_toc: false
permalink: /hands-on/throughput/gaussian_hq.html
---

# Using HyperQueue for farming Gaussian jobs on Roihu

> This tutorial is done on **Roihu**, which requires that:

- You have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
- Your account belongs to a project [that has access to the Roihu service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

> This tutorial is **optional** as it requires that your account belongs to the
Gaussian users group. See [Docs CSC](https://docs.csc.fi/apps/gaussian/#license)
for details on how to get added.

## Overview

💬 [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) is a tool for efficient
sub-node task scheduling and well suited for task farming and running
embarrassingly parallel jobs.

💬 In this example, we have several similar molecular structures and would like
to know how they differ energetically.

- The aim is to run Gaussian calculations on 200 different structural isomers
  corresponding to the C<sub>7</sub>O<sub>2</sub>H<sub>10</sub> molecular
  formula.
- The computational cost of each of the 200 calculations is expected to be
  comparable.

### The workflow of this exercise

1. Download 200 sample molecular structures.
2. Convert these structures to Gaussian format.
3. Construct the corresponding Gaussian input files.
4. Build a command list, and a small script that picks one
   command per HyperQueue task.
5. Write and submit a batch script that starts the HyperQueue
   server and worker(s) that runs the task array.
6. Analyze the results.

## Download 200 sample 3D molecular structures

1. Create and enter a suitable scratch directory on Roihu (replace `<project>`
   with your CSC project, e.g. `project_2001234`):

   ```bash
   mkdir -p /scratch/<project>/$USER/gaussian-hq
   cd /scratch/<project>/$USER/gaussian-hq
   ```

2. Download the 200 C<sub>7</sub>O<sub>2</sub>H<sub>10</sub> structures that
   have originally been obtained from the
   [QM9 dataset](https://doi.org/10.6084/m9.figshare.c.978904.v5):
  
   ```bash
   wget https://a3s.fi/CSC_training/C7O2H10.tar.gz
   ```

3. Unpack the archive:

   ```bash
   tar -xzf C7O2H10.tar.gz
   ```

4. Go to the directory containing the structure files that are in [`.mol`
   format](https://openbabel.org/docs/FileFormats/MDL_MOL_format.html):

   ```bash
   cd C7O2H10
   ```

## Convert the structures to Gaussian format

💬 [Gaussian](https://docs.csc.fi/apps/gaussian/) is a program for molecular
electronic structure calculations.

1. Use [OpenBabel](https://docs.csc.fi/apps/openbabel/) to convert the
   structures to Gaussian format:

   ```bash
   module load gcc/15.2.0 openmpi/5.0.10 openbabel/3.2.0
   obabel *.mol -ocom -m
   ```

2. Now we have converted the 200 structures into `.com` format that is used by
   Gaussian.

## Construct the corresponding Gaussian input files

💬 In this example we want to do a `b3lyp/cc-pVDZ` calculation on these
structures, i.e. a hybrid density functional theory calculation using the
B3LYP exchange-correlation functional and the cc-PVDZ basis set.

1. Add the `b3lyp/cc-pVDZ` keyword at the beginning of each `.com` file:

   ```bash
   sed -i '1s/^/#b3lyp\/cc-pVDZ \n/' *.com
   ```

2. Set 4 cores per job by adding the flag `%NProcShared=4` to each input file:

   ```bash
   sed -i '1s/^/%NProcShared=4\n/' *.com
   ```

3. Now you have 200 complete Gaussian input files corresponding to the original
   molecular structures and the method of choice.

## Build a command list to run the jobs as a HyperQueue task array

💬 A task array can sometimes be lengthy, so rather than typing it by hand, it
is more feasible to use bash scripting to create a suitable task list file for
HyperQueue.

1. Move back up to your main directory:

   ```bash
   cd ..
   ```

2. Create the task list and name it `commandlist`:

   ```bash
   for f in ${PWD}/C7O2H10/*.com; do
     echo "subg16 < ${f} >> output/$(basename ${f%.*}).log" >> commandlist
   done
   ```

3. Inspect the task list with `more`, `less` or `cat`. The file should look
   like:

   ```bash
   g16 < /scratch/<project>/$USER/gaussian-hq/C7O2H10/dsC7O2H10nsd_0001.com >> output/dsC7O2H10nsd_0001.log
   g16 < /scratch/<project>/$USER/gaussian-hq/C7O2H10/dsC7O2H10nsd_0002.com >> output/dsC7O2H10nsd_0002.log
   g16 < /scratch/<project>/$USER/gaussian-hq/C7O2H10/dsC7O2H10nsd_0003.com >> output/dsC7O2H10nsd_0003.log
   ...
   ```

4. Notice that the output will be directed into a directory called `output`.
   Create this directory:

   ```bash
   mkdir -p output
   ```

5. Write a small executable script, `run_task.sh`, that each HyperQueue task
   will run. It picks out and executes the single line of `commandlist`
   corresponding to its own task ID, available to the task as the `$HQ_TASK_ID`
   environment variable:

   ```bash
   #!/bin/bash
   # Pick the line matching this task's HyperQueue task ID
   line=$(sed -n "${HQ_TASK_ID}p" commandlist)
   eval "${line}"
   ```

### Run the HyperQueue task array

💬 Running a HyperQueue task array is similar to running a Slurm array job.
However, HyperQueue packs the individual tasks within a single Slurm job step
and is thus much more efficient, especially if there are a huge number of
tasks. 

1. Create a batch script called `batch.sh`:

   ```bash
   #!/bin/bash
   #SBATCH --account=<project>
   #SBATCH --partition=small
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=1
   #SBATCH --cpus-per-task=40
   #SBATCH --mem-per-cpu=500
   #SBATCH --time=00:15:00

   module load hyperqueue gaussian/G16RevC.02

   # Server files go in a job-specific directory. One server per job to avoid mixing computations
   export HQ_SERVER_DIR="$PWD/hq-server/$SLURM_JOB_ID"
   mkdir -p "$HQ_SERVER_DIR"

   # Start the server in the background and wait until it is up
   hq server start &
   until hq job list &> /dev/null ; do sleep 1 ; done

   # Start one worker with srun
   srun --overlap --cpu-bind=none --mpi=none hq worker start \
      --manager slurm \
      --on-server-lost finish-running \
      --cpus="$SLURM_CPUS_PER_TASK" &
   hq worker wait "$SLURM_NTASKS"

   # Submit the 200 Gaussian calculations as a task array. Each task reserves
   # 4 cores, matching the %NProcShared=4 setting in the Gaussian input files,
   # so up to 10 tasks run concurrently on the 40 reserved cores
   hq submit --stdout=none --stderr=none --cpus=4 --array=1-200 ./run_task.sh
   hq job wait all

   # Shut down the worker and server to avoid a false error from Slurm
   hq worker stop all
   hq server stop
   ```

💬 The batch script requests the following resources:

- 40 cores, `--cpus-per-task=40`, on the shared `small` partition
  (which allows up to 384 CPUs per job)
- Computing time for 15 minutes, `--time=00:15:00`
- Billing project `--account=<project>` (replace `<project>` accordingly)

💬 Given that 40 cores are reserved and each Gaussian task uses 4 cores
(`--cpus=4` in the `hq submit` line, matching `%NProcShared=4`), 10 tasks
are able to run concurrently. This means that no reserved cores sit idle 
in the final wave.

2. Submit the batch script:

   ```bash
   sbatch batch.sh
   ```

## Monitor the job

1. You can monitor the Slurm queue with (replace `<slurmjobid>` with the
   assigned Slurm job ID):

   ```bash
   squeue -j <slurmjobid>
   # or
   squeue --me
   # or
   squeue -u $USER
   ```

2. This does, however, not provide you information about the progress of the
   individual sub-tasks. To monitor these, export the location of the
   HyperQueue server and use the `hq` commands:

   ```bash
   export HQ_SERVER_DIR=$PWD/hq-server/<slurmjobid>   # replace <slurmjobid> with the actual id of your Slurm job
   hq job info 1
   ```

3. Once the workflow has finished (should take a bit more than 10 minutes),
   print a list of the `b3lyp/cc-pVDZ` energies for each of the 200 structures
   sorted by energy (most stable structure first):

   ```bash
   grep -r "E(RB3LYP)" output | sort -k6 -n -o energies.txt
   ```

4. Using `head energies.txt`, the output should look like:

   ```bash
   output/dsC7O2H10nsd_0015.log: SCF Done:  E(RB3LYP) =  -423.218630672     A.U. after   14 cycles
   output/dsC7O2H10nsd_0192.log: SCF Done:  E(RB3LYP) =  -423.216601925     A.U. after   12 cycles
   output/dsC7O2H10nsd_0193.log: SCF Done:  E(RB3LYP) =  -423.214963908     A.U. after   12 cycles
   output/dsC7O2H10nsd_0028.log: SCF Done:  E(RB3LYP) =  -423.214781165     A.U. after   13 cycles
   output/dsC7O2H10nsd_0037.log: SCF Done:  E(RB3LYP) =  -423.214421420     A.U. after   14 cycles
   output/dsC7O2H10nsd_0026.log: SCF Done:  E(RB3LYP) =  -423.214326717     A.U. after   14 cycles
   output/dsC7O2H10nsd_0008.log: SCF Done:  E(RB3LYP) =  -423.213824577     A.U. after   14 cycles
   output/dsC7O2H10nsd_0036.log: SCF Done:  E(RB3LYP) =  -423.212123483     A.U. after   14 cycles
   output/dsC7O2H10nsd_0025.log: SCF Done:  E(RB3LYP) =  -423.212093937     A.U. after   14 cycles
   output/dsC7O2H10nsd_0191.log: SCF Done:  E(RB3LYP) =  -423.211777369     A.U. after   13 cycles
   ```

## More information

- [HyperQueue page at Docs CSC](https://docs.csc.fi/apps/hyperqueue/)
- [Gaussian page at Docs CSC](https://docs.csc.fi/apps/gaussian/)
