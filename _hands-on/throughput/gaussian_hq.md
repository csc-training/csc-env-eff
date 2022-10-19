---
topic: throughput
title: Advanced tutorial - Gaussian with HyperQueue
---

# Using HyperQueue for farming Gaussian jobs on Puhti

> This tutorial requires that

- you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
- your account belongs to a project [that has access to Puhti
  service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).
- your account belongs to the [Gaussian users group](https://docs.csc.fi/apps/gaussian/)

> This tutorial is done on Puhti

## Overview

💬 [HyperQueue](https://docs.csc.fi/apps/hyperqueue/) is a tool for efficient sub-node
task scheduling and well suited for farming and running embarrassingly parallel jobs.

💬 In this example, we have several similar molecular structures and would like to know
how they differ energetically

- The aim is to run Gaussian calculations on 10 different structural isomers corresponding
  to the C<sub>6</sub>H<sub>12</sub> molecular formula
- The computational cost of each of the 10 calculations is expected to be comparable

### The workflow of this exercise

- Download 10 sample 3D molecular structures
- Convert these structures to Gaussian format
- Construct the corresponding Gaussian input files
- Build a HyperQueue task list to run the jobs
- Submit the the HyperQueue job
- Detect and resubmit a failed job
- Analyze the results

## Download 10 sample 3D molecular structures

1. Create and enter a suitable scratch directory on Puhti (replace `<id>` with your CSC
   project number).

```bash
mkdir -p /scratch/project_<id>/$USER/gaussian_hq
cd /scratch/project_<id>/$USER/gaussian_hq
```

2. Download the 10 C<sub>6</sub>H<sub>12</sub> structures that have originally been obtained
   from [ChemSpider](https://www.chemspider.com/Search.aspx).
  
```bash
wget https://a3s.fi/C6H12_structures_10/C6H12_structures_10.tgz
```

3. Unpack the archive.

```bash
tar -xzf C6H12_structures_10.tgz
```

4. Go to the directory containing the structure files that are in [.mol
   format](https://openbabel.org/docs/dev/FileFormats/MDL_MOL_format.html).

```bash
cd C6H12_structures_10
```

## Convert these structures to Gaussian format

💬 [Gaussian](https://docs.csc.fi/apps/gaussian/) is a program for molecular electronic
structure calculations.

1. Use [OpenBabel](http://openbabel.org/wiki/Main_Page) to convert the structures to
   Gaussian format.

```bash
module load openbabel
obabel *.mol -ocom -m
```

2. Now we have converted the 10 structures into `.com` format that is used by Gaussian.

## Construct the corresponding Gaussian input files

💬 In this example we want to do do a `b3lyp/cc-pVDZ` calculation on these structures,
i.e. a hybrid density functional theory calculation using the B3LYP exchange-correlation
functional and the cc-PVDZ basis set.

1. Add the `b3lyp/cc-pVDZ` keyword at the beginning of each `.com` file.

```bash
sed -i '1s/^/#b3lyp\/cc-pVDZ \n/' *.com
```

2. Set 4 cores per job by adding the flag `%NProcShared=4` to each input file.

```bash
sed -i '1s/^/%NProcShared=4\n/' *.com
```

3. Now you have 10 complete Gaussian input files corresponding to the original molecular
   structures and the method of choice.

## Build a task list to run the jobs as a HyperQueue task array

💬 A task array can sometimes be lengthy so rather than typing it by hand it is more
feasible to use bash scripting to create a suitable task list file for HyperQueue. In this
case the task list used to specify the task array will just contain the paths to each input
file, so generating it is very simple.

1. Move back up to your main directory.

```bash
cd ..
```

2. Create the task list and name it `tasklist.txt`.

```bash
ls ${PWD}/C6H12_structures_10/*.com > tasklist.txt
```

3. Check out the tasklist with `more`, `less` or `cat`. The file should look like:

```bash
/scratch/project_<id>/$USER/gaussian_hq/C6H12_structures_10/10737.com
/scratch/project_<id>/$USER/gaussian_hq/C6H12_structures_10/10775.com
/scratch/project_<id>/$USER/gaussian_hq/C6H12_structures_10/10776.com
...and so on
```

### Run the HyperQueue task array

💬 Running a HyperQueue task array is similar to running a Slurm array job. However,
HyperQueue packs the individual tasks within a single Slurm job step and is thus much
more efficient, especially if there are a huge number of tasks.

1. Create a batch script `hq_array.sh` for initializing and running the HyperQueue job.

```bash
nano hq_array.sh
```

2. Copy the example script below into the file (edit `<id>` with your CSC project number).
   The inline comments attempt to explain what is going on in the file. For more details,
   please consult [our HyperQueue documentation](https://docs.csc.fi/apps/hyperqueue/).
   See also [the official documentation](https://it4innovations.github.io/hyperqueue/stable/).

```bash
#!/bin/bash
#SBATCH --partition=small
#SBATCH --account=project_<id>
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --time=00:05:00

export SLURM_EXACT=1

# Load the required HyperQueue and Gaussian modules
module load hyperqueue gaussian

# Set the directory where the HyperQueue server will run
export HQ_SERVER_DIR=$PWD/hq-server-$SLURM_JOB_ID
mkdir -p "$HQ_SERVER_DIR"

# Start the server and wait until it has started
echo "STARTING HQ SERVER, log in $HQ_SERVER_DIR/HQ.log"
echo "===================="
hq server start &>> "$HQ_SERVER_DIR/HQ.log" &
until hq job list &>/dev/null ; do sleep 1 ; done

# Start the HyperQueue workers (1 per node) and wait until they have started
echo "STARTING HQ WORKERS ON $SLURM_NNODES nodes"
echo "===================="
srun --cpu-bind=none --mpi=none hq worker start --cpus=$SLURM_CPUS_PER_TASK &>> "$HQ_SERVER_DIR/HQ.log" &

until [[ $num_up -eq $SLURM_NNODES ]]; do
    num_up=$(hq worker list 2>/dev/null | grep -c RUNNING)
    echo "WAITING FOR WORKERS TO START ( $num_up / $SLURM_NNODES )"
    sleep 1
done

# Submit the HyperQueue task array and wait until all jobs have finished
hq submit --cpus 4 --each-line tasklist.txt --stdout=none --stderr=none gaussian.sh

while hq job list --all | grep -q "RUNNING\|PENDING"; do
    echo "WAITING FOR JOBS TO FINISH"
    # Adjust the timing here if you get to much output in the Slurm log file
    # Now set to 30 seconds
    sleep 30
done

# Print a summary of the tasks and shut down the workers and server
hq task list 1 > task_summary.txt

echo "===================="
echo "DONE"
echo "===================="
echo "SHUTTING DOWN HYPERQUEUE"
echo "===================="
hq worker stop all
hq server stop
```

3. Close `nano` and save the file.

💬 The batch script above starts the HyperQueue server and worker(s) and submits the
task array with inputs read from the generated `tasklist.txt` file. The following
resources are requested:

- 40 cores, `--cpus-per-task=40`, i.e. 4 for each task (matching the specification in each
  Gaussian input file and the `hq submit --cpus 4` command)
- Computing time for five minutes, `--time=00:05:00`
- Computation on a single node `--nodes=1` using a single rank `--ntasks-per-node=1`
- Billing project `--account project_<id>` (replace `<id>` accordingly)

💬 By using the `hq submit --each-line` flag, each line from the `tasklist.txt` file
will be passed to a separate task, which can access the value of the line using the
environment variable `$HQ_ENTRY`. This environment variable is used in the submitted
`gaussian.sh` file wherein the actual Gaussian calculation is executed.

4. Create the `gaussian.sh` file.

```bash
nano gaussian.sh
```

5. Copy the script below into the file.

```bash
#!/bin/bash

input_base=$(basename ${HQ_ENTRY%%.*})
mkdir -p output/${input_base}

echo "ASSIGNED TASK ID ${HQ_TASK_ID} TO INPUT ${input_base}" > output/${input_base}/${input_base}.log
g16 < $HQ_ENTRY >> output/${input_base}/${input_base}.log
```

6. Close `nano` and save the file.

💬 The `gaussian.sh` script creates a directory to which the output of the corresponding
Gaussian calculation is directed. Moreover, before launching the actual calculation, each
log file is prepended with the HyperQueue task ID and the ID of the input file for bookkeeping.

7. Finally, submit the HyperQueue task array job.

```bash
sbatch hq_array.sh
```

## Check the HyperQueue task summary

1. Monitor the Slurm queue with (replace `<slurm jobid>` with the assigned Slurm job ID):

```bash
squeue -j <slurm jobid>
# or
squeue --me
# or
squeue -u $USER
```

2. When the HyperQueue job has finished, a summary of the status of each task is dumped into
   the file `task_summary.txt`. Check the contents of this file.

```bash
cat task_summary.txt
```

3. The final lines of the file should read:

```bash
|       9 | FAILED   | r17c04.bullx | Start: 18.10.2022 11:43:15 | Workdir: /scratch/project_2001659/rkronber/hyperqueue/gaussian | Error: Program terminated with exit code 1 |
|         |          |              | End: 18.10.2022 11:43:15   | Stdout: <None>                                                 |                                            |
|         |          |              | Makespan: 515ms            | Stderr: <None>                                                 |                                            |
+---------+----------+--------------+----------------------------+----------------------------------------------------------------+--------------------------------------------+
```

4. This indicates that the calculation with ID 9 failed for some reason! Check which input
   this corresponds to.
  
```bash
grep "ID 9" output/*/*
```

5. The output should reveal that the failed task ID 9 is associated with job 7787. Check
   the log of the failed job with.

```bash
tail output/7787/7787.log
```

6. The output should look like:

```text
Charge and Multiplicity card seems defective:
Wanted an integer as input.
                                                                                
?
Error termination via Lnk1e in /appl/soft/chem/gaussian/G16RevC.02/g16/l101.exe at Wed Oct 19 08:50:48 2022.
Job cpu time:       0 days  0 hours  0 minutes  0.1 seconds.
Elapsed time:       0 days  0 hours  0 minutes  0.2 seconds.
File lengths (MBytes):  RWF=      6 Int=      0 D2E=      0 Chk=      1 Scr=      1
```

## Fix and resubmit a failed job

1.  Check out the defective input file plus another input file for reference.

```bash
cat C6H12_structures_10/7*.com
```

2. The result shows two input files one after another. You should be able to spot
   what is missing from the defective input file.

3. Correct the defective file by inserting the missing title "7787" at line 6.

```bash
sed -i "6s/^/7787/" C6H12_structures_10/7787.com
```

4. Rerun the job. You do not need HyperQueue as it is just a single job.

```bash
module load gaussian
srun -p interactive --ntasks=1 --cpus-per-task=4 --time=00:05:00 -A project_<id> g16 < C6H12_structures_10/7787.com > output/7787/7787.log
```

5. Once the job has finished ensure that it terminated normally.

```bash
tail output/7787/7787.log
```

6. Print a list of the `b3lyp/cc-pVDZ` energies for each of the 10 structures.

```bash
grep -rnw 'output/' -e 'E(RB3LYP)'
```

7. The output should look like:

```bash
output/12446/12446.log:265: SCF Done:  E(RB3LYP) =  -235.836869989     A.U. after   13 cycles
output/10737/10737.log:265: SCF Done:  E(RB3LYP) =  -235.826753630     A.U. after   13 cycles
output/10776/10776.log:246: SCF Done:  E(RB3LYP) =  -235.851091573     A.U. after   12 cycles
output/10775/10775.log:246: SCF Done:  E(RB3LYP) =  -235.835303716     A.U. after   12 cycles
output/11742/11742.log:246: SCF Done:  E(RB3LYP) =  -235.845122585     A.U. after   13 cycles
output/7024/7024.log:246: SCF Done:  E(RB3LYP) =  -235.875921299     A.U. after   11 cycles
output/553629/553629.log:262: SCF Done:  E(RB3LYP) =  -235.838082463     A.U. after   11 cycles
output/12201/12201.log:246: SCF Done:  E(RB3LYP) =  -235.823223660     A.U. after   13 cycles
output/7787/7787.log:246: SCF Done:  E(RB3LYP) =  -235.882771348     A.U. after   10 cycles
output/11109/11109.log:265: SCF Done:  E(RB3LYP) =  -235.823585171     A.U. after   12 cycles
```
