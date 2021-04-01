---
topic: disk-areas
title: Tutorial - Disk areas in CSC supercomputing environment
---

# Disk areas in CSC supercomputing environment

CSC users working in a supercomputing environment have access to different disk areas (or directories) to manage their data in supercomputers. It is therefore important to understand his or her own disk areas to manage personal and project-specific data.

Upon completion of this tutorial, you will get familiar with:
- Personal and project-specific disk areas and their quotas in CSC supercomputing environment
- Ideal disk areas for large I/O operations

## Identify your personal and project-specific directories in Puhti and Mahti supercomputers

Each user at CSC supercomputer (Puhti or Mahti) owns disk areas (or directories), each one with a specific purpose. You can get an overview of directories by using the following command in login node:

```bash
csc-workspaces 
```
The above command shows information about your directories and their current quotas. These directories can be briefly summerised as below:

- User-specific directory: It is your home directory ($HOME) and is also the default directory when you login to Puhti/Mahti. You can store configuration files and other minor personal data. 

- Project-specific directories: These are *scratch* and *projappl* directories. Each project contains its scratch disk space where actual data analysis tasks are performed. Scratch area is a temporary space. *Projappl* directory on the other hand is mainly for storing and sharing compiled applications and libraries etc. with other members of the project. 


## Perform a light-weight pre-porcessing on data files using fast I/O local disks

We sometimes come across situations where we have to handle an uncommonly large number of smaller files that can cause heavy I/O load on supercomputing environment. In order to facilitate such operations, CSC provides fast local disk areas in login and compute nodes.

In order to identify such directories in login nodes, use the following command:

```bash
echo $TMPDIR
```
This local disk area in login nodes is meant for some light-weight preprocessing of data before you start actual analysis on scratch drive. Let's look at the below  toy example where you can download a tar file containing thousands of small files and then you can  merge all of those files into one big file using local storage disks.

1. Download tar file from *allas* object storage as shown below:

```bash 
cd $TMPDIR           
wget https://a3s.fi/CSC_training/Individual_files.tar.gz
```
2. Unpack the downloaded tar file as below:

```
tar -xavf Individual_files.tar.gz
cd Individual_files
```
3. Merge all those small files into one file and remove all small files

```
find . -name 'individual.fasta*' | xargs cat  >> Merged.fasta
find . -name 'individual.fasta*' | xargs rm
```

However, if you are going to perform heavy-weight computing tasks on those larger number of smaller files, you have to use local storage areas in compute nodes which are accessed either [interactively](https://docs.csc.fi/computing/running/interactive-usage/) or using [batch jobs](https://docs.csc.fi/computing/running/creating-job-scripts-puhti).

In the interactive jobs, use the following command to find out a local storage area in that compute node:

```bash
echo $LOCAL_SCRATCH 
```
When using batch job, use the environment variable $LOCAL_SCRATCH in your [batch job scripts](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage) to access the local storage on that node.

## Move your pre-proceessed data to a project-specific scratch area before analysis

Currently, all directories on scratch drive are project-based and one should be aware of a project number to find out actual path on scratch directory. While we can actually find *scratch* directories corresponding to all your project numbers using `csc-workspace`, it may not be immediately obvious to map those project numbers to metadata of your projects. You can instead also use the following command to find more details on your project(s).

```bash
csc-projects
```

Once you know the project number which would be in the form of project_xxx, you can move your pre-processed data (i.e., Merged.fasta file) from earlier step to a project-specific directory on scratch area as below:

```bash
mkdir /scratch/project_xxx/$USER
mv Merged.fasta /scratch/project_xxx/$USER
```
You have now successfully moved your data to scratch area and can start performing actual analysis using batch job scripts which you will learn in-depth in a different module.

