---
topic: singularity
title: Tutorial - Singularity introduction continued
---

# Singularity tutorial part 2

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
More than one bind pair can be specified. The option is available for all the run methods 
described above.

First try listing the contents of your project directory (substitute the correct path) 
from inside the container without bind:

```bash
export SCRATCH=/scratch/project_12345
singularity exec tutorial.sif ls $SCRATCH
```
This will not work. The container can not see the host diectory, so you will get a 
"No such file or directory" error.

Now try binding host directory `/scratch` to directory `/scratch` inside the container.

```bash
singularity exec --bind /scratch:/scratch tutorial.sif ls $SCRATCH
```
This time the host directory is linked to to the container directory and the command works.

The path does not need to be the same in host and in the container. Some containers may 
be set up, for example, to expect input data or configuration files in a certain directory.

In this example we bind host directory specified in `$SCRATCH` into directory `/input`:
```bash
singularity exec --bind $SCRATCH:/input tutorial.sif ls /input
```

If you use wrapper script `singularity_wrapper`, it will take care of the binds for most 
common use cases. 
```bash
singularity_wrapper exec tutorial.sif ls $SCRATCH
```
If environment variable `$SING_IMAGE` is set, you don't even need to provide path to the 
image file.
```bash
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
```bash
export TEST1="value1"
export SINGULARITYENV_TEST2="value2"
```
Compare the outputs of:

```bash
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
```bash
singularity exec tutorial.sif echo $TEST2
```
This will result in empty output because $TEST2 has not been set on host.

## Exploring containers

Our test container includes program `hello2`, but it is not in the `$PATH`. One way to 
find it is to try running `find` inside the container

```bash
singularity exec tutorial.sif find / -type f -name "hello2" 2>/dev/null
```
You can now run it by providing the full path:
```bash
singularity exec tutorial.sif /found/me/hello2
```
Or you could add it to `$PATH` inside the container:
```bash
export SINGULARITYENV_PREPEND_PATH=/found/me
singularity exec tutorial.sif hello2
```
If you can't locate the desired binary with `find`, you can always use `singularity shell` 
to explore the container.

## More information

This tutorial is meant as a brief introduction to get you started.

When searching the internet for instruction, pay attention that the instructions are
for the same version of Singularity that you are using. There has been some command 
syntax changes etc. between the versions, so older instructions may not work with copy-paste.

For authoritative instructions see [Singularity documentation](https://sylabs.io/docs/).
