---
theme: csc-2019
lang: en
---

# Understanding resource usage {.title}

This lecture helps you to optimize your resource usage in CSC's HPC environment.

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
This lecture gives instructions on how to use computational resources efficiently.
:::

# Optimal usage in multiuser platforms

- The computing resources are shared among hundreds of your colleagues, who all have different resource needs.
- Resources allocated to your job are not available for others
   - Request only resources you need and make sure you are actually using those resources
- If you _can_ use more resources, should you?

:::info (speech)
Remember that there are many users doing their work on CSC supercomputers simultaneously?
To maximise the resource usage, all users should know how much resources to request.
The rule number one is: you should not reserve more resources than your job actually needs. 
That will also minimize the queueing time.

When it seems your jobs start to need more resources, please justify your larger requests.
In the end it is up to you to decide that: does it make sense to spend five hours work, to make the job run two hours faster? 
If you are going to repeat that job multiple times in the future, it really starts to pay off. 
This lecture aims to help you to optimise you resource requests.
:::

# One resource type will be a bottle neck

<div class="column">
- One node can host many jobs from different users
- Different jobs need different resources
- Typically the cores run out first, but there's memory left
- Sometimes one job uses only one core, but will take up all memory
   - No further jobs are possible
   - If the job is *not* using the memory, resources are wasted
</div>
<div class="column">
![](img/node-cpu-full.svg "Node cpu full"){width=45%}
![](img/node-mem-full.svg "Node memory full from one job"){width=45%}
</div>

:::info (speech)
The picture illustrates two opposite example cases of a job on a single node.
On the left there is a job, which uses all the CPUs on that node, but it lefts most of the memory free.
On the right there is a job, which uses only one core, but then reserves all of the memory.

An average job needs a few cores, and a fair amount of memory.
Usually one node is capable of hosting several jobs from different users.
At some point, the resources of a single node are all in use, and it can not host any additional jobs, before some resources are freed.
Typically a node runs out of cores first, which makes the remaining memory unavailable and wasted.
On the other hand: if one one-core job uses all the memory, then all the other cores on that node remain idle and therefore wasted.

These both are extreme examples.
If your job actually uses such resources, it is fine to reserve those.
Remember to avoid reserving resources for "just in case".
That is considered as actually wasting resources.
:::

# Slurm accounting: batch job resource usage 1/2

<div class="column">
- Resource usage can be queried with `seff SLURM_JOBID`
- Things to note:
   - low CPU Efficiency:
      - Too many cores selected?
      - Cores waiting for other processes?
      - Cores waiting for data from disk?
      - Cores spread on too many nodes? 
   - low Memory Efficiency:
      - Too much memory requested?
      - Lots of caveats here
   - low GPU efficiency:
      - Better use CPU instead? Disk I/O?
</div>
<div class="column">
![](img/seff-output.png "Seff output"){width=90%}
</div>

:::info (speech)
And now to the billion billing unit question: "how to find out how much resources my job actually used?"

Slurm accounting is a database, where every job makes an entry.
The data can be queried with the command called seff followed by the job ID. 
You can see the job ID, when you submit the job, or with command squeue --me.

This command seff prints out first where the job was run, by who, whether completed or failed, and how many node and cores were used. 
Then there are three different times included in the seff output.
CPU utilized tells the actual time the CPUs spent computing something.
CPU efficiency tells how much the CPUs were active of the total CPU walltime.
The job wall-clock time tells how long the computation took between the actual job start and job finish - note that it does not include the queueing time.
Notice that in this example the core-walltime is about four times larger than job wall time, because four cores were used. 
Moving forward, there is the utilised memory and the memory efficiency, which includes the total memory requested.
The rest is about the billing units consumed, which project was billed, and how the billing units were spent on different resources.
Here you can also see if the job used NVMe disk or GPU resources.

Now the important parts to note on this seff output.
You should optimise for a high CPU efficiency, and short enough wall time – especially if you're running on on multiple cores. 
If you try to use too many cores – to the limit where the the code would not scale anymore – the code would spend more time communicating information between different cores, and less time actually computing something. 
So in that case, the wall time might drop a little bit, but the efficiency would go down.
If file I/O is slowing the code down, that will show in lower CPU efficiency, and you should consider using NVMe disk.
Also it is good practice to specify the amount of nodes in the parallel job resource request, so that the job will not spread on too many nodes.
The data transfer between nodes is slower than within one node. 
If everyone fails to specify the amount of nodes, the SLURM system will spread parallel jobs across all nodes, and there will be unnecessarily few full nodes available.

