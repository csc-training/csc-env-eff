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
All materials (C) 2020-2023 by CSC - IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# The purpose of large computers

- Typically large computers, like those at CSC, are not that much faster than others -- they are just bigger
   - For fast computation they utilize parallelism (and typically have special disk, memory and network solutions, too)
- Parallelism simplified:
   - You use hundreds of ordinary computers simultaneously to solve a single problem

# First steps for fast jobs (1/2)

- Spend a little time to investigate:
   - Which of the available software would be the best to solve the kind of problem you have?
      - Ask experienced colleagues or [servicedesk@csc.fi](mailto:servicedesk@csc.fi) for guidance
- Consider:
   - The software that solves your problem fastest might not always be the best
      - Issues like ease-of-use and compute-power/memory/disk demands are also highly relevant
   - Quite often it is useful to start simple and gradually use more complex approaches if needed

# First steps for fast jobs (2/2)

- When you've found the software you want to use, check if it is available at CSC as a [pre-installed optimized version](https://docs.csc.fi/apps/)
   - Spend some time getting familiar with the software user manual, if available
- If you need to install a software package yourself and it happens to be distributed through Conda, [you need to containerize it](https://docs.csc.fi/computing/usage-policy/#conda-installations)
   - Conda environments installed directly on the parallel file system are highly inefficient due to the large number of files they contain
   - Containerizing greatly speeds up performance at start up and can be done easily with the [Tykky wrapper](https://docs.csc.fi/computing/containers/tykky/)
- If you can't find a suitable software, consider writing your own code

# Optimize the performance of your own code (1/2)

- If you have written your own code, compile it with optimizing compiler options
   - Docs CSC: [Compiling in Puhti](https://docs.csc.fi/computing/compiling-puhti/), [Compiling in Mahti](https://docs.csc.fi/computing/compiling-mahti/)
- Construct a small and quick test case and run it in the test queue
   - Docs CSC: [Queue options](https://docs.csc.fi/computing/running/batch-job-partitions/)
   - Use the test case to optimize computations before starting massive ones

# Optimize the performance of your own code (2/2)

- Use profiling tools to find out how much time is spent in different parts of the code
   - Docs CSC: [Performance analysis](https://docs.csc.fi/computing/performance/)
- When the computing bottlenecks are identified, try to figure out ways to improve the code
   - Again, [servicedesk@csc.fi](mailto:servicedesk@csc.fi) is a channel to ask for help
      - [The more concrete the problem is described, the better](https://docs.csc.fi/support/support-howto/)

# Running your software

- It is not only how your software is constructed and compiled that affects performance
- It can also be run in different ways

# HPC parallel jobs

- A parallel job distributes the calculation over several cores in order to achieve a shorter wall-time (and/or a larger allocatable memory)
- [Examples of batch job scripts on Puhti](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/)
- [Examples of batch job scripts on Mahti](https://docs.csc.fi/computing/running/example-job-scripts-mahti/)
- **The best starting point:** [Software-specific batch scripts in Docs CSC](https://docs.csc.fi/apps/)

# Running in parallel

- Parallel programs are typically parallelized with MPI and/or OpenMP standards, which can be run in several different ways
   - Can you split your work into smaller, fully independent, bits and run them simultaneously?
      - Check out [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) or [Slurm array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - Can you automate setting up, running and analyzing your array jobs?
      - Then you may want to use [high-throughput workflows](https://docs.csc.fi/computing/running/throughput/)
   - Can your software utilize GPUs?
      - [GPUs in Puhti batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#gpus)
      - [GPUs in Mahti batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-mahti/#gpu-batch-jobs)

# What is MPI?

- MPI (and OpenMP too) are widely used standards for writing software that run in parallel.
- MPI (Message Passing Interface) is a standard that utilizes parallel _processes_ that do not share memory
   - To exchange information, processes pass data messages back and forth between the cores
- MPI is required when running on multiple nodes

# What is OpenMP?

- OpenMP (Open Multi-Processing) is a standard that utilizes compute cores that share memory, also known as _threads_
   - They do not need to send messages between each other
- OpenMP is easier for beginners, but problems quickly arise with so-called _race conditions_
   - This appears when different compute cores process and update the same data without proper synchronization
- OpenMP is restricted to a single node

# Self study materials for OpenMP and MPI

- There are many tutorials available on the internet
   - Look with simple searches for _e.g._ "MPI tutorial"
- Check the documented exercise material and model answers from the CSC course "Introduction to Parallel Programming"
   - Available on [GitHub](https://github.com/csc-training/parallel-prog/)
   - See also the [materials of CSC Summer School in HPC](https://github.com/csc-training/summerschool)

# Task farming -- running multiple independent jobs simultaneously

- Task farming == running many similar independent jobs simultaneously
- If jobs are serial or few in number (~100), an easy solution is [array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - Individual tasks should last at least 30 minutes or more. If not, you're generating too much overhead &rarr; consider another solution
   - Array jobs with parallel tasks create _job steps_. If there are thousands of tasks Slurm will get overloaded &rarr; consider another solution
- If running your jobs gets more complex, requiring _e.g._ dependencies between subtasks, workflow tools can be used
   - Guidelines and solutions are suggested on CSC's [high-throughput page](https://docs.csc.fi/computing/running/throughput/)
   - Many options: [FireWorks](https://docs.csc.fi/computing/running/fireworks/), [Nextflow](https://docs.csc.fi/support/tutorials/nextflow-puhti/), [Snakemake](https://snakemake.github.io/), [Knime](https://www.knime.com/), [BioBB](http://mmb.irbbarcelona.org/biobb/), ...

# Task farming 2.0

- Before opting for an external workflow manager, check if the code you run has built-in high-throughput capabilities
  - Many chemistry software ([CP2K](https://docs.csc.fi/apps/cp2k/#high-throughput-computing-with-cp2k), [GROMACS](https://docs.csc.fi/apps/gromacs/#high-throughput-computing-with-gromacs), [LAMMPS](https://docs.csc.fi/apps/lammps/#high-throughput-computing-with-lammps)) provide methods for efficient task farming
  - Also [Python](https://docs.csc.fi/apps/python/#python-parallel-jobs) and [R](https://docs.csc.fi/support/tutorials/parallel-r/), if you write your own code
- Task farming can be combined with _e.g._ OpenMP to accelerate sub-jobs
  - [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) is the best option for sub-node task scheduling (non-MPI)
- Finally, MPI can be used to run several jobs in parallel
   - With array jobs you'd have three levels of parallelism: array--MPI--OpenMP
   - Setting this up will take skill and time. Always test your setup before scaling -- a typo can result in a lot of lost resources!

# Things to consider in task farming

- In a big allocation each computing core should have work to do
   - If the separate tasks are very different, some will end before the others, leaving some cores idle &rarr; waste of resources
   - A fix would be to use _e.g._ loops to lump really small and numerous jobs into fewer and bigger ones.
- As always, try to estimate as exactly as possible the required memory and the time it takes for the separate tasks to finish.
   - Consult _e.g._ this [biojob tutorial with examples](https://docs.csc.fi/support/tutorials/biojobs-on-puhti/)

# GPUs can speed up jobs

- GPUs, or Graphics Processing Units, are extremely powerful processors developed for graphics and gaming
- They can be used for science, but are often really tricky to program
   - Only a small set of algorithms can use the full power of GPUs
- Check the manual if the software can utilize GPUs
   - If you process lots of data, make sure you [use disk efficiently](https://docs.csc.fi/support/tutorials/ml-data/#using-the-shared-file-system-efficiently)
- Do not try to use GPUs, unless you know what you are doing
   - If you're unsure, consult [how to check if your batch job used GPU](https://docs.csc.fi/support/tutorials/gpu-ml/#gpu-utilization)
   - The [CSC usage policy](https://docs.csc.fi/computing/usage-policy/#gpu-nodes) limits GPU usage to where it is most efficient
- If your code can run on AMD GPUs, [LUMI-G](https://docs.lumi-supercomputer.eu/hardware/compute/lumig/) is a great opportunity!

# Tricks of the trade 1/4

- Although it is reasonable to try to achieve best performance by using the fastest computers available, it is far from the only important issue
- Different codes may give very different performance for a given use case
    - Compare the options you have in [CSC's software selection](https://docs.csc.fi/apps/)
- Before launching massive simulations, look for the most efficient algorithms to get the job done
    - (examples on the next slide)

# Tricks of the trade 2/4

- Well-known boosters are:
    - Enchanced sampling methods in molecular dynamics (_vs._ plain brute force MD)
    - Bayesian Optimization Structure Search ([BOSS](https://pypi.org/project/aalto-boss/), potential energy mapping)
    - When starting a new project, begin with small/fast tests before scaling up
      - Don't submit large jobs before you know the results are really what you are looking for
    - When using separate runs to scan a parameter space, start with a coarse scan, and improve resolution where needed
      - Be mindful of the number of jobs/job steps and pack your jobs into bigger ones through smart task farming
    - Try to use or implement checkpoints/restarts in your software, and _always check results in between restarts_

# Tricks of the trade 3/4

- Try to formulate your scientific results when you have a minimum amount of computational results
    - Helps to clarify what you still need to compute, what computations would be redundant and what data you need to store
- Reserving more memory and/or more compute cores does not necessary equal faster computations
    - Check with `seff`, `sacct` and from software-specific log files if the memory was used and whether the job ran faster
- Testing for optimal setup regarding compute cores and memory is good practice before performing massive computations

# Tricks of the trade 4/4

- If possible, running the same job on a laptop may be useful for comparison
- Avoid unnecessary reads and writes of data and containerize Conda environments to improve IO-performance
    - Read and write in big chunks and avoid reading/writing lots of small files
       - If unavoidable, use [fast local NVMe disk](https://docs.csc.fi/computing/disk/#compute-nodes-with-local-ssd-nvme-disks), not Lustre (_i.e._ `/scratch`)
- Don't run too short jobs to minimize queuing and scheduling overhead
    - There's a time overhead in setting up a batch job, aim for >30 minute jobs
    - Don't run too many/short _job steps_ -- they will bloat Slurm accounting
- Don't run too long jobs without restart option
    - Increased risk of something going wrong, resulting in lost time/results
