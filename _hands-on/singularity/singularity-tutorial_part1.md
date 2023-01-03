---
topic: apptainer
title: Tutorial - Introduction to Apptainer (essential)
---

# Singularity tutorial

💬 In this tutorial, we will get familiar with the basic usage of Apptainer (Singularity) containers. 

1. To run these exercises in Puhti, use `sinteractive`.
```bash
sinteractive --account project_xxxx   # Change the xxxx for the project number
```

## Getting started

{:start="2"}
2. Download a test container image from allas.
    ```bash
    wget  https://a3s.fi/saren-2001659-pub/tutorial.sif
    ls -lh tutorial.sif
    ```
3. As you can see, the container is a single file. In this case, the container is very bare-bones, and thus quite small, about 50 MB. 
    - Actual application containers are typically larger, since they also contain the software installation, and may in some cases include some reference data, etc.

## Basic usage

💬 There are three basic ways to run software in an Apptainer container:

### Apptainer exec
1. To execute a command inside the container, the command is `singularity exec`.
    ```bash
    apptainer exec tutorial.sif hello_world
    ```
2. Compare the outputs of the following commands:
    ```bash
    cat /etc/*release
    apptainer exec tutorial.sif cat /etc/*release
    ```
    - The first command is run in the host. The second command is run inside the container.

💭 The tutorial container is based on Ubuntu 18.04. The host and the container use the same kernel, but the rest of the system can vary. 
- That means a container can be based on a different Linux distribution than the host (as long as they are kernel-compatible), but it can't run a totally different OS, such as Windows or macOS.

#### Apptainer exec in batch jobs
💡 `apptainer exec` is the run method you will typically use in a batch job script.

1. Make a file called `test.sh`:
    ```bash
    module load nano   # The computing node does not have nano by default
    nano test.sh
    ```
2. Copy the following contents into the file and change "project_xxxx" to the correct project name:
    ```bash
   #!/bin/bash
   #SBATCH --job-name=test           # Name of the job visible in the queue.
   #SBATCH --account=project_xxxx    # Choose the billing project. Has to be defined!
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

💡 For more information on batch jobs, please see [CSC Docs pages](https://docs.csc.fi/computing/running/getting-started/).

### Apptainer runs
💬 When containers are created, a standard action, called the `runscript` is defined. Depending on the container, it may simply print out a message, or it may launch a program or service inside the container. 

💭 If you are using a container created by somebody else, you will need to check the documentation provided by the creator for details.

1. In our test container it prints out a simple message:
    ```bash
    apptainer run tutorial.sif
    ```
2. Give the container image execute rights and you can also run it directly:
    ```bash
    chmod u+x tutorial.sif
    ./tutorial.sif
    ```
3. You can see the actual script with command:
    ```bash
    apptainer inspect --runscript tutorial.sif
    ```

### Apptainer shell

1. Open a shell inside the container. 
    ```bash
    apptainer shell tutorial.sif
    ```
2. You can see the command prompt change to `apptainer>`. You can now run any software inside the container interactively:
    ```bash
    hello_world
    ```
3. Exit the container with:
    ```bash
    exit
    ```

## More information

💬 This tutorial is meant as a brief introduction to get you started.

☝🏻 When searching the internet for instruction, note that the instructions are for the same version of Apptainer that you are using. There has been some command syntax changes, etc., between the versions, so older instructions may not work with copy-paste. Also note that Apptainer used to be called Singularity. 

💡 For more details, see [Apptainer documentation]([https://apptainer.org/docs/user/latest/](https://apptainer.org/docs/user/latest/)).
