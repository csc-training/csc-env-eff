---
topic: disk-areas
title: Exercise - I/O intensive computing tasks (advanced) 
---

# How to run I/O intensive computing tasks efficiently?

💬 _This exercise requires usage of the batch queue system. Feel free to carry on or return to this after Topic 5._

## Background

Lustre-based project-specific directories `/scratch` and `/projappl` can store large amounts of data and are accessible to all compute nodes of Puhti. However, these directories are not good for managing a large number of files or performing intensive input/output (I/O) operations. If you need to work with a huge number of smaller files or perform frequent reads/writes, you should consider using the NVMe-based local temporary scratch directories, either through normal or interactive batch jobs. Read more about the advantages of using the local scratch disk in [Docs CSC](https://docs.csc.fi/support/faq/local_scratch_for_data_processing/).

## Convert the following normal batch job script into one that uses local scratch for faster I/O

Below is a normal batch job script that pulls a docker image from DockerHub and converts it into an Apptainer image that is compatible with HPC environments such as CSC supercomputers Puhti/Mahti. During the conversion process, several layers are retrieved, cached and then converted into an Apptainer image file `.sif`.

```bash
#!/bin/bash
#SBATCH --account=<project>       # Choose the billing project. Has to be defined!
#SBATCH --time=01:00:00           # Maximum duration of the job. Upper limit depends on the partition. 
#SBATCH --partition=small         # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --mem=10G                 # Reserve memory

export APPTAINER_TMPDIR=/scratch/<project>/$USER    # Use these folders instead of the default $HOME
export APPTAINER_CACHEDIR=/scratch/<project>/$USER  # $HOME has less space and you hate cleaning, don't you?

apptainer pull --name trinity.simg docker://trinityrnaseq/trinityrnaseq
```

Copy the script above to a file (e.g. `batch_job.sh`) and modify it accordingly. You can then submit the script file to a compute node using the command

```bash
sbatch batch_job.sh
```

### How long did it take to finish the job? What about when using NVMe?

### Hints

- If you first ran the default script (above), then you need to clear the cache before running the next one.
- Request NVMe fast local storage using the `--gres` flag in the `#SBATCH` directive as follows:

```bash
#SBATCH --gres=nvme:<local_storage_space_per_node>  # e.g., to request 200 GB of fast disk space, use --gres=nvme:200 
```

- Use the environment variable `$LOCAL_SCRATCH` to access the local storage on each compute node.
- Important! Move any data back to the shared area (`/scratch`) once the job is finished, otherwise the data will be lost!

### Solution for script

```bash
#!/bin/bash
#SBATCH --account=<project>      # Choose the billing project. Has to be defined!
#SBATCH --time=01:00:00          # Maximum duration of the job. Upper limit depends on the partition. 
#SBATCH --partition=small        # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --mem=10G                # Reserve memory
#SBATCH --gres=nvme:100          # Reservation of local NVMe storage. Default unit: GB

export APPTAINER_TMPDIR=$LOCAL_SCRATCH    # Set the local storage area to the environment.. 
export APPTAINER_CACHEDIR=$LOCAL_SCRATCH  # ..variable that Apptainer understands.
unset XDG_RUNTIME_DIR                     # Get rid of some unnecessary warnings in output

cd $LOCAL_SCRATCH
pwd
singularity pull --name trinity.simg docker://trinityrnaseq/trinityrnaseq
mv trinity.simg /scratch/<project>/$USER/                                                            
```

Below is a comparison of execution time for running the same job on `$LOCAL_SCRATCH` _vs_. normal `/scratch`.  

|                 | `$LOCAL_SCRATCH` | `/scratch` |
|-----------------|------------------|------------|
| Wall-clock time | 22m 06s          | 50m 06s    |
