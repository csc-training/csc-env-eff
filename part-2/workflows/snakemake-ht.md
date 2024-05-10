---
layout: default
title: Snakemake workflows on Puhti
parent: 11. How to speed up jobs
grand_parent: Part 2
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/throughput/snakemake.html
---

# Running Snakemake Workflow at Scale on Puhti

Snakemake workflow is one of the popular scientific workflow managers in the bioinformatics community. The workflow manager enables scalable and reproducible scientific pipelines by chaining a series of rules in a fully-specified software environment. Snakemake software is available as a pre-installed module in Puhti supercomputing environment.


## Use Containers as a Runtime Environment 

HPC-friendly containers like Singularity/Apptainer can be used as an alternative to native or Tykky container-based installations for better portability and reproducibility. If you don't have a ready-made container image for your needs, you can build a Singularity/Apptainer image on Puhti using **--fakeroot** option.  

For the purpose of this tutorial a pre-built container image is provided later to run snakemake workflow at scale.

## Use HyperQueue Executor to Submit Jobs

If a workflow manager is using `sbatch` for each process execution (i.e., a rule in snakemkae terminology), and a workflows has many short processes, it's advisable to switch to HyperQueue to improve throughput and decrease unnecessary overload on system batch scheduler.

HyperQueue and Snakemake modules on Puhti can be loaded as below:
```bash
module load hyperqueue/0.16.0
module load snakemake/8.4.6
```
‼️ In case you are planning to use Snakemake workflow tests on LUMI supercomputer, you can use module installations done by CSC staff on LUMI. You can load HyperQueue and Snakemake modules as below:
```bash
           module use /appl/local/csc/modulefiles/
           module load hyperqueue/0.18.0
           module load snakemake/8.4.6
```

HyperQueue executor settings for snakemake workflow can be changed depending on the version of Snakemake, as shown below:

```bash
# snakemake version 7.xx.x
snakemake --cluster "hq submit  ..."  
# snakemake version 8.x.x.x
snakemake --executor cluster-generic --cluster-generic-submit-cmd "hq submit ..."  
```


## Submit Snakemake Workflow on Cluster

Download tutorial material, which has been adapted from the [official Snakemake documentation](https://snakemake.readthedocs.io/en/v6.6.1/executor_tutorial/google_lifesciences.html), from CSC Allas object storage as below:

```bash
wget https://a3s.fi/snakemake_scale/snakemake_scaling.tar.gz
tar -xavf snakemake_scaling.tar.gz
```
The downloaded material includes scripts and data to run snakemake pipeline.  You can use `snakemake_hq_puhti.sh` whose content is posted below:

```bash 
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=project_xxxx
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=2G
#SBATCH --nodes=1
#SBATCH --cpus-per-task=40
#SBATCH --ntasks-per-node=1
#SBATCH --partition=small

module load hyperqueue
module load snakemake/8.4.6

# Create a per job directory

export HQ_SERVER_DIR=$PWD/.hq-server-$SLURM_JOB_ID
mkdir -p $HQ_SERVER_DIR

hq server start &
srun --cpu-bind=none --hint=nomultithread --mpi=none -N $SLURM_NNODES -n $SLURM_NNODES  hq worker start --cpus=40 &

num_up=$(hq worker list | grep RUNNING | wc -l)
while true; do

    echo "Checking if workers have started"
    if [[ $num_up -eq $SLURM_NNODES ]];then
        echo "Workers started"
        break
    fi
    echo "$num_up/$SLURM_NNODES workers have started"
    sleep 1
    num_up=$(hq worker list | grep RUNNING | wc -l)

done

snakemake -s Snakefile -j 1 --use-singularity --executor cluster-generic --cluster-generic-submit-cmd "hq submit --cpus 5"
# snakemake -s Snakefile --jobs 1 --use-singularity --cluster "hq submit --cpus 2"

hq worker stop all
hq server stop
```

Please use correct CSC project number in the sbatch directives of above script and submit the Snakemake workflow job as below:

```
sbatch snakemake_hq_puhti.sh
```

### How Do You Parallelise Snakemake Workflow?

Once you reserve sufficient resources in batch script, parallelism can be achieved by allowing more parallel jobs (tip: check the flag, -j) from snakemake command as below:

```
snakemake -s Snakefile -j 8 --use-singularity --executor cluster-generic --cluster-generic-submit-cmd "hq submit --cpus 5"
``` 

One can also use more than one node to achieve even more high-throughput as HyperQueue can make use of multi-node resource allocations.


### How Do You Follow the Progress of Jobs ?

1. Monitor the status of submitted job

```
squeue -j <slurmjobid>
# or
squeue --me
# or
squeue -u $USER

```

2. Monitor the progress of the individual sub-tasks using HyperQueue usub-commands

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

## More Information

- [CSC documentation on Snakemake](https://docs.csc.fi/support/tutorials/snakemake-puhti/)
- [Snakemake official documentation](https://snakemake.readthedocs.io/en/stable/)