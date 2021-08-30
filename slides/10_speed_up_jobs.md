---
theme: csc-2019
lang: en
---

# Not fast enough? How HPC can help. {.title}

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

# The purpose of large computers

- Typically large computers, like those at CSC, are not faster than others - they are just bigger.
   - For fast computation they utilize parallelism (and typically have special disk and memory solutions, too)
- Parallelism simplified:
   - You use hundreds of ordinary computers simultaneously to solve a single problem.

# First steps for fast jobs (1/2)
- Spend a little time to investigate:
   - Which of all the available software would be the best solve the kind of problem you have? 
      - Ask experienced colleagues and [servicedesk@csc.fi](mailto:servicedesk@csc.fi) for guidance.
- Consider:
   - The software that is the fastest to solve your problem might not always be the best. 
      - Issues like ease-of-use and compute-power/memory demands are also highly relevant. 
   - Quite often it is useful to start simple and gradually use more complex approaches if needed.

# First steps for fast jobs (2/2)
- When you have found the software you want to use, check if it is available at CSC as a ready installed optimal version [docs.csc.fi/apps](https://docs.csc.fi/apps/)
   - Spend some time getting familiar with the software users manual, if available.
- If you can't find a suitable software, consider writing your own code.

# Optimize the performance of your own code (1/2)
- If you have constructed your own code, compile it with optimizing compiler options. 
   - Docs: [Compiling in Puhti](https://docs.csc.fi/computing/compiling-puhti/), [Compiling in Mahti](https://docs.csc.fi/computing/compiling-mahti/)
- Construct a small and quick test case and run it in the test queue 
   - Docs: [Queue options](https://docs.csc.fi/computing/running/batch-job-partitions/). 
   - Use the test case to optimize computations before starting massive ones.

# Optimize the performance of your own code (2/2)
- Use profiling tools to find out how much time is spent in different parts of the code 
   - Docs: [Performance tools](https://docs.csc.fi/computing/performance/)
- When the computing bottle-necks are identified try to figure out ways to improve the code. 
   - Again, [servicedesk@csc.fi](mailto:servicedesk@csc.fi) is a channel to ask for help. The more concrete the problem is described, the better.


# Running your software
- It is not only how your software is constructed and compiled that affect performance.
- It can also be run in different ways

# HPC parallel jobs

- A parallel job distributes the calculation over several cores in order to achieve a shorter wall time (and/or a larger allocatable memory)   
- [Examples of batch job scripts on Puhti](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/)
- [Examples of batch job scripts on Mahti](https://docs.csc.fi/computing/running/example-job-scripts-mahti/)
- **The best starting point:** [Software specific batch scripts in docs](https://docs.csc.fi/apps/)

# Running in parallel 
- A code is typically parallelized with MPI and/or OpenMP standards. They can be run in several different ways.  
   - Can you split your work into smaller, fully independent, bits and run them simultaneously? 
      - Check out [array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - Can you automate setting up, running and analysing your array jobs? 
      - Then you may want to use [workflows](https://docs.csc.fi/computing/running/throughput/)
   - Can your software utilize GPUs? 
      - [GPUs in batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-mahti/#gpu-batch-jobs)

# What is MPI? 
- MPI (and OpenMP too!) are widely used standards for writing software that run in parallel.
- MPI (Message Passing Interface) is a standard that utilizes compute cores that do not share their memory
   - It passes data-messages back and forth between the cores.

# What is OpenMP? 
- OpenMP (Open Multi-Processing) is a standard that utilize compute cores that share memory
   - They do not need to send messages betwen each other. 
- Basically OpenMP is easier for beginners, but problems quickly arise with so called 'race conditions'. 
   - This appears when different compute cores process and update the same data without proper synchronization.

# Self study materials for OpenMP and MPI
- There are many tutorials available on the internet.
   - Look with simple searches for _e.g._ 'MPI tutorial'. 
- Check the documented exercise material and model answers from the CSC course "Introduction to Parallel Programming"
   - Available on GitHub [Parallel programming](https://github.com/csc-training/parallel-prog/). 

# Task farming - running multiple independent jobs simultaneously

- Task farming means that you have a set of, more or less, similar jobs that can be run fully independently of each other.
- Such jobs are most easily run as so called [array-jobs](https://docs.csc.fi/computing/running/array-jobs/).
   - Individual tasks should take at least 30 minutes or more - otherwise you're generating too much overhead
   - In this case, there is likely a more efficient solution
- If running your jobs become slightly more complex, with _e.g._ some minor dependencies, workflows can be used. 
   - Some potential solutions are listed on CSCs [High throughput page](https://docs.csc.fi/computing/running/throughput/)
   - There are naturally lots of choice: [FireWorks](https://materialsproject.github.io/fireworks/), [Snakemake](https://snakemake.github.io/), [Knime](https://www.knime.com/), [BioBB](http://mmb.irbbarcelona.org/biobb/), ...

# Task farming 2.0

- Task farming can be combined with _e.g._ OpenMP to speed up the subjobs,
- And on top of those with MPI to run several jobs in parallel.
   - In this setup you'd have three layers or parallelization array-MPI-OpenMP
   - Setting this up will take skill and time
   - Always test your setup - a typo can result in a lot of lost resources

# Things to consider in task farming

- In a big allocation each computing core should have work to do
   - If the separate jobs are very different, some will end before the others, and some cores will idle - wasting resources
   - A fix would be to use _e.g._ loops, to lump really small and numerous jobs into fewer and bigger ones.
- As always, try to estimate as exact as possible the amount of memory and the time it takes the separate runs to finish.
   - Consult e.g. this [biojob tutorial with examples](https://docs.csc.fi/support/tutorials/biojobs-on-puhti/)

# GPUs can speed up jobs

- GPUs, or Graphics Processing Units, are extremely powerful processors developed for graphics and gaming.
- They can be used for science, but are often really tricky to program.
   - Only a small set of algorithms can use the full power of GPUs.
- Check the manual if the software can utilize GPUs.
   - If you process lots of data, make sure you [use disk efficiently](https://docs.csc.fi/support/tutorials/gpu-ml/#gpu-utilization)
- Do not try to use GPUs, unless you know what you are doing.
   - If you're unsure, consult [how to check if your batch job used GPU](https://docs.csc.fi/support/tutorials/gpu-ml/#gpu-utilization)
   - The [CSC Usage policy](https://docs.csc.fi/computing/overview/#gpu-nodes) limits GPU usage to where it is most efficient
      - In Puhti, one GPU should be more than 2x as fast as a full node of CPUs
      - Performance depends on code and use case, so you need to test this.

# Tricks of the trade 1/4

- It is reasonable to try to achieve best performance by using the fastest computers available. This is however far from the only important issue.
- Different codes may give very different performance. 
    - Compare the options you have in [the CSC Software selection](https://docs.csc.fi/apps/)
- Before launching massive simulations, look for the most efficient algorithms to get the job done.
    - (examples on the next slide)

# Tricks of the trade 2/4

- Well known boosters are:
    - Enchanced sampling methods in molecular dynamics (vs. brute force plain MD)
    - Bayesian Optimization Structure Search ([BOSS](https://pypi.org/project/aalto-boss/), potential energy mapping)
    - When starting a new project, begin with small and fast test cases, and scale up gradually.
    - When using separate runs to scan a parameter space, start with a coarse scan, and improve resolution where needed.
    - Be careful in submitting large numbers of jobs before you know the results are really what you are looking for.
    - Try to use or implement so called 'restart options' in your software, and _always check results in between restarts_.


# Tricks of the trade 3/4

- Try to first formulate your scientific results when you have a minimum amount of computational results
    - it often helps to clarify what you still need to compute and what computations would be redundant.
    - and what results you need to store
- Reserving more memory resources and more compute cores does not necessary mean faster comutations.
    - Check with `seff`, `sacct` and from the logs if the memory was used, and if the job ran faster
- Testing for optimal setup regarding compute cores and memory is good practice before performing massive computations.

# Tricks of the trade 4/4

- Running the same job on a laptop may be useful for comparison.
- Avoid unnecessary reads and writes of data.
    - If you do, read and write in big chunks. Avoid writes/reads of huge numbers of small files. If this is necessary, use [NVMe in Puhti](https://docs.csc.fi/computing/disk/#compute-nodes-in-puhti), not Lustre.
- Don't run too short jobs.
    - There's a time-overhead in setting up a batch job. Aim for at least 30 minute jobs.
    - Also, don't run too short _job steps_. They will clutter Slurm accounting.
- Don't run too long jobs.
    - The possibility of something going wrong gets bigger with risk of losing time and results. Restart option saves.
