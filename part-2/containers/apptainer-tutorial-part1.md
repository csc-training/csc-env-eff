---
layout: default
title: Apptainer tutorial 1
parent: 10. Containers and Apptainer
grand_parent: Part 2
nav_order: 1
has_children: false
has_toc: false
permalink: /hands-on/singularity/singularity-tutorial_part1.html
---

# Apptainer tutorial

💬 In this tutorial, we will get familiar with the basic usage of Apptainer
(previously Singularity) containers.

- To run these exercises on Puhti, use `sinteractive` or open a compute node
  shell in the [Puhti web interface](https://www.puhti.csc.fi).

  ```bash
  sinteractive --account <project>  # replace <project> with your CSC project, e.g. project_2001234
  ```

## Getting started

1. Download a test container image from Allas:

   ```bash
   wget  https://a3s.fi/saren-2001659-pub/tutorial.sif
   ls -lh tutorial.sif
   ```

2. The file we downloaded is a container image. It contains all the software
   and data of the container in a single file. In this case, the container is
   very bare-bones and thus quite small, about 50 MB.
   - Actual application containers are typically larger since they also contain
     the software installation and may in some cases include reference data,
     etc.

## Basic usage

💬 There are three basic ways to run software in an Apptainer container:

### Apptainer `exec`

1. To execute a command inside the container, use `apptainer exec`:

   ```bash
   apptainer exec tutorial.sif hello_world
   ```

2. Compare the outputs of the following commands:

   ```bash
   grep "^NAME" /etc/os-release
   apptainer exec tutorial.sif grep "^NAME" /etc/os-release
   ```

   - The first command is run on the host, the second command is run inside the
     container.

   💭 The tutorial container is based on Ubuntu 18.04. The host and the
   container use the same kernel, but the rest of the system can vary.

   - This means that a container can be based on a different Linux distribution
     than the host (as long as they are kernel-compatible), but it can't run a
     totally different OS, such as Windows or macOS.

#### In batch jobs

💡 `apptainer exec` is the run method you would typically use in batch job
scripts.

1. Create a file called `test.sh`:

   ```bash
   module load nano  # The compute nodes do not have nano available by default
   nano test.sh
   ```

2. Copy the following contents into the file and replace `<project>` with your
   actual CSC project, e.g. `project_2001234`:

   ```bash
   #!/bin/bash
   #SBATCH --job-name=test           # Name of the job visible in the queue.
   #SBATCH --account=<project>       # Choose the billing project. Has to be defined!
   #SBATCH --partition=test          # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
   #SBATCH --time=00:01:00           # Maximum duration of the job. Max: depends of the partition. 
   #SBATCH --mem=1G                  # How much RAM is reserved for job per node.
   #SBATCH --ntasks=1                # Number of tasks. Max: depends on partition.
   #SBATCH --cpus-per-task=1         # How many processors work on one task. Max: Number of CPUs per node.
   
   apptainer exec tutorial.sif hello_world
   ```

3. Submit the job to the queue with:

   ```bash
   sbatch test.sh
   ```

💡 For more information about batch jobs, see the
[batch jobs section](../../part-1/batch-jobs/index.md).

### Apptainer `run`

💬 When containers are created, a standard action called the `runscript` is
defined. Depending on the container, it may simply print out a message, or it
may launch a program or service inside the container.

💭 If you are using a container created by someone else, you will need to check
the documentation provided by the creator for details.

1. In our test container the `runscript` prints out a simple message:

   ```bash
   apptainer run tutorial.sif
   ```

2. Give the container image execution rights so that you can run it directly:

   ```bash
   chmod u+x tutorial.sif
   ./tutorial.sif
   ```

3. You can see the actual script with the command:

   ```bash
   apptainer inspect --runscript tutorial.sif
   ```

### Apptainer `shell`

1. Open a shell inside the container:

   ```bash
   apptainer shell tutorial.sif
   ```

2. Notice that the command prompt changed. You can now run any software inside
   the container interactively:

   ```bash
   hello_world
   ```

1. Exit the container with:

   ```bash
   exit
   ```

## More information

💬 This tutorial is meant as a brief introduction to get you started.

☝🏻 When searching online for instructions, pay attention that the instructions
are for the same version of Apptainer as you are using. There has been some
command syntax changes etc. between versions, so older instructions may not
work as is. Also note that Apptainer was formerly known as Singularity.

💡 For more detailed instructions, see the official
[Apptainer documentation](https://apptainer.org/docs/user/latest/).
