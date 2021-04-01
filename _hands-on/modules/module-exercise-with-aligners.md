---
topic: modules
title: Exercise - module-with-aligners
---

# Biosoftwares in Puhti

This exercise requires that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
and it is a member of a project that [has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/). 

You will learn:
- About the biokit module
- How to look for applications
- About the bioconda environment

Let's imagine that we have some sequencing data that we wish to align to a reference genome, and check the quality of the alignment. 

## Looking for applications and related modules

1. Let's see the [list of applications](https://docs.csc.fi/apps/) and look for suitable aligners. Can you find for example TopHat, STAR, Bowtie and BWA aligners in the list? Which module is needed to run these applications?

The *biokit module* sets up a set of commonly used bioinformatics tools. 

2. All softwares installed in CSCs super computers don't necessarily have their own manual page in the application list (yet): they might be new installations, or installed from request of a single research group etc. Let's check if HISAT2 aligner is also available:

```bash
module spider hisat
```
Is there some version of HISAT2 also available?

3. Let's load the biokit module and see what is included.
```bash
module load biokit
module list
```
Was HISAT2 available in the biokit?

## Bioconda environment

4. After aligning, we might want to check the quality of the alignment with RSeQC tool. As we can see from the `module list` command above, it was not included in the biokit. Like we learned, you can try to look for it from the application manual page and by using the `module spider rseqc`. 

No luck? What next? Let's take a look at the bioconda environment.

Some applications are installed and used as Conda environments in Puhti. You can use [CSC's bioconda environment](https://docs.csc.fi/apps/bioconda/) also to easily install tools from [Bioconda repository](http://bioconda.github.io).

Let's check what is available with spider again, and load one of the modules:
```bash
module spider bioconda
module load bioconda/3
```
Take a look at the message you get. Note, that some dependency modules were re-loaded in the background. It also says that we first need to set the PROJAPPL environment variable.
To do so, run command (you can check the name/number of your project(s) with command `csc-workspaces`):
```bash
export PROJAPPL=/projappl/project_XXXXXXX
```
Re-run the ```module load``` command and then check which applications are available in this bioconda environment:
```bash
module load bioconda/3
conda env list
```
See RSeQc there? 

## Using modules in a batch script

5. When we loaded the bioconda module, some dependency modules were loaded in the background. This means, that the environment changed, and the softwares that were previously loaded might not be available anymore. Note, that if you are writing a batch script that uses applications from different modules, you want to be careful that you load and unload the modules at the right time!
