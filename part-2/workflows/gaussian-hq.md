---
layout: default
title: Running Gaussian with sbatch-hq
parent: 11. How to speed up jobs
grand_parent: Part 2
nav_order: 4
has_children: false
has_toc: false
permalink: /hands-on/throughput/gaussian_hq.html
---

# Using HyperQueue for farming Gaussian jobs on Puhti

> This tutorial is done on **Puhti**, which requires that:

- You have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
- Your account belongs to a project [that has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

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
- We will use the `sbatch-hq` wrapper which allows easy execution of many
  commands without needing to write a batch script.

### The workflow of this exercise

1. Download 200 sample molecular structures.
2. Convert these structures to Gaussian format.
3. Construct the corresponding Gaussian input files.
4. Build a `sbatch-hq` command list to run the jobs.
5. Submit the job using the `sbatch-hq` wrapper.
6. Analyze the results.

## Download 200 sample 3D molecular structures

1. Create and enter a suitable scratch directory on Puhti (replace `<project>`
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
   module load openbabel
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
     echo "g16 < ${f} >> output/$(basename ${f%.*}).log" >> commandlist
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

### Run the HyperQueue task array with `sbatch-hq`

💬 Running a HyperQueue task array is similar to running a Slurm array job.
However, HyperQueue packs the individual tasks within a single Slurm job step
and is thus much more efficient, especially if there are a huge number of
tasks. In this case, submitting the job is also very easy since we can use the
`sbatch-hq` wrapper to avoid having to create a batch script by hand.

1. Submit the list of Gaussian commands using `sbatch-hq`:

   ```bash
   module load sbatch-hq gaussian
   sbatch-hq --cores=4 --nodes=1 --account=<project> --partition=small --time=00:15:00 commandlist
   ```

💬 The `sbatch-hq` command creates and submits a batch script that starts the
HyperQueue server and worker(s) and submits the task array with inputs read
from the `commandlist` file. The following resources are requested:

- One Puhti node, `--nodes=1`, i.e. 40 cores in total
- 4 cores per command, `--cores=4`, matching the specification in each Gaussian
  input file
- Computing time for 15 minutes, `--time=00:15:00`
- Billing project `--account <project>` (replace `<project>` accordingly)
- The `small` partition

💬 Given that 40 cores are requested for running 200 tasks, each using 4 cores,
10 tasks are able to run concurrently. The number of commands in the file can
(usually should) be much larger than the number of commands that can fit
running simultaneously on the reserved resources to avoid creating too short
Slurm jobs.

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
   export HQ_SERVER_DIR=$PWD/hq-server-<slurmjobid>   # replace <slurmjobid> with the actual id of your Slurm job
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
