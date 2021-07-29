---
topic: Batch jobs
title: Tutorial - Parallel batch jobs
---

# Batch job tutorial - Parallel jobs

> In this tutorial we'll get familiar with the basic usage of the Slurm batch queue system at CSC
- The goal is to learn how to request resources that **match** the needs of a job  

💬 A batch job consists of two parts: resource requests and the job step(s)

☝🏻 Examples are done on Puhti 

## Parallel jobs
💬 A parallel program is capable of utilizing several cores and other resources simultaneously for the same job.  
💬 The aim of a parallel program is to solve a problem (job) faster and to tackle a larger problem that wouldn't fit into a single core

💡 There are two major strategies to divide the computational burden over several cores:
- [OpenMP](https://e-learn.csc.fi/pluginfile.php/3007/mod_resource/content/1/09-OpenMP-intro.pdf) 
- [MPI](https://e-learn.csc.fi/pluginfile.php/2997/mod_resource/content/1/04-intro-to-mpi.pdf)
- Depending on the parallel program and the type of job, the optimal resource request is often difficult to decide.

### A simple OpenMP job
💬 An OpenMP enabled program can take advantage of multiple cores that share the same memory on a **single node** 

1. Dowload a simple OpenMP parallel program with the
    ```
    wget https://a3s.fi/hello_omp.x/hello_omp.x
    ```
2. Make it executable using the command:
    ```bash
    chmod +x hello_omp.x
    ``` 
3. Copy the following example into a file called `my_parallel_omp.bash` and change the `projet_XXXX` to the project you actually want to use:

    ```bash
    #!/bin/bash
    #SBATCH --account=project_XXXX    # Choose the billing project. Has to be defined!
    #SBATCH --time=00:00:10          # Maximum duration of the job. Max: depends of the partition. 
    #SBATCH --partition=test        # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
    #SBATCH --ntasks=1               # Number of tasks. Max: depends on partition.
    #SBATCH --cpus-per-task=4        # How many processors work on one task. Max: Number of CPUs per node.

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun hello_omp.x
    ```

{:start="4"}
4. Submit the job to the queue with the command:
    ```
    sbatch my_parallel_omp.bash
    ```

💬 In the batch job example above we are requesting 
- resources for one OpenMP job (--ntasks=1)
- using four cores (`--cpus-per-task=4`)
- for ten seconds (`--time=00:00:10`)
- from the test queue (`--partition=test`)

💬 We want to run the program `hello_omp.x`, that will be able to utilise four cores.  
💭 The variable `OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK` tells the program that it can use four cores.   
🗯 Each of the four threads launced by `hello_omp.x` will print their own output.

#### Check the output
💬 When finished, the output file `slurm-XXXXXXX.out` should contain the results printed from the four OpenMP threads 

1. Check which files exist in the folder:
    ```bash
    ls
    ```
2. Check the output with:
    ```bash
    cat slurm-XXXXXXX.out     # replace XXXXXXXX
    ``` 
3. The results should look something like this: 
    ```bash
    cat slurm-5118404.out
    Hello from thread: 0
    Hello from thread: 3
    Hello from thread: 2
    Hello from thread: 1
    ```

### A simple MPI job
💬 A MPI enabled program can take advantage of resourses that are spread over multiple nodes.

1. Dowload a simple MPI parallel program with the command 
    ```bash
    wget https://a3s.fi/hello_mpi.x/hello_mpi.x
    ```
2. Make it executable using the command 
    ```bash
    chmod +x hello_mpi.x
    ``` 
3. Copy the example below into a file called `my_parallel.bash` and change the `project_XXXX` to the project you actually want to use

    ```bash
    #!/bin/bash
    #SBATCH --account=project_XXXX    # Choose the billing project. Has to be defined!
    #SBATCH --time=00:00:10          # Maximum duration of the job. Max: depends of the partition. 
    #SBATCH --partition=test        # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
    #SBATCH --nodes=2                # Number of computer nodes. Max: depends on partition.
    #SBATCH --ntasks-per-node=4      # How many tasks one node works on. Depends on max cores and memory of a node.

    srun hello_mpi.x
    ```

{:start="4"}
4. Submit the job to the queue with the command:
    ```bash
    sbatch my_parallel.bash
    ```

💬 In the batch job example above we are requesting 
- resources from two nodes (`--nodes=2`)
- four cores from each node (`--ntasks-per-node=4`)
- for ten seconds (`--time=00:00:10`) from the test queue (`--partition=test`)

💬 We want to run the program `hello_mpi.x`, that will, based on the resource request, start 8 simultaneous tasks.  
💬 Each of the 8 tasks launced by `hello_mpi.x` will report on which node they got their resource. 

#### Check the output and the efficiency
💬 When finished, the output file `slurm-XXXXXXX.out` should contain the results obtained by the `hello_mpi.x` program on how the 8 tasks were distributed over the two reserved nodes

1. Check The output with:
    ```bash
    cat slurm-XXXXXXX.out    # replace XXXXXXXX
    ```
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
3. The output above verifies that the requested 8 tasks were distributed over two nodes (`r07c01.bullx, r07c02.bullx`), four tasks on each
4. Check the efficiency of the job compared to the reserved resources by issuing the command `seff XXXXXXX` (replace `XXXXXXX` with the actual job ID number from the `slurm-XXXXXXX.out` file)

🗯 **Note!** This example asks 4 cores from each of the 2 nodes. Normally, this would not make sense, but it would be better to run all 8 cores in the same node (in Puhti one node has 40 cores). Typically, you want your resources (cores) to be spread on as few nodes as possible.

## More information
💡 [FAQ on CSC batch jobs ](https://docs.csc.fi/support/faq/#batch-jobs) in Docs CSC

💭 You can get a list of all your jobs that are running or queuing with the command `squeue -u $USER`  
💭 A submitted job can be cancelled using the command `scancel XXXXXXX` 
