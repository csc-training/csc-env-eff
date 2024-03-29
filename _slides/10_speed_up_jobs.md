---
theme: csc-eurocc-2019
lang: en
---

# Not fast enough? How HPC can help. {.title}

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All materials (c) 2020-2023 by CSC – IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# The purpose of large computers

- Typically, large computers like those at CSC are not much faster than personal ones -- they are simply bigger
   - For fast computation, they utilize parallelism (and typically have special disk, memory and network solutions, too)
- Parallelism simplified:
   - You use hundreds of ordinary computers simultaneously to solve a single problem

# First steps for fast jobs (1/2)

- Spend a little time to investigate:
   - Which of the available software would be the best to solve the kind of problem you have?
      - Ask experienced colleagues or <servicedesk@csc.fi> for guidance
- Consider:
   - The software that solves your problem fastest might not always be the best
      - Issues like ease-of-use and compute power/memory/disk demands are also highly relevant
   - Quite often it is useful to start simple and gradually use more complex approaches if needed

# First steps for fast jobs (2/2)

- When you've found the software you want to use, check if it is available at CSC as a [pre-installed optimized version](https://docs.csc.fi/apps/)
   - Familiarize yourself with the software manual, if available
- If you need to install a software package distributed through Conda, [you need to containerize it](https://docs.csc.fi/computing/usage-policy/#conda-installations)
   - Containerizing greatly speeds up performance at startup and can be done easily with the [Tykky wrapper](https://docs.csc.fi/computing/containers/tykky/)
- If you can't find suitable software, consider writing your own code

# Optimize the performance of your own code (1/2)

- If you have written your own code, compile it with optimizing compiler options
   - Docs CSC: compiling on [Puhti](https://docs.csc.fi/computing/compiling-puhti/) and [Mahti](https://docs.csc.fi/computing/compiling-mahti/)
   - [Compiling on LUMI](https://docs.lumi-supercomputer.eu/development/)
- Construct a small and quick test case and run it in the test queue
   - Docs CSC: [Queue options](https://docs.csc.fi/computing/running/batch-job-partitions/)
   - [Available partitions on LUMI](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/)
   - Use the test case to optimize computations before starting massive ones

# Optimize the performance of your own code (2/2)

- Use profiling tools to find out how much time is spent in different parts of the code
   - Docs CSC: [Performance analysis](https://docs.csc.fi/computing/performance/)
   - [Profiling on LUMI](https://docs.lumi-supercomputer.eu/development/profiling/strategies/)
- When the computing bottlenecks are identified, try to figure out ways to improve the code
   - Again, [servicedesk@csc.fi](mailto:servicedesk@csc.fi) is a channel to ask for help
      - [The more concrete the problem is described, the better](https://docs.csc.fi/support/support-howto/)
   - If your issue concerns LUMI, contact the [LUMI User Support Team](https://lumi-supercomputer.eu/user-support/need-help/)

# Running your software

- It is not only how your software is constructed and compiled that affects performance
- It may also be run in different ways

# HPC parallel jobs

- A parallel job distributes the calculation over several cores in order to achieve a shorter wall-time (and/or a larger allocatable memory)
- Examples of batch job scripts for [Puhti](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/) and [Mahti](https://docs.csc.fi/computing/running/example-job-scripts-mahti/)
- Examples of batch job scripts for [LUMI-C](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumic-job/) and [LUMI-G](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/)
- **The best starting point:** [Software-specific batch scripts in Docs CSC](https://docs.csc.fi/apps/)

# Running in parallel

- Parallel programs are typically parallelized with the MPI and/or OpenMP standards
- Further parallelization possible if you can split your whole workflow into smaller independent tasks and run them simultaneously
   - [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) or [Slurm array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - More details about high-throughput computing and workflow automation in [Docs CSC](https://docs.csc.fi/computing/running/throughput/)
- Can your software utilize GPUs?
   - [GPUs in Puhti batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#gpus)
   - [GPUs in Mahti batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-mahti/#gpu-batch-jobs)
   - [GPUs in LUMI batch jobs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/)

# What is MPI?

- MPI (Message Passing Interface) is a widely used standard for writing software that runs in parallel
- MPI utilizes parallel **processes** that _do not share memory_
   - To exchange information, processes pass data messages back and forth between the cores
   - Communication can be a performance bottleneck
- MPI is required when running on multiple nodes

# What is OpenMP?

- OpenMP (Open Multi-Processing) is a standard that utilizes compute cores that share memory, i.e. **threads**
   - They do not need to send messages between each other
- OpenMP is easier for beginners, but problems quickly arise with so-called _race conditions_
   - This appears when different compute cores process and update the same data without proper synchronization
- OpenMP is restricted to a single node

# Self study materials for OpenMP and MPI

- There are many tutorials available online
   - Look with simple searches for _e.g._ "MPI tutorial"
- Check the documented exercise material and model answers from the CSC course "Introduction to Parallel Programming"
   - Available on [GitHub](https://github.com/csc-training/parallel-prog/)
   - See also the [materials of CSC Summer School in HPC](https://github.com/csc-training/summerschool)

# Task farming -- running multiple independent jobs simultaneously

- Task farming == running many similar independent jobs simultaneously
- If subtasks are few (<100), an easy solution is [array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - Individual tasks should run >30 minutes. Otherwise, you're generating too much overhead &rarr; consider another solution
   - Array jobs create _job steps_ and for 1000s of tasks Slurm database will get overloaded &rarr; consider another solution
- If running your jobs gets more complex, requiring _e.g._ dependencies between subtasks, workflow tools can be used
   - Guidelines and solutions are suggested in [Docs CSC](https://docs.csc.fi/computing/running/throughput/)
   - Many options: [FireWorks](https://docs.csc.fi/computing/running/fireworks/), [Nextflow](https://docs.csc.fi/support/tutorials/nextflow-puhti/), [Snakemake](https://snakemake.github.io/), [Knime](https://www.knime.com/), [BioBB](http://mmb.irbbarcelona.org/biobb/), ...

# Task farming 2.0

- Before opting for a workflow manager, check if the code you run has built-in high-throughput features
  - Many chemistry software ([CP2K](https://docs.csc.fi/apps/cp2k/#high-throughput-computing-with-cp2k), [GROMACS](https://docs.csc.fi/apps/gromacs/#high-throughput-computing-with-gromacs), [Amber](https://docs.csc.fi/apps/amber/#high-throughput-computing-with-amber), _etc._) provide methods for efficient task farming
  - Also [Python](https://docs.csc.fi/apps/python/#python-parallel-jobs) and [R](https://docs.csc.fi/support/tutorials/parallel-r/), if you write your own code
- Task farming can be combined with _e.g._ OpenMP to accelerate sub-jobs
  - [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) is the best option for sub-node task scheduling (non-MPI)
- Finally, MPI can be used to run several jobs in parallel
   - Three levels of parallelism, requires skill and time to set up
   - Always test before scaling up -- a small mistake can result in lots of wasted resources!

# Things to consider in task farming

- In a big allocation, each computing core should have work to do
   - If the separate tasks are different, some might finish before the others, leaving some cores idle &rarr; waste of resources
   - Try combining small and numerous jobs into fewer and bigger ones
- As always, try to estimate as accurately as possible the required memory and the time it takes for the separate tasks to finish
   - Consult _e.g._ this [bio job tutorial with examples](https://docs.csc.fi/support/tutorials/biojobs-on-puhti/)

# GPUs can speed up jobs

- GPUs, or Graphics Processing Units, are extremely powerful processors developed for graphics and gaming
- They can be used for science, but are often challenging to program
   - Not all algorithms can use the full power of GPUs
- Check the manual if the software can utilize GPUs, don't use GPUs if you're unsure
   - Consult [how to check if your batch job used GPU](https://docs.csc.fi/support/tutorials/gpu-ml/#gpu-utilization)
   - The [CSC usage policy](https://docs.csc.fi/computing/usage-policy/#gpu-nodes) limits GPU usage to where it is most efficient
   - Also, if you process lots of data, make sure you [use the disk efficiently](https://docs.csc.fi/support/tutorials/ml-data/#using-the-shared-file-system-efficiently)
- Does your code run on AMD GPUs? [LUMI](https://docs.lumi-supercomputer.eu/hardware/compute/lumig/) has a massive GPU capacity!

# Tricks of the trade 1/4

- Although it is reasonable to try to achieve best performance by using the fastest computers available, it is not the only important issue
- Different codes may give very different performance for a given use case
    - Compare the options you have in [CSC's software selection](https://docs.csc.fi/apps/)
- Before launching massive simulations, look for the most efficient algorithms to get the job done

# Tricks of the trade 2/4

- Well-known boosters are:
    - Enhanced sampling methods _vs._ brute force molecular dynamics
    - Machine learning methods
      - _E.g._ Bayesian optimization structure search ([BOSS](https://cest-group.gitlab.io/boss/), potential energy maps)
    - Start with coarser models and gradually increase precision (if needed)
      - _E.g._ pre-optimize molecular geometries using a small basis set
    - When starting a new project, begin with small/fast tests before scaling up
      - Don't submit large jobs before knowing that the setup works as intended
    - When using separate runs to scan a parameter space, start with a coarse scan, and improve resolution where needed
      - Be mindful of the number of jobs/job steps, use meta-schedulers if needed
    - Try to use or implement checkpoints/restarts in your software, and _check results between restarts_

# Tricks of the trade 3/4

- Try to formulate your scientific results when you have a minimum amount of computational results
    - Helps to clarify what you still need to compute, what computations would be redundant and what data you need to store
- Reserving more memory and/or more compute cores does not necessary equal faster computations
    - Check with `seff`, `sacct` and from software-specific log files if the memory was used and whether the job ran faster
    - Testing for optimal amount of cores and memory is advised before performing massive computations

# Tricks of the trade 4/4

- If possible, running the same job on a laptop may be useful for comparison
- Avoid unnecessary reads and writes of data and containerize Conda environments to improve I/O performance
    - Read and write in big chunks and avoid reading/writing lots of small files
       - If unavoidable, use [fast local NVMe disk](https://docs.csc.fi/computing/disk/#compute-nodes-with-local-ssd-nvme-disks), not Lustre (i.e. `/scratch`)
- Don't run too short jobs to minimize queuing and scheduling overhead
    - There's a time overhead in setting up a batch job, aim for >30 minute jobs
    - Don't run too many/short _job steps_ -- they will bloat Slurm accounting
- Don't run too long jobs without a restart option
    - Increased risk of something going wrong, resulting in lost time/results
