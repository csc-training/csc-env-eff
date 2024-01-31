---
theme: csc-2019
lang: en
---

# Introduction to Singularity containers {.title}

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All material (C) 2020-2021 by CSC -IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

:::info (speech)

:::

# The one-slide lecture
- Some software packages on CSC supercomputers are installed as containers
  - May cause some changes to usage
  - See instructions for each software for details
- Containers provide an easy way for you to install software
  - Single command installation if a suitable Docker or Singularity container exists

:::info (speech)
Why should we care for Singularity containers in HPC environments? 
In HPC centers applications are often installed as containers.
CSC makes no exception to that. 
There may be slight differences in how you use regular software and software in a container.
Check the documentation of that particular software to see whether it is installed as a container. 
Users also benefit from the use of containers.
They can install software easily - no need for HPC admins. 
If a container with desired software exists, users need only a single command to install it.
:::

# Containers
- Containers are a way to package software with its dependencies (libraries, etc)
- Popular container engines include Docker, Singularity, Shifter
- Singularity is the most popular in HPC environments

:::info (speech)
Let me tell you an example usecase, where containers can solve the problem.
A scientific developer writes some code, and wants to hand it over to a friend for testing. 
The friend tells the developer that the test code is not working in the test environments. 
Turns out the first test environment has slightly different versions of the used libraries. 
The second test environment has a different operating system. 
How to make sure that same code works on your computer, and in HPC environment or cloud environment?

That is the challenge that containers are going to solve. 
Basically if something works on your computer, it should work anywhere regardless of the underlying host environment. 
A container packages everything needed to run the application - that includes the code and all dependencies.
The container image can be run like a binary file.
There are many container platforms around.
The most popular container engine is probably Docker.
Singularity is very popular in HPC environments, and it is used also in CSC environment. 
:::

# Containers vs. Virtual Machines (1/2)
<div style="text-align:center"><img src="./img/containers-fig1.png" /></div>

:::info (speech)
Both containers and virtual machines are solving this dependency issue.
The comparison here shows three ways of deploying your applications. 
First is the native application - that is you compile and launch it. 
Then it depends on your environment whether it works or not.
The second one is the virtual machine approach. 
Virtual machine applications are usually rendered through a special software called hypervisor.
Virtual machine includes OS and Kernel like a normal computer.
It basically is a virtual computer, and there you can install everything from the scratch.
Another user can install the saved image of the system, and use it with good compatibility.

Third option is the container approach, which is a bit more lightweight than a virtual machine. 
You just install the container engine, but not kernel or any operating system. 
So the key difference between virtual machines and containers is how they use kernel.
Containers share the kernel with the hardware, whereas virtual machines have their own kernel. 
From the user point of view: virtual machines boot the operating system – which takes time, and containers can be loaded in milliseconds.
:::

# Containers vs. Virtual Machines (2/2)
- Virtual machines can run totally different OS than host
(e.g. Windows on Linux host or vice versa)
- Containers share kernel with host, but can have its own libraries etc
  - Can run e.g. different Linux distribution than host

:::info (speech)
Virtual machines are useful, if you need to run a different Operating System, than your regular system. 
You may have MacOS or Linux, and then you need some Windows software - so you can install Windows into a virtual machine and run that on your Mac.
If you need to use Linux from another OS, you can open an SSH-connection to Puhti or Mahti.
But that you probably knew already!
Containers can not run a different OS, because the share the kernel with the host.
They can have their own libraries - and that is how they solve the dependency issue, which I described earlier with the example code test case, remember? No?
Containers can have a different Linux distribution - like Centos or Ubuntu - than the host has.
:::

# Container benefits: Ease of installation
- Containers are becoming a popular way to distribute software
  - Single command installation
  - All dependencies included, so more portable
  - Normal user rights enough when using an existing container
- Root access on build system is enough
  - Root access, package managers (yum, apt, etc) can be utilized even
  when not available in the target system.
  - Makes installing libraries etc. easier

:::info (speech)
Containers are popular, for example because they provide an easy way of distributing software.
They can be used like binary files, which means that once you have the container you just run it.
Including all the dependencies inside the containers makes it portable and compatible.

Singularity containers can be run as a normal user, so they work nicely in HPC environments. 
In comparison, Docker containers are inconvenient in HPC systems, because they require root access to run.
Users do not have root access in multi-user IT environment, like HPC environments. 

In general all containers need root access when built.
For that you can use your local computer – in which you probably have the root access. 
There you can install all the packages you want inside the container.
Then you can copy the container into CSC enviroment, and run it there with normal user rights.
That provides a convenient way of transforming your code - with all your custom libraries - to the supercomputer.
:::

# Container benefits: Environment isolation
- Containers use host system kernel, but can have their own Bins/Libs layer
  - Can be a different Linux distribution that the host
  - Can solve some incompatibilities
  - Less likely to be effected by changes in the host system

