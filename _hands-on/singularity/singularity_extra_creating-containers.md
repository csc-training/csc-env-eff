---
topic: singularity
title: Extra Exercise - Creating singularity containers
---

# Creating singularity containers

This is an extra exercise. It can not be run in Puhti. You will need  access
to a computer or a virtual machine where you have sudo rights and that has
Singularity 3.x installed.

In this tutorial we create a Singularity container, and install the same software
as we installed in the tutorial 
[Installing a simple C code from source](..\installing\installing_hands-on_c.md).
You can see that tutorial for more information on the installation
commands.

In this tutorial we only cover the basics. Detailed instructions can be found
in the [Singularity manual](https://sylabs.io/guides/3.7/user-guide).

## Sandbox mode

One way to create a Singularity container is to do it in so-called sandbox
mode. Instead of an image file, we create a directory structure
representing the file system of the container. 

To start with, we create a basic container from a definition file. To choose
a suitable Linux distribution, you should check the documentation of the
software you wish to install. If the the developers provide installation 
intructions for a specific distribution, it is usually easiest to start with that.

In this case there is no specific reason to choose one distribution over another,
but from past experience I know the software installs without problems in CentOS,
so we start with that.

We start from a very bare-bones definition file. Copy the following lines to
a file called `centos.def`.
```text
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum
```
We then use that definition file to build the container:
```text
sudo singularity build --sandbox mcl centos.def
```
Note that instead of an image file, we created a directory called `mcl`. If
you need to include some reference files etc, you can copy them to correct subfolder.

We can then open a shell in the container. We need the container file system 
to be writable, so we include option `--writable`:
```text
sudo singularity shell --writable mcl
```
The command prompt should now be `singularity>`

If there is a need to make the container as small as possible, we should only
install the dependencies we need. Usually the size is not that critical, so we may
opt more for ease of use. 

In this case we install application group "Development tools" that includes 
most of the components we need (C, C++, make), but also a lot of things we 
don't actually need in this case.

Notice that unlike in the CSC machine, we are able to use the package mangement 
tools (in this case `yum`). This will often make installing libraries and other 
dendencies easier.

Also notice that it is not necessary to use `sudo` inside the container.

```text
yum group install "Development Tools" -y
yum install wget -y
```
We are now ready to install the software. 

Download and extract the distribuition package:
```text
wget https://micans.org/mcl/src/mcl-latest.tar.gz
tar xf mcl-latest.tar.gz
cd mcl-14-137
```
Run configure:
```text
./configure
```
Check the output of `configure` and install any missing dependencies
(In this case there should not be any.)

And finally run `make`:
```text
make
make install
```

We can now test the application to see it works:
```text
mcl --version
```
If everything works we can clean up:
```text
cd ..
rm -rf mcl-*
```
We can also add a runscript:
```text
echo 'exec /bin/bash "$@"' >> /singularity
```
We can now exit the container:
```text
exit
```
In order to run the container without sudo rights we need to build
a production image from the sandbox:

```text
sudo singularity build  mcl.sif mcl
```
We can now test it. Note that we no longer need `sudo`:
```text
singularity exec mcl.sif mcl --version
```

## Definition file

The above method is applicable as-is if you intend the
container to be only used by you and your close collaborators.
However, if you plan to distribute it wider, it's best to write
a definition file for it. That way the other users can see
what is in the container and they can, if they so choose, easily 
rebuild the production image.

A definition file will also make it easier to modify and re-use 
the container later. For example, software update can often be done
simply by modifying the version number in the definition file and
re-building the image.

To write the definition file we can start from the original 
bare-bones file and add various sections to it as necessary.

The installation commands go to section `%post`

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
If you need to set any environment variables, they go to section `%environment`

If you need to include any files in the container they go to `%files`.

Runscript goes to `%runscript`.

There are also other sections available as necessary. More information can be found in the
[Definition file chapter](https://sylabs.io/guides/3.7/user-guide/definition_files.html#)
of the Singularity manual

The final definition file will look like this:
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
In more complex cases it often helpful to first build the image in
sandbox mode and make note of all the commands needed.