The memory efficiency is a bit more tricky to evaluate.
The default memory request for one core is one gigabyte, which is quite small but often sufficient amount. 
It is recommended to have some buffer on top of the assumed memory amount.
In this example we have 2.5 gigabytes of memory buffer.
Depending the size of your job, the buffer could be for example from one to 10 gigabytes.
The nodes in Puhti have at least 192 GB memory.
Still it is good to keep the buffer well below 50 gigabytes – to avoid the situation where node memory is full, and the cores stay idle.

For GPU jobs low efficiency implies, that you should use CPUs instead, and make sure that the disk usage is not slowing you down. 
:::

# Slurm accounting: batch job resource usage 2/2

- Not all usage is captured by Slurm accounting
   - If CPU usage seems too low, look at the completion time
   - Some applications also print out timing data on log files
   - Sometimes jobs run outside `srun` don't record properly
- Job output can be tailored with `sacct`
   - `sacct -j SLURM_JOBID -o jobid,partition,state,elapsed,start,end`
   - `sacct -S 2021-08-01` would show all jobs started after that date
   - Note: these are heavy operations for Slurm. **Don't** query
     too long times, or loop these commands in scripts

:::info (speech)
Sometimes seff does not capture all the usage statistics.
You might find that the CPU or memory usage is suspiciously low, although the job performed well.
In that case you should compare the job wall time – or timing info – from your program log files. 
You can correlate the elapsed time with how many cores or memory you're using.

It's recommended to use srun to launch programs in batch scripts.
In some cases it is not feasible, but then the seff output can be missing something.

In addition to seff, there is something called Slurm Accounting or sacct. 
You can use sacct to find details on the jobs.
You can also look for the job IDs of all jobs.
Please note that these are a bit heavy operations on the Slurm database.
Do not query from the beginning of last year, and never put these commands in scripts that you loop over.
:::

# Billing units

- CPU time and storing files consume "[Billing units](https://docs.csc.fi/accounts/billing/)" (BU)
- BUs are a property of computing projects not users
- Monitor the BU usage with command `csc-projects` in the command line
   - For help/options, try `csc-projects -h`
- Batch job billing scheme:
   - Amount of resources allocated: All requested resources are billed ie. number of cores, amount of memory
   - Time allocated: Resources are billed based on the actual (wall) _time_ a job has **used**, not the reserved maximum time

:::info (speech)
Using resources like CPU and file storage consume billing units.
Billing is done per project, which means that the computing time, and the quotas are properties of a project. 
A user can belong to many projects, and choose which project will be billed.
All the users in a same project will use the same billing unit quota. 
Use the command CSC-projects to see your remaining billing units per project.

The billing scheme takes into account of the requested resources, and the time the resources are used.
The key here is to think how the reserved resources are unavailable to others.
If you reserve four cores and use only one, your project is billed for four cores, because no one else can use those during that time.
On the other hand if you reserve an hour of time, and the job runs only for 10 minutes, 
your project is billed for using resources for 10 minutes.
That means also, that if your job stops immediately because of an error, only a really small amount of billing units are spent.
:::

# Applying for Billing units

