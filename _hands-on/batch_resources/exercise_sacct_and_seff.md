---
topic: batch resources
title: Exercise - sacct and seff 
---
# Using sacct and seff to look at finished jobs

In this exercise we look at commands `sacct` and `seff`.

`Sacct` is usefull when you want to look at a listing of jobs, but
by default it only shows minimal data.

`Seff`, on the other hand, shows detailed data on used resources 
in an easy-to-read format, but can only show one job at a time.

By deafault it shows the jobs you have run since last midnight:
```text
sacct
```
With the `-S`option you can specify the start time of listing.

```text
sacct -S 2021-03-01
```
With the ´-j` option you can specify a job id.

In this example we look at an array job that was run previously:
```text
sacct -j 5431722
```
Sacct is especially handy here, because it is easy to spot the 
failed sub jobs.

In this case we have only a few sub jobs, but if the array job 
is larger, it's probably clearer to look at just the jobs, and 
not at all the job steps:
```text
sacct -X -j 5431722
```
In this case it easy to see why one subjob died: Reason is listed as
TIMEOUT, meaning job ran out of time reservation. 

Often the reason may be listed simply as FAILED. To find out why 
the steps may have failed, you can use `seff` to look at those steps.

```text
seff 5431722_6
```
You should naturally also look at any error messages and log 
files produced by the failed jobs.

In this case you can check the succesful jobs, and see how much 
time they took.
```text
seff 5431722_1
```
When you know which subjobs failed and why, it you can adjust the
resource requests as necessary, and re-run the failed subjobs.

You can read more about [array jobs](https://docs.csc.fi/computing/running/array-jobs)
and [seff](https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/) in CSC Docs.