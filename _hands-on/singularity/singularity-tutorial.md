---
topic: singularity
title: Tutorial - Singularity 
---

# Singularity tutorial

In this tutorial we get familiar with the basic usage of Singularity containers. 

To run these exercises in Puhti, use `sinteractive`.
```text
sinteractive -i
```
## Getting started

To get started, download a test container image from allas.

```text
wget  https://a3s.fi/saren-2001659-pub/tutorial.sif
ls -lh tutorial.sif
```
As you can see, the container is a single file. In this case the container is very 
bare-bones, and thus quite small, about 50 MB. 

Actual application containers are typically larger, since they also contain the 
software installation, and may in some cases include some reference data etc.


## Basic usage

There are three basic ways to run software in a Singularity container:

### 1. Singularity exec
To execute a command inside the container, the command is `singularity exec`.

```text
singularity exec tutorial.sif hello_world
```
Compare the outputs of the following commands:
```text
cat /etc/*release
singularity exec tutorial.sif cat /etc/*release
```
The first command is run in the host. The second command is run inside the container.

The tutorial container is based on Ubuntu 18.04. The host and the container use the 
same kernel, but the rest of the system can vary. That means a container can be based 
on a different Linux distribution than the host (as long as they the are kernel compatible), 
but can't run a totally differen OS like Windows.

`Singularity exec` is the run method you will typically use in a batch job script.

