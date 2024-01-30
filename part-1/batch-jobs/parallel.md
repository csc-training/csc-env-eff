---
layout: default
title: Parallel batch jobs
parent: 5. Batch queue system and interactive use
grand_parent: Part 1
nav_order: 2
has_children: false
has_toc: false
permalink: /hands-on/batch_jobs/parallel.html
---

# Batch job tutorial - Parallel jobs

> In this tutorial we'll get familiar with the basic usage of the Slurm batch queue system at CSC
- The goal is to learn how to request resources that **match** the needs of a job

💬 A batch job consists of two parts: resource requests and the job step(s)

☝🏻 Examples are done on Puhti. If using the web interface, open a login node shell.

## Parallel jobs

💬 A parallel program is capable of utilizing several cores and other resources simultaneously for the same job

💬 The aim of a parallel program is to solve a problem (job) faster and to tackle larger problems that would be intractable to run on a single core

💡 There are two major approaches to dividing a computational burden over several cores:

- [OpenMP](https://e-learn.csc.fi/pluginfile.php/3007/mod_resource/content/1/09-OpenMP-intro.pdf)
- [MPI](https://e-learn.csc.fi/pluginfile.php/2997/mod_resource/content/1/04-intro-to-mpi.pdf)
- Depending on the parallel program and the type of job, the optimal resource request is often difficult to predict beforehand
    - Always start small and scale up gradually! Don't run on 1000 cores unless you're sure your program can use each of them efficiently.

☝🏻 Note! You need to have an MPI module loaded when running parallel batch jobs. If you get an error saying `error while loading shared libraries: libmpi.so.40: cannot open shared object file: No such file or directory`, try `module load StdEnv` to load the default environment (or load a specific MPI module, e.g. `openmpi`).

### A simple OpenMP job

💬 An OpenMP-enabled program can take advantage of multiple cores that share the same memory on a **single node**, a.k.a. _threads_

1. Go to your personal folder under the `/scratch` directory of your project:

```bash
cd /scratch/<project>/$USER         # replace <project> with your CSC project, e.g. project_2001234
```

- Now your input (and output) will be on a shared disk that is accessible to the compute nodes.

💡 You can list your projects with `csc-projects`

{:style="counter-reset:step-counter 1"}
2. Download a simple program parallelized with OpenMP:

```bash
wget https://a3s.fi/hello_omp.x/hello_omp.x
```

{:style="counter-reset:step-counter 2"}
3. Make it executable using the command:

```bash
chmod +x hello_omp.x
```

{:style="counter-reset:step-counter 3"}
4. Copy the following script into a file called `my_parallel_omp.bash` and change `<project>` to the CSC project you actually want to use:

```bash
#!/bin/bash
#SBATCH --account=<project>      # Choose the billing project. Has to be defined!
#SBATCH --time=00:00:10          # Maximum duration of the job. Upper limit depends on partition. 
#SBATCH --partition=test         # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --ntasks=1               # Number of tasks. Upper limit depends on partition.
#SBATCH --cpus-per-task=4        # How many processors work on one task. Max: Number of CPUs per node.

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun hello_omp.x
```

{:style="counter-reset:step-counter 4"}
5. Submit the job to the queue with the command:

```bash
sbatch my_parallel_omp.bash
```

💬 In the batch job example above we are requesting

- resources for one OpenMP job (`--ntasks=1`)
- using four cores (threads) per task (`--cpus-per-task=4`)
- for ten seconds (`--time=00:00:10`)
- from the test queue (`--partition=test`)

💬 We want to run the program `hello_omp.x` that will be able to utilize four cores

💭 Exporting the environment variable `OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK` will tell the program that it can use four threads

🗯 Each of the four threads launched by `hello_omp.x` will print their own output

#### Check the output

💬 When finished, the output file `slurm-<jobid>.out` should contain the results printed from each of the four OpenMP threads

1. Check which files exist in the folder:

```bash
ls
```

{:style="counter-reset:step-counter 1"}
2. Check the output with:

```bash
cat slurm-<jobid>.out     # replace <jobid> with the actual Slurm job ID
```

{:style="counter-reset:step-counter 2"}
3. The results should look something like this:

```bash
cat slurm-5118404.out
Hello from thread: 0
Hello from thread: 3
Hello from thread: 2
Hello from thread: 1
```

### A simple MPI job

💬 An MPI-enabled program can take advantage of resources that are spread over multiple compute nodes

1. Download a simple program parallelized with MPI:

```bash
wget https://a3s.fi/hello_mpi.x/hello_mpi.x
```

{:style="counter-reset:step-counter 1"}
2. Make it executable using the command:

```bash
chmod +x hello_mpi.x
```

{:style="counter-reset:step-counter 2"}
3. Copy the script below into a file called `my_parallel.bash` and change `<project>` to the CSC project you actually want to use:

```bash
#!/bin/bash
#SBATCH --account=<project>      # Choose the billing project. Has to be defined!
#SBATCH --time=00:00:10          # Maximum duration of the job. Upper limit depends of the partition. 
#SBATCH --partition=test         # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --nodes=2                # Number of compute nodes. Upper limit depends on partition.
#SBATCH --ntasks-per-node=4      # How many tasks to launch per node. Depends on the number of cores and memory on a node.

srun hello_mpi.x
```

{:style="counter-reset:step-counter 3"}
4. Submit the job to queue with the command:

```bash
sbatch my_parallel.bash
```

💬 In the batch job example above we are requesting

- resources from two nodes (`--nodes=2`)
- four cores from each node (`--ntasks-per-node=4`)
- for ten seconds (`--time=00:00:10`)
- from the test queue (`--partition=test`)

💬 We want to run the program `hello_mpi.x` that will, based on the resource request, start 8 simultaneous tasks

💬 Each of the 8 tasks launched by `hello_mpi.x` will report their number and on which node they ran

#### Check the output and the efficiency

💬 When finished, the output file `slurm-<jobid>.out` will contain the results from the `hello_mpi.x` program on how the 8 tasks were distributed over the two reserved nodes

1. Check the output with:

```bash
cat slurm-<jobid>.out    # replace <jobid> with the actual Slurm job ID
```

{:style="counter-reset:step-counter 1"}
2. The output should look something like this:

```bash
Hello world from node r07c01.bullx, rank 0 out of 8 tasks
Hello world from node r07c02.bullx, rank 5 out of 8 tasks
Hello world from node r07c02.bullx, rank 7 out of 8 tasks
Hello world from node r07c01.bullx, rank 2 out of 8 tasks
Hello world from node r07c02.bullx, rank 4 out of 8 tasks
Hello world from node r07c01.bullx, rank 3 out of 8 tasks
Hello world from node r07c01.bullx, rank 1 out of 8 tasks
Hello world from node r07c02.bullx, rank 6 out of 8 tasks
```

{:style="counter-reset:step-counter 2"}
3. The output above verifies that the requested 8 tasks were distributed over two nodes (`r07c01.bullx, r07c02.bullx`), four tasks on each
4. Check the efficiency of the job compared to the reserved resources by issuing the command `seff <jobid>` (replace `<jobid>` with the actual Slurm job ID)

🗯 **Note!** This example asks 4 cores from each of the 2 nodes. Normally, this would not make sense, and instead it would be better to run all 8 cores in the same node (in Puhti one node has 40 cores!). Typically, you want your resources (cores) to be spread on as few nodes as possible to avoid unnecessary communication between nodes.

## More information

💡 [FAQ on CSC batch jobs](https://docs.csc.fi/support/faq/#batch-jobs) in Docs CSC

💭 You can get a list of all your jobs that are running or queuing with the command `squeue -u $USER`

💭 A submitted job can be cancelled using the command `scancel <jobid>`
