---
layout: default
title: Biosoftware in Puhti
parent: 4. Module system
grand_parent: Part 1
nav_order: 2
permalink: /hands-on/modules/module-exercise-with-aligners.html
---

# Biosoftware in Puhti

> In this tutorial you will learn:
- About the `biokit` module
- How to search for applications
- How to install Bioconda packages

💬 Let's imagine that we have some sequencing data that we wish to align to a reference genome and check the quality of the alignment.

## Looking for applications and related modules

1. See the [list of applications in Docs CSC](https://docs.csc.fi/apps/) and look for suitable aligners.
   - Can you find for example TopHat, STAR, Bowtie and BWA aligners in the list?
   - Which modules are needed to run these applications?  

💡 The *biokit module* loads a set of commonly used bioinformatics tools.

{:style="counter-reset:step-counter 1"}
2. Let's check if the HISAT2 aligner is also available:

```bash
module spider hisat2
```

☝🏻 All software installed on CSC's supercomputers don't necessarily have their own documentation page in the application list (yet). They might be new installations or installed by request of a single research group etc.

{:style="counter-reset:step-counter 2"}
3. Load the `biokit` module and see what is included:

```bash
module load biokit
module list
```

- Was HISAT2 also available in the `biokit` module?

## RSeQC

💬 Let's imagine you just did a successful aligning of the sequence data.

- After aligning, you might want to check the quality of the alignment with the RSeQC tool.

💬 As you can see from the `module list` command above, the RSeQC tool is not included in the `biokit` module.

1. Try searching for the RSeQC tool by using the `module spider` command:

```bash
module spider rseqc
```

{:style="counter-reset:step-counter 1"}
2. Load the module and try to run one of the RSeQC commands (open the help for [`bam_stat.py`](http://rseqc.sourceforge.net/#bam-stat-py)):

```bash
bam_stat.py -h
```

## Extra: Installing packages from Bioconda

Bioconda is a popular Conda channel for bioinformatics software. It provides an easy method to install thousands of software packages related to biomedical research. Conda environments are, however, problematic on supercomputers with parallel file systems since they create too many files. The solution is to use containerized environments.

☝🏻 Installing software and containers will be discussed more in sections [8](https://csc-training.github.io/csc-env-eff/part-2/installing/) and [9](https://csc-training.github.io/csc-env-eff/part-2/containers/). Feel free to return to this tutorial later.

1. Look for the MetaBAT2 application like we did above with RSeQC:

```bash
module spider metabat2
```

{:style="counter-reset:step-counter 1"}
2. Check whether MetaBAT2 is available in [Bioconda](http://bioconda.github.io) (type metabat2 in the search field):
3. All packages in Bioconda have a ready-made Docker container image available. While those images could be pulled and used directly, CSC's [Tykky container wrapper](https://docs.csc.fi/computing/containers/tykky/) provides an easy method to install them so that they are usable without any special container commands.
4. On the [Bioconda page](http://bioconda.github.io/recipes/metabat2/README.html) find the command to use Docker (don't run it). In this case:

```bash
docker pull quay.io/biocontainers/metabat2:<tag>
```

{:style="counter-reset:step-counter 4"}
5. From the command we need the Docker address:

```bash
quay.io/biocontainers/metabat2
```

{:style="counter-reset:step-counter 5"}
6. And from the [tags page](https://quay.io/repository/biocontainers/metabat2?tab=tags) the desired version. In this case we choose the latest (secure) version:

```bash
2.15--h986a166_1
```

{:style="counter-reset:step-counter 6"}
7. Combine the address and tag to form the Docker URL:

```bash
docker://quay.io/biocontainers/metabat2:2.15--h986a166_1
```

{:style="counter-reset:step-counter 7"}
8. Clean your environment and load the Tykky container wrapper

```bash
module purge
module load tykky
```

{:style="counter-reset:step-counter 8"}
9. Create a directory for the installation under your project's `/projappl` directory:

```bash
mkdir -p /projappl/<project>/$USER/metabat-2.15    # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 9"}
10. Wrap the container with:

```bash
wrap-container -w /usr/local/bin docker://quay.io/biocontainers/metabat2:2.15--h986a166_1 --prefix /projappl/<project>/$USER/metabat-2.15    # replace <project> with your CSC project, e.g. project_2001234
```

☝🏻 The `-w` option specifies the installation directory *inside the container*. For containers from Bioconda this is always `/usr/local/bin`.

☝🏻 The `--prefix` option is used to indicate the directory where we want to install the software.

💡 After the installations finishes, the executables of the program will be in the directory `metabat-2.15/bin`. Note that these are not the actual binaries, but rather wrapper scripts for the executables *inside the container*. You can, however, use them as if they were the actual commands.

{:style="counter-reset:step-counter 10"}
11. Add the `bin` directory to your `$PATH` as suggested by Tykky. This is analogous to activating the Conda environment in case of a direct Conda installation and allows you to execute commands from anywhere (without providing the full path to the binaries):

```bash
export PATH="/projappl/<project>/$USER/metabat-2.15/bin:$PATH"    # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 11"}
12. Try opening the help for the `metabat` command:

```bash
metabat --help
```

🗯 See here [how to install containers from other sources such as the BioContainer registry or local image files](https://docs.csc.fi/support/tutorials/bioconda-tutorial/#containers-from-other-source).

## More information

### Using modules in a batch script

💬 Make sure to load all necessary modules and export required paths also in your batch scripts before launching any actual commands. It is good practice to start with `module purge` to ensure that you are working in a clean environment.

☝🏻 Note that if you are writing a batch script that uses applications from different modules, you should be mindful of the order in which you load (and possibly unload) the modules. Loading one module might automatically replace other ones to avoid conflicts.
