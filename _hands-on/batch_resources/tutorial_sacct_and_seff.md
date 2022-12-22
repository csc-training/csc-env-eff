---
topic: batch resources
title: Tutorial - sacct and seff, resources used  (essential)
---
# Using sacct and seff to look at finished jobs

💬 In this tutorial we look at commands `seff` and `sacct`.

💭 `Seff` shows detailed data on used resources in an easy-to-read format, but can only show one job at a time.

💭 `Sacct` is useful when you want to look at a listing of jobs, but by default it only shows minimal data.

## Get details about batch jobs

1. Try `sacct` which by default shows the jobs you have run on current date (_i.e._ since last midnight):

```bash
sacct
```

2. Try specify the start time of listing with the `-S` option:

```bash
sacct -S YYYY-MM-DD    # replace YYYY-MM-DD
```

3. Look for a spesific job – ie. specify the job ID with the `-j` option:

```bash
sacct -j slurmjobid      # replace slurmjobid with a job ID
```

4. Check out all the available data for a job, try:

```bash
sacct -l -j slurmjobid   # replace slurmjobid with a job ID
```

5. Select only the interesting data with the `-o` option, for example to see job name, job ID, used memory, job finish state and elapsed wall clock time try:

```bash
sacct -o jobname,jobid,maxrss,state,elapsed -j slurmjobid    # replace slurmjobid
```

6. Check out the list of all available data fields with:

```bash
sacct -e
```

‼️ NOTE: running `sacct` is heavy on the batch job system
- You should not, for example, write scripts that run it repeatedly.

## Running a test job

💬 Run a simple array job to practice using `seff` and `sacct`.

1. Create file `array.sh` and paste the following contents in to it.

```bash
#!/bin/bash
#SBATCH --account=project_xxxx    # Choose the billing project. Has to be defined!
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

{:start="2"}
2. Replace `project_xxxx` with your actual project name.

3. Submit the job with command:

```bash
sbatch array.sh
```

4. You will see a message like:

```bash
Submitted batch job 123456
```

5. Make note of the actual job id.

6. Follow the progress of the job with command:

```bash
squeue -u $USER
```

💭 How is an array job listed in the queue?

## Examining the finished job

1. When the job has finished (you can no longer see any of the sub jobs with `squeue`), you can use `sacct` to look at it:

```bash
sacct -j slurmjobid           # replace slurmjobid with job ID
```

2. Get cleaner view by omitting the job steps:

```bash
sacct -X -j slurmjobid        # replace slurmjobid with job ID
```

💬 `Sacct` is especially handy here, because it is easy to spot the 
failed sub jobs.
- Which sub jobs failed?
    - Can you figure out why they failed?
    - How do they compare to jobs that finished?

{:start="3"}
3. Use `seff` to look at individual sub jobs:

```bash
seff slurmjobid_5             # replace slurmjobid again
```

4. Try `sacct` with the `-o` option (discussed above). This time add fields `reqmem` (requested memory) and `timelimit` (requested time):

```bash
sacct -o jobname,jobid,reqmem,maxrss,timelimit,elapsed,state -j slurmjobid    # replace slurmjobid
```

💭 Note that in this case we can not use the `-X` option, as we want to see memory usage for each step.

## Readjusting the job-file

1. Look at the error messages produced by the failed jobs.
2. When you know which subjobs failed and why, adjust the resource requests as necessary

- Change time and memory reservations:

```bash
#SBATCH --time=00:05:00
#SBATCH --mem=2000
```

{:start="3"}
3. Re-run the failed subjobs:

```bash
#SBATCH --array=3,5    # Specify which ones to run
```

4. Use `seff` and `sacct` to look at the jobs. How much memory and time did they use?

## More information

💡 You can read more about [array jobs](https://docs.csc.fi/computing/running/array-jobs) and [seff and sacct](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/) in CSC Docs.
