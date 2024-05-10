---
layout: default
title: Understanding resource usage with sacct and seff
parent: 6. Batch job resource usage
grand_parent: Part 1
nav_order: 1
has_children: false
has_toc: false
permalink: /hands-on/batch_resources/tutorial_sacct_and_seff.html
---

# Using `sacct` and `seff` to understand resource usage of finished jobs

💬 In this tutorial we look at the `seff` and `sacct` commands. The tutorial should be done on Puhti.

💭 `seff` shows detailed data on used resources in an easy-to-read format, but can only show one job at a time.

💭 `sacct` is useful when you want to look at a listing of jobs, but by default it only shows minimal data.

## Get details about batch jobs

1. Try `sacct` which by default shows the jobs you have run on the current date (_i.e._ since last midnight):

```bash
sacct
```

{:style="counter-reset:step-counter 1"}
2. Try specifying the start time of the listing using the `-S` option. Don't query too long time intervals, since this causes significant load on the system (max. queryable interval is three months).

```bash
sacct -S YYYY-MM-DD    # replace YYYY-MM-DD
```

{:style="counter-reset:step-counter 2"}
3. Look for a specific job – _i.e._ specify the job ID using the `-j` option (if you can't think of one, you can use `21320280`):

```bash
sacct -j <slurmjobid>    # replace <slurmjobid> with a valid job ID 
```

{:style="counter-reset:step-counter 3"}
4. To print out all the available data for a job, try:

```bash
sacct -l -j <slurmjobid>    # replace <slurmjobid> with a valid job ID
```

{:style="counter-reset:step-counter 4"}
5. Select only the interesting data using the `-o` option. For example, to see job name, job ID, used memory, job state and elapsed wall-clock time, try:

```bash
sacct -o jobname,jobid,maxrss,state,elapsed -j <slurmjobid>   # replace <slurmjobid> with a valid job ID
```

{:style="counter-reset:step-counter 5"}
6. Check out the list of all available data fields with:

```bash
sacct -e
```

‼️ Note, running `sacct` is heavy on the batch queue system.

- You should not, for example, write scripts that run it repeatedly.

## Running a test job

💬 Run a simple array job to practice using `seff` and `sacct`.

☝🏻 If you have limited time, you can skip to [Examining the finished job](#examining-the-finished-job) and use the job ID `20363893` (it is the same job).

1. Create a file named `array.sh` and paste the following contents in it.

```bash
#!/bin/bash
#SBATCH --account=<project>      # Choose the billing project. Has to be defined!
#SBATCH --time=00:01:00          # Maximum duration of the job. Max: depends of the partition. 
#SBATCH --partition=small        # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --job-name=array_job     # Name of the job visible in the queue.
#SBATCH --output=out_%A_%a.txt   # Name of the output-file.
#SBATCH --error=err_%A_%a.txt    # Name of the error-file.
#SBATCH --ntasks=1               # Number of tasks. Max: depends on partition.
#SBATCH --cpus-per-task=1        # How many processors work on one task. Max: Number of CPUs per node.
#SBATCH --mem=1000               # How much RAM is reserved for job per node. Unit: MiB
#SBATCH --array=1-6              # The indices of the array jobs.

/appl/soft/bio/course/sacct_exercise/test-a ${SLURM_ARRAY_TASK_ID}
```

{:style="counter-reset:step-counter 1"}
2. Replace `<project>` with your actual project name, e.g. `project_2001234`
3. Submit the job with the command:

```bash
sbatch array.sh
```

{:style="counter-reset:step-counter 3"}
4. You will see a message like:

```bash
Submitted batch job 123456
```

{:style="counter-reset:step-counter 4"}
5. Make note of the Slurm job ID.
6. Follow the progress of the job with the command:

```bash
squeue -u $USER
```

💭 How is an array job listed in the queue?

## Examining the finished job

1. When the job has finished (you can no longer see any of the sub jobs with `squeue`), you can use `sacct` to study it:

```bash
sacct -j <slurmjobid>    # replace <slurmjobid> with the actual job ID
```

{:style="counter-reset:step-counter 1"}
2. Get a cleaner view by omitting the job steps:

```bash
sacct -X -j <slurmjobid>    # replace <slurmjobid> with the actual job ID
```

💬 `sacct` is especially handy here, because it is easy to spot the failed sub jobs.

- Which sub jobs failed?
    - Can you figure out why they failed?
    - How do they compare to jobs that finished?

{:style="counter-reset:step-counter 2"}
3. Use `seff` to look at individual sub jobs, e.g.:

```bash
seff <slurmjobid>_5    # replace <slurmjobid> with the actual job ID
```

{:style="counter-reset:step-counter 3"}
4. Try `sacct` with the `-o` option (discussed above). This time add the fields `reqmem` (requested memory) and `timelimit` (requested time):

```bash
sacct -o jobname,jobid,reqmem,maxrss,timelimit,elapsed,state -j <slurmjobid>    # replace <slurmjobid> with the actual job ID
```

💭 Note that in this case we can not use the `-X` option as we want to see the memory usage for each step.

## Adjusting the job-file

1. Look at the error messages produced by the failed jobs.
2. When you know which sub jobs failed and why, adjust the resource requests as necessary.

☝🏻 If you have limited time, you can skip to step 4 and use the job ID `20363922` (it is the same job with adjusted resource requests).

- Change time and memory reservations:

```bash
#SBATCH --time=00:05:00
#SBATCH --mem=2000
```

{:style="counter-reset:step-counter 2"}
3. Re-run the failed sub jobs:

```bash
#SBATCH --array=3,5    # Specify which ones to run
```

{:style="counter-reset:step-counter 3"}
4. Use `seff` and `sacct` to look at the jobs. How much memory and time did they use?

## More information

💡 You can read more about [array jobs](https://docs.csc.fi/computing/running/array-jobs) and [seff and sacct](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/) in Docs CSC.
