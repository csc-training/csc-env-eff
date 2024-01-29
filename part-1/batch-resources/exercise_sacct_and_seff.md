---
layout: default
title: Find resource usage of recent jobs
parent: 6. Batch job resource usage
grand_parent: Part 1
nav_order: 2
has_children: false
has_toc: false
permalink: /hands-on/batch_resources/exercise_sacct_and_seff.html
---

# Get an overview of the resource usage of recent jobs

## What were my recent jobs?

Using the commands shown in the previous tutorial, list your jobs from the past
month and print out enough details so that you can remember the purpose of the
jobs (perhaps job ID, the name, partition, start time, allocated cores, used
and requested memory). The job ID could be connected to Slurm output files, if
you still have those available.

Some tips:

* The `sacct` command is a rather heavy query to the Slurm accounting database.
  Don't make large queries for testing as we don't want to slow down jobs getting
  scheduled to run! Start with the past day or so until you get the syntax right.
  This applies to learning all new commands and applications.
* With `man sacct` you can see which keywords to use for printing out different
  fields stored in the database.
* Once you have the data, print it to a file so that you don't need to re-request
  it from the Slurm accounting database. For example,

```bash
sacct -S 2022-11-01 > sacct_output.txt
```

* Work with this file using your favorite tools (e.g. `more` or `less`) to look
  at the contents (and `grep`, `awk`, `python`, etc. to extract/analyze data).

## Look for patterns or anomalies

Some things to look for:

* Did some jobs fail? If so, why?
* How long did the jobs take?
* Did you request a suitable amount of time?
* Was the memory request appropriate?
* Take a sample of some parallel jobs (based on the `sacct` output parameters
  you should be able to find representative jobs for each type that you've been
  running recently) and use `seff` to look for the CPU Efficiency.
* If you requested GPU resources, did those jobs really use the GPUs efficiently? (also shown with `seff`)

Use this information to set the resource requests for similar new jobs. You can
also look in [My CSC](https://my.csc.fi) for previous (monthly) usage per project.
