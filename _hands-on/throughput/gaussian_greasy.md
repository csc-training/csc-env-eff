---
topic: throughput
title: Exercise - Gaussian GREASY
---

# Using GREASY for running multiple Gaussian jobs on Puhti

This tutorial requires that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
and that your account belongs to a project [that has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/). You should also belong to the [Gaussian users group](https://docs.csc.fi/apps/gaussian/)
## Overview

- As an example, we have several similar molecular structures and would like to know how they are energetically related to each other   
- The aim is to run Gaussian calculations on 10 different isomers corresponding to the C<sub>6</sub>H<sub>12</sub> molecular formula 
- The computational effort of each of the 10 calculations is expected to be comparable
- Here we are using the [GREASY](https://docs.csc.fi/computing/running/greasy/) metascheduler to orchestrate the jobs
- This tutorial is done on Puhti 

## The workflow of this exercise is:
 - Download 10 sample 3D molecular structures
 - Convert these structures to Gaussian format
 - Construct the corresponding Gaussian input files
 - Build  a  GREASY tasklist to run the jobs
 - Submit the the GREASY job
 - Resubmit a failed job
 - Analyse the results 

### Download 10 sample 3D molecular structures

- Create and enter a suitable scratch directory on Puhti (replace **`yourprojectname`** with the actual project name )

```text
mkdir -p /scratch/yourprojectname/gaussian_greasy
cd /scratch/yourprojectname/gaussian_greasy 
```
- Download the 10 C<sub>6</sub>H<sub>12</sub> structures that have originally been obtained from [ChemSpider](https://www.chemspider.com/Search.aspx) 

`wget https://a3s.fi/C6H12_structures_10/C6H12_structures_10.tgz`
- Unpack the archive 

`tar xzf C6H12_structures_10.tgz`
- Go to the directory containing the structure files that are in [mol format](https://openbabel.org/docs/dev/FileFormats/MDL_MOL_format.html)

`cd C6H12_structures_10`

### Convert these structures to Gaussian format
- Use [OpenBabel](http://openbabel.org/wiki/Main_Page) to convert the structures to gaussian format

```text
module load openbabel
obabel *.mol -ocom -m
```
- Now we have converted the 10 structures into `com` format that is used by gaussian 

### Construct the corresponding Gaussian input files
- We want to do do a `b3lyp/cc-pVDZ` calculation on these structures, so we add this keyword at the beginning of all the com files

`for i in *.com; do sed -i '1s/^/#b3lyp\/cc-pVDZ \n/' $i; done`
- We also want to use 4 cores per job so we want to add the flag `%NProcShared=4` to the input files

`for i in *.com; do sed -i '1s/^/%NProcShared=4\n/' $i; done`

- Now we have 10 complete Gaussian input files corresponding to the original molecular structures and the method of choise 
   
### Build a GREASY tasklist to run the jobs
Here we write a Bash script that will create a suitable tasklist file for GREASY  
- Move back up to the main directory

 `cd ..`
  
First we write a Bash script that will create a tasklist that can be processed by greasy.

```text
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
- Copy the script above into a file named `generate_tasklist.bash` and run it:

`bash ./generate_tasklist.bash`

After running the script you should have a tasklist file `greasy_10.tasklist` that contains  
the Gaussian executing commands for the 10 com files on separate lines, like  

```bash
g16 < /scratch/yourprojectname/gaussian_greasy/C6H12_structures_10/10737.com > output/10737/10737.log
g16 < /scratch/yourprojectname/gaussian_greasy/C6H12_structures_10/10775.com > output/10775/10775.log
g16 < /scratch/yourprojectname/gaussian_greasy/C6H12_structures_10/10776.com > output/10776/10776.log
g16 < /scratch/yourprojectname/gaussian_greasy/C6H12_structures_10/11109.com > output/11109/11109.log
...
```
### Submit the GREASY tasklist

- Load the required GREASY and Gaussian modules

`module load greasy gaussian`
- Use the tool `sbatch-greasy` to start the the 10 Gaussian jobs
- Based on the previous job setup, reserve for each job 4 cores **`--cores 4`**, for two minutes **`--time 02:00`**, from a single node **`--nodes 1`**
- Declare the billing project **`--account yourprojectname`**, (replace **`yourprojectname`** with the actual project)
- Submit the GREASY job using the newly generated GREASY tasklist `greasy_10.tasklist` and the resource requests above  

```text
sbatch-greasy --cores 4 --time 02:00 --nodes 1 --account yourprojectname greasy_10.tasklist
```
- A successful submission should report something like:

```text
sbatch-greasy --cores 4 --time 02:00 --nodes 1 --account yourprojectname greasy_10.tasklist

Task list "greasy_10.tasklist" includes 10 tasks.
The first two rows of the task list are:

g16 < /scratch/yourprojectname/gaussian_greasy/C6H12_structures_10/10737.com > output/10737/10737.log
g16 < /scratch/yourprojectname/gaussian_greasy/C6H12_structures_10/10775.com > output/10775/10775.log

-------------------------------------------------------------------------
Submitting GREASY job consisting of 10 tasks to 1 nodes.
The job will run 10 tasks at the time each using 4 cores.
The maximum runtime reseved to process all the tasks is 0 h 5 m.

Job submitted with ID 5162452

You can monitor the progress of the task with command:
  squeue -j 5162452

Once the job has started you can monitor the progress of the job with command:
 tail -f greasy-5162452.log
``` 

## Check the GREASY tasklist results

- When the GREASY job has finished you can quickly check the summary using the command:

```text
grep Summary greasy-*.log
INFO: Summary of 10 tasks: 9 OK, 1 FAILED, 0 CANCELLED, 0 INVALID.
```
- This tells that 9 of the 10 Gaussian jobs succeeded, but one failed due to some reason
- GREASY creates a restart file based on failed jobs, in our case the file is named **`greasy_10.tasklist-undefined.rst`**
- The command `cat greasy_10.tasklist-undefined.rst` shows:
```text
# Greasy restart file generated at 2021-03-09 20:10:27
# Original task file: /scratch/yourprojectname/gaussian_greasy/greasy_10.tasklist
# Log file: /scratch/yourprojectname/gaussian_greasy/greasy-5162452.log
# 
# Warning: Task 10 failed
g16 < /scratch/yourprojectname/gaussian_greasy/C6H12_structures_10/7787.com > output/7787/7787.log
# End of restart file
```
- The error report shows that the job `7787.com` has failed
- Check the output of the failed job with `tail output/7787/7787.log`

```text

Charge and Multiplicity card seems defective:
 Wanted an integer as input.
                                                                                 
 ?
 Error termination via Lnk1e in /appl/soft/chem/gaussian/G16RevC.01_new/g16/l101.exe at Tue Mar  9 20:10:15 2021.
 Job cpu time:       0 days  0 hours  0 minutes  0.8 seconds.
 Elapsed time:       0 days  0 hours  0 minutes  0.2 seconds.
 File lengths (MBytes):  RWF=      6 Int=      0 D2E=      0 Chk=      1 Scr=      1
```
- The error message pointing to the input of job 7787, turns out to be a missing title at line 6
- We correct it by inserting the missing title "7787" at row 6 
```text
sed -i "6s/^/7787/" C6H12_structures_10/7787.com
```
- Restart the job 

```text
sbatch-greasy --cores 4 --time 02:00 --nodes 1 --account yourprojectname greasy_10.tasklist-undefined.rst
```
- When the GREASY job has finished check that the previously failed job has finnished

```text
grep Summary greasy-*.log
INFO: Summary of 1 tasks: 1 OK, 0 FAILED, 0 CANCELLED, 0 INVALID.
```
- You can print a list of the `b3lyp/cc-pVDZ` energies for the 10 structures

```text
grep -rnw 'output/' -e 'E(RB3LYP)'
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


