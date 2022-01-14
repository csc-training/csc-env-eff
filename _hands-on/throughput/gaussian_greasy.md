---
topic: throughput
title: Advanced tutorial - Gaussian with GREASY
---

# Using GREASY for running multiple Gaussian jobs on Puhti

> This tutorial requires that 
- you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
- your account belongs to a project [that has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/). - your account belongs to the [Gaussian users group](https://docs.csc.fi/apps/gaussian/)

> This tutorial is done on Puhti 

## Overview

💬 [GREASY](https://docs.csc.fi/computing/running/greasy/) metascheduler is a tool for task/job farming and running "embarrassingly parallel" jobs. 

💬 As an example, we have several similar molecular structures and would like to know how they are energetically related to each other   
- The aim is to run Gaussian calculations on 10 different isomers corresponding to the C<sub>6</sub>H<sub>12</sub> molecular formula 
- The computational effort of each of the 10 calculations is expected to be comparable


### The workflow of this exercise is:
 - Download 10 sample 3D molecular structures
 - Convert these structures to Gaussian format
 - Construct the corresponding Gaussian input files
 - Build a GREASY tasklist to run the jobs
 - Submit the the GREASY job
 - Resubmit a failed job
 - Analyse the results 

## Download 10 sample 3D molecular structures

1. Create and enter a suitable scratch directory on Puhti 
    ```bash
    mkdir -p /scratch/project_xxxx/yourcscusername/gaussian_greasy    # replace xxxx to match the project name and yourcscusername to match – well – your user name...
    cd /scratch/project_xxxx/gaussian_greasy 
    ```
2. Download the 10 C<sub>6</sub>H<sub>12</sub> structures that have originally been obtained from [ChemSpider](https://www.chemspider.com/Search.aspx) 
    ```bash
    wget https://a3s.fi/C6H12_structures_10/C6H12_structures_10.tgz
    ```
3. Unpack the archive 
    ```bash
    tar -xzf C6H12_structures_10.tgz
    ```
4. Go to the directory containing the structure files that are in [mol format](https://openbabel.org/docs/dev/FileFormats/MDL_MOL_format.html)
    ```bash
    cd C6H12_structures_10
    ```

### Convert these structures to Gaussian format

💬 [Gaussian](https://docs.csc.fi/apps/gaussian/) is a program for molecular electronic structure calculations.

1. Use [OpenBabel](http://openbabel.org/wiki/Main_Page) to convert the structures to gaussian format:
    ```bash
    module load openbabel
    obabel *.mol -ocom -m
    ```
2. Now we have converted the 10 structures into `com` format that is used by gaussian 

### Construct the corresponding Gaussian input files

💬 In this example ee want to do do a `b3lyp/cc-pVDZ` calculation on these structures.

1. Add `b3lyp/cc-pVDZ` keyword at the beginning of all the com files:
    ```bash
    for i in *.com; do sed -i '1s/^/#b3lyp\/cc-pVDZ \n/' $i; done
    ```
2. Set 4 cores per job by adding the flag `%NProcShared=4` to the input files:
    ```bash
    for i in *.com; do sed -i '1s/^/%NProcShared=4\n/' $i; done
    ```
3. Now you have 10 complete Gaussian input files corresponding to the original molecular structures and the method of choice.
   
### Build a GREASY tasklist to run the jobs

💬 A tasklist can sometimes be lengthy so rather than typing the list by hand it is more feasible to use a Bash script that will create a suitable tasklist file for GREASY.

1. Move back up to your main directory:
    ```bash
    cd ..
    ```
2. Create a file `generate_tasklist.sh` 
    ```bash
    nano generate_tasklist.sh
    ```
3. Copy the script below into the file:
```bash
#!/bin/bash
#
submission_dir=$PWD                            # Directory from where the job is submitted    
com_dir=${submission_dir}/C6H12_structures_10  # Subdirectory containing the com files 
Ntasks=$(ls -l ${com_dir}/*.com|wc -l)         # Number of tasks equals the number of com-files
Ncores=4                                       # Number of threads per task 
rm -f greasy_"${Ntasks}".tasklist              # Remove possible old tasklist
for f in ${com_dir}/*.com;                     # Loop over all com files and create a separate
do                                             # output directory named after the input file name
input_base=`basename ${f%%.*}`
mkdir -p output/${input_base}
# Write all the Gaussian command lines into a common tasklist file 
echo "g16 < ${f} > output/${input_base}/${input_base}.log" >> greasy_"${Ntasks}".tasklist
done
```
4. Close `nano` and save the file.
5. Run the Bash script that creates a tasklist:
    ```bash
    bash ./generate_tasklist.sh
    ```
6. After the script is finished you should have a tasklist file `greasy_10.tasklist` that contains the Gaussian executing commands for the 10 `com` files on separate lines.
7. Check out the tasklist with `more`, `less` or `cat`. The file should look like:
    ```bash
    g16 < /scratch/project_xxxx/gaussian_greasy/C6H12_structures_10/10737.com > output/10737/10737.log
    g16 < /scratch/project_xxxx/gaussian_greasy/C6H12_structures_10/10775.com > output/10775/10775.log
    g16 < /scratch/project_xxxx/gaussian_greasy/C6H12_structures_10/10776.com > output/10776/10776.log
    g16 < /scratch/project_xxxx/gaussian_greasy/C6H12_structures_10/11109.com > output/11109/11109.log
    ...and stuff
    ```

### Submit the GREASY tasklist

💬 Submitting a GREASY tasklist is in a way equal to submitting a sbatch jobfile.

1. Load the required GREASY and Gaussian modules:
    ```bash
    module load greasy gaussian
    ```
2. Use the tool `sbatch-greasy` to start the the 10 Gaussian jobs:
    ```bash
    sbatch-greasy --cores 4 --time 02:00 --nodes 1 --account project_xxxx greasy_10.tasklist  # replace xxxx to match your project name
    ```

💬 The command submits the GREASY job using the newly generated GREASY tasklist `greasy_10.tasklist` and the following resource requests:
 - 4 cores **`--cores 4`** for each job (matches to the spesification in gaussian input files)
 - Computation time for two minutes **`--time 02:00`**
 - Computation on a single node **`--nodes 1`**
 - Billing project **`--account project_xxxx`** 
    - If you don't remember to replace **`project_xxxx`** with the actual project name the prompt asks you to choose one

{:start="3"}
3. A successful submission should report something like:
    ```bash
    Task list "greasy_10.tasklist" includes 10 tasks.
    The first two rows of the task list are:

    g16 < /scratch/project_xxxx/gaussian_greasy/C6H12_structures_10/10737.com > output/10737/10737.log
    g16 < /scratch/project_xxxx/gaussian_greasy/C6H12_structures_10/10775.com > output/10775/10775.log

    -------------------------------------------------------------------------
    Submitting GREASY job consisting of 10 tasks to 1 nodes.
    The job will run 10 tasks at the time each using 4 cores.
    The maximum runtime reseved to process all the tasks is 0 h 5 m.

    Job submitted with ID slurmjobid

    You can monitor the progress of the task with command:
    squeue -j slurmjobid

    Once the job has started you can monitor the progress of the job with command:
    tail -f greasy-slurmjobid.log
    ``` 

## Check the GREASY tasklist results

1. Monitor the queue with
    ```bash
    squeue -j slurmjobid    # replace slurmjobid with the job ID
    ```
    - Or:
        ```bash
        squeue --me
        ```
    - Or: 
        ```bash
        squeue -u $USER
        ```
2. When the GREASY job has finished you can quickly check the summary using the command:
    ```bash
    grep Summary greasy-*.log
    ```
3. The output should look like:
    ```bash
    INFO: Summary of 10 tasks: 9 OK, 1 FAILED, 0 CANCELLED, 0 INVALID.
    ```
    - This tells that 9 of the 10 Gaussian jobs succeeded, but one failed due to some reason
4. GREASY creates a restart file based on failed jobs, in our case the file is named **`greasy_10.tasklist-undefined.rst`**
5. Check out which jobs failed with the command:
    ```bash
    cat greasy_10.tasklist-undefined.rst
    ````
6. The output should look like:
    ```bash
    # Greasy restart file generated at 2021-03-09 20:10:27
    # Original task file: /scratch/project_xxxx/gaussian_greasy/greasy_10.tasklist
    # Log file: /scratch/project_xxxx/gaussian_greasy/greasy-5162452.log
    # 
    # Warning: Task 10 failed
    g16 < /scratch/project_xxxx/gaussian_greasy/C6H12_structures_10/7787.com > output/7787/7787.log
    # End of restart file
    ```
    - The error report shows that the job `7787.com` has failed!
7. Check the output of the failed job with:
    ```bash
    tail output/7787/7787.log
    ```
8. The output should look like:
    ```text
    Charge and Multiplicity card seems defective:
    Wanted an integer as input.
                                                                                 
    ?
    Error termination via Lnk1e in /appl/soft/chem/gaussian/G16RevC.01_new/g16/l101.exe at Tue Mar  9 20:10:15 2021.
    Job cpu time:       0 days  0 hours  0 minutes  0.8 seconds.
    Elapsed time:       0 days  0 hours  0 minutes  0.2 seconds.
    File lengths (MBytes):  RWF=      6 Int=      0 D2E=      0 Chk=      1 Scr=      1
    ```
    - The error message pointing to the input of job 7787
9. Check out the defective input file plus an other input file for reference:
    ```bash
    cat C6H12_structures_10/7*.com
    ````
10. The result shows two input files one after another. You should be able to spot what is missing from the defective input file.
11. Correct the defective file it by inserting the missing title "7787" at line 6:
```bash
sed -i "6s/^/7787/" C6H12_structures_10/7787.com
```
12. Restart the job with the restart file created by GREASY:
    ```bash
    sbatch-greasy --cores 4 --time 02:00 --nodes 1 --account project_xxxx greasy_10.tasklist-undefined.rst  # replace xxxx to match your project name
    ```
13. When the GREASY job has finished check that the previously failed job has successfully finished 
```bash
grep Summary greasy-*.log
```
14. Print a list of the `b3lyp/cc-pVDZ` energies for the 10 structures:
    ```bash
    grep -rnw 'output/' -e 'E(RB3LYP)'
    ```
15. The output should look like:
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