:::info (speech)
While sharing the kernel with the host, containers have their own environment.
That means they can have different Linux distribution, which can include different libraries.
Your code might require Centos while the host has Ubuntu, so you can have Centos in the container.
There might be some exeptions to that – for example when working with GPUs or MPI libraries. 
Still in general containers solve many incompatibilities, and are less likely to be effected by changes in the host system.
:::

# Container benefits: Enviroment reproducibility
- Analysis environment can be saved as a whole
  - Useful with e.g. Python, where updating underlaying 
  libraries (Numpy etc) can lead to differences in behavior  
- Sharing with collaborators easy (single file)

:::info (speech)
Containers ensure that your computational environment and your collaborators environment are the same.
You can save a whole analysis environment, which means for example all the libraries and their versions. 
That means you can easily share the environment with collaborators as a single file. 
:::

# Singularity in a nutshell
- Containers can be run with user level rights
  - But: Building new containers requires root access
- Minimal performance overhead
- Supports MPI
  - Requires containers tailored to host system
- Can use host driver stack (Nvidia/cuda)
  - Add option `--nv`
- Can import and run Docker containers
  - Running Docker directly would require root rights

:::info (speech)
Singularity is a container platform like Docker.
Singularity containers can be run with a basic user level rights. 
Note that you cannot elevate your user privileges inside the container - which is also good from administration point-of-view. 
Containers are faster to deploy than virtual machines, because they only load the libraries, not a full operating system.
Singularity containers support MPI, but make sure to use compatible MPI libraries inside the container.
Here compatible means: the hosts should have at least the version, which is available in the container. 
Singularity can use also a driver stack e.g. when using GPUs.
That means you don't need to install drivers inside the container, but the container can use the driver that is already available in the whole system.
Option --nv tells the container to use driver stack. 
There are a lot of Docker images around, because Docker is very popular.
You can convert Docker containers into Singularity containers, and use that also in an HPC environment.
:::

# Singularity on CSC servers
- Singularity jobs should be run as batch jobs or with `sinteractive`
- No need to load a module
- Users can run their own containers
- Some CSC software installations provided as containers
  - See software pages for details

:::info (speech)
In general containers should be run as a batch job or an interactive job.
Singularity commands are available also in the login node - no need to load a module. 
Users can always bring their own containers, and start using them right away. 
Some software in Puhti or Mahti are installed as containers.
Always check software information in DocsCSC for details on usage.
:::

# Running Singularity containers: Basic syntax
- Execute a command in the container
  - `singularity exec [exec options...] <container> <command>`
- Run the default action (runscript) of the container
  - Defined when the container is built
  - `singularity run [run options...] <container>`
- Open a shell in the container
  - `singularity shell [shell options...] <container>`

:::info (speech)
There is only three commands needed for running Singularity containers. 
The first one is: singularity exec with container name and a command, that you want to run in the container. 
It let's you to use same commands – that you use for your application – also with the container.
Command singularity run: runs the default action of the container.
The default script is defined when building the container.
If you want to interactively work inside the container - instead of the host command line - you can open a command line inside the container with command: singularity shell and the container name.
Then you will be in a different file system environment, which is built inside the container.
:::

# File system
- Containers have their own, internal file system
  - The internal FS is always read-only when run with user level rights 
- To access host directories, they  need to be mapped to container directories
  - E.g. to map host directory `/scratch/project_12345` to directory `/data` 
  inside the container: `--bind /scratch/project_12345:/data`
  - Target directory inside the container does not need to exist. It is created as
necessary
  - More than one directory can be mapped

:::info (speech)
The container file system includes the files that are put there when the container is built.
You can always go inside the container, and check out the file system there. 
Usually containers are read only systems, which means you cannot change the files inside the container.
Often the container needs to access some files in the host computer.
To do that we can mount or bind host directories inside the container. 
Note that they are writable, so file changes there are permanent. 
To mount a directory into a container, use the flag --bind. 
If the target directory - in this example /data - does not exist, it is created automatically.
If you don't define the target directory, it will use the host directory name by default. 
If you need to bind more than one host folders to a container, just write more folders after the bind flag.
:::

# Environment variables
- Most environment variables from host are inherited by the container
- Can be prevented, if necessary, by adding option `--cleanenv`
- Environment variables can be set specifically inside the container by 
setting in host `$SINGULARITYENV_variablename`.
  - E.g. to set `$TEST` in container, set `$SINGUALRITYENV_TEST` in host

:::info (speech)
Environment variables – like HOME and USER – get their values typically through some functionality built into the operating system.
Most environment variables are inherited by the containers.
HPC systems generally have many environmental variables, and some of them might interfere with your container.
If you want to prevent the container inheriting all the environmental variables, you can use flag clean-env.
However you can define environment variables so that they are used only in the container.
Defining an environmental variable: singularity env test in the host creates such a variable, that it shows as "test" inside the container.
:::

