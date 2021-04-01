---
theme: csc-2019
lang: en
---

# Getting most out of CSC computers {.title}

# The purpose of large computers

Typically, large computers, like those at CSC, are not faster than others - they are just bigger. That is, for fast computation they utilize parallelism.
Parallelism means that you may use, simply speaking, hundreds or thousands of ordainary computers simultaneously for the solution of a single problem.

# Basic considerations
- Spend a little time to investigate which of all available software would be the best solve the kind of problem you have. Experienced colleagues and servicedesk@csc.fi are good places to ask for guidance.
- The software that has the capacity to solve your problem the fastest may, however, not always be the best. Issues like ease-of-use and compute-power/memory demands are also higly relevant. Quite often it is useful to start simple and gradually use more complex approaches if needed.
- When you have found the software you want to use, check if it is available at CSC as a ready installed optimal version https://docs.csc.fi/apps/, and spend some time getting familiar with the softwares users manual, if available.
- If you cant find a suitable software, consider writing your own code.

# Optimize the performance of your own code
- If you have constructed your own code, compile it with optimizing compiler options. [Compiling Puhti](https://docs.csc.fi/computing/compiling-puhti/), [Compiling Mahti](https://docs.csc.fi/computing/compiling-mahti/)
- Construct a small and quick test case and run it in the test queue [Queue options](https://docs.csc.fi/computing/running/batch-job-partitions/). Use the test case to optimize computations before starting massive ones.
- Use profiling tools to find out how much time is spent in different parts of the code [Performance tools](https://docs.csc.fi/computing/performance/)
- When the compute bottle-necks are identified try to figure out ways to improve the code. Again, servicedesk@csc.fi is a channel to ask for help. The more concrete the problem is descried, the better.

# Running your software
- It is not only how your software is constructed and compiled that affect performance.
- It can also be run in different ways

# Running in parallel 
- A code is typically parallelized with MPI and/or OpenMP standards. They can be run in several different ways.  
- Can you split your work into smaller, fully independent, bits and run them simultaneously? [array jobs](https://docs.csc.fi/computing/running/array-jobs/)
- Can you automate setting up, running and analysing your array jobs? The you may want to use [workflows](https://docs.csc.fi/support/tutorials/many/)
- Can your software utilize GPUs? 

# What is OpenMP and what is MPI? 
- MPI and OpenMP and widely used standards for writing software that run in parallel.
- MPI or (Message Passing Interface) is a standard the utilize compute cores that do not share their memory, and therefore passes data-messages back and forth between them.
- OpenMP or Open Multi-Processing is a standard that utilize compute cores that share memory, and therefore do not need to send messages betwwen each other. Basically OpenMP is easier for beginners, but problems quickly arise with so called 'race conditions'. This appears when different compute cores process and update the sama data without proper synchronization.

# Self study materials for OpenMP and what is MPI
- There are many tutorials available on the internet.
   - Look with simple searches for e.g. 'MPI tutorial'. 
- Check the documented exercise material and model answers from the CSC course "Introduction to Parallel Programming"
   - Available on GitHub [Parallel programming](https://github.com/csc-training/parallel-prog/). 

# Task farming - running multiple independent jobs simultaneously

- Task farming means that you have a set of, more or less, similar jobs that can be run fully independently of each other.
- Such jobs are most easily run as so called array-jobs. [array jobs](https://docs.csc.fi/computing/running/array-jobs/)
   - Individual tasks should take at least 30 minutes or more - otherwise you're generating too much overhead
   - In this case, there might be a more efficient solution
- If running your jobs become slightly more complex, with e.g. some minor dependencies, workflows can be used. 
   - Here's a [tutorial using gnu parallel](https://docs.csc.fi/support/tutorials/many/) 
   - This is suited for very short individual jobs

# Task farming 2.0

- Task farming can be combined with _e.g._ OpenMP to speed up the subjobs,
- And on top of those with MPI to run several jobs in parallel.
   - In this setup you'd have three layers or parallelization array-MPI-OpenMP
   - Setting this up will take skill and time

# Things to consider in task farming

- In a big allocation each computing core should have work to do
   - If the separate jobs are very different, some will end before the others, and some cores will idle - wasting resources
   - A fix would be to use e.g. loops, to lump really small and numerous jobs into fewer and bigger ones.
- As always, try to estimate as exact as possible the amount of memory and the time it takes the separate runs to finish.
   - Consult e.g. this [biojob tutorial with examples](https://docs.csc.fi/support/tutorials/biojobs-on-puhti/)

# GPUs can speed up jobs

- GPUs, or Graphics Processing Units, are extremely powerful processors developed for graphics and gaming.
- They can be used for science, but are often really tricky to program.
   - Only a small set of algorithms can use the full power of GPUs.
- For any ready made software, check the manual if the software can utilize GPUs.
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
