---
theme: csc-eurocc-2019
lang: en
---

# Introduction to Apptainer/Singularity containers {.title}

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All materials (c) 2020-2023 by CSC – IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# The one-slide lecture
- Some software packages on the CSC supercomputers are installed as containers
  - May cause some changes to usage
  - See the instructions for each software for details
- Containers provide an easy way for you to install software
  - A single-command installation if a suitable Docker or Apptainer/Singularity container exists

# Containers
- Containers are a way of packaging software and its dependencies (libraries, etc.)
- Popular container engines include Docker, Apptainer (previously called Singularity), Shifter
- Apptainer is the most popular in HPC environments

# Containers vs. Virtual Machines (1/2)
<div style="text-align:center"><img src="./img/containers-fig1.png" /></div>

# Containers vs. Virtual Machines (2/2)
- Virtual machines can run a totally different OS than the host computer
(e.g. Windows on a Linux host or vice versa)
- Containers share the kernel with the host, but they can have their own libraries 
  - They can run, e.g., a different Linux distribution than the host

# Container benefits: Ease of installation
- Containers are becoming a popular way of distributing software
  - A single-command installation
  - All dependencies are included, so more portable
  - Normal user rights are enough when using an existing container
- Root access on build system is enough
  - Root access, package managers (yum, apt, etc) can be utilized even
  when not available on the target system.
  - Makes installing libraries easier

# Container benefits: Environment isolation
- Containers use the host system kernel, but they can have their own bins/libs layer
  - Can be a different Linux distribution that the host
  - Can solve some incompatibilities
  - Less likely to be affected by changes in the host system
  
# Container benefits: Enviroment reproducibility
- Analysis environment can be saved as a whole
  - Useful with, e.g., Python, where updating underlaying 
  packages (NumPy, etc) can lead to differences in the behavior  
- Sharing with collaborators is easy (a single file)

# Apptainer in a nutshell
- Containers can be run with user-level rights
  - But: building new containers requires root access
- Minimal performance overhead
- Supports MPI
  - Requires containers tailored to the host system
- Can use host driver stack (Nvidia/CUDA)
  - Add the option `--nv`
- Can import and run Docker containers
  - Running Docker directly would require root rights

# Apptainer on the CSC servers
- Apptainer jobs should be run as batch jobs or with `sinteractive`
- No need to load a module
- Users can run their own containers
- Some CSC software installations are provided as containers
  - See the software pages for details

# Running Apptainer containers: Basic syntax
- Execute a command in the container
  - `apptainer exec [exec options...] <container> <command>`
- Run the default action (runscript) of the container
  - Defined when the container is built
  - `apptainer run [run options...] <container>`
- Open a shell in the container
  - `apptainer shell [shell options...] <container>`

# File system
- Containers have their own internal file system (FS)
  - The internal FS is always read-only when executed with user-level rights 
- To access host directories, they need to be mapped to container directories
  - E.g., to map host directory `/scratch/project_12345` to directory `/data` 
  inside the container: `--bind /scratch/project_12345:/data`
  - The target directory inside the container does not need to exist. It is created if
necessary
  - More than one directory can be mapped

# Environment variables
- Most environment variables from the host are inherited by the container
- That can be prevented, if necessary, by adding the option `--cleanenv`
- Environment variables can be set specifically inside the container by 
setting on the host `$SINGULARITYENV_variablename`.
  - E.g., to set `$TEST` in a container, set `$SINGUALRITYENV_TEST` on the host

# apptainer_wrapper
- Running containers with `apptainer_wrapper` takes care of the most common `--bind` commands
  - `apptainer_wrapper exec image.sif myprog <options>`
- If the environment variable `$SING_IMAGE` is set with the path to the image, even the image file can be omitted
  - `apptainer_wrapper exec myprog <options>`

# Using Docker containers with Apptainer
- You can build an Apptainer container from a Docker container with normal user rights:
  - `apptainer build <image> docker://<address>:<tag>`
- For example:
  - `apptainer build pytorch_19.10-py3.sif docker://nvcr.io/nvidia/pytorch:19.10-py3`
- Documentation in Docs:
  - [Running Apptainer containers](https://docs.csc.fi/computing/containers/run-existing/)
  - [Creating Apptainer containers](https://docs.csc.fi/computing/containers/creating/)
  - [Using tykky to create Apptainer containers](https://docs.csc.fi/computing/containers/tykky/)

# Apptainer containers as an installation method
- Apptainer is a good option in cases where the installation is
otherwise problematic:
  - Complex installations with many dependencies
  - Obsolete dependencies incompatible with general environments
    - Still needs to be kernel-compatible
- Should be considered even when other methods exist

# Just a random example (FASTX-toolkit)
- Tested installation methods:
  - Native: 47 files, total size 1,9 MB
  - Conda: 27464 files, total size  1,1 GB 
  - Apptainer: 1 file, total size 339 MB
- Containers are not the solution for everything, but they do have their uses…

# Building a new Apptainer container (1/2)
- ‼️ Requires root access: Can not be done directly in, e.g., Puhti

- 1. Build a basic container in sandbox mode (`--sandbox`)
    - Uses a folder structure instead of an image file
- 2. Open a shell in the container and install the software
  - Depending on base image system, package managers can be used to install 
    libraries and dependencies (`apt install` , `yum install` etc)
  - Installation as per the software developer instructions
  
# Building a new Apptainer container (2/2)
- 3. Build a production image from the sandbox
- 4. (optional) Make a definition file and build a production image from it
  - Mostly necesary if you wish to distribute your container 
  - Also helps with updating and re-using containers
- The production image can be transferred to, e.g., Puhti and can be run with user rights

