---
topic: disk-areas
title: Exercise - disk-areas fastdisks 
---

# Where to run computing tasks that require high I/O operations ?

## Background

Lustre-based project-specific directories, *scratch* and *projappl*, can store large amounts of data and are accessible to all compute nodes of Puhti. However, these directories are not good for managing a large number of files.  If you need to work with a huge number of smaller files, you should consider using the NVMe based local temporary scratch directories, either through normal or interactive batch jobs. Read more about the advantages of using local scratch drive on [CSC docs pages](https://docs.csc.fi/support/faq/local_scratch_for_data_processing/)
 
## Convert the following normal batch job script into the one that uses local scratch drive for faster computational tasks? 

Below is a normal batch job that pulls docker image from DockerHub and converts into a singularity one that is compatible with working in HPC environments such as CSC Puhti and Mahti supercomputers. During the conversion process, several layers are retrieved, cached and then converted into a singularity file (.sif format)

```bash
#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --partition=small
#SBATCH --account=project_xxx

export SINGULARITY_TMPDIR=/scratch/project_xxx/$USER
export SINGULARITY_CACHEDIR=/scratch/project_xxx/$USER
singularity pull --name trinity.simg  docker://trinityrnaseq/trinityrnaseq
```

Copy above script to a file (e.g.,batch_job.sh) and modify it. You can then submit the script file to compute nodes using the following command:

```
sbatch batch_job.sh

```

### How much tim,e did it take to finish above job?

### Hints

- Request NVME fast local storage using the --gres flag  in sbatch directive as below:

```
#SBATCH --gres=nvme:<local_storage_space_per_node>  # e.g., to claim 200 GB of storage, use option --gres=nvme:200 

```
- Use environment variable $LOCAL_SCRATCH to access the local storage on each node.

- Please move any data to shared area once  the job is finished


### Solution for script

```bash
#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --partition=small
#SBATCH --account=project_xxx
#SBATCH  --gres=nvme:100

export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH
unset XDG_RUNTIME_DIR

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
