---
topic: singularity
title: Exercise - Replicating a Conda environment
---

# Extra exercise: Replicating a Conda environment in a container

This is an extra exercise. It can not be run in Puhti. You will need  access
to a computer or a virtual machine where you have sudo rights and that has
Singularity 3.x installed.

## Conda
Conda is a useful tool for installing software with complex dependencies. 
It has, however, some problems, especially on systems like Puhti. 

The main problems are related to storage: Conda environments can be quite large,
and they can have tens of thousands of files. Just 3-4 environments are enough to fill
the basic quota of a project's /projapp directory.

Conda environments can also be somewhat sensitive to changes in the base system, 
meaning that, e.g., updates in Puhti can sometimes break Conda environments, 
necessitating a re-install.

Using an Apptainer container instead can help with both problems: 
a container is just a single file that is typically smaller than the total size
of the Conda environment directory. It is also less sensitive to changes in the
host system.

It is relatively easy to replicate an existing Conda environment inside a container.

## Check for ready containers

You should check first if the software package is already avaliable as a Singularity/Apptainer
or a Docker container. 

The advantage of a ready container is that it can be usually pulled/converted with
normal user rights in Puhti.

You can find more detailed instructions for converting Docker images in Docs CSC: 
[Running existing containers](https://docs.csc.fi/computing/containers/run-existing/)

## Replicating existing Conda environment

If you have an existing Conda environment, you can save `environment.yml` file and
use it to replicate the environment in the container.

Please note that the `environment.yml` file will only reflect changes to environment
made using conda commands. If you have made any changes directly, you will need to replicate
those changes in the definition file.

Make sure the environment you want to replicate is activated, and give command:
```bash
conda env export > environment.yml
```
You can try with one of your own environments, or download an example to use for
this exercise:
```bash
wget https://raw.githubusercontent.com/CSCfi/csc-env-eff/master/data/environment.yml
```
In addition to the `environmet.yml` file, you will need an Apptainer definition file.

Create a file called `conda_environment.def` with following content (you can copy-paste).
```text
Bootstrap: docker

From: continuumio/miniconda3

%files
    environment.yml

%environment

%post
    ENV_NAME=$(head -1 environment.yml | cut -d' ' -f2)
    echo ". /opt/conda/etc/profile.d/conda.sh" >> $SINGULARITY_ENVIRONMENT
    echo "conda activate $ENV_NAME" >> $SINGULARITY_ENVIRONMENT

    . /opt/conda/etc/profile.d/conda.sh
    conda env create -f environment.yml -p /opt/conda/envs/$ENV_NAME
    conda clean --all

%runscript
    exec "$@"
```
Make sure files `environment.yml` and `conda_environment.def` are in the
current directory and give command:

```bash
sudo apptainer build fastx.sif conda_environment.def
```
This will build an Apptainer image file called `fastx.sif`. 

We can test now that it works:
```bash
apptainer exec fastx.sif fastq_to_fasta -h
```
The image file could now be transferred and used in Puhti.

## Comparision of installation methods

This particular environment was chosen because it is a good "bad example" on
what effect different installation methods can have.

The software package is a collection of applications written in C++ with 
only a few dependencies. Usually similar packages are best installed natively. 
In this case, however, the code is quite old, and it will not compile with modern 
versions of gcc without some changes to the source code.

It is available in Bioconda repository, so it can be installed by:
```bash
conda install fastx_toolkit
```
- Good: Can be done with user rights
- Bad: Using this method, you will end up with a directory with a total size of 990 MB 
and over 26000 files. The default file number limit for /projappl is 10000 files, 
so this single installation already used 25% of that.

Replicating the Conda environment as a container like we did in this exercise is already 
better.
- Good: We ended up with a single 813 MB file. The default total file size limit for 
/projapp is 50 GB, so this installation only used 1,6%.
- Bad: Can not be done directly in Puhti

In this case there would even better option: Building from a ready container:
```bash
apptainer build fastx.sif docker://biocontainers/fastx-toolkit:v0.0.14-6-deb_cv1
```
- Good: This can be done with user right in Puhti and you end up with a single 61 MB file.
- Bad: Finding a ready, working container may take some time.

Containers are not a "silver bullet" solution to all installation problems, but they can
be in many cases a preferable alternative for conda.

