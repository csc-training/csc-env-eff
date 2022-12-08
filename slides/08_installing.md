---
theme: csc-eurocc-2019
lang: en
---

# Installing own software {.title}

This topic is about installing your own software on the CSC servers.

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All material (C) 2020-2022 by CSC -IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# The one-slide lecture

- It is possible for users to install software on the CSC supercomputers
- If you don't know how or run into problems while trying, contact servicedesk@csc.fi

# Code categories

- Start by reading the software documentation
  - The installation method depends on code type (or category)
  - Instructions found on the web rarely work as "copy/paste" in an HPC environment
- Before doing a lot of work, check if an alternative software is already available in the [CSC application list](https://docs.csc.fi/apps/)
  - Also check with `module spider`

# Binaries

- If you have ready-made binaries, you can just try to run them
- The problem with ready made binaries is that they are hardly ever optimal for the computer they are used on
  - Especially MPI codes should always be re-compiled
- Ready binaries can be considered if
  - The source code is not available
  - The software is compiled on an identical computer 
  - The software is for relatively light (serial or threaded) computation

# Interpreted languages

- Examples of high-level interpreted languages are
  -  Python, Java, Perl, R etc. 
- These languages do not need to be compiled, but they often can be. 
- Running these programs often requires loading a suitable module for the language
  - Loading modules also ensures the software behaves the same in the compute nodes

# High-Performance-Computing languages

- Programming languages that need a compiler 
   - Typical examples are _e.g._ C, C++, and Fortran. 
- Most resource-intensive software has been programmed with them
- As a researcher, you typically _only_ need to compile them (unless already available) 
  - Can sometimes be complicated
  - If you run into problems, contact servicedesk@csc.fi

# Some general notes

- No `sudo` for normal users on the CSC computers
  - You can't use package managers (`apt`, `yum`, etc)
  - You can't install in "standard" locations (/usr/bin, /usr/lib, etc)
    - Set the installation directory to `/projappl` or similar (see the software documentation for details)
- Start by loading the suitable compiler suite or language module
  - Many commonly used libraries are available as modules
- New software is not automatically added to `$PATH`
  - Provide the path when running or add it to `$PATH`

# Installation methods: Native installations

- Installing directly to the system
- Usually the preferred way for software with few or no dependencies

# Installation methods: Containers

- [Containers](09_singularity.html) are an easy method to install software and its dependencies
  - Especially if a ready-made container is available
- Recommended particularly for software with complex dependencies

# Installation methods: Conda

- Conda is a common installation system, but it is problematic on HPC systems
  - Creates a huge number of files and leads to bad performance on the Lustre FS
  - Installations easily break when the system changes
- Containers are preferred
  - It is possible to wrap Conda installations into a container. This alleviates some of the problems
  - CSC has created [a tool called `tykky`](https://docs.csc.fi/computing/containers/tykky/) which does this automatically

# Testing - it's important to test _first_

- Construct a [batch job script](05_batch_jobs.html)
- Make a short and simple test run
  - Use known test data, e.g., test data provided by the code developer if you use a ready-made code
  - Run a tutorial provided with the code
- Run your test in the `test` queue or in an [interactive session](https://docs.csc.fi/computing/running/interactive-usage/) directly from the command line
- Compare performance and results to existing data (your old data, reference from the web, etc)

# More information 

- See the tutorials for each category for more detailed instructions
  - [Installation tutorials](https://csc-training.github.io/csc-env-eff/#8-installing-your-own-software)
- Check the CSC Docs pages:
  - [Compiling applications in Puhti](https://docs.csc.fi/computing/compiling-puhti/)
  - [Compiling applications in Mahti](https://docs.csc.fi/computing/compiling-mahti/)
  - [High-performance libraries](https://docs.csc.fi/computing/hpc-libraries/)
- Lots of information online
  - Try searching for the error messages you come across
