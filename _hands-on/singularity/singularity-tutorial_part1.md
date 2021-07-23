---
topic: singularity
title: Tutorial - Singularity introduction 
---

# Singularity tutorial

💬 In this tutorial we get familiar with the basic usage of Singularity containers. 

- To run these exercises in Puhti, use `sinteractive`.
```bash
sinteractive --account project_XXXX   # Change the XXXX for the project number
```
## Getting started

- To get started, download a test container image from allas.
```bash
wget  https://a3s.fi/saren-2001659-pub/tutorial.sif
ls -lh tutorial.sif
```
- As you can see, the container is a single file. In this case the container is very bare-bones, and thus quite small, about 50 MB. 
    - Actual application containers are typically larger, since they also contain the 
software installation, and may in some cases include some reference data etc.

## Basic usage

- There are three basic ways to run software in a Singularity container:

### 1. Singularity exec
- To execute a command inside the container, the command is `singularity exec`.
```bash
singularity exec tutorial.sif hello_world
```
- Compare the outputs of the following commands:
```bash
cat /etc/*release
singularity exec tutorial.sif cat /etc/*release
```
- The first command is run in the host. The second command is run inside the container.

💭 The tutorial container is based on Ubuntu 18.04. The host and the container use the same kernel, but the rest of the system can vary. That means a container can be based on a different Linux distribution than the host (as long as they are kernel-compatible), but can't run a totally different OS like Windows or macOS.

💡 `Singularity exec` is the run method you will typically use in a batch job script.

- Make a file called `test.sh`:
```bash
module load nano   # The computing node does not have nano by default
nano test.sh
```
- Copy the following contents into the file. 
    - Change "project_xxxx" to the correct project name.
```bash
#!/bin/bash
#SBATCH --job-name=test           # Name of the job visible in the queue.
#SBATCH --account=project_xxxx    # Choose the billing project. Has to be defined!
#SBATCH --partition=test          # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --time=00:01:00           # Maximum duration of the job. Max: depends of the partition. 
#SBATCH --mem=1G                  # How much RAM is reserved for job per node.
#SBATCH --ntasks=1                # Number of tasks. Max: depends on partition.
#SBATCH --cpus-per-task=1         # How many processors work on one task. Max: Number of CPUs per node.

singularity exec tutorial.sif hello_world
```
- Submit the job to the queue with:
```bash
sbatch test.sh
```
💭 For more information on batch jobs, please see [CSC Docs pages](https://docs.csc.fi/computing/running/getting-started/).

### 2. Singularity run
💬 When containers are created, a standard action, called the `runscript` is defined. Depending on the container, it may simply print out a message, or it may launch a program or service inside the container. 

💭 If you are using a container created by somebody else, you will need to check the documentation provided by the creator for details.

- In our test container it prints out a simple message:
```bash
singularity run tutorial.sif
```
- Give the container image execute rights and you can also run it directly:
```bash
chmod u+x tutorial.sif
./tutorial.sif
```
- You can see the actual script with command:
```bash
singularity inspect --runscript tutorial.sif
```

### 3. Singularity shell
- It is also possible to open a shell inside the container. 
```bash
singularity shell tutorial.sif
```
- You can see the command prompt change to `Singularity>`. You can now run any software inside the container interactively:
```bash
hello_world
```
- You can exit the container with:
```bash
exit
```

## More information

💬 This tutorial is meant as a brief introduction to get you started.

💭 When searching the internet for instruction, pay attention that the instructions are for the same version of Singularity that you are using. There has been some command syntax changes etc. between the versions, so older instructions may not work with copy-paste.

💡 For authoritative instructions see [Singularity documentation](https://sylabs.io/docs/).
