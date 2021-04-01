---
topic: installing
title: Tutorial - Installing a simple C code from source
---

# Installing a simple C code from source

In this example we install MCL Markov cluster algorithm program 
to users own [projappl directory](https://docs.csc.fi/computing/disk/) in Puhti.

This software would also be available as installation packages (.deb, .rpm)
for various Linux distributions, but these can not be used in Puhti. Instead we 
install it from the source code.

To follow the instructions, set up environment variable to point to your projects
/projappl folder (substitute "project_12345" with your project name):

```text
export PROJAPPL=/projappl/project_12345
```
## Downloading

Move to your `$PROJAPPL` directory and create there a new directory called mcl

```text
cd $PROJAPPL
mkdir mcl
```
Move to the newly created directory and download the distribution package:
```text
cd mcl
wget https://micans.org/mcl/src/mcl-latest.tar.gz
```
In this case the installation package is a tar-archive file that has been compressed 
with gzip program. You can unpack this file with commands
```text
tar xvf mcl-latest.tar
ls -l
```
After unpacking, the `ls` command shows that a new directory called `mcl-14-137` has 
been created. This directory contains the actual installation files and documentation of the
software. 

Create a new empty directory called `version-14-137` to the mcl directory. This vill be the actual
installation directory.
```text
mkdir version-14-137
```
After this go to the `mcl-14-137` directory and study its content
```text
cd mcl-14-137
ls -l
```
Installation packages contain often a short installation instructions. Typically this 
instruction file is called as INSTALL or README. In this case you should read the 
INSTALL file to find out how the  installation should be done.
```text
less INSTALL
```
## Installation
Many open source software tools are installed using following three steps:
1 Building up the so called Makefile with a `./configure` command.
2 Running `make`  command that compiles the source code according to the instructions in the
Makefile
3 Installing the compiled executables with command `make install`

Normally the installation packages assume that the user has permissions to install the software to
the locations where the standard linux commands and programs normally get installed. However,
at CSC this is not the case. You can install software only to your own disk areas. Often you can
use option `--prefix=/path/` to tell to the configure command, where to the program should be
installed. 

The `./configure` command checks that all the compilers and libraries that the software needs, are
available. It is not uncommon that `./configure` reports about missing libraries or incorrect
compilation options. In those cases you can check if the missing library or program can be taken in
use with the module system. 

CSC environment has several compiler and program versions available. In some cases you may for 
example need to use certain C-compiler or python version in order to install the software. Try
with different versions. If you still fail with the installation, ask help from the HelpDesk of CSC.

For mcl we choose gcc environment.
```text
module load gcc/9.1.0
```

In this case we wish to install the software to the `version-14-137` directory in you
$PROJAPPL area. Thus you must use following `./configure` command:
```text
./configure --prefix=$USERAPPL/mcl/version-14-137
```
Next we need to compile and install the software with commands:
```text
make
make install
```
If `make` and `make install` commands don't give any error messages, you have successfully
installed your software. 

Typically the executables, i.e. the compiled programs that can be launched, are stored to a 
subdirectory called `bin`. 

Check what got installed  with:
```text
ls -l $PROJAPPL/mcl/version-14-137/bin
```

## Running command

The software is now ready to run, but it is not in your `$PATH`. That means that if you try to run:
```text
mcl --help
```
you get an error message `bash: mcl: command not found`.

You need to tell the computer where to find that command. You can do this by providing the path for the 
program, e.g.
```text
$PROJAPPL/mcl/version-14-137/bin/mcl --help
```
You can also add the directory path of you executables to the `$PATH` environment variable. In this case 
we add path `${USERAPPL}/mcl/version-14-137/bin` to the `$PATH` variable. This is done with command:
```text
export PATH=${PROJAPPL}/mcl/version-14-137/bin:${PATH}
```
Note that the first `PATH` word in the command above is without the dollar sign. Also note that we include 
the current `$PATH`. If we omitted it, the normal shell commands would stop working.

Now you can launch the program you have installed with simply:
```text
mcl --help
```

Remember that also in the future, when you log in to CSC, the `PATH` variable must be set up
before you can use mcl command without providing the path. 

Also in the batch job files you need to run the correct `export PATH` command above before 
executing the program you have installed yourself.

If you want to make the addition permanent, you can add the `export PATH` command to you `.bashrc`
file in your home directory. It should be noted, however, that making changes to the `.bashrc` can
couse incompatibilities with CSC installed software.

If you wish to revert your `.bashrc` (and your environment in general) back to default, you can use
the [csc-env command](https://docs.csc.fi/support/tutorials/using_csc_env/).

## Cleaning up

If the software you have installed works correctly, you can remove the installation package and
temporary directories that were used during the compilation. In this case we could remove the 
`mcl-latest.tar.gz` file and the directory `mcl-14-137`
```text
cd $PROJAPPL/mcl
rm mcl-latest.tar.gz
rm -rf mcl-14-137
```



