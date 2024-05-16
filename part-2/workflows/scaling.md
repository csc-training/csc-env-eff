---
layout: default
title: Performing a simple scaling test
parent: 11. How to speed up jobs
grand_parent: Part 2
nav_order: 1
has_children: false
has_toc: false
permalink: /hands-on/throughput/scaling.html
---

# Performing a simple scaling test

> This tutorial is done on **Puhti**, which requires that

- you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
- your account belongs to a project that has
  [access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

## Overview

💬 Before running large jobs using a lot of computing resources (cores), it is
important to verify that the calculation actually can utilize the requested
resources efficiently.

💡 In this tutorial, you will perform a very simple scalability test, i.e.
running a parallel program with a varying number of cores and observing how it
speeds up.

## Download a sample parallel program

1. Create and enter a suitable scratch directory on Puhti (replace `<project>`
   with your CSC project, e.g. `project_2001234`):

   ```bash
   mkdir -p /scratch/<project>/$USER/scalability-test
   cd /scratch/<project>/$USER/scalability-test
   ```

2. Download a toy program that performs a simple molecular dynamics simulation
   in parallel using OpenMP threading. Understanding the details of the code is
   not important for the completion of this tutorial.

   ```bash
   wget https://a3s.fi/CSC_training/md
   ```

3. Edit the access permissions of the file to allow execution:

   ```bash
   chmod +x md
   ```

## Create a parallel batch job script

💬 We will run the MD program multiple times using six different thread counts;
1, 2, 4, 8, 16 and 32.

1. Copy the following script into a file `job.sh` using, e.g., `nano`:

   ```bash
   #!/bin/bash
   #SBATCH --partition=test
   #SBATCH --account=<project>   # replace <project> with your CSC project, e.g. project_2001234
   #SBATCH --nodes=1
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=<N>   # Replace <N> with appropriate number of threads
   #SBATCH --time=00:05:00

   export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
   srun md --particles=500 --steps=5000
   ```

2. Replace `--cpus-per-task=<N>` in the script with `--cpus-per-task=1` in
   order to run the program using one thread per task.
3. Submit the script with:

   ```bash
   sbatch job.sh
   ```

4. After a few moments, an output file `slurm-<jobid>.out` will appear in the
   current directory. View its contents once the job has finished (takes less
   than a minute):

   ```bash
   cat slurm-<jobid>.out   # Replace <jobid> with the actual Slurm job id
   ```

5. Repeat the above steps for the thread counts 2, 4, 8, 16 and 32 by editing
   `--cpus-per-task` in the `job.sh` script and then resubmitting the job. If
   you have limited time, you may also just download a set of pre-calculated
   results:

   ```bash
   wget https://a3s.fi/CSC_training/scaling-test.tar
   tar -xvf scaling-test.tar
   ```

6. Check the elapsed time of each simulation once they have completed:

   ```bash
   grep "Elapsed time" *.out | sort -n
   ```

💭 Did the computation become faster? If so, is the scaling ideal, i.e. does
doubling the thread count also make it run twice as fast? If not, can you think
of any reasons that might limit the scalability? How many threads does it make
sense to run the program with?

☝🏻 To ensure efficient use of resources, a good rule of thumb is that when
you double the number of used cores the job should become *at least* 1.5 times
faster. If this is not the case, request fewer cores.

💡 Bonus! Increase the problem size by increasing `--particles=<value>`. Is the
program now able to scale to a larger number of threads? Why does
`--steps=<value>` not have the same effect?

## More information

💡 Docs CSC: [Performance checklist](https://docs.csc.fi/computing/running/performance-checklist/)
