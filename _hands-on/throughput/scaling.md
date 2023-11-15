---
topic: throughput
title: Tutorial - Performing a simple scaling test (essential)
---

# Performing a simple scaling test

> This tutorial requires that

- you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
- your account belongs to a project [that has access to the Puhti
  service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

> This tutorial is done on Puhti

## Overview

💬 Before running large jobs using a lot of computing resources (cores), one
needs to verify that the calculation actually can utilize the requested
resources efficiently.

💡 In this tutorial, you will perform a very simple scaling test, i.e. running
a parallel program with a varying number of cores and observing how it speeds
up.

## Download a sample parallel program

1. Create and enter a suitable scratch directory on Puhti (replace `<project>`
   with your CSC project, e.g. `project_2001234`):

```bash
mkdir -p /scratch/<project>/$USER/scaling-test
cd /scratch/<project>/$USER/scaling-test
```

{:start="2"}
2. Download a small program that computes the
   [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set) (a 2D fractal
   image) in parallel using OpenMP threading:
 
```bash
wget https://a3s.fi/CSC_training/mandelbrot.x
```

{:start="3"}
3. Edit the access permissions of the file to allow execution:

```bash
chmod +x mandelbrot.x
```

## Create a parallel batch job script

💬 We will run the Mandelbrot program multiple times using five different
thread counts; 1, 2, 4, 8 and 16.

1. Copy the following script into a file `job.sh` using, e.g., `nano`:

```bash
#!/bin/bash
#SBATCH --partition=test
#SBATCH --account=<project>   # replace <project> with your CSC project, e.g. project_2001234
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=<N>   # Replace <N> with appropriate number of threads
#SBATCH --time=00:05:00

srun mandelbrot.x
```

{:start="2"}
2. Replace `--cpus-per-task=<N>` in the script with `--cpus-per-task=1` in
   order to run the program using one thread per task.
3. Submit the script with:

```bash
sbatch job.sh
```

{:start="4"}
4. After a few moments, an output file `slurm-<jobid>.out` will appear in the
   current directory. View its contents once the job has finished (takes about
   one minute):

```bash
cat slurm-<jobid>.out   # Replace <jobid> with the actual Slurm job id
```

{:start="5"}
5. Repeat the above steps for the thread counts 2, 4, 8 and 16 by editing
   `--cpus-per-task` in the `job.sh` script and then resubmitting the job.

💭 Did the computation become faster? If so, is the scaling ideal, i.e. does
doubling the thread count also make it run twice as fast? If not, can you think
of any reasons that might limit the scalability? (Hint: Does all threads have
equal amount of work to do?)

☝🏻 To ensure efficient use of resources, a good rule of thumb is that when
you double the number of used cores the job should become *at least* 1.5 times
faster. If this is not the case, request fewer cores.

💡 Bonus! The example program produces a nice image of the Mandelbrot fractal.
You can view it with command `eog mandelbrot.png` (requires that you've enabled
X11 forwarding by connecting to Puhti with `ssh -X`), or by opening it from
the [Puhti web interface](https://www.puhti.csc.fi) file browser.
