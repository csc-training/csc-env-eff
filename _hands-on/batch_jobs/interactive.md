---
topic: Batch jobs
title: Tutorial - Interactive batch job tutorial
---

# Batch job tutorial - Interactive jobs

- In this tutorial we'll get familiar with the basic usage of the Slurm batch queue system at CSC
- The goal is to learn how to request resources that **match** the needs of a job
- A job consists of two parts: resource requests and the job step(s)
- Examples are done on Puhti

## Interactive jobs

- In an interactive batch job, an interactive shell session is launced on a computing node. For heavy interactive tasks one can request specific resources (time, memory, cores, disk). 

- You can also use tools with graphical user interfaces in an interactive shell session. For such usage the [NoMachine](https://docs.csc.fi/support/tutorials/nomachine-usage/) remote desktop often provides an improved experience.  

### A simple interactive job 

- To start an interactive job using one core for ten minutes
```text
sinteractive --account myprojectname --time 00:10:00
```
- You should see that the command prompt (what's shown to the left to your cursor) has changed from _puhti-login1_ (or _puhti-login2_) to e.g. _r07c51_
- Once on the compute node, you can run commands directly from the command line without `srun`, e.g. launch the (default) Python interpreter:
```
module load python-env
python3
```
- Quit the Python interpreter with `quit()`
- This way you can work interactively for extended period, using lots of memory without creating load on the login nodes, which is forbidden in [the Usage Policy](https://docs.csc.fi/computing/overview/#usage-policy).
- Quit the interactive batch job with `exit`. Note, that above you asked only for 10 minutes of time. Once that is up, you will be automatically logged out from the compute node. From the command line prompt you can see whether you're in the compute node (e.g. _r07c51_) or back to the login node (e.g. _puhti-login2_). Giving `exit` in the login node, will log you out from Puhti.
- See the documetation at docs.csc.fi of [Interactive usage](https://docs.csc.fi/computing/running/interactive-usage/), for further information
 
## Additional material [FAQ on CSC batch jobs ](https://docs.csc.fi/support/faq/#batch-jobs) in Docs CSC