# singularity_wrapper
- Running containers with `singularity_wrapper` takes care of most common `--bind` commands
  - `singularity_wrapper exec image.sif myprog <options>`
- If environment variable `$SING_IMAGE` is set with the path to the image, even image file can be omitted
  - `singularity_wrapper exec myprog <options>`

:::info (speech)
Already worrying too much about mounts and variables?
Fear not!
We at CSC provide you with a special wrapper for this singularity application. 
This singularity_wrapper takes care of common binds, so you are able to see your home, scratch and projappl directories inside the container.
You can use singularity wrapper with command: singularity_wrapper exec image.sif program name --options
Here this image.sif is the container image file.
Most modules also set this singularity image as special environment variable.
Then you do not need to write the image name the wrapper command.
:::

# Using Docker containers with Singularity
- You can build a Singularity container from a Docker container with normal user rights:
  - `singularity build <image> docker://<address>:<tag>`
- For example:
  - `singularity build pytorch_19.10-py3.sif docker://nvcr.io/nvidia/pytorch:19.10-py3`
- Documentation in Docs:
  - [Running Singularity containers](https://docs.csc.fi/computing/containers/run-existing/)
  - [Creating Singularity containers](https://docs.csc.fi/computing/containers/creating/)

:::info (speech)
A lot of applications are written as Docker containers. 
As I already mentioned: you can use the Docker containers in Singularity. 
The command: singularity build with the docker address converts a Docker container into a Singularity container.
You can do that with basic user privileges - which is dope!
Let's take this PyTorch image as an example.
You can define the name for the new converted Singularity container by yourself.
But the name of the source Docker container has to match to the one that exists in the original repository.
So have the address right.
Check the documentation about running containers and creating Singularity containers from DocsCSC.
:::

# Singularity containers as installation method
- Singularity is a good option in cases where installation is
otherwise problematic:
  - Complex installations with many dependencies
  - Obsolete dependencies incompatible with general environment
    - Still needs to be kernel compatible
- Should be considered even when other methods exist

:::info (speech)
It is quite clear already, that Singularity containers provide a convenient installation method, especially in HPC environments.
If the software exists as a container, use that and you do not need to worry about the dependencies, because they can get very complex sometimes.
Also some old versions of the dependency software may be incompatible with the host environment.
For example with scientific publications, it is important that you can reproduce the results even after a few years. 
Going back to same data analysis – with same libraries and versions – after many years could get tricky. 
With containers you can ensure that you have the same image, and running it leads to similar results. 
Consider using containers even though other methods were available.
:::

# Just a random example (FASTX-toolkit)
- Tried different installation methods:
  - Native: 47 files, total size 1,9 MB
  - Conda: 27464 files, total size  1,1 GB 
  - Singularity: 1 file, total size 339 MB
- Containers are not the solution for everything, but they do have their uses…

:::info (speech)
Here is an example of a software that has three methods of installation in CSC computing environment. 
The first one is the native application compiled from the source code.
When installed it consists of 47 files with total size of 1.9 MB. 
The second option in comparison is Conda, which is quite easy to use.
Installing the same software with Conda results in 27000 files with total size of 1.1 GB. 
With so many files it hammers the Lustre file system, and the whole Puhti slows down.
We have written a DocsCSC page telling why you should not use Conda.
Then the point of this comparison: Singularity container.
There you have only one file - the container image - with total size of 339 MB.
So containers may get quite big, which may limit the usability sometimes.
But remember that the container has also the dependencies installed.
With only one file it is Lustre-friendly and user-friendly.
:::

# Building a new Singularity container (1/2)
- ‼️ Requires root access: Can not be done directly in e.g. Puhti

- 1. Build a basic container in sandbox mode (`--sandbox`)
    - Uses a folder structure instead of an image file
- 2. Open a shell in the container and install software
  - Depending on base image system, package managers can be used to install 
    libraries and dependencies (`apt install` , `yum install` etc)
  - Installation as per software developer instructions

:::info (speech)
In case you don't find a container that you want to use, you might need to build your own.
It is a bit more involved process, and requires root access so you need to use your own computer.
You can start the building with the sandbox mode - if you want.
Open a shell inside the container to do the software installations.
If the base system is Ubuntu, you can use apt – or then in CentOS use yum – to install packages and dependencies.
Consult software developer documentation for spesific instructions.
:::

# Building a new Singularity container (2/2)
- 3. Build a production image from the sandbox
- 4. (optional) Make a definition file and build a production image from it
  - Mostly necesary if you wish to distribute your container wider
  - Also helps with updating and re-using containers
- Production image can be transferred to e.g. Puhti and run with user rights

:::info (speech)
You can build the production image using the sandbox version.
Another option is that you write a definition file, which is kind of a recipe of the container.
Once you have the production image, you can transfer it to CSC environment and start working. 

The tutorials about containers continue from here. 
They cover the basic use cases with easy-to-follow examples.
Container documentation covers the introduction to containers including technical details.
:::
