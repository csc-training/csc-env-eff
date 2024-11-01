---
layout: default
title: Apptainer tutorial 2
parent: 10. Containers and Apptainer
grand_parent: Part 2
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/singularity/singularity-tutorial_part2.html
---

# Apptainer tutorial, part 2

## Using files

💬 Apptainer containers have their own internal file system that is separated
from the host file system.

- The internal file system is always read-only when the container is run with
  normal user privileges.

💭 In most real use cases you might want to access the host file system to read
and write files.

- To do this, you must bind a writable directory on the host file system to the
- internal file system of the container.

💡 This is done using the command line argument `--bind` (or `-B`). The basic
syntax is `--bind /path/inside/host:/path/inside/container`.

💭 Some remarks:  
- The bind path does not need to exist inside the container – it is created if
  necessary.  
- More than one bind pair can be specified.  
- The option is available for all run methods described in the previous
  tutorial.  

1. To run these exercises on Puhti, use `sinteractive` or open a compute node
   shell in the [Puhti web interface](https://www.puhti.csc.fi):

   ```bash
   sinteractive --account <project>  # replace <project> with your CSC project, e.g. project_2001234
   ```

2. Try listing the contents of your project's `/projappl` directory (edit the path as needed)
   from inside the container without `--bind`:

   ```bash
   apptainer exec tutorial.sif ls /projappl/<project> # replace <project> with your CSC project, e.g. project_2001234
   ```

3. The container cannot see the host directory, so you will get a
   `No such file or directory` error.

4. Try binding the host directory `/projappl` to the directory `/projappl` inside
   the container:

   ```bash
   apptainer exec --bind /projappl:/projappl tutorial.sif ls /projappl/<project> # replace <project> with your CSC project, e.g. project_2001234
   ```

5. This time, the host directory is linked to the container directory and the
   command shows what the container sees inside `/projappl`.

   If the path is same in both host and container, you can simplify the
   command a bit. This does the same as the above command:

   ```bash
   apptainer exec --bind /projappl tutorial.sif ls /projappl/<project> # replace <project> with your CSC project, e.g. project_2001234 
   ```

   💡 You can use `--bind` to set the container, for example, to find input
   data or configuration files from a certain directory.

6. Bind a host directory in `/projappl` to a directory called `/config` indide
the container:

   ```bash
   apptainer exec --bind /projappl/<project>:/config tutorial.sif ls /config # replace <project> with your CSC project, e.g. project_2001234
   ```

### Using the `apptainer_wrapper` script

1. If you use the wrapper script `apptainer_wrapper`, it will automatically
   take care of the most common bind use cases.

2. You just need to set a `$SING_IMAGE` environment variable to point to the
   correct Apptainer image file:

   ```bash
   export SING_IMAGE=$PWD/tutorial.sif
   apptainer_wrapper exec ls /projappl/<project> # replace <project> with your CSC project, e.g. project_2001234
   ```

   💡 Note that the image file name is not needed in the `apptainer_wrapper`
   command since `$SING_IMAGE` is set.

   ‼️ Since some modules set `$SING_IMAGE` when loaded, it is a good idea to
   start with `module purge` to make sure the correct image is used if you plan
   to use `apptainer_wrapper`.

## Environment variables

💬 Some software may require environment variables to be set, e.g., to point to
some reference data or a configuration file.

💬 Most environment variables set on the host are inherited by the container.

☝🏻 Sometimes this may be undesired, in which case the command line option
`--cleanenv` can be used to prevent the host environment from being inherited
by the container.

💬 To set an environment variable specifically inside the container, you can
set an environment variable `$APPTAINERENV_XXX` (where `XXX` is the variable
name) on the host before invoking the container.

1. Set some test variables:

   ```bash
   export TEST1="value1"
   export APPTAINERENV_TEST2="value2"
   ```

2. Compare the outputs of:

   ```bash
   env | grep TEST
   apptainer exec tutorial.sif env | grep TEST
   apptainer exec --cleanenv tutorial.sif env | grep TEST
   ```

   - Command `env` lists all set environment variables.
   - The first command is run on the host and we see `$TEST1` and
     `$APPTAINERENV_TEST2`.
   - The second command is run inside the container and we see `$TEST1`
     (inherited from the host) and `$TEST2` (specifically set inside the
     container by setting `$APPTAINERENV_TEST2` on the host).
   - The third command is also run inside the container, but this time we
     omitted the host environment variables so we only see `$TEST2`.

3. Note that any command-line variables on the host are substituted by their
   values when passed to the container:

   ```bash
   apptainer exec tutorial.sif echo $TEST1
   apptainer exec tutorial.sif echo $TEST2
   ```

   - The first line prints the value set on the host.
   - The second line results in an empty output because a variable called
     `$TEST2` has not been set on host. It was `APPTAINERENV_TEST2="value2"`,
     remember?

4. If you need to pass environment variables to a container, in most cases it is
   easiest just to set them on host. If this is not possible, you need to make
   sure that variable names instead of their values are passed on to the 
   container, e.g:

   ```bash
   apptainer exec tutorial.sif bash -c 'echo $TEST2'   
   ```

  In this example we run `bash` shell inside the container and user the `-c` 
  option to give commands to run as a string. Since the string is encased in 
  single quotes, any variables are passed literally instead of being 
  substituted for their values.

## Exploring containers

💬 Our test container includes the program `hello2`, but it has not been added
to the `$PATH` variable.

1. One way to find it is to try running `find` inside the container:

   ```bash
   apptainer exec tutorial.sif find / -type f -name "hello2" 2>/dev/null
   ```

2. You can now run it by providing the full path:

   ```bash
   apptainer exec tutorial.sif /found/me/hello2
   ```

3. Or you could add it to `$PATH` inside the container:

   ```bash
   export APPTAINERENV_PREPEND_PATH=/found/me
   apptainer exec tutorial.sif hello2
   ```

💡 If you can't locate the desired binary with `find`, you can always use
`apptainer shell` to explore the container.

## More information

💬 This tutorial is meant as a brief introduction to get you started.

☝🏻 When searching online for instructions, pay attention that the instructions
are for the same version of Apptainer as you are using. There has been some
command syntax changes etc. between versions, so older instructions may not
work as is. Also note that Apptainer was formerly known as Singularity.

💡 For more detailed instructions, see the official
[Apptainer documentation](https://apptainer.org/docs/user/latest/).
