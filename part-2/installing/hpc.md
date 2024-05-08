---
layout: default
title: Installing own C, C++ or Fortran programs
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 7
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_hands-on_hpc.html
---

# Installing and developing your own C, C++, or Fortran program in the CSC computing environment

## Case A: you have the source code, you want to install and run it

1. Create a directory for your code. The recommended location is under the `/projappl` directory of your project:

```bash
mkdir -p /projappl/<project>/myprog    # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 1"}
2. You need the source files of the code. Depending on the software, you can typically download them from e.g. GitHub. If you have the source code on your own computer, use e.g. [`scp`](https://docs.csc.fi/data/moving/scp/) to upload the data to the supercomputer.

3. If the source files are distributed as a zip file, use `unzip` to decompress:

```bash
unzip filename.zip    # modify the filename accordingly
```

{:style="counter-reset:step-counter 3"}
4. Read and follow any instructions on how to install. Usually, the code comes with a `README` or `INSTALL` file outlining the installation procedure.

5. When compiling, consider using the fast local disk on the login nodes (`$TMPDIR`) to move I/O load away from the parallel file system.

### Scenario A1: The code uses `cmake`

1. Load the `cmake` module:

```bash
module load cmake
```

{:style="counter-reset:step-counter 1"}
2. Download and install external libraries that the code might need. Always check first if these can be found as pre-installed modules (the most common ones are available):

```bash
module spider <modulename>   # replace <modulename>, e.g. fftw
```

{:style="counter-reset:step-counter 2"}
3. Create and move to a `build` directory in the root of the source code:

```bash
mkdir build
cd build
```

{:style="counter-reset:step-counter 3"}
4. Run `cmake` with `cmake /path/to/source/code`:

```bash
cmake ..
```

{:style="counter-reset:step-counter 4"}
5. If you get errors, try to fix the problems. Sometimes it might be easiest to remove everything and start from the beginning, i.e. by unzipping the `.zip` file.
6. After `cmake`, run `make` to compile the specific applications you want to use:

```bash
make
```

{:style="counter-reset:step-counter 6"}
7. Ask help from [CSC Service Desk](https://docs.csc.fi/support/contact/) if you get stuck.

### Scenario A2: The code comes with a Makefile

1. `module load` or install separately all required libraries. Check for availability of modules with:

```bash
module spider <modulename>    # replace <modulename>, e.g. fftw
```

{:style="counter-reset:step-counter 1"}
2. Load the library modules with:

```bash
module load <modulename>/<version>   # replace <modulename>/<version>, e.g. fftw/3.3.10-mpi
```

{:style="counter-reset:step-counter 2"}
3. Edit the `Makefile` manually or by running `./configure` to replace compile and link commands with proper ones for [Mahti](https://docs.csc.fi/computing/compiling-mahti/) or [Puhti](https://docs.csc.fi/computing/compiling-puhti/).
4. Run the command `make` to compile and `make install` to install. Custom installation location is typically specified with the `--prefix` option of the `configure` script.

```bash
./configure --prefix=/projappl/<project>/myprog    # replace <project> with your CSC project, e.g. project_2001234 
make
make install
```

{:style="counter-reset:step-counter 4"}
5. Read any error messages and try to fix the possible issues.
6. Ask help from [CSC Service Desk](https://docs.csc.fi/support/contact/) if you get stuck.

## Case B: You want to write your own code

1. You need [an editor](https://docs.csc.fi/support/tutorials/env-guide/text-and-image-processing/).
2. Launch an editor and write the code. If not developing locally, consider using the [Puhti web interface](https://www.puhti.csc.fi) and e.g. [VSCode](https://docs.csc.fi/computing/webinterface/vscode/).
3. Compile your code [on Puhti](https://docs.csc.fi/computing/compiling-puhti/) or [on Mahti](https://docs.csc.fi/computing/compiling-mahti/).
4. Fix bugs until compiler accepts code.

## Exercise

- Write your own simple C/C++/Fortran code, compile it and run it.