- Billing units can be also applied via [My Projects page in MyCSC](https://my.csc.fi/welcome)
   - Please acknowledge using CSC resources in your publications
   - Please also inform us about your work by adding your publications to the resource application!
- Academic usage is one of the [free-of-use cases](https://research.csc.fi/pricing)
- You can estimate [usage with the online billing calculator](https://research.csc.fi/billing-and-monitoring#buc) 
   - The calculator can also be used to estimate the value of the resources

:::info (speech)
If you run out of billing units, you can apply for more. 
Go to MyCSC web page, where you can monitor and apply for billing units.
There is a separate entry for each of the projects you are involved in. 
Please spread the knowledge about CSC, if you have used CSC resources for your research.
Remember also inform us about all those Nature papers and other publications, where you have acknowledged CSC.
A convenient way of doing that is to mention them in the resource application.
That helps us to inform our funders about the resource usage.
You can check the Docs CSC to see if your research is considered as a free–to–use cases.
For example usage for universities has been paid by the Ministry of Education and Culture.
The online billing unit calculator will help you to estimate how much billing units are needed for different types of jobs, and how much that would cost in Euros.
:::

# Billing units - also a currency to compare usage efficiency

- Different resources have different rates
   - 1 CPU core hour in Puhti equals 1 BU
   - 1 GPU card hour in Puhti equals 60 BU (+ allocated CPU cores)
   - 1 node hour in Mahti equals 100 BU
   - 1 GiB hour of Memory in Puhti equals 0.1 BU
   - 1st TiB of disk quota (scratch, projappl) is free
      - Used excess quota is billed by 5 BU/TiBh. (5 Billing Units per hour)
   - 1 used TiB hour in Allas equals 1 BU (i.e. 1 TiB of data equals 8760 BU in a year.)
   - [This and other service billing information in Docs](https://docs.csc.fi/accounts/billing/)

:::info (speech)
Billing units can also be considered as a kind of measure of efficiency.
For example a one hour 40-core CPU job is cheaper than one hour one GPU job.
Of course that does not tell which of them gets more computation done - that is to be determined case-by-case.

Here is a more detailed list of the cost of different resources in billing units. 
In Puhti one CPU core hour equals one billing unit.
Then one GPU card hour equals 60 billing units – plus all the CPUs, that you need to allocate with the job as well. 
However, in Mahti, the resources are allocated by nodes instead of cores.
Using one node for one hour in Mahti consumes 100 billing units. 
In Puhti you also neet to request some memory for your jobs.
One gibibyte hour of memory equals zero point one billing units. 
In Mahti you don't need to request memory, because you get all memory in the requested node anyway. 

Regarding disk space in Scratch or projAppl, the first terabyte of quota is free. 
But if you need more space, you can apply for more by sending e-mail to a service desk.
The billing for the extra space is done based on the usage.
Excessing the first terabyte costs 5 billing units per terabyte per hour.
It means you can use more space when you need some, but it is still a good idea to move your files elsewhere when you don't need them.
In Allas, the billing unit cost is based on how much data you actually have there.
One terabyte of data in Allas equals nine thousand billing units in a year.
That favours a workflow where you move your data from scratch to Allas, when you are not actively using it.
:::

Switch to # [Docs: Billing information](https://docs.csc.fi/accounts/billing/)

:::info (speech)
There is a link to docs.csc.fi, where billing scheme is explained in more detail.
There is a formula, that you can use to calculate the total billing unit consumption for a job.
The further links take you to the information about cloud resource billing, and quantum simulator billing. 
:::

# Before starting large-scale calculations

- Check how the software and your actual input performs
    - Common job errors are caused by typos in the script
- Use short runs in the queue `--partition=test` to check that the input works and that the resource requests are interpreted correctly
- Check the output from the `seff` command to ensure that the cpu and memory performances are sufficient 
    - It's OK if a job is (occasionally) killed due to too small resource requests: just adjust and rerun/restart.
   - It's _worse_ to run with way too big requests (often) without knowing it!

:::info (speech)
The first thing to do with any new batch job script is to test that it works.
You don't want to queue for days – just to see that your tiny typo made the job fail.
Shorter runs queue less, so create a short test run, and submit in the queue called "test".
That has usually really short queueing times, and you will quickly see how your job performs. 

Examining the test job with seff tells you if it actually used the requested resources.
You can use the information to refine resource requests for similar kinds of jobs. 
If you run only one calculation, it is not so important.
But that really pays off when you start to scale up your calculations.

If you request too little memory or too little time, the job will fail. 
This is normal and fine.
Usually the explanation is provided either by the queuing system, or somewhere in the log files. 
Then you can adjust the parameters, and preferably restart the job. 
Or you can run a new batch job with the same batch script.
If you run jobs with so large requests that your jobs never fail, it leads to most of the resources left unused and wasted.
Also your jobs will be queueing more.
:::

# Parallelising the workflow

- There are multiple ways of parallelizing your workflow
   - Maybe several smaller jobs are better than one big?
   - Is there a more efficient code or algorithm?
   - Is the file I/O slowing you down? (lots of file operations)
- Optimize usage considering single job wall time, overall used cpu time
- [Docs: Tools for high throughput computing](https://docs.csc.fi/computing/running/throughput/)

:::info (speech)
If you want to use parallel computation resources, you should consider the workflow.
For example, you could run multiple smaller simulations instead of one big simulation.
Or maybe use a completely different code or algorithm, if that is more efficient. 
Typically the easy–to–use codes written by non-specialists can do something well enough in a small scale. 
But when you move on to run in a large scale, you might need to switch to something more complicated, that has much better performance. 

Remember your job can be slow just because it is reading or writing a lot of files. 
Then the solution is not adding CPUs, but instead use the fast local storage available in some nodes.

When optimising and considering parallel resources, you should think about wall time and CPU time.
Wall time means how long it takes before the job is finished. 
CPU time is what consumes billing units, and it multiplies with the amound of CPUs you use.
Adding more CPUs may reduce the wall time, but at some point it becomes quite expensive in terms of billing units.
:::

# Reserving and optimizing batch job resources 

**Important resource requests that should be monitored with `seff` are:**

- [Memory requirement](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/)  
- [Disk workload](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage)
- [GPU efficiency](https://docs.csc.fi/computing/overview/#gpu-nodes)
- [Scaling of a job over several cores and nodes](https://docs.csc.fi/computing/running/performance-checklist/#perform-a-scaling-test)
   - Parallel job must always benefit from the requested parallel resources 
   - When you double the resources the job should run 1.5x faster

:::info (speech)
This summary slide also includes links to further documentation.
The most important things to monitor when you start doing some heavy computing are:
whether the job is using all of the memory,
whether the job is using disk efficiently,
whether it makes sense to use GPUs,
and whether adding more resources speeds up stuff.

With memory, it is recommended to always have some reserve – as instructed in the slides about Slurm accounting.
Avoiding excessive disk workload means: not to burden the Lustre parallel file system, but to use fast local storage if necessary. 

If your application can use GPUs, check that it also gains a real performance improvement compared to using CPUs.
The documentation includes a quite detailed GPU usage policy. 
The GPUs should be used on those applications where it speeds up running the jobs the most. 
In some cases - typically machine learning - the speedup can be even 6-fold compared to CPUs. 
If the speedup is barely at the minimum level allowed by the usage policy, you may lose the gain if you need to queue for the resources.

For parallel jobs it is important to check that adding more resources makes the job run faster.  
Otherwise it does not make sense to run in parallel. 
The kind of rule of thumb is: when you double the resources - for example from four cores to eight cores - the job should run at least one and a half times faster. 
The documentation covers instructions on how to perform a scaling test.
The idea is that you run a job first with two cores, then four and eight cores, and monitor the performance. 
If the running time goes down - or the performance increases - then it is okay to add more resources. 
:::

# `seff` examples

<div class="column">
![](img/gpu-seff.png "seff output of a GPU job"){width=90%}
</div>
<div class="column">
<small>
Left: GPU usage ok! (for _this_ others ok, too)

Bottom: CPU usage way too low, memory usage too high, job killed.
</small>
![](img/seff-oom.png "seff output when memory runs out"){width=90%}
</div>

:::info (speech)
Here are two illustrative examples of seff results. 
The first example job has run for only two minutes until finished, which is fairly short. 
The CPU efficiency is really low. 
Either the system is not logging CPU usage correctly, or there is something wrong with this job. 
Memory efficiency is five percent out of five GB, which is also very low. 
On the other hand, this is a GPU job – and the GPUs are used with 83% efficiency. 
So this job has been making really good use of the expensive resources. 
Apparently this application does not need the CPU, but keeps the GPU busy. 
There is four GPUs per one GPU node.
In this example the memory usage is well below one fourth of the available memory, which leaves sufficient memory for other GPUs.
Although 5% memory efficiency is low, the remaining "buffer size" is only about 4 GB in this case.
So overall, the two small efficiencies here are fine, because of the well utilised expensive GPU resource.
Also the amount of not utilised CPU and memory resources is small.

The second example is a job that has actually failed.
The CPU efficiency is even smaller than with the previous example.
But, it has a problem in the memory efficiency.
It has used more than 100% of available memory. 
That is probably the reason why the job has failed. 
In this case the job error file might have a clear error message – telling that the job was using too much memory, and it was killed by the queueing system. 
That is not alarming as such.
Tou might have been testing the optimal amount of resources and this happens.
However, the CPU efficiency here is also very small. 
It would be best to check that this job is actually doing what it is supposed to do. 

The tutorials about resource usage continue from here. 
They cover the basic use cases with easy–to–follow examples.
The documentation has more information about available resources – including technical details and example batch scripts.
:::
