---
layout: default
title: Application performance
parent: 11. How to speed up jobs
grand_parent: Part 2
nav_order: 5
has_children: false
has_toc: false
permalink: /hands-on/throughput/tune_performance.html
---

# Application performance

> This exercise is done on **Mahti**, which requires that

- you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
- your account belongs to a project [that has access to the Mahti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

## Overview

💬 In this exercise, you will optimize the performance of a real simulation use
case by tuning the number of cores used and ratio between MPI tasks and OpenMP
threads. As an example application, we will use the [CP2K](https://docs.csc.fi/apps/cp2k/)
software. The details of the code and what it does is not important for the
completion of this exercise. Just take it as an example parallel program that
uses hybrid MPI/OpenMP parallelization.

## Download a sample input file

1. Create and enter a suitable scratch directory on Puhti (replace `<project>`
   with your CSC project, e.g. `project_2001234`):

   ```bash
   mkdir -p /scratch/<project>/$USER/app-perf
   cd /scratch/<project>/$USER/app-perf
   ```

2. Download a sample input file:
 
   ```bash
   wget https://a3s.fi/CSC_training/cp2k.inp
   ```

💬 Reading/understanding the contents of this input file is not important for
the sake of completing this exercise.

## Scalability test

💬 You should first check how many CPU nodes can be used efficiently to run the
example simulation.

1. Modify the following batch script to request 1 node and save it into a file
   `cp2k.sh` using, e.g., `nano`:
   
   ```bash
   #!/bin/bash
   #SBATCH --partition=medium
   #SBATCH --account=<project>    # replace <project> with your CSC project, e.g. project_2001234
   #SBATCH --nodes=<N>            # replace <N> with the number of nodes to run on
   #SBATCH --ntasks-per-node=128  # Mahti has 128 CPU cores per node
   #SBATCH --time=00:10:00

   module purge
   module load gcc/9.4.0 openmpi/4.1.2 cp2k/2023.2
   srun cp2k.psmp -i cp2k.inp
   ```

2. Submit the batch script:
   
   ```bash
   sbatch cp2k.sh
   ```

3. Once the job has completed, you may use the program's internal timer to
   check how many seconds it took to run the simulation:

   ```bash
   grep "CP2K " slurm-<jobid>.out | awk '{print $7}'
   ```

4. Repeat the job for the number of nodes listed below and complete the table!
   Calculate the speedup by dividing the previous elapsed time with the elapsed
   time obtained using twice as many nodes:

   | Number of nodes | Elapsed time (s) | Speedup                         |
   |:---------------:|:----------------:|:-------------------------------:|
   |1                |                  | -                               |
   |2                |                  | *t*<sub>1</sub>/*t*<sub>2</sub> |
   |4                |                  | *t*<sub>2</sub>/*t*<sub>4</sub> |
   |8                |                  | *t*<sub>4</sub>/*t*<sub>8</sub> |

☝🏻 Remember that the speedup should be *at least* 1.5x when you double the
number of cores! This is important to ensure that the CPU resources are used
efficiently.

💭 To how many nodes is the job able to scale up to efficiently? Using that
node count, proceed to the next part!

## Assess optimal thread–task balance

💬 The performance of software using hybrid MPI/OpenMP parallelism may be 
further improved by running multiple OpenMP threads per MPI task. The optimal
ratio between the number of tasks and threads varies for each program and job
input and should be tested.

☝🏻 To run multiple threads, one needs to set `--cpus-per-task`. The default
is one CPU (thread) per task. To use all 128 physical cores in a Mahti node,
the value of `--ntasks-per-node` multiplied by `--cpus-per-task` should equal
128 (40 on Puhti). Most applications also require setting the `OMP_NUM_THREADS`
environment variable to be equal to the number of threads per task.

1. Copy the following script into a file `job.sh` using, e.g., `nano`:

   ```bash
   #!/bin/bash
   #SBATCH --partition=medium
   #SBATCH --account=<project>   # replace <project> with your CSC project, e.g. project_2001234
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=128
   #SBATCH --cpus-per-task=1
   #SBATCH --time=00:10:00

   export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

   module purge
   module load gcc/9.4.0 openmpi/4.1.2 cp2k/2023.2
   srun cp2k.psmp -i cp2k.inp
   ```

2. Submit the job using different combinations of `--ntasks-per-node` and
   `--cpus-per-task`.
   
   💡 The number of threads is stored by Slurm in the `SLURM_CPUS_PER_TASK`
   environment variable, which can then be used to set the value of
   `OMP_NUM_THREADS`.

3. Complete the table below:

   | MPI tasks per node  | OpenMP threads per task | Elapsed time (s) | Memory utilized (GB) |
   |:-------------------:|:-----------------------:|:----------------:|:--------------------:|
   |128                  |                         |                  |                      |
   |64                   |                         |                  |                      |
   |32                   |                         |                  |                      |
   |16                   |                         |                  |                      |
   |8                    |                         |                  |                      |

💭 Were you able to run the calculation faster by launching multiple OpenMP
threads per MPI task? What is the optimum ratio?

💭 How does the memory usage vary when you increase the number of threads per
task? Use the `seff` command to check. Can you explain the reason for your
observation?

## More information

- [Docs CSC: Performance checklist](https://docs.csc.fi/computing/running/performance-checklist/)
