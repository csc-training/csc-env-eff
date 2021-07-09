---
topic: batch resources
title: Tutorial - sacct and seff, resources used 
---
# Using sacct and seff to look at finished jobs

In this tutorial we look at commands `seff` and `sacct`.

`Seff` shows detailed data on used resources in an easy-to-read 
format, but can only show one job at a time.

`Sacct` is useful when you want to look at a listing of jobs, but
by default it only shows minimal data.

By default `sacct` shows the jobs you have run on current date (_i.e._
since last midnight):
```text
sacct
```
With the `-S` option you can specify the start time of listing.

```text
sacct -S YYYY-MM-DD
```

With the `-j` option you can specify a job id, and only look at
a specific job.

```text
sacct -j xxxxxxx
```
You can select what data `sacct` shows. To see all available
data for a job, you can use:
```text
sacct -l -j xxxxxxx
```
As there are a lot of data fields, it is usually better to
select only the interesting ones. This can be done with the 
`-o` option.

For examaple to see job name, job id, used memory, job finish 
state and elapsed wall clock time you could use:
```text
sacct -o jobname,jobid,maxrss,state,elapsed -j xxxxxx
```
You can list all available data fields with:
```text
sacct -e
```
It should be noted that running `sacct` is heavy on the batch
job system, and you should not, for example, write scripts that
run it repeatedly.

## Running a test job

Let's run a simple array job to look at.

Create file `array.sh` and paste the following contents in to it.
Replace `project_xxxxxx` with your actual project name.

```text
#!/bin/bash
#SBATCH --job-name=array_job
#SBATCH --output=out_%A_%a.txt
#SBATCH --error=err_%A_%a.txt
#SBATCH --account=project_xxxxxx
#SBATCH --partition=small
#SBATCH --time=00:01:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1000
#SBATCH --array=1-6

/appl/soft/bio/course/sacct_exercise/test-a ${SLURM_ARRAY_TASK_ID}
```
Submit the job with command:
```text
sbatch array.sh
```
You will see a message like:
```text
Submitted batch job 123456
```
Make note of the actual job id.

You can follow the progress of the job with command:
```text
squeue -u $USER
```
How is an array job listed in the queue?

## Looking at the finished job

When the job has finished (you can no longer see any of the sub jobs
with `squeue`), you can use `sacct` to look at it. (Substitute xxxxx with 
your job id).
```text
sacct -j xxxxxx
```
In this case, we have only a few sub jobs, but if the array job 
is larger, it's probably clearer to look at just the jobs, and 
not at all the job steps. (Substitute xxxxx with your job id):
```text
sacct -X -j xxxxxx
```
`Sacct` is especially handy here, because it is easy to spot the 
failed sub jobs.

Which sub jobs failed?

Can you figure out why they failed?

How do they comapre to jobs that finished?

You can use `seff` to look at individual sub jobs. (Substitute 
xxxxx with your job id):
```text
seff xxxxx_5
```
You can also use `sacct` with the `-o` option we discussed above.
This time we also add fields `reqmem` (requested memory) and `timelimit`
(requested time). 

Note that in this case we can not use the `-X` option, as we want to
see memory usage for each step:

```text
sacct -o jobname,jobid,reqmem,maxrss,timelimit,elapsed,state -j xxxxxx
```

Also look at the error messages produced by the failed jobs.

When you know which subjobs failed and why, you can adjust the
resource requests as necessary, and re-run the failed subjobs.

Change time and memory reservations:
```text
#SBATCH --time=00:05:00
#SBATCH --mem=2000
```
Only rerun the failed sub jobs:
```text
#SBATCH --array=3,5
```
Did the jobs finish this time?

Use `seff` and `sacct` to look at the jobs. How much memory and time
did they use?

## Further reading
You can read more about [array jobs](https://docs.csc.fi/computing/running/array-jobs)
and [seff and sacct](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/) in CSC Docs.
