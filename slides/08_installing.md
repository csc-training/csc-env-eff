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

# The one-slide lecture

- It is possible for users to install software on CSC supercomputers
- If you don't know how, or run into problems while trying, contact servicedesk@csc.fi

# Code categories

- Start by reading the software documentation
  - Installation method depends on code type (or category)
  - Instructions found on the web rarely work "copy/paste" in HPC environment
- Before doing a lot of work, check if an alternative software is already available in [CSC application list](https://docs.csc.fi/apps/)
  - Also check with `module spider`

# Binaries

- If you have ready made binaries, you can just try to run them
- The problem with ready made binaries is that they are hardly ever optimal for the computer they are used on
  - Especially MPI codes should always be re-compiled
- Ready binaries can be considered if
  - Source code not available
  - Software is compiled on an identical computer 
  - Software is for relatively light (serial or threaded) computation

# Interpreted languages

- Examples of High-level interpreted languages are
  -  Python, Java, Perl, R etc. 
- These languages do not need to be compiled, but they often can be. 
- Running these programs often requires loading a suitable module for the language
  - Loading modules also ensures the software behaves the same in the compute nodes

# Interpreted languages (continued)

- Some notes on code development/selection:
  - Interpreted languages are often quite easy and efficient to program and therefore to get a result, but for very extensive computations they are rarely optimal (and can easily be very far from optimal). 
  - An efficient code should be constructed so that heavy computations utilize libraries and/or subroutines written in High-Performance-Computing programming languages

# High-Performance-Computing languages

- Programming languages that need a compiler 
   - Typical examples are _e.g._ C, C++, and Fortran. 
- These languages are not easy to program and for complicated tasks need quite a lot of experience and much work.
- Most of the resource intensive software have been programmed with these
- As a researcher, you typically _only_ need to compile them (unless already available) 

# Basic requirements

- You need a computer with a decent internet connection.
- You need a CSC account and need to be [part of a project](https://research.csc.fi/accounts-and-projects)
- You need to [log in to a CSC computer](https://docs.csc.fi/computing/connecting/)
- You need to know, at least basic, Unix/Linux line commands 
  - CSC's [Linux basics tutorial](https://docs.csc.fi/support/tutorials/env-guide/using-linux-in-command-line/)
  - [Linux Command line quick reference / Cheat Sheet](https://docs.csc.fi/img/csc-quick-reference.pdf)

# Some general notes

- No `sudo` for normal users in CSC machines
  - You can't use package managers (`apt` , `yum`, etc)
  - You can't install in "standard" locations (/usr/bin, /usr/lib, etc)
    - Set installation directory to `/projappl` or similar (see software documentation for details)
- Start by loading suitable compiler suite or language module
  - Also many commonly used libraries available as modules
- New software is not automatically added to `$PATH`
  - Provide path when running or add to `$PATH`

# Installing

- See tutorials for each category for more detailed instructions
  - [Installation tutorials](https://csc-training.github.io/csc-env-eff/#8-installing-your-own-software)
- Applications may also be available as [containers](09_singularity.html), which can be used in CSC environment.

# Testing - it's important to test _first_

- Construct a [batch job script](05_batch_jobs.html)
- Make a short and simple test run
  - Use known test data, e.g. test data provided by the code developer if you use a ready made code.
  - Run a tutorial provided with the code
- Run your test in the `test` queue or in an [interactive session](https://docs.csc.fi/computing/running/interactive-usage/) directly from the command line
- Compare performance and results to existing data (your old data, reference from the web, ...)

# More information 

- Check CSC Docs pages:
  - [Compiling applications in Puhti](https://docs.csc.fi/computing/compiling-puhti/)
  - [Compiling applications in Mahti](https://docs.csc.fi/computing/compiling-mahti/)
  - [High performance libraries](https://docs.csc.fi/computing/hpc-libraries/)
- Lot's of information in the net
  - Try searching with error messages from compiling etc