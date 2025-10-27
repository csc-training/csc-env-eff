---
layout: default
title: Installing a simple C code from source
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 4
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_hands-on_mcl.html
---

# Installing a simple C code from source

💬 In this tutorial we will install HMMER, a toolkit for biological sequence alignment and database 
homology search to the [`/projappl` directory](https://docs.csc.fi/computing/disk/) of the user on
Puhti.

💭 This software is also available as an installation package (`.deb`, `.rpm`)
for various Linux distributions, but these can not be used on Puhti. Instead,
we install it from the source code.

☝🏻 To follow the instructions, first set an environment variable pointing to
your project's `/projappl` directory:

```bash
export PROJAPPL=/projappl/<project>  # replace <project> with your CSC project, e.g. project_2001234
```

## Obtaining the source code

1. Create your own directory under `$PROJAPPL` (if not done already) and move
   there. Then, create and move to a new directory for the installation:

   ```bash
   mkdir -p $PROJAPPL/$USER
   cd $PROJAPPL/$USER
   mkdir hmmer
   cd hmmer
   ```

### Downloading a distribution package

1. Download the distribution package:

   ```bash
   wget http://eddylab.org/software/hmmer/hmmer.tar.gz
   ```

   💬 In this case the installation package is a tar-archive file that has been
   compressed with `gzip` program.

2. Unpack the file with the command:

   ```bash
   tar -xvf hmmer.tar.gz
   ```

   💬 After unpacking, the `ls` command shows that a new directory called
   `hmmer-3.4` has been created. This directory contains the actual
   installation files and documentation of the software.

### Alternative option: Get the software from GitHub

1. Clone source code from Github:

   ```bash
   module load git
   git clone https://github.com/EddyRivasLab/hmmer.git
   ```

   💬 After cloning, the `ls` command shows that a new directory called `hmmer`
   has been created. This directory contains the actual installation files and
   documentation of the software.

   For this software we also need to clone some additional dependencies.

    ```bash
    cd hmmer
    git clone https://github.com/EddyRivasLab/easel
    ```

## Preparing to install

1. Create a new directory called `version-3.4` under the `$PROJAPPL/$USER/hmmer` directory for
   the actual installation.

   ```bash
   mkdir version-3.4
   ```

2. Move to the `hmmer-3.4` (or `hmmer` if cloning from git) directory and study
   its contents:

   ```bash
   cd hmmer-3.4
   ls
   ```

   💬 Installation packages often contain short installation instructions.
   Typically, this instructions file is called `INSTALL` or `README`.

3. Read the `INSTALL` file to learn how the installation should be done.

   ```bash
   less INSTALL
   ```

   💡 Move in the file opened with `less` with up and down arrows, and exit
   with `q`.

## Installation

💬 Many open-source software tools are installed using the so-called
"configure-make" procedure following three steps:

1. Configuring a so-called `Makefile` with a `./configure` script.
2. Running the `make` command that compiles the source code according to the
   instructions in `Makefile`.
3. Installing the compiled executables with the command `make install`.

💭 Normally, installation packages assume that the user has the required
permissions to install the software to the locations where Linux binaries and
libraries normally get installed.

- However, at CSC this is not the case. You can install software only to your
  own (or your project's) disk areas.
- Often you can use the option `--prefix=<path>` to tell to the `configure`
  script where the program should be installed (replacing `<path>` with the
  actual path).

💭 The `./configure` script checks that all compilers and libraries that the
software needs are available.

- It is not uncommon that `./configure` reports about missing libraries or
  incorrect compilation options.
- In such cases, you should check if the missing library or program could be
  made available by loading a suitable module.

🗯 The CSC computing environment has several compiler versions and HPC
libraries available.

- In some cases you may, for example, need to use a specific C compiler or
  Python version in order to install a software. Read the compilation
  instructions carefully and try different versions if needed.
- If the compilation still fails, don't hesitate to ask for help from the
  [CSC Service Desk](https://docs.csc.fi/support/contact/).

1. To compile `HMMER` make sure you have no conflicting modules loaded, and load the GNU C compiler 
(`gcc`) version 11.3.0:

   ```bash
   module purge
   module load StdEnv
   module load gcc/11.3.0
   ```

2. In this case we wish to install the software under the `version-3.4`
   directory in your `$PROJAPPL` area. Thus, you need to specify the custom
   location for the installation using the `--prefix` option:

   ```bash
   ./configure --prefix=$PROJAPPL/$USER/hmmer/version-3.4  # double check that the path is correct
   ```

  ☝🏻 If you clone the source code from git,the `configure` script is not included. You must first generate it with command:
   ``bash
   autoconf
   ```

3. Compile and install the software with the commands:

   ```bash
   make
   make install
   ```

   ☝🏻 If you intend to compile software packages larger than the rather small HMMER
   example used here, please use the fast local disk (`$TMPDIR`) to avoid
   stressing the parallel file system. Compiling complex applications typically
   cause a lot of I/O load.

4. If the `make` and `make install` commands don't give any error messages, you
   have successfully installed your own software!

   💭 Typically, the executables/binaries, i.e. the compiled programs that can
   be launched, are stored in a subdirectory called `bin`.

5. Check what binaries were installed with:

   ```bash
   ls $PROJAPPL/$USER/hmmer/version-3.4/bin
   ```

## Running the software

💬 Although the software is now ready to be run, it is not automatically added
to your `$PATH`. This means that running:

```bash
hmmscan -h
```

will give an error message `bash: hmmscan: command not found`.

💬 You need to tell the computer where to find that command.

1. Try running the software by providing the full path to the binary, i.e.:

   ```bash
   $PROJAPPL/$USER/hmmscan/version-3.4/bin/hmmscan -h
   ```

2. Add the path of the HMMER executables to your `$PATH` environment variable.
   This is done with the command:

   ```bash
   export PATH=$PROJAPPL/$USER/hmmer/version-3.4/bin:$PATH  # double check that this path matches your actual installation path
   ```

   ‼️ When running `export`, note that the variable we are defining (first
   `PATH`) should *not* have a dollar sign. Also, note that we include the
   current `$PATH` at the end (*with* a dollar sign).

   ☝🏻 If we omit the current path, the normal shell commands will stop working!

3. Now you can launch the program you have installed from anywhere without
   first going to the `bin` directory or specifying the full path:

   ```bash
   hmmscan -h
   ```

💬 Remember that the `PATH` variable must be set each time you log in to the
supercomputer before you can run the `hmmscan` command without providing the full
path.

☝🏻 You need to run the correct `export PATH=...` command also in batch job
files before launching self-installed programs without the full path.

💡 If you want to make the addition automatically, add the `export PATH=...`
command to your `.bashrc` file in your `$HOME` directory.

‼️ Making changes to the `.bashrc` file may cause incompatibilities with
software installed by CSC.

💭 If you wish to revert your `.bashrc` file (and your environment in general)
back to default, you can use the
[csc-env command](https://docs.csc.fi/support/tutorials/using_csc_env/).

💡 Note that loading modules installed by CSC will automatically modify your
`$PATH` as needed, so no exports are typically required if you only run
pre-installed applications.

## Cleaning up

- If the software you have installed works correctly, you can remove the
  installation package and temporary directories that were used during the
  compilation.
- In this case we can remove the `hmmer.tar.gz` and the whole
  `hmmer-3.4` directory:

   ```bash
   cd $PROJAPPL/$USER/hmmer
   rm hmmer.tar.gz
   rm -r hmmer-3.4
   ```
