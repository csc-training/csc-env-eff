---
topic: Batch jobs
title: Tutorial - Serial batch jobs (essential)
---

# Batch job tutorial - Serial jobs

> In this tutorial we'll get familiar with the basic usage of the Slurm batch queue system at CSC
- The goal is to learn how to request resources that **match** the needs of a job  

💬 A batch job consists of two parts: resource requests and the job step(s)

☝🏻 Examples are done on Puhti 

## Serial jobs

💬 A serial program can use only one core (cpu)
    - One should request only one core from Slurm. 
    - The job doesn't benefit from additional cores
    - Excess reservation is wasted since it wouldn't be available to other users

💬 Within the job (or allocation), the actual program is launched using the command `srun` 

☝🏻 If you use a software that is preinstalled at CSC, please [check its info-page](https://docs.csc.fi/apps/): it might have a batch job template with useful default settings

### Launching a serial job

1. Go to the scratch folder. 
    ```bash
    cd /scratch/project_XXXX         # replace XXXX
    ```
    - Now your input (and output) are on a disk that is accessible on the compute node.
    
💡 You can list your projects with `csc-projects`).
💡 Note! If you're using a project with other members (like the course project), first make a subfolder for yourself (e.g. `mkdir MYSERNAME` (change MYUSERNAME) and then change there not to clutter thet scratch root of your project `cd MYUSERNAME`)

{:start="2"}
2. Create a file called `my_serial.bash` eg. with Nano:
    ```bash
    nano my_serial.bash
    ```

{:start="3"}
3. Copy the the following **batch script** there: 

    ```bash
    #!/bin/bash
    #SBATCH --account=project_XXXX    # Choose the billing project. Has to be defined!
    #SBATCH --time=00:02:00          # Maximum duration of the job. Max: depends of the partition. 
    #SBATCH --partition=test         # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
    #SBATCH --ntasks=1               # Number of tasks. Max: depends on partition.

    srun hostname                    # Run hostname-command in each task
    srun sleep 60                    # Run sleep-command in each task
    ```  

{:start="4"}
4. Change the `project_XXXX` to the project you actually want to use (e.g. with `nano`)
- Submit the job to the queue and then check the queue with the commands:

    ```bash
    sbatch my_serial.bash
    squeue -u $USER
    ``` 

💬 In the batch job example above we are requesting 
- one core (`--ntasks=1`) 
- for two minutes (`--time=00:02:00`) 
- from the test queue (`--partition=test`)  

💬 We want to run the program `hostname`, that will print the name of the Puhti computing node that has been allocated for this particular job.  
💬 In addition, we are running the `sleep` program to keep the job running for an additional 60 seconds, in order to have time to monitor the job  

#### Checking the output and the efficiency
- By default the output is written into a file named `slurm-XXXXXXX.out` where `XXXXXXX` is the unique job ID
- Check the efficiency of the job compared to the reserved resources by issuing the command `seff XXXXXXX` (replace `XXXXXXX` with the job ID number from the `slurm-XXXXXXX.out` file) 

💭 You can get a list of all your jobs that are running or queuing with the command `squeue -u $USER`  
🗯 A submitted job can be cancelled using the command `scancel XXXXXXX` 

## More information
💡 [FAQ on CSC batch jobs ](https://docs.csc.fi/support/faq/#batch-jobs) in Docs CSC
