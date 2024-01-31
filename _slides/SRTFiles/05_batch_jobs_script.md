---
theme: csc-2019
lang: en
---

# The batch job system in CSC's HPC environment {.title}

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All material (C) 2020-2021 by CSC -IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

:::info (speech)
This lecture is about batch jobs and how to submit them in CSC supercomputers.
:::

# What is a batch job? 1/2
- On a laptop we are used to start a program (job) by clicking on an icon and the job starts instantly
- If we start many jobs at the same time we occasionally run into problems like running out of memory _etc._
- In an HPC environment the computer is shared among hundreds of other users who all have different resource needs
- HPC batch jobs include an **estimate (requirement) on how much resources they are expected to use**

:::info (speech)
On a laptop when you run something, you double click an icon, and the program starts to run.
Modern computers can run multiple tasks at the same time – but with too many simultaneus tasks, you start to run out of memory or CPU power, which slows down the computer. 
In the HPC environment really many people are using that same computer, and they all need different amounts of resources.
It is not possible to let everyone start their programs and run them in real time.
A batch job tells the batch job scheduler the resource requirements: how much resources should be available for that particular job.
:::

# What is a batch job? 2/2
- A batch job consists of two parts: A resource request and the actual computing step
- A job is not started directly, but is sent into a **queue**
- Depending on the requested resources and load, the job may need to wait to get started
- At CSC (and HPC systems in general) all heavy computing must be done via batch jobs (see [Usage policy](https://docs.csc.fi/computing/overview/#usage-policy))

:::info (speech)
In addition to the resource request, a batch job includes some script, that does the actual computing. 
To ensure that there's sufficient computing power available for all users, the batch jobs are sent to a queue. 
Depending on what kind of resources you requested, and the current load on the system, the job may need to queue for some time before it starts.
On HPC systems all heavy computing needs to be done by a batch job, so that they get executed on the compute nodes.
:::

Switch to # [Docs: Usage policy](https://docs.csc.fi/computing/overview/#usage-policy)

:::info (speech)
The usage policy in docs.csc.fi says that the login nodes are not meant for long or heavy processes.
Instead the login nodes are used for compiling, managing batch jobs, moving data, light pre- and postprocessing.
:::

# What is a batch job system?
- A resource management system that keeps track of all batch jobs that use, or would like to use the computing resources
- Aims to share the resources in an efficient and fair way
- Optimizes resource usage by filling the compute node with most suitable jobs

:::info (speech)
A batch job system handles the batch jobs submitted to the supercomputer.
It keeps track on what resources exist, which requests have been made, when to allocate resources, and how to run those jobs with the given resources. 
The aim is to use the resources as efficiently as possible, but also share them in a fair way.
For example, when a job needs a lot of memory, then it is allocated to a node where this memory is available.
Then if an other job does not need that much memory, it gets allocated so that the more demanding jobs can run with enough resources. 
:::

# Queueing and fair share of resources
- A job is queued and starts when the requested resources become available
- The order in which the queued jobs start depends on their priority and available resources
- At CSC the priority is configured to use "fair share"
   - The _initial_ priority of a job _decreases_ if the user has recently run lots of jobs
   - Over time (while queueing) its priority _increases_ and eventually it will run
   - Some queues have a lower priority (like _longrun_ -- use shorter if you can!)
- See our main documentation on [Getting started with running jobs](https://docs.csc.fi/computing/running/getting-started/) section in docs.csc.fi

:::info (speech)
The fair way of allocating resources is not the "first come first served", but instead that everyone gets resources, at least at some point.
Obviously a job cannot start before the requested resources are available. 
Each job has a "priority", which is used to determine the order of starting jobs.
The "fair share" configuration has the following rules of defining the priority.

When you submit a job it gets an initial priority. 
This initial priority decreases, if you have recently run a lot of jobs. 
That makes it possible to first run some small test, and get the results fast, before submitting a large set of calculations.
Once a job is in queue, its priority increases over time.
At some point it will have high enough priority, and it will be its turn next. 
The priority depends also on which queue the job is submitted.
For example longrun has lower priority – to discourage people to run in this unless necessary. 
If you do not want to queue so much for longrun resources, then consider refining your job, so that you can use the standard three day queues.
The documentation at docs.csc.fi has a guide for getting started with running jobs.
:::

# Schema on how the batch job scheduler works
![](./img/slurm-sketch.svg)

:::info (speech)
Here is an illustration on what the batch job scheduler is doing. 
The batch jobs are pictured here as two dimensional rectangles. 
The horisontal dimension represents the number of CPUs, and the vertical dimension represents time.
For example this tall but thin rectangle would correspond to a fairly long job, which is using just one core.
Then this short but wide rectangle would be a shorter job using many cores.
The batch job system sees these kind of job requests, and then it knows about the resources that the compute nodes have. 
The aim of the batch job scheduler is: to keep all the supercomputer resources busy with computing all of the time. 
That happens by allocating the jobs to the cores, leaving as little gaps as possible.
It is like playing Tetris, but with a variable size pieces.

But if the scheduler filled each gap with small jobs, there would never be enough resources free for larger jobs.
The increasing job priority enables that everybody gets resources at some point.
There are more resources than just CPUs, that the scheduler has to take into account.
As an example here is this small one-core job, which is colored in orange.
That job requires a lot of memory, and it is using all the memory left in this node.
That renders the node unavailable for new jobs to run, because there's no memory left. 
It means that these other cores in that node will be idle. 
And if this job really needs and uses this memory, this is totally fine. 
That is what memory is for, and one will run out before the other - memory or cores.
But, if the job does not need that much memory, then these cores will be unavailable for everyone for no reason.
Then everyone will be queuing more.
The lecture 6 will cover how to use the resources effectively, and I hope this example shows you the importance of that topic.
:::

# The batch job system in CSC's HPC environment
- CSC uses a batch job system [(SLURM)](https://slurm.schedmd.com/sbatch.html) to manage jobs 
- SLURM is used to control how the overall computing resources are shared among all projects in an efficient and fair way
- SLURM controls how a single job request gets resources, like:
    - computing time
    - number of cores
    - amount of memory
    - other resources like gpu, local disk, *etc.*

:::info (speech)
The batch job system used at CSC is called Slurm.
If you ever again wonder why you must use this Slurm, you remember that it is for sharing the awesome supercomputer resources in a fair and efficient way.
Some resources that you can ask from Slurm are listed here.
Computing time means how long should the resources be allocated to you. 
Number of cores, and the amount of memory, are the basic resources needed. 
Then there are a bit more special resources like GPUs, or the NVMe disks for fast file input and output.
:::

# Example serial batch job script for Puhti
- A batch job is a shell script (bash) that consists of two parts:
   - A resource request flagged with `#SBATCH` and the actual computing step(s)

```bash
#!/bin/bash
#SBATCH --job-name=print_hostname     # Defines the job name shown in the queue.
#SBATCH --time=00:01:00               # Defines the max time the job can run.
#SBATCH --partition=test              # Defines the queue in which to run the job.
#SBATCH --ntasks=1                    # Defines the number of tasks.
#SBATCH --cpus-per-task=1             # Number of cores is ntasks * cpus-per-task.
#SBATCH --account=project_20001234    # Defines the billing project. Mandatory field.

srun echo "Hello $USER! You are on node $HOSTNAME"
```
- The options have been described in [Create batch jobs for Puhti](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/)
   - The actual _program_ is launched using the `srun` command
   - The content above could be copied into a file like `simple_serial.bash` and put into the queue with the command `sbatch simple_serial.bash`

:::info (speech)
There is this example script in the slides, that you can use as a starting point when creating your first batch job.
This one uses only one core, so it is a serial job.
Consider a batch job as an ordinary shell script, like what you use with bash.
Therefore it also starts with the line: hashtag exclamation mark slash bin slash bash.
The difference to bash scripts is that the first part of the batch job contains the resource requests flagged with #SBATCH.
Remember that hashtag is a comment symbol in bash, so lines starting with hashtag-SBATCH does nothing as a bash script. 
Instead the queuing system understands those flags there.

The first one is called jobname, and in this example we provide it with a value print-hostname. 
The following flags define the requested time, and the partition in which to run the job.
Together the number of tasks, and the number of CPUs per task, define the number of cores needed for the job.
The last flag defines the billing project, which is very important.
If you don't specify a project – that you have access to, you will get an error. 
Then if you make some other mistake here, typically the error message will give you an idea how to proceed. 
If you omit any of the flags, it will use some reasonable default values, except of course with the account-flag.

Then the actual commands – or computing steps – come after the resource requests.
In general: they are scripted as in any batch script. 
Some commands or variables are spesific to CSC computing environment, and we try to provide you with best materials to get used to those.
Here this command srun tells the Slurm system to run a command.
Using srun makes the resource usage reports more accurate.
This echo-command is basic bash command, and it prints out the following string. 
In this example the string contains some useful environmental parameters.

To use this script you can copy-paste it into a textfile – named for example simple_serial.bash.
If you run it straight in Terminal, it would be run on the login node.
Never run these in the login node!
The right way to run this kind of script is with command sbatch, and then the name of the script.
The documentation covers the definitions and options of the SBATCH-flags.
:::

# Use an application specific batch script template

<div class="column">

- The [application list in docs](https://docs.csc.fi/apps/) contains example scripts for some software
- Use these as the *starting point* for your own scripts
- They have been tested and optimized (although for minimal resources) for *that* application
   - Consult the manual or other examples to adapt to your own needs
</div>
<div class="column">

![](img/apps-list.png "Applications list in docs.csc.fi"){width=90%}
</div>

:::info (speech)
Whenever you start to use a new application in CSC supercomputers, you should first consult the documentation at docs.csc.fi.
There you might also find a batch script template, that gives you a starting point with the application. 
The templates have some default values for the resources, so you may try those and edit them to suit your needs. 
Of course you will need to change the actual inputs and such in the computation step. 
In general it is better to start with these application spesific templates, than with a generic template. 
In any case, you will need to edit your batch job, so that it will match your use case.
:::

# Submitting, cancelling and stats of batch jobs
- The job script file is submitted with the command:
   - `sbatch example_job.sh`
- List all your jobs that are queuing/running:
   - `squeue -u $USER`
- Detailed info of a queuing/running job:
   - `scontrol show job <jobid>`
- A job can be deleted using the command:
   - `scancel <jobid>`
- Display the used resources of a completed job:
   - `seff <jobid>`

:::info (speech)
These are the most important commands for using the queueing system. 
Submit the batch job with command: sbatch example_job.sh.
Find all your jobs that are queuing or running with: squeue -u $USER. 
Pay attention to the job-ID, because that is needed for other commands such as
getting info on a job with: scontrol show job and the job-ID.
If you want to cancel a submitted job you can use: scancel and the job-ID.
The last command in this list is: seff and the job-ID.
That can be used to monitor the resources that the job used.
The point is to check whether your resource request actually matches what the job used. 
:::

# Available batch job partitions

- [The available batch job partitions](https://docs.csc.fi/computing/running/batch-job-partitions/) are listed in docs.csc.fi
- In order to use the resources in an efficient way, it is important to estimate the request as accurately as possible
- By avoiding an excessive "just-in-case" requests, the job will start earlier

:::info (speech)
The partitions, or job queues, have different properties that are listed in docs.csc.fi.
The purpose of having these different job queues is that the jobs can have very different needs – for example in terms of memory and computing time.
So estimate your resource request with thought, and choose which partition suits your job the best.
It is really bad practice just to ask so much resources that it will always be enough.
So please put some effort to study how much resources your jobs actually need. 
You will also benefit there, because your job is likely to start a little bit earlier, and there will be more resources for everyone using the supercomputer.
:::

Switch to # [Available batch job partitions in Docs CSC](https://docs.csc.fi/computing/running/batch-job-partitions/)

:::info (speech)
The available partitions are listed here in the docs.csc.fi.
Check the link to the instructions in the partition name.
The columns in the partition spreadsheet list for example the limits on run time, maximum number of tasks and nodes, and also the maximum memory available per job. 
Please notice, that there are a lot of these medium sized nodes available in some queues. 
Thus if you can specify your job such, that it fits in the medium sized node, then there are a lot of these resources available. 
The jobs that require more time or more memory – and therefore need to use hugemem or longrun – will probably be queuing longer. 
It is perfectly fine to ask for a lot of memory. 
This is why we have these big memory nodes. 
But if you don't need that much, then you might want to consider asking for resources, that are faster and easier to provide.
:::

# Different type of HPC jobs

- Typically an HPC job can be classified as serial, parallel or GPU, depending on the main requested resource 
- The following slides will provide you with an overview of different job types
- A serial job is the simplest type of job whereas parallel and GPU-jobs may require some advanced methods to fully utilise their capacity
- If you use already installed software be sure to study if it needs resources for serial, parallel or GPU jobs

:::info (speech)
One way to categorize jobs is: if it uses one or multiple cores.
Also a job can be interactive or non-interactive.
Different types of jobs are explained in the following slides.
Serial jobs are the simplest type of jobs, and thus a great starting point.
It is important to know the basics of different job types, also when using already installed software: 
you need to know which resources to request when you start the job.
:::

# HPC serial jobs

- A serial software can only use one core, so don't reserve more!
- Why could your serial job benefit from being executed using CSC's resources instead of on your own computer? 

    - Part of a larger workflow
    - Avoid data transfer between CSC and your own computer
    - Data sharing among other project members
    - CSC's software licensing
    - It was already installed
    - Memory and/or disk demands

:::info (speech)
One-core jobs are serial, because the core has to process the tasks one after another.
Please note, that you must not request more than one core for a serial job, because the job cannot utilise those extra cores.
That can be seen in a resource scaling test:
no matter how many cores you allocate, the job does not get any faster.
You could run many serial jobs in your laptop.
There are still reasons to run serial jobs in CSC supercomputers.
A serial jobs can be part of a larger user-defined workflow. 
The job might produce some results that you want to analyse with a supercomputer.
Or you want to share the results with your other CSC-project members.
You know already that there are many preinstalled software available in the CSC environment. 
You don't need to install the programs, or they might even have a license that we have already paid for. 
Also serial jobs can have some big demands on memory or fast disk. 
This is why we have Puhti huge memory nodes, and the local NVMe disks.
:::

# Running multiple serial jobs
- You can utilize parallel resources for running multiple serial jobs at the same time
    - [Array jobs](https://docs.csc.fi/computing/running/array-jobs/) 
    - [Other high throughput tools](https://docs.csc.fi/computing/running/throughput/)
    - Lots of other workflow tools or DIY scripts
- Pure serial resources are only available in Puhti
    - Some tools can make a set of serial jobs suitable for Mahti
    - **But**, the workflow needs to fill (at least) one Mahti node and keep the CPUs busy for the job duration

:::info (speech)
You can combine individual serial jobs to create a workflow, that can utilise parallel resources.
Here is two documented ways of running multiple jobs at the same time.
Array jobs mean simply that you submit multiple jobs with a simple command.
Other high throughput workflow tools are documented in DocsCSC. 
Of course, there are hundreds of other workflow tools, that somehow combine multiple single jobs into a bigger workflow. 
If your individual job is a serial job, then you should run it in Puhti. 
Some workflow tools make it possible to run multiple serial jobs also in Mahti. 
In that case all the jobs combined should fill at least one Mahti node – which means 128 cores – and they should keep it busy for the duration of the whole allocation. 
This is a bit advanced way of running jobs, so we recommend to start by running serial jobs in Puhti.
:::

# HPC parallel jobs

- A parallel job distributes the calculation over several cores in order to achieve a shorter wall time (and/or a larger allocatable memory)   
- There are two major parallelization schemes: [OpenMP](https://en.wikipedia.org/wiki/OpenMP) and [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface)
   - Note, depending on the parallellization scheme there is a slight difference between _how_ the resource reservation is done  
- Batch job script [how-to create](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/) and [examples](https://docs.csc.fi/computing/running/example-job-scripts-puhti/) for Puhti
- Batch job script [how-to create](https://docs.csc.fi/computing/running/creating-job-scripts-mahti/) and [examples](https://docs.csc.fi/computing/running/example-job-scripts-mahti/) for Mahti
- **The best starting point:** [Software specific batch scripts in docs](https://docs.csc.fi/apps/)

:::info (speech)
A parallel job distributes the calculation over several cores. 
That means it can use many cores for the same task simultaneously. 
On the other hand, you can also use the memory of multiple nodes at the same time, if your job requires it. 
There are two major schemes for parallelising jobs: openMP and MPI.
If you run a pre-installed code, then you don't need to worry about the details of these. 
Jobs parallelised with openMP can run only within one node, whereas MPI jobs can technically be spread over multiple nodes.
In certain cases, you can even combine those two. 
The important thing is: the job resource request is different for openMP and MPI. 
There are instructions and example batch scripts for both Puhti and Mahti available in docs.csc.fi.
Use them if there is no software specific batch script template available.
:::

# HPC GPU jobs 

- A graphics processing unit (GPU, a video card), is capable of doing certain type of simultaneous calculations very efficiently
- In order to take advantage of this power, a computer program must be reprogrammed to adapt on how GPU handles data   
- CSC's GPU resources are relatively scarce and hence should be used with [particular care](https://docs.csc.fi/computing/overview/#gpu-nodes)
    - A GPU uses 60 times more billing units than a single CPU core - see above for performance requirements
    - In practice, 1-10 CPU cores (but not more) should be allocated per GPU on Puhti

:::info (speech)
A GPU is a graphics processing unit. 
They are developed for very efficient parallel processing, because graphics processing requires that.
Hence they can also run certain kinds of HPC jobs very efficiently, for example machine learning jobs. 
To use GPUs a code has to be rewritten, compiled and linked to the libraries that can use GPU processors. 
GPU cards are also a bit more expensive than regular CPU cards. 
Therefore, one hour on GPU core spends 60 times more billing units than on a single CPU core. 
That means a full CPU node is a lot cheaper than one GPU core. 
On Puhti you should reserve one to 10 CPU cores for each reserved GPU core, because each Puhti GPU node has four GPU cards and 40 CPU cores. 
This means that in practice using GPU cores requires more than 60 times the billing units than to use a CPU core.
Please keep in mind, that if you allocate more than 10 CPU cores for one GPU, the node may run out of CPUs – which renders the GPUs unavailable.
:::

# Interactive jobs

- When you login to CSC's supercomputers, you end up in one of the login nodes of the computer
    - These login nodes are shared by all users and they are [not intended for heavy computing.](https://docs.csc.fi/computing/overview/#usage-policy)
- If you have a heavier job that still requires interactive response (_e.g._ a graphical user interface)
    - Allocate the resource via the the [interactive partition](https://docs.csc.fi/computing/running/interactive-usage/)
    - This way your work is performed in a compute node, not on the login node

:::info (speech)
As you login to a supercomputer, you get the command line interface, that enables you to execute commands in the supercomputer.
Please remember, that straight after login you are on a login node, which can not be used for any computing!
So if you want to use the powerful computational resources and to interact with your code, you can use the interactive jobs.
Those run on the interactive partition which has compute nodes. 
There you can execute commands as if it was your local laptop, albeit a more powerful one. 
Once you are there, you don't need to go through the queuing system.
For example a Jupyter notebook is something that you need to interact with, but you also might need some heavy computing resources.

The tutorials about batch jobs continue from here. 
They cover the basic use cases with easy-to-follow examples.
Remember that the batch job documentation includes some example batch scripts that you can start experimenting.
:::
