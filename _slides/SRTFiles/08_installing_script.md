---
theme: csc-2019
lang: en
---

# Installing own software {.title}

This topic is about installing your own software on CSC servers.

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
This topic is about installing your own software on CSC servers.
:::

# The one-slide lecture

- It is possible for users to install software on CSC supercomputers
- If you don't know how, or run into problems while trying, contact servicedesk@csc.fi

:::info (speech)
The take home message is that you can install software on CSC supercomputers. 
There might be an application that is not already installed on Puhti or Mahti.
Or you might have implemented a program yourself, and you want to use that in Puhti.
This lecture gives an overview of different types of software and installation methods.
Remember that you can always contact servicedesk@csc.fi for guidance.
Especially, if the program you are trying to install is very complicated, or requires compiling it from a source code. 
:::

# Code categories

- Start by reading the software documentation
  - Installation method depends on code type (or category)
  - Instructions found on the web rarely work "copy/paste" in HPC environment
- Before doing a lot of work, check if an alternative software is already available in [CSC application list](https://docs.csc.fi/apps/)
  - Also check with `module spider`

:::info (speech)
The most important thing to begin with is: to read the software documentation. 
How the software is installed depends a lot on what type of code you are trying to install. 
It might be just a Python package, or then it is a large parallel program.
Note that in general simple copy and paste examples from the internet do not work in an HPC environment. 
Before you invest a lot of effort and time into trying to install something, it is a better option to check out the CSC application list.
Also remember that with command module spider you can see software available in CSC supercomputing environment.
It may well be that there is some other program - similar to the one you would like to use - already installed.
:::

# Binaries

- If you have ready made binaries, you can just try to run them
- The problem with ready made binaries is that they are hardly ever optimal for the computer they are used on
  - Especially MPI codes should always be re-compiled
- Ready binaries can be considered if
  - Source code not available
  - Software is compiled on an identical computer 
  - Software is for relatively light (serial or threaded) computation

:::info (speech)
If your application is a single binary file, you can try to run it on the CSC supercomputer. 
Usually these binaries may not be suitable or efficient in HPC environments. 
If they are compiled on a laptop, they are optimized for a laptop, and not for a supercomputer. 
Especially if your program is massively parallelized - like MPI codes which run on multiple nodes - it must be recompiled for the best performance. 
Binary file might be the only option, if the source code is not available.
They might work fine, if the program has been compiled on an identical HPC system, or if it is a very simple program, that runs for example lightweight serial or threaded processes.
:::

# Interpreted languages

- Examples of High-level interpreted languages are
  -  Python, Java, Perl, R etc. 
- These languages do not need to be compiled, but they often can be. 
- Running these programs often requires loading a suitable module for the language
  - Loading modules also ensures the software behaves the same in the compute nodes

:::info (speech)
Different kind of programs can be categorised based on the used programming languages. 
The highest level of programming languages are the interpreted languages.
For example Python, Java, and R, are all interpreted coding languages.
The main advantage of those is that they are easy to program, and they do not need to be compiled.
If performance is an issue, e.g. Python can be compiled to a faster C-code using cython.
Programming – and running programs – based on interpreted languages usually require loading specific modules on the CSC supercomputers.
E.g. Python module enables access to some of the most important Python libraries. 
It also ensures that the software behaves the same on all the compute nodes. 

If the computational problem you are dealing with is very complicated, then interpreted languages are usually not the best option, because they are not efficient for numerically heavy tasks. 
To do heavy tasks somewhat efficiently with interpreted languages, make sure you utilize libraries to perform some of the most demanding computational tasks.
There might be high performance computing libraries, or libraries that have been written using high performance computing programming languages. 
:::

# High-Performance-Computing languages

- Programming languages that need a compiler 
   - Typical examples are _e.g._ C, C++, and Fortran. 
- Most of the resource intensive software have been programmed with these
- As a researcher, you typically _only_ need to compile them (unless already available) 
  - Can sometimes be complicated
  - If you run into problems, contact servicedesk@csc.fi

:::info (speech)
These programming languages do not run as such, but when they are compiled and run, they have great performance.
Examples of HPC languages are e.g. C, C++, and FORTRAN. 
It requires some experience to write efficient codes with HPC languages.
They are not so easy to program, and the syntax might not be so simple. 
Most of very resource intensive scientific applications have been programmed using HPC languages – because they are good in heavy number crunching, linear algebra and such tasks.
If someone - a person involved with method development - has already implemented the program, then researchers need only to compile the code.
If you consider compiling complicated, contact servicedesk.
:::

# Some general notes

- No `sudo` for normal users in CSC machines
  - You can't use package managers (`apt`, `yum`, etc)
  - You can't install in "standard" locations (/usr/bin, /usr/lib, etc)
    - Set installation directory to `/projappl` or similar (see software documentation for details)
- Start by loading suitable compiler suite or language module
  - Also many commonly used libraries available as modules
- New software is not automatically added to `$PATH`
  - Provide path when running or add to `$PATH`

:::info (speech)
There are some things to keep in mind, when installing custom software on the CSC supercomputers.
It is not the same as installing something on your own computer. 
For example you can not use sudo for getting root privileges.
Also you can not use package managers like apt or yum.
Then you don't have permissions to install into default locations.
Instead custom installations should go to the PROJAPPL directory - where you have write access. 

When you start to compile your application, you should first load required compiler suites or language modules. 
When you install custom software, it is not automatically added to the PATH.
That means you can't run the program from anywhere – without providing the path to the binary file.
:::

# Installation methods: Native installations

- Installing directly to system
- Usually preferred way for software with few or no dependencies

:::info (speech)
If you install software directly to the system, it is called native installation.
That would be for example the binary file, that you have compiled and run.
It is a good way of installing, if the program does not have many dependencies.
:::

# Installation methods: Containers

- [Containers](09_singularity.html) are an easy method to install software and it's dependencies
  - Especially if a ready container is available
- Recommended especially for software with complex dependencies

:::info (speech)
Applications can also be available as containers.
Containers provide a convenient way of installing software and its dependencies.
There are many containers available in public.
Please consider using containers – even if other installation methods were available.
See the container lecture and the documentation for more information.
:::

# Installation methods: Conda

- Conda is a common installation system, but it is problematic on HPC systems
  - Creates a huge number of files and leads to bad performance on Lustre fs
  - Installations easily break when system changes
- Containers are preferred
  - It is possible to wrap Conda installations into a container. This alleviates some of the problems

:::info (speech)
Conda is a package manager used especially for many Python packages.
It is very popular, but unfortunately it is also problematic in HPC systems.
A Conda environment contains a huge number of files, which really slows down Lustre file system.
They are also difficult to maintain, because of many dependencies.
Containers are a preferred installation method, because they package everything in a single file.
Also Conda installations can be put into a container and used in HPC environment.
:::

# Testing - it's important to test _first_

- Construct a [batch job script](05_batch_jobs.html)
- Make a short and simple test run
  - Use known test data, e.g. test data provided by the code developer if you use a ready made code.
  - Run a tutorial provided with the code
- Run your test in the `test` queue or in an [interactive session](https://docs.csc.fi/computing/running/interactive-usage/) directly from the command line
- Compare performance and results to existing data (your old data, reference from the web, ...)

:::info (speech)
Check out the batch job lecture for details on submitting batch jobs.
Test the software with short batch jobs.
It you submit a long and heavy job with no knowledge of how it works, you are wasting time and resources - not only yours but other users and admins as well.
Try to reproduce some results that you know beforehand.
That way you can deduce whether the program works as intended.
Some software might have a tutorial that you can run.
Run your tests in the test queue or in an interactive session.
Check also the efficiency of the code by comparing it to your previous compilations. 
In other words, be sure to benchmark your new software. 
:::

# More information 

- See tutorials for each category for more detailed instructions
  - [Installation tutorials](https://csc-training.github.io/csc-env-eff/#8-installing-your-own-software)
- Check CSC Docs pages:
  - [Compiling applications in Puhti](https://docs.csc.fi/computing/compiling-puhti/)
  - [Compiling applications in Mahti](https://docs.csc.fi/computing/compiling-mahti/)
  - [High performance libraries](https://docs.csc.fi/computing/hpc-libraries/)
- Lot's of information in the net
  - Try searching with error messages from compiling etc

:::info (speech)
The tutorials about installing software have some easy-to-follow examples.
Be sure to check out the documentation in DocsCSC pages.
There is information on how to compile applications in Puhti or Mahti, and how to use different HPC libraries. 
There is also guidelines for loading different compilers. 
For example: whether to compile using an Intel or GNU compiler, what kind of optimization flags you can use, or how to link different HPC libraries to your codes. 
There is of course a lot of information available online. 
If you get some errors or problems in the compilation, copy paste the error messages and Google for some tips. 
Also be sure to contact the servicedesk in case of any issues. 
:::
