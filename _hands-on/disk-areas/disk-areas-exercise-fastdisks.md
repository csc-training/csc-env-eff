---
topic: disk-areas
title: Exercise - High I/O operation computing tasks (advanced) 
---

# Where to run computing tasks that require high I/O operations ?

💬 _This exercise requires usage of the batch queue. Feel free to carry on or return to this after Topic 5._

## Background

Lustre-based project-specific directories, *scratch* and *projappl*, can store large amounts of data and are accessible to all compute nodes of Puhti. However, these directories are not good for managing a large number of files.  If you need to work with a huge number of smaller files, you should consider using the NVMe based local temporary scratch directories, either through normal or interactive batch jobs. Read more about the advantages of using local scratch drive on [CSC docs pages](https://docs.csc.fi/support/faq/local_scratch_for_data_processing/)
 
## Convert the following normal batch job script into the one that uses local scratch drive for faster computational tasks? 

Below is a normal batch job that pulls docker image from DockerHub and converts into a singularity one that is compatible with working in HPC environments such as CSC Puhti and Mahti supercomputers. During the conversion process, several layers are retrieved, cached and then converted into a singularity file (.sif format)

```bash
#!/bin/bash
#SBATCH --account=project_xxx    # Choose the billing project. Has to be defined!
#SBATCH --time=01:00:00          # Maximum duration of the job. Max: depends of the partition. 
#SBATCH --partition=small        # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
export SINGULARITY_TMPDIR=/scratch/project_xxx/$USER    # Use these folders instead of the default: $HOME
export SINGULARITY_CACHEDIR=/scratch/project_xxx/$USER  # because at $HOME there's less space and you hate cleaning, don't you?
singularity pull --name trinity.simg  docker://trinityrnaseq/trinityrnaseq
```

Copy above script to a file (e.g.,batch_job.sh) and modify it. You can then submit the script file to compute nodes using the following command:

```
sbatch batch_job.sh

```

### How much time did it take to finish above job?

### Hints

- If you run the default script (above) first then you need to clear the cache before running the modified one.
- Request NVME fast local storage using the --gres flag  in sbatch directive as below:

```bash
#SBATCH --gres=nvme:<local_storage_space_per_node>  # e.g., to claim 200 GB of storage, use option --gres=nvme:200 
```
- Use environment variable `$LOCAL_SCRATCH` to access the local storage on each node.

- Please move any data to shared area once  the job is finished


### Solution for script

```bash
#!/bin/bash
#SBATCH --account=project_xxx    # Choose the billing project. Has to be defined!
#SBATCH --time=01:00:00          # Maximum duration of the job. Max: depends of the partition. 
#SBATCH --partition=small        # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --gres=nvme:100          # Reservation of local NVMe storage. Unit: MiB

export SINGULARITY_TMPDIR=$LOCAL_SCRATCH    # Set the local storage area to the environmental.. 
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH  # ..variable that Singularity understands.
unset XDG_RUNTIME_DIR  # Get rid of some onnecessary warnings in job.out

cd $LOCAL_SCRATCH
#pwd
#df -lh
singularity pull --name trinity.simg docker://trinityrnaseq/trinityrnaseq
mv trinity.simg /scratch/project_xxx/$USER/                                                            
```

Below is the comparison of execution time for running the same job in LOCAL_SCRATCH *vs.* normal scratch.  

|                               | LOCAL_SCRATCH |         scratch|
|-------------------------------|---------------|----------------|    
|Wall-clock time     |22m 06s      |  50m 06s        |
