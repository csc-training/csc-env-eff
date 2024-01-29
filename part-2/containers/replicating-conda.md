---
layout: default
title: Replicating a Conda environment
parent: 9. Containers and Apptainer
grand_parent: Part 2
nav_order: 5
has_children: false
has_toc: false
permalink: /hands-on/singularity/singularity_extra_replicating-conda.html
---

# Replicating a Conda environment in a container

This is an extra exercise which can not be run on Puhti. You will need access to a computer or virtual machine where you have root privileges and that has Apptainer installed.

On Puhti, you can use [Tykky](https://docs.csc.fi/computing/containers/tykky/) to easily containerize Conda environments. This method is recommended over the manual procedure detailed in this exercise, which is mainly provided for you to develop your skills in working with containers. For tutorials on using Tykky, see:

- [Containerizing a Conda environment with Tykky](https://csc-training.github.io/csc-env-eff/hands-on/installing/installing_hands-on_python.html#example-containerizing-a-conda-environment-with-tykky)
- [Installing packages from Bioconda using Tykky](https://csc-training.github.io/csc-env-eff/hands-on/modules/module-exercise-with-aligners.html#extra-installing-packages-from-bioconda)

## Conda

Conda is a useful tool for installing software with complex dependencies. It has, however, some problems, especially on HPC systems like Puhti with shared parallel file systems. Because of these issues, installing Conda environments directly on the file system of CSC supercomputers is not allowed (see [usage policy](https://docs.csc.fi/computing/usage-policy/#conda-installations)).

The main problems of Conda environments are related to storage. Conda environments are quite large, containing tens to hundreds of thousands of files. Just 3-4 environments are enough to fill the basic quota of a project's `/projappl` directory. Moreover, many of these files will be accessed each time you launch a program installed with Conda, generating massive I/O load which may degrade the performance of the system for all users.

Conda environments can also be somewhat sensitive to changes in the base system, meaning that, e.g., updates on Puhti can sometimes break existing Conda environments, necessitating a re-install.

Using an Apptainer container can help with both problems. A container is just a single file that is typically smaller than the total size of the Conda environment directory. It is also less sensitive to changes in the host system.

It is relatively easy to containerize an existing Conda environment.

## Check for ready containers

You should first check if the software package is already available as an Apptainer/Singularity or Docker container. The advantage of a ready-made container is that it can usually be pulled/converted with normal user privileges on Puhti.

You can find more detailed instructions on converting Docker containers in [Docs CSC](https://docs.csc.fi/computing/containers/creating/#converting-a-docker-container).

## Replicating an existing Conda environment

If you have an existing Conda environment, you can save the `environment.yml` file and use it to replicate the environment in a container.

Please note that the `environment.yml` file will only reflect changes to the environment made using `conda` commands. If you have made any changes directly, you will need to replicate those changes in the definition file.

Make sure the environment you want to replicate is activated, and give the command:

```bash
conda env export > environment.yml
```

You can try with one of your own environments, or download an example to use for this exercise:

```bash
wget https://raw.githubusercontent.com/CSCfi/csc-env-eff/master/data/environment.yml
```

In addition to the `environment.yml` file, you will need an Apptainer definition file. Create a file called `conda_environment.def` with the following content (copy/paste).

```text
Bootstrap: docker

From: continuumio/miniconda3

%files
    environment.yml

%environment

%post
    ENV_NAME=$(head -1 environment.yml | cut -d' ' -f2)
    echo ". /opt/conda/etc/profile.d/conda.sh" >> $APPTAINER_ENVIRONMENT
    echo "conda activate $ENV_NAME" >> $APPTAINER_ENVIRONMENT

    . /opt/conda/etc/profile.d/conda.sh
    conda env create -f environment.yml -p /opt/conda/envs/$ENV_NAME
    conda clean --all

%runscript
    exec "$@"
```

Make sure the files `environment.yml` and `conda_environment.def` are in the current directory and give the command:

```bash
sudo apptainer build fastx.sif conda_environment.def
```

This will build an Apptainer image file called `fastx.sif`. We can now verify that it works:

```bash
apptainer exec fastx.sif fastq_to_fasta -h
```

The image file could now be transferred to and used on Puhti.

## Comparison of installation methods

This particular environment was chosen because it is a good "bad example" of the effects different installation methods can have.

The software package is a collection of applications written in C++ with only a few dependencies. Usually, similar packages are best installed natively. In this case, however, the code is quite old, and it will not compile with modern versions of `gcc` without some changes to the source code.

The software is available in the Bioconda repository, so it can also be installed with:

```bash
conda install fastx_toolkit
```

- Good: Can be done with user privileges
- Bad: Using this method, you will end up with a directory with a total size of about 1 GB and over 26000 files. The default file number limit for `/projappl` is 100000 files, so this single installation would already use more than 25 % of that.

Containerizing the Conda environment like we did in this exercise is better:

- Good: We ended up with a single 465 MB file. The default capacity limit of `/projappl` is 50 GB, so this installation would only use less than 1 % of the quota.
- Good: Although containerization as outlined above cannot be done directly on Puhti, you can use Tykky to circumvent the need for root privileges (see the tutorials linked at the top).

In this case there's also another good option – converting a ready-made Docker container:

```bash
apptainer build fastx.sif docker://biocontainers/fastx-toolkit:v0.0.14-6-deb_cv1
```

- Good: This can be done with user-level rights also on Puhti and you'll end up with a single 61 MB file.
- Bad: Finding a ready, working container may take some time.

Containers are not a "silver bullet" solution to all installation problems, but they are nonetheless a much more favorable alternative to direct Conda installations on HPC systems.