Make a file called `test.sh`, and copy the following contents to it. Change "project_xxxx"
to the corrct project name.
```text
#!/bin/bash
#SBATCH --job-name=test
#SBATCH --account=project_xxxx
#SBATCH --partition=test
#SBATCH --time=00:01:00
#SBATCH --mem=1G
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

singularity exec tutorial.sif hello_world
```
Submit the job to the queue with:
```text
sbatch test.sh
```
For more information on batch jobs, please see [CSC Docs pages](https://docs.csc.fi/computing/running/getting-started/).

### 2. Singularity run
When containers are created, a standard action, called the `runscript` is defined. 
Depending on the container, it may simply print out a message, or it may launch a program 
or service inside the container. If you are using a container created by somebody else, 
you will need to check the documentation provided by the creator for details.

In our test container it prints out a simple message:
```text
singularity run tutorial.sif
```
If the container image has execute rights, you can also run it directly:
```text
chmod u+x tutorial.sif
./tutorial.sif
```
You can see the actual script with command:
```text
singularity inspect --runscript tutorial.sif
```

### 3. Singularity shell
It is also possible to open a shell inside the container. 
```text
singularity shell tutorial.sif
```
You can see the comamnd prompt change to `Singularity>`. You can now run any software 
inside the container interactively:
```text
hello_world
```
You can exit the container with:
```text
exit
```

## Using files
Singularity containers have their own internal file system that is separate from the 
host file system. The internal file system is always read-only when the container is 
run with normal user rights.

In most real-world use cases you probably want to access the host file system to read 
and write files. To do this you must bind a writable directory on host file system to 
the internal file system of the
container. 

This is done with command line argument `--bind` (or `-B`). The basic syntax is 
`--bind /path/in/host:/path/inside/container`.

The bind path does not need to exist inside the container. It is created if necessary. 
More that one bind pair can be specified. The option is available for all the run methods 
described above.

First try listing the contents of your project directory (substitute the correct path) 
from inside the container without bind:

```text
export SCRATCH=/scratch/project_12345
singularity exec tutorial.sif ls $SCRATCH
```
This will not work. The container can not see the host diectory, so you will get a 
"No such file or directory" error.

Now try binding host directory `/scratch` to directory `/scratch` inside the container.

```text
singularity exec --bind /scratch:/scratch tutorial.sif ls $SCRATCH
```
This time the host directory is linked to to the container directory and the command works.

The path does not need to be the same in host and in the container. Some containers may 
be set up, for example, to expect input data or configuration files in a certain directory.

In this example we bind host directory specified in `$SCRATCH` into directory `/input`:
```text
singularity exec --bind $SCRATCH:/input tutorial.sif ls /input
```

If you use wrapper script `singularity_wrapper`, it will take care of the binds for most 
common use cases. 
```text
singularity_wrapper exec tutorial.sif ls $SCRATCH
```
If environment variable `$SING_IMAGE` is set, you don't even need to provide path to the 
image file.
```text
export SING_IMAGE=$PWD/tutorial.sif
singularity_wrapper exec ls $SCRATCH
```
Since some modules set `$SING_IMAGE` when loaded, it is a good idea to start with 
`module purge` if you plan to use it, to make sure correct image is used.

## Environment variables
Some software may reguire some environment variables to be set, e.g. to point to some 
reference data or a configuration file.

Most environment variables set on the host are inherited by the container. Sometimes 
this may be undesirable. With command line option `--cleanenv` host environment is not 
inherited by the container.

To set an environment variable specifically inside the container, you can set an 
environment variable `$SINGULARITYENV_xxx` (where xxx is the variable name) on the host 
before invoking the container.

Set some test variables:
```text
export TEST1="value1"
export SINGULARITYENV_TEST2="value2"
```
Compare the outputs of:

```text
env |grep TEST
singularity exec tutorial.sif env |grep TEST
singularity exec --cleanenv tutorial.sif env |grep TEST
```
The first command is run on host, and we see `$TEST1` and `$SINGULARITYENV_TEST2`. The 
second command is run in the container and we see `$TEST1` (inherited from host) and 
`$TEST2` (specifically set inside the container by setting `$SINGULARITYENV_TEST2` on host). 
The third command is also run  inside the container, but this time we omitted host environment
variables, so we only see `$TEST2`.

It should be noted that any variables on command line are substituted by their values on the host.
```text
singularity exec tutorial.sif echo $TEST2
```
This will result in empty output because $TEST2 has not been set on host.

## Exploring containers

Our test container includes program `hello2`, but it is not in the `$PATH`. One way to 
find it is to try running `find` inside the container

```text
singularity exec tutorial.sif find / -type f -name "hello2" 2>/dev/null
```
You can now run it by providing the full path:
```text
singularity exec tutorial.sif /found/me/hello2
```
Or you could add it to `$PATH` inside the container:
```text
export SINGULARITYENV_PREPEND_PATH=/found/me
singularity exec tutorial.sif hello2
```
If you can't locate the desired binary with `find`, you can always use `singularity shell` 
to explore the container.

## How to get containers
Building containers from scratch requires root access, so it can not be done on Puhti. 
Instead, you will have to import a ready image file.

There are various option to do this.

### 1. Run or pull an existing Singularity container from a repository
It is possible to run containers directly from repository:
```text
singularity run shub://vsoch/hello-world:latest
```
This can, however, lead to a batch job failing if there are network problems.
Usually it is preferable to pull the container first and use the image file.
```text
singularity pull shub://vsoch/hello-world:latest
singularity run hello-world_latest.sif
```

### 2. Convert an existing Docker container to Singularity

Docker images are downloaded as layers. These layers are stored in the cache directory. 
Default location for this is `$HOME/.singularity/cache`. Since the home directory has 
limited capacity, and some images can be large, it's best to set `$SINGULARITY_CACHE` 
to point to some other location with more space.

If running with `sinteractive`, or as batch job on an IO node, you can use the 
fast local storage:
```text
export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH
```
If running on a node with no local storage, you can use e.g. /scratch.

You can avoid some unnecessary warnings by unsetting a variable:
```text
unset XDG_RUNTIME_DIR
```
You can now run `singularity build`:
```text
singularity build alpine.sif docker://library/alpine:latest
```
You can find more detailed instructions for converting Docker images in Docs CSC: 
[Running existing containers](https://docs.csc.fi/computing/containers/run-existing/)

### 3. Build the image on another system and transfer the image file to Puhti
To do this you will need an access to system where you have root access and that has 
Singularity installed.

Singularity version does not need to be exactly same, but it should be same major varsion 
e.g. (3.x as oppsed to 2.x).

You can check the current version on Puhti with:
```text
singularity --version
```
After creating an image file, you can transfer it to Puhti to use.

## More information

This tutorial is meant as brief introduction to get you started.

When searching the internet for instruction, pay attention that the instructions are
for the same version of Singularity that you are using. There has been some command 
syntax changes etc. between the versions, so older instructions may not work with copy-paste.

For authoritative instructions see [Singularity documentation](https://sylabs.io/docs/).
