---
theme: csc-2019
lang: en
---

# The batch job system in CSC's HPC environment {.title}

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png)
</div>
<div class="column">
<small>
All material (C) 2020-2021 by CSC -IT Center for Science Ltd. and the authors.
This work is licensed under a **Creative Commons Attribution-NonCommercial-ShareAlike** 3.0
Unported License, [http://creativecommons.org/licenses/by-nc-sa/3.0/](http://creativecommons.org/licenses/by-nc-sa/3.0/)
</small>
</div>

# What is a batch job? 1/2
- On a laptop we are used to start a program (job) by clicking on an icon and the job starts instantly
- If we start many jobs at the same time we occasionally run into problems like running out of memory etc. 
- In an HPC environment the computer is shared among hundreds of other users who all have different resource needs
- HPC batch jobs include an **estimate (requirement) on how much resources they are expected to use**

# What is a batch job? 2/2
- A batch job consists of two parts: A resource request and the actual computing step
- A job is not started directly, but sent into a **queue**
- Depending on the requested resources and load, the job may need to wait to get started
- At CSC (and HPC systems in general) all heavy computing must be done via batch jobs (see [Usage policy](https://docs.csc.fi/computing/overview/#usage-policy))

# What is a batch job system? 1/2
- A resource management system that keeps track of all batch jobs that use, or would like to use the computing resources
- Aims to share the resources in an efficient and fair way
- Optimizes resource usage by filling the compute node with most suitable jobs

# What is a batch job system? 2/2
- A job is queued and starts when the requested resources become available
- The order in which the queued jobs start depend on available resources and their priority
- At CSC the priority is configured to use "fair share"
   - The initial priority of a job decreases if the user has recently run lots of jobs
   - Over time (while the job queues) its priority increases and eventually it will run
   - Some partitions may have a lower priority (like longrun - use shorter if you can!)

# Schema on how the batch job sheduler works
![](./img/slurm-sketch.svg)

# The batch job system in CSC's HPC environment 
- CSC uses a batch job system [(SLURM)](https://slurm.schedmd.com/sbatch.html) to manage jobs 
- SLURM is used to control how the overall computing resources are shared among all projects in an efficient and fair way
- SLURM controls how a single job request gets resources, like:
    - computing time
    - number of cores
    - amount of memory
    - other resources like gpu, local disk, etc.

# Example serial batch job script for Puhti

```text
#!/bin/bash -l
#SBATCH --job-name=print_hostname
#SBATCH --time=00:01:00
#SBATCH --partition=test
#SBATCH --ntasks=1
#SBATCH --account=project_20001234

srun echo "Hello $USER! You are on node $HOSTNAME"
```
- A batch job is a shell script (bash) that consists of two parts:
   - A resource request flagged with `#SBATCH` and the actual computing step(s)
- The `--account` option is mandatory to tell which project should be billed.
- The actual program is launched using the `srun` command
- The content above could be copied into a file like `simple_serial.bash` and put into the queue with the command `sbatch simple_serial.bash`

# Use an application specific batch script template

<div class="column">
- The [application list in docs](https://docs.csc.fi/apps/) contains example scripts for each software
- Use these as the *starting point* for your own scripts
- They have been tested and optimized (although for minimal resources) for *that* application
   - Consult the manual or other examples to adapt to your own needs
</div>
<div class="column">
![](img/apps-list.png "Applications list in docs.csc.fi"){width=90%}
</div>
 
# Available batch job partitions

- [The available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/) in docs.csc.fi
- In order to use the resources in an efficient way, it is important to estimate the request as accurately as possible
- By avoiding an excessive "just-in-case" request, the job will start earlier 
- Consult our [Getting started with the batch job system ](https://docs.csc.fi/computing/running/getting-started/)

# Different type of HPC jobs 1/2

- Typically an HPC job can be classified as serial, parallel or gpu, depending on the main requested resource 
- Each batch job is billed using a scheme that takes into account the requested resources
   - Note that the billing is based on the actual _time_ a job has **used**, not the reserved maximum time, but for _memory_ the **reservation** is billed
- See the [Billing unit (BU) and price calculator at research.csc.fi](https://research.csc.fi/billing-and-monitoring#buc)
- The billing is done per project

# Different type of HPC jobs 2/2
- Via the [My Projects page in MyCSC](https://my.csc.fi/welcome) you can monitor the BU consumption and apply for more billing units
- "csc-projects" is a command line tool for showing the BU consumption per project    

# Mapping your needs and the performance

- Before starting any large-scale calculations it's a good practice to check how the software and your actual input performs
    - Use short runs in the queue `--partition=test` to check that the input works and that the resource requests are interpreted correctly
    - If the program works in parallel check that it benefits from the requested parallel resources 
    - Check the output from the `seff` command to ensure that the cpu and memory performances are sufficient 

# HPC serial jobs 1/2

- A serial software can only use one core, so don't reserve more!
- Why could your serial job benefit from being executed using CSC's resources instead of on your own computer? 

    - Part of a larger workflow
    - Avoid data transfer between CSC and your own computer
    - Data sharing among other project members
    - CSC's software licensing
    - Memory and/or disk demands

# HPC serial jobs 2/2
- You can utilize parallel resources for running multiple serial jobs at the same time
    - [Array jobs](https://docs.csc.fi/computing/running/array-jobs/) 
    - [GREASY jobs](https://docs.csc.fi/computing/running/greasy/)
- Pure serial resources are only available in Puhti, but **GREASY jobs** can use Mahti, as well
 
# HPC parallel jobs

- A parallel job distributes the calculation over several cores in order to achieve a shorter wall time (and/or a larger allocatable memory)   
- There are two major parallelization schemes: [OpenMP](https://en.wikipedia.org/wiki/OpenMP) and [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface)
   - Note, depending on the parallellization scheme there is a slight difference between how the resource reservation is done  
- [Examples of batch job scripts on Puhti](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/)
- [Examples of batch job scripts on Mahti](https://docs.csc.fi/computing/running/example-job-scripts-mahti/)
- **Best:** [Software specific batch scripts in docs](https://docs.csc.fi/apps/)

# HPC GPU jobs 

- A graphics processing unit (GPU, a video card), is capable of doing certain type of simlutaneous calculations very efficiently
- In order to take advantage of this power, a computer program has to be reprogrammed to be adapt to how GPU's handles data   
- CSC's gpu resources are relatively scarce and hence should be used with [particular care](https://docs.csc.fi/computing/overview/#gpu-nodes)
    - A GPU uses 60 times more billing units than a single CPU core - see above for performance requirements

# Interactive jobs

- When you login to CSC's supercomputers, you end up in one of the login nodes of the computer.
    - These login nodes are shared by all users and they are [not intended for heavy computing.](https://docs.csc.fi/computing/overview/#usage-policy)
- If you have a heavier job that still requires interactive response (_e.g._ graphical user interface )
    - >llocate the resource via the the [interactive partition](https://docs.csc.fi/computing/running/interactive-usage/)

# Submitting, cancelling and stats of batch jobs
- The job script file is submitted with the command:
   - `sbatch batch_job.bash`
- List all your jobs that are queuing/running:
   - `squeue -u $USER`
- Detailed info of a queuing/running job:
   - `scontrol show job <jobid>`
- A job can be deleted using the command:
   - `scancel <jobid>`
- Display the used resources of a completed job:
   - `seff <jobid>`

# Reserving and optimizing batch job resources 

The computing resources are shared among hundreds of your colleagues, who all have different resource needs.
Try to estimate the resources that are needed for _your_ job, in order to minimize the **waste** 

* It's OK if a job is (occasionally) killed due to too small resource requests: just adjust and rerun/restart.
   - It's _worse_ to run with way too big requests without knowing it.
- Important resource requests that should be monitored are:
   - [Scaling of a job over several cores and nodes](https://docs.csc.fi/computing/running/performance-checklist/#perform-a-scaling-test)
   - [Memory requirement](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/)  
   - [Disk workload](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage)
   - [GPU efficiency](https://docs.csc.fi/computing/overview/#gpu-nodes)

