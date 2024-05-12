---
layout: default
title: High-throughput Snakemake workflows
parent: 11. How to speed up jobs
grand_parent: Part 2
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/throughput/snakemake-ht.html
---

# Running Snakemake workflows at scale on Puhti

> This tutorial is done on **Puhti**, which requires that:

- You have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
- Your account belongs to a project [that has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

💬 Snakemake is a popular scientific workflow manager, especially within the
bioinformatics community. The workflow manager enables scalable and
reproducible scientific pipelines by chaining a series of rules in a
fully-specified software environment.
[Snakemake is available as a pre-installed module on Puhti](https://docs.csc.fi/apps/snakemake/).

## Use containers as runtime environment 

💬 HPC-friendly containers like Singularity/Apptainer can be used as an
alternative to native or Tykky-based installations for better portability and
reproducibility. If you don't have a ready-made container image for your needs,
you can build a Singularity/Apptainer image on Puhti using `--fakeroot` option.  

☝🏻 For the purpose of this tutorial, a pre-built container image is provided
later to run Snakemake workflows at scale.

## Use HyperQueue executor to submit jobs

‼️ If a workflow manager is using `sbatch` (or `srun`) for each process execution
(i.e., a rule in Snakemake terminology), and the workflow has many short
processes, it's advisable to use HyperQueue executor to improve throughput and
decrease load on the Slurm batch job scheduler.

1. HyperQueue and Snakemake modules on Puhti can be loaded as below:
   ```bash
   module load hyperqueue/0.16.0
   module load snakemake/8.4.6
   ```

   ‼️ Note! In case you are planning to use Snakemake on LUMI supercomputer, you
   can use CSC module installations as below:

   ```bash
   module use /appl/local/csc/modulefiles/
   module load hyperqueue/0.18.0
   module load snakemake/8.4.6
   ```

2. HyperQueue executor settings for a Snakemake workflow can be changed
   depending on the version of Snakemake as shown below:

   ```bash
   # snakemake version 7.x.x
   snakemake --cluster "hq submit  ..."
   # snakemake version 8.x.x
   snakemake --executor cluster-generic --cluster-generic-submit-cmd "hq submit ..."  
   ```

## Submit a Snakemake workflow on Puhti

1. Create and enter a suitable scratch directory on Puhti (replace `<project>`
   with your CSC project, e.g. `project_2001234`):

   ```bash
   mkdir -p /scratch/<project>/$USER/snakemake-ht
   cd /scratch/<project>/$USER/snakemake-ht
   ```

2. Download the tutorial material, which has been adapted from the
   [official Snakemake documentation](https://snakemake.readthedocs.io/en/v6.6.1/executor_tutorial/google_lifesciences.html),
   from Allas:

   ```bash
   wget https://a3s.fi/snakemake_scale/snakemake_scaling.tar.gz
   tar -xavf snakemake_scaling.tar.gz
   ```

3. The downloaded material includes scripts and data to run a Snakemake
   pipeline. You can use `snakemake_hq_puhti.sh`, the contents of which are
   posted below:

   ```bash 
   #!/bin/bash
   #SBATCH --job-name=snakemake
   #SBATCH --account=<project>  # replace <project> with your CSC project, e.g. project_2001234
   #SBATCH --partition=small
   #SBATCH --time=00:10:00
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=1
   #SBATCH --cpus-per-task=40
   #SBATCH --mem-per-cpu=2G
   
   module load hyperqueue/0.16.0
   module load snakemake/8.4.6
   
   # Specify a location for the HyperQueue server
   export HQ_SERVER_DIR=${PWD}/hq-server-${SLURM_JOB_ID}
   mkdir -p "${HQ_SERVER_DIR}"
    
   # Start the server in the background (&) and wait until it has started
   hq server start &
   until hq job list &>/dev/null ; do sleep 1 ; done
    
   # Start the workers in the background and wait for them to start
   srun --exact --cpu-bind=none --mpi=none hq worker start --cpus=${SLURM_CPUS_PER_TASK} &
   hq worker wait "${SLURM_NTASKS}"
   
   snakemake -s Snakefile --jobs 1 --use-singularity --executor cluster-generic --cluster-generic-submit-cmd "hq submit --cpus 5"
   
   # For Snakemake versions 7.x.x, use command:
   # snakemake -s Snakefile --jobs 1 --use-singularity --cluster "hq submit --cpus 5"
   
   # Wait for all jobs to finish, then shut down the workers and server
   hq job wait all
   hq worker stop all
   hq server stop
   ```

### How to parallelize Snakemake workflow jobs?

☝🏻 The default script provided above is not optimized for throughput, as the
Snakemake workflow manager just submits one job at a time to the HyperQueue
meta-scheduler.

1. You can run multiple workflow tasks (i.e., rules) concurrently by submitting
   more jobs using the `snakemake` command as:

   ```bash
   snakemake -s Snakefile --jobs 8 --use-singularity --executor cluster-generic --cluster-generic-submit-cmd "hq submit --cpus 5"
   ``` 

2. Replace the above modification in the `snakemake_hq_puhti.sh` batch script
   (and use your own project number) before submitting the Snakemake workflow
   job with:

   ```
   sbatch snakemake_hq_puhti.sh
   ```

☝🏻 Note that just increasing the value of `--jobs` will not automatically make
all those jobs run at the same time. This option of the `snakemake` command is
just a maximum limit for the number of concurrent jobs. Jobs will eventually
run when resources are available. In this case, we run 8 concurrent jobs, each
using 5 CPU cores to match the reserved 40 CPU cores (one Puhti node) in the
batch script. In practice, it is also a good idea to dedicate a few cores for
the workflow manager itself.

💡 It is also possible to use more than one node to achieve even higher
throughput as HyperQueue can make use of multi-node resource allocations.
Just remember that with HyperQueue the workflow tasks themselves should be
sub-node (use one node at most) as MPI tasks are poorly supported.

### Follow the progress of jobs

💡 You can already check the progress of your workflow by simply observing the
current working directory where lots of new task-specific folders are being
created. However, there are also formal ways to check the progress of your jobs
as shown below.

1. Monitor the status of submitted *Slurm* job:

   ```
   squeue -j <slurmjobid>
   # or
   squeue --me
   # or
   squeue -u $USER
   ```

2. Monitor the progress of the individual sub-tasks using HyperQueue commands:

   ```
   module load hyperqueue
   export HQ_SERVER_DIR=$PWD/hq-server-<slurmjobid>
   hq worker list
   hq job list
   hq job info <hqjobid>
   hq job progress <hqjobid>
   hq task list <hqjobid>
   hq task info <hqjobid> <hqtaskid>
   ```

### How to clean task-specific folders automatically?

💭 HyperQueue creates task-specific folders (`job-<n>`) in the same directory
from where you submitted the batch script. These are sometimes useful for
debugging. However, if your code is working fine, the creation of many folders
may be annoying besides causing some load on the Lustre parallel file system.
You can prevent the creation of such task-specific folders by setting `stdout`
and `stderr` HyperQueue flags to `none` as shown below:

```bash
snakemake -s Snakefile -j 24 --use-singularity --executor cluster-generic --cluster-generic-submit-cmd "hq submit --stdout=none --stderr=none --cpus 5"
```

## More Information

- [Docs CSC: Snakemake apps page](https://docs.csc.fi/apps/snakemake/)
- [Official Snakemake documentation](https://snakemake.readthedocs.io/en/stable/)
