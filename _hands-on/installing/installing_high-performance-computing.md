---
topic: installing
title: Exercise - Installing own C, C++, or Fortran
---

# installing, making and making your own C, C++, or Fortran program in the CSC environment

## scenario A: you have a code already, you want to install it and run it.

- Create a proper directory for your code (the recommended location is in the projappl directory of your project):

```bash
cd /projappl/project_xxxx/    # replace xxxx
mkdir dir-name                # replace dir-name
```

- You need the source files for the code. Download them from e.g. GitHub, or use e.g. [scp](https://docs.csc.fi/data/moving/scp/) to upload e.g. a .zip file to your directory 
- If your code is compressed with zip, unzip your code:

```bash
unzip code-name.zip   # replace code-name.zip 
```

- Follow any instructions on how to install. Usually the code comes with a `readme` or `how to install` file.

### Install scenario A1: the code comes with cmake

- Load the module cmake with line command:

```bash
module load cmake
```
- Load also any other e.g. libraries that the code needs. Check if these can be found as available modules with: 

```bash
module spider somename   # replace somename
```

- You can also download and install the needed libraries.

- Create a `build` directory, and go to that directory:

```bash
mkdir build
cd build
```

- Run cmake

- If you get error messages, try to fix the problems. If it becomes really messed up, remove all and start again from the .zip file.

- Run `make` to compile the specific codes you want to use.

- Ask help from servicedesk if you really get stuck (mail to: servicedesk@csc.fi)

### Install scenario A2: the code comes with a makefile

- `Module load` or install separately any needed libraries. Check available modules with:

```bash
module spider somename   # replace somename
```

- Load the module with: 

```bash
module load name-of-module   # replace name-of-module
```

- Edit the `makefile` and replace the compile and link commands with proper ones for [Mahti](https://docs.csc.fi/computing/compiling-mahti/) or [Puhti]( https://docs.csc.fi/computing/compiling-puhti/)

- Run the command `make`

- Read the error messages and try to fix the possible issues

- Ask help from servicedesk if not successfull (mail to: servicedesk@csc.fi)

## Scenario B: you want to write your own code
 - You need [an editor](https://docs.csc.fi/support/tutorials/env-guide/text-and-image-processing/)
 - Launch an editor and write the code
 - Compile your code [on Puhti](https://docs.csc.fi/computing/compiling-puhti/), and [on Mahti](https://docs.csc.fi/computing/compiling-mahti/)
 - Fix bugs until compiler accepts code
 
## Exercise
 - Write your own simple code, compile it if necessary and run it.
