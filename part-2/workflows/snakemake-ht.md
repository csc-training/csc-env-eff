# Running Snakemake Workflow at Scale on Puhti

Snakemake workflow is one of the popular scientific workflows in the bioinformatics community. The workflow manager enables scalable and reproducible scientific pipelines by chaining a series of rules in a fully-specified software environment. Snakemake software is available as a module in Puhti supercomputing environment.


## Use Containers as Runtime Environment 

One can use Singularity/Apptainer container as an alternative to native or Tykky container-based installations for better portability and reproducibility.  If you don't have a ready-made container image for your needs, you can build a Singularity/Apptainer image on Puhti using **--fakeroot** option.  

For the purpose of this tutorial a pre-built container image is provided to run snakemake workflow at scale.

## Use HyperQueue Executor to Submit Jobs

If a workflow manager is using `sbatch` for each process execution (i.e., a rule), and you have many short processes, it's advisable to switch to HyperQueue to improve throughput and decrease load on the system batch scheduler.

You can load HyperQueue and Snakemake modules on Puhti as below:
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

One can use HyperQueue executor settings depending on the Snakemake version as below:

```bash
# snakemake version 7.xx.x
snakemake --cluster "hq submit  ..."  
# snakemake version 8.x.x.x
snakemake --executor cluster-generic --cluster-generic-submit-cmd "hq submit ..."  
```


## Submit Snakemake Workflow on Cluster

Download tutorial materials (scripts and data), which have been adapted from the [official Snakemake documentation](https://snakemake.readthedocs.io/en/v6.6.1/executor_tutorial/google_lifesciences.html), from CSC Allas object storage as below:

```bash
wget https://a3s.fi/snakemake_scale/snakemake_scaling.tar.gz
tar -xavf snakemake_scaling.tar.gz
```

The downloaded material includes scripts and data to run snakemake pipeline. You can use `snakemake_hq_puhti.sh` whose content is posted below:

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

Please use correct project number in sbatch directives and submit the Snakemake workflow job as below:

```
sbatch snakemake_hq_puhti.sh
```

### How Do You Parallelise Snakemake Workflow?

Parallelism can be achieved by allowing more parallel jobs (here modify the flag, -j) from snakemake as below:

```
snakemake -s Snakefile -j 8 --use-singularity --executor cluster-generic --cluster-generic-submit-cmd "hq submit --cpus 5"
``` 

One can also use more than one node to achieve even more high-throughput as HyperQueue can make use of multi-node resource allocations.


### Follow the Progress of Jobs

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