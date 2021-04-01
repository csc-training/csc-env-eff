---
topic: Batch jobs
title: Tutorial - Serial batch job tutorial
---

# Batch job tutorial - Serial jobs

- In this tutorial we'll get familiar with the basic usage of the Slurm batch queue system at CSC
- The goal is to learn how to request resources that **match** the needs of a job  
- A job consists of two parts: resource requests and the job step(s)
- Examples are done on Puhti 

## Serial jobs

- For a program that can use only one core (cpu), one should request only one core from Slurm. 
- The job doesn't benefit from additional cores, hence don't request more 
- Excess reservation is wasted since it wouldn't be available to other users
- Within the job (or allocation), the actual program is launched using the command `srun` 
- If you use a software that is preinstalled at CSC, please [check its infopage](https://docs.csc.fi/apps/): it might have a batch job template with useful default settings

```text 
#!/bin/bash
#SBATCH --account=myprojectname
#SBATCH --partition=test
#SBATCH --ntasks=1
#SBATCH --time=00:02:00

srun hostname
srun sleep 60
```

- In the batch job example above we are requesting one core (`--ntasks=1`) for two minutes (`--time=00:02:00`) from the test queue (`--partition=test`)
- We want to run the program `hostname`, that will print the name of the Puhti computing node that has been allocated for this particular job.
- In addition, we are running the `sleep` program to keep the job running for an additional 60 seconds, in order to have time to monitor the job
- Copy the example above into a file called `my_serial.bash` and change the `myprojectname` to the project you actually want to use (e.g. with `nano`)
- Submit the job to the queue with the command:
```
sbatch my_serial.bash
```   
- If you are quick enough you should see your job in the queue by issuing the command `squeue -u $USER` 
- By default the output is written into a file named `slurm-XXXXXXX.out` where `XXXXXXX` is a unique number corresponding to the job ID of the job 
- Check the efficiency of the job compared to the reserved resources by issuing the command `seff XXXXXXX` (replace `XXXXXXX` with the actual  job ID number from the `slurm-XXXXXXX.out` file) 
- You can get a list of all your jobs that are running or queuing with the command `squeue -u $USER`
- A submitted job can be cancelled using the command `scancel XXXXXXX` 


## Additional material [FAQ on CSC batch jobs ](https://docs.csc.fi/support/faq/#batch-jobs) in Docs CSC
