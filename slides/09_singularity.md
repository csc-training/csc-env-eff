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

# The one-slide lecture
- Some software packages on CSC supercomputers are installed as containers
  - May cause some changes to usage
  - See instructions for each software for details
- Containers provide an easy way for you to install software
  - Single command installation if a suitable Docker or Singularity container exists

# Containers
- Containers are a way to package software with its dependencies (libraries, etc)
- Popular container engines include Docker, Singularity, Shifter
- Singularity is the most popular in HPC environments

# Containers vs. Virtual Machines (1/2)
<div style="text-align:center"><img src="./img/containers-fig1.png" /></div>

# Containers vs. Virtual Machines (2/2)
- Virtual machines can run totally different OS than host
(e.g. Windows on Linux host or vice versa)
- Containers share kernel with host, but can have its own libraries etc
  - Can run e.g. different Linux distribution than host

# Container benefits: Ease of installation
- Containers are becoming a popular way to distribute software
  - Single command installation
  - All dependencies included, so more portable
  - Normal user rights enough when using an existing container
- Root access on build system is enough
  - Root access, package managers (yum, apt, etc) can be utilized  even
  when not available in the target system.
  - Makes installing libraries etc. easier

# Container benefits: Environment isolation
- Containers use host system kernel, but can have their own Bins/Libs layer
  - Can be a different Linux distribution that the host
  - Can solve some incompatibilities
  - Less likely to be effected by changes in the host system
  
# Container benefits: Enviroment reproducibility
- Analysis environment can be saved as a whole
  - Useful with e.g. Python, where updating underlaying 
  libraries (Numpy etc) can lead to differences in behavior  
- Sharing with collaborators easy (single file)

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

# Singularity on CSC servers
- Singularity jobs should be run as batch jobs or with `sinteractive`
- No need to load a module
- Users can run their own containers
- Some CSC software installations provided as containers
  - See software pages for details

# Running Singularity containers: Basic syntax
- Execute a command in the container
  - `singularity exec [exec options...] <container> <command>`
- Run the default action (runscript) of the container
  - Defined when the container is built
  - `singularity run [run options...] <container>`
- Open a shell in the container
  - `singularity shell [shell options...] <container>`

# File system
- Containers have their own, internal file system
  - The internal FS is always read-only when run with user level rights 
- To access host directories, they  need to be mapped to container directories
  - E.g. to map host directory `/scratch/project_12345` to directory `/data` 
  inside the container: `--bind /scratch/project_12345:/data`
  - Target directory inside the container does not need to exist. It is created as
necessary
  - More than one directory can be mapped

# Environment variables
- Most environment variables from host are inherited by the container
- Can be prevented, if necessary, by adding option `--cleanenv`
- Environment variables can be set specifically inside the container by 
setting in host `$SINGULARITYENV_variablename`.
  - E.g. to set `$TEST` in container, set `$SINGUALRITYENV_TEST` in host

# singularity_wrapper
- Running containers with `singularity_wrapper` takes care of most common `--bind` commands
  - `singularity_wrapper exec image.sif myprog <options>`
- If environment variable `$SING_IMAGE` is set with the path to the image, even image file can be omitted
  - `singularity_wrapper exec myprog <options>`

# Using Docker containers with Singularity
- You can build a Singularity container from a Docker container with normal user rights:
  - `singularity build <image> docker://<address>:<tag>`
- For example:
  - `singularity build pytorch_19.10-py3.sif docker://nvcr.io/nvidia/pytorch:19.10-py3`
- Documentation in Docs:
  - [Running Singularity containers](https://docs.csc.fi/computing/containers/run-existing/)
  - [Creating Singularity containers](https://docs.csc.fi/computing/containers/creating/)

# Singularity containers as installation method
- Singularity is a good option in cases where installation is
otherwise problematic:
  - Complex installations with many dependencies
  - Obsolete dependencies incompatible with general environment
    - Still needs to be kernel compatible
- Should be considered even when other methods exist

# Just a random example (FASTX-toolkit)
- Tried different installation methods:
  - Native: 47 files, total size 1,9 MB
  - Conda: 27464 files, total size  1,1 GB 
  - Singularity: 1 file, total size 339 MB
- Containers are not the solution for everything, but they do have their uses…

# Building a new Singularity container (1/2)
- ‼️ Requires root access: Can not be done directly in e.g. Puhti

- 1. Build a basic container in sandbox mode (`--sandbox`)
    - Uses a folder structure instead of an image file
- 2. Open a shell in the container and install software
  - Depending on base image system, package managers can be used to install 
    libraries and dependencies (`apt install` , `yum install` etc)
  - Installation as per software developer instructions
  
# Building a new Singularity container (2/2)
- 3. Build a production image from the sandbox
- 4. (optional) Make a definition file and build a production image from it
  - Mostly necesary if you wish to distribute your container wider
  - Also helps with updating and re-using containers
- Production image can be transferred to e.g. Puhti and run with user rights

