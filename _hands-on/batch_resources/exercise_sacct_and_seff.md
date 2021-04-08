---
topic: batch resources
title: Exercise - find your past job resource usage
---
# Get an overview of recent jobs' resource usage

## What were my recent jobs?

Using the commands as shown in the tutorial above, list
your jobs from the past month and print out enough details
so that you can remember what the jobs were about (perhaps,
jobid, the name, partition, start time, allocated cores, used and
requested memory). The jobid you can connect to slurm output
files, if you still have those available.

Some tips:

* The `sacct` command is a little bit heavy query for the 
  scheduler accounting database. Don't make big queries for
  testing (we don't want to slow down jobs getting scheduled
  to run!), but start with the past day or so, until you get
  the syntax right. (This applies to learning all new commands
  and applications).
* With `man sacct` you can see what keywords to use to print
  out different fields stored in the database.
* Once you have the data, print it out a file, so that you don't
  need to rerequest it from the Slurm database. Then work with
  the file. E.g. `sacct -S 2021-04-01 > output.txt` and then
  use your favourite tools (`more` or `less`) to look at the 
  contents (and `grep`, `awk`, `python`, etc.)

## Look for patterns or anomalies

Some things to look for:

* Did some jobs fail, why?
* How long did the jobs take?
* Did you request a suitable amount of time? 
* Was the memory request appropriate?
* Take a sample of some parallel jobs (based on the `sacct` output parameters you should be able to find representative jobs for each type, that you've been running recently) and use `seff` to look for the CPU Efficiency.
* If you used GPU, did those jobs really use GPU? (Also shown with `seff`)

Use this information to set the resource requests for similar new jobs.
You can also look at [my.csc.fi](https://my.csc.fi] for previous (monthly)
usage per project.
