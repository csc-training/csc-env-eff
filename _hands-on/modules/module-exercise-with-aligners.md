---
topic: modules
title: Advanced tutorial - Biosoftwares in Puhti
---

# Biosoftwares in Puhti

> In this tutorial you will learn:
- About the biokit module
- How to look for applications
- About the bioconda environment

💬 Let's imagine that we have some sequencing data that we wish to align to a reference genome, and check the quality of the alignment. 

## Looking for applications and related modules

1. See the [list of applications](https://docs.csc.fi/apps/) and look for suitable aligners. 
   - Can you find for example TopHat, STAR, Bowtie and BWA aligners in the list?
   - Which module is needed to run these applications?

💡 The *biokit module* sets up a set of commonly used bioinformatics tools. 

2. Let's check if HISAT2 aligner is also available:
```bash
module spider hisat
```
   - Is there some version of HISAT2 also available?

☝🏻 All softwares installed in CSCs super computers don't necessarily have their own manual page in the application list (yet): they might be new installations, or installed from request of a single research group etc. 

3. Load the biokit module and see what is included.
```bash
module load biokit
module list
```
   - Was HISAT2 available in the biokit?

## Bioconda environment

💬 Let's imagine you just did a successful aligning of the sequence data. 
   - After aligning, you might want to check the quality of the alignment with RSeQC tool. 

💬 As you can see from the `module list` command above, the RSeQC tool is not included in the biokit. 

1. Try to look for RSeQC tool from the application manual page and by using the `module spider`. 
```bash
module spider rseqc
```

💬 No luck? What next? Let's take a look at the bioconda environment.

☝🏻 Some applications are installed and used as Conda environments in Puhti. 
   - You can use [CSC's bioconda environment](https://docs.csc.fi/apps/bioconda/) also to easily install tools from [Bioconda repository](http://bioconda.github.io).

2. Check what bioconda versions are available with spider again, and load one of the modules:
```bash
module spider bioconda
module load bioconda/3
```
   - Take a look at the message you get. Note, that some dependency modules were re-loaded in the background. 
   - It also says that we first need to set the PROJAPPL environment variable.

3. Check the name/number of your project(s) with command `csc-workspaces`)

4. Set the PROJAPPL environment variable with command :
```bash
export PROJAPPL=/projappl/project_XXXX    # replace the XXXX
```

5. Re-run the ```module load``` command and then check which applications are available in this bioconda environment:
```bash
module load bioconda/3
conda env list
```
   - See RSeQc there? 

6. Try to run one of the RSeQC commands: open a help for [`bam_stat.py`](http://rseqc.sourceforge.net/#bam-stat-py).
```bash
bam_stat.py -h
```

7. Then activate the RSeQC environment, and try again. 
```bash
source activate rseqc
bam_stat.py -h
```

8. Finally deactivate the conda environment.
```bash
conda deactivate
```

## EXTRA: Install an application to your own bioconda environment

1. Look for [SeqKit application](https://bioinf.shenwei.me/seqkit/) like we did above with RSeQC:
```bash
module spider seqkit
```
2. Check whether SeqKit is available in [BioConda](http://bioconda.github.io): type rseqc in the search field.

3. Create a new Conda environment with SeqKit installed:
```bash
conda create -n my_biotools seqkit
```
4. Activate the environment:
```bash
conda activate my_biotools
```
5. Try running SeqKit help:
```bash
seqkit -h
```
6. Deactivate the Conda environment when you are finished:
```bash
conda deactivate
```

🗯 Here you can read [how to install an application for your own use with bioconda](https://docs.csc.fi/apps/bioconda/#2-installing-software-for-your-own-use-with-bioconda). 


## More information

### Using modules in a batch script

💬 When we loaded the bioconda module, some dependency modules were loaded in the background. This means, that the environment changed, and the softwares that were previously loaded might not be available anymore. 

☝🏻 Note, that if you are writing a batch script that uses applications from different modules, you want to be careful that you load and unload the modules at the right time!
