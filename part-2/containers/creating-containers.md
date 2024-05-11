---
layout: default
title: Creating Apptainer containers
parent: 10. Containers and Apptainer
grand_parent: Part 2
nav_order: 6
has_children: false
has_toc: false
permalink: /hands-on/singularity/singularity_extra_creating-containers.html
---

# Creating Apptainer containers

In this tutorial we will create an Apptainer container and install the same software as we installed in the tutorial ["Installing a simple C code from source"](https://csc-training.github.io/csc-env-eff/hands-on/installing/installing_hands-on_mcl.html). Feel free to revisit that tutorial for more information on the installation commands.

CSC supercomputers support the `fakeroot` feature of Apptainer, so it is possible to build
container images without root privileges. There are some limitations, so it is possible to run into problems, especially when using package managers. In these cases it is necessary to either use an
alternate installation method for the dependency, or build in system where you do have root privileges.

We will only cover Apptainer basics here. Detailed instructions can be found in the [official Apptainer documentation](https://apptainer.org/docs/user/latest/quick_start.html).

## Sandbox mode

One way to create an Apptainer container is in the so-called sandbox mode. Instead of an image file, we create a directory structure representing the file system of the container.

First, we'll create a basic container from a definition file. In order to choose a suitable Linux distribution, you should check the documentation of the software you wish to install. If the developers provide installation instructions for a specific distribution, it is usually easiest to start with that.

In this case there is no specific reason to choose one distribution over another, but from past experience it is known that the software installs without problems on CentOS, so we'll start with that.

Start from a very bare-bones definition file. Copy the following lines to a file called `centos.def`.

```text
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum
```

By default Apptainer uses the home directory for cached files. As the home directory is quite
small and easily fills up, it is recommended to use some other directory. For example to use
$TMPDIR (make sure it is defined) set:

```bash
export APPTAINER_CACHEDIR=$TMPDIR
```

You can clean the cache with command:

```bash
apptainer cache clean
```

Using this definition file, build the container:

```bash
apptainer build --fakeroot --sandbox mcl centos.def
```

Note that instead of an image file, we created a directory called `mcl`. If you need to include some reference files etc., you can copy them to the correct subdirectory.

We can now open a shell in the container. We need the container file system to be writable, so we include the option `--writable`. We will also need to include `--fakeroot`:

```bash
apptainer shell --fakeroot --writable mcl
```

The command prompt should now be `Apptainer>`

The base container images are typically very barebones and do not contain any compilers, 
download tools etc, so those need to be installed. If there is a need to make the container as small as possible, we should only install the dependencies we need. Usually the size is not that critical, so we may opt for ease of use.

In this case we will install the application group "Development Tools" that includes most of the components we need (C, C++, make), but also a lot of tools not needed in this example. We also
install `wget` to download the source code.

Notice that unlike on CSC supercomputers, we are able to use package management tools (in this case `yum`). This will often make installing libraries and other dependencies easier. Also notice that it is not necessary to use `sudo` inside the container.

```bash
yum group install "Development Tools" -y
yum install wget -y
```

We are now ready to install the `mcl` software. Download and extract the distribution package:

```bash
wget https://micans.org/mcl/src/mcl-latest.tar.gz
tar xf mcl-latest.tar.gz
cd mcl-14-137
```

Run configure:

```bash
./configure
```

Check the output of `configure` and install any missing dependencies. In this case there should not be any. Finally, run `make`:

```bash
make
make install
```

We can now test the application to see it works:

```bash
mcl --version
```

If everything works we can clean up:

```bash
cd ..
rm -rf mcl-*
```

We can also add a `runscript`:

```bash
echo 'exec /bin/bash "$@"' >> /apptainer
```

We can now exit the container:

```bash
exit
```

We can then build a production image from the sandbox:

```bash
apptainer build --fakeroot mcl.sif mcl
```

We can now test it:

```bash
apptainer exec mcl.sif mcl --version
```

## Definition file

The above method is fine if you intend the container to be only used by you and your close collaborators. However, if you plan to distribute it wider, it's best to write a definition file for it. That way the other users can see what is in the container, and they can, if they so choose, easily rebuild the production image.

A definition file will also make it easier to modify and reuse the container later. For example, software updates can often be done simply by modifying the version number in the definition file and rebuilding the image.

To write the definition file, we can start from the original bare-bones file and add various sections to it as required. The installation commands go into the `%post` section:

```text
%post
    yum group install "Development Tools" -y
    yum install wget -y
    wget https://micans.org/mcl/src/mcl-latest.tar.gz
    tar xf mcl-latest.tar.gz
    cd mcl-14-137
    ./configure
    make
    make install
```

If you need to set any environment variables, they go into the `%environment` section. If you need to include any files in the container, they go into `%files`. The `runscript` goes to `%runscript`.

There are also other sections available if needed. More information can be found in the [Definition Files chapter](https://apptainer.org/docs/user/latest/definition_files.html) of the Apptainer documentation.

The final definition file would look like this:

```text
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%post
    yum group install "Development Tools" -y
    yum install wget -y
    wget https://micans.org/mcl/src/mcl-latest.tar.gz
    tar xf mcl-latest.tar.gz
    cd mcl-14-137
    ./configure
    make
    make install
    cd ..
    rm -rf mcl-*

%environment
    export LC_ALL=C

%runscript
    exec /bin/bash "$@"
```

You can now build the image:

```bash
apptainer build --fakeroot mcl.sif mcl.def
```

In more complex cases, it often helpful to first build the image in the sandbox mode and make note of all the commands needed. You can then write a definition file to replicate the necessary steps.
