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
All materials (c) 2020-2024 by CSC – IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# The one-slide lecture

- It is possible for users to install software on the CSC supercomputers
  - [Docs CSC page about installing own software](https://docs.csc.fi/computing/installing/)
- If you don't know how or run into problems while trying, contact <servicedesk@csc.fi>
  - For LUMI-related queries, [contact the LUMI User Support Team](https://lumi-supercomputer.eu/user-support/need-help/)

# Code categories

- Start by reading the software documentation
  - The installation method depends on code type (or category)
  - Instructions found online rarely work as "copy/paste" in an HPC environment
- Before doing a lot of work, check if an alternative software is already available in the [CSC application list](https://docs.csc.fi/apps/)
  - Also check with `module spider`

# Binaries

- If you have ready-made binaries, you can simply try to run them
- The problem with ready-made binaries is that they are hardly ever optimal for the computer they are used on
  - Especially MPI codes should always be re-compiled for best performance
- Ready binaries can be considered if
  - The source code is not available
  - The software is compiled on an identical computer
  - The software is for relatively light (serial or threaded) computation

# Interpreted languages

- Examples of high-level interpreted languages are
  -  Python, Java, Perl, R, etc.
- These languages do not _need_ to be compiled, but they often can be
- Running these programs usually requires loading a suitable module for the language
  - Loading modules ensures also that the software will run the same on the compute nodes

# High-performance computing languages

- Programming languages that need to be compiled
   - Typical examples are _e.g._ C, C++ and Fortran
- Most resource-intensive software have been programmed using these
- As a researcher, you typically _only_ need to compile a software (unless available pre-installed)
  - Can sometimes be complicated
  - If you run into problems, contact <servicedesk@csc.fi>

# About compilers and profiling

- A compiler is a special program that reads, analyses and translates a human-readable source code into a machine-readable object code
- It performs 4 steps: Lexical analysis, syntactic and semantic analysis, optimization and output code generation
- Compilers target specific operating systems and computer architectures and
  are usually programming language-specific
- **Code profiling**: Analysis of an application (memory, CPU, network utilized) to understand its performance
  - Checking how much time is spent in different software routines is important to identify performance bottlenecks (don't optimize before this!)

# Some general notes

- No `sudo` available for users on the CSC supercomputers
  - You can't use package managers (`apt`, `yum`, etc.)
  - You can't install into "standard" locations (`/usr/bin`, `/usr/lib`, etc.)
    - Set the installation directory to `/projappl` or similar
- Start by loading a suitable compiler suite or language module
  - Many commonly used [HPC libraries](https://docs.csc.fi/computing/hpc-libraries/) (e.g. OpenMPI, ScaLAPACK, FFTW) are available as modules (search with `module spider`)
- Compile on the fast local disk (`$TMPDIR`) to avoid stressing Lustre
- New software is not automatically added to `$PATH`
  - Include the full path or add with `export PATH="/path/to/my/sw:$PATH"`

# Installation methods: Native installations

- Installing directly to the system
- Usually the preferred way for software with few or no dependencies

# Installation methods: Containers

- [Containerization](09_singularity.html) is an efficient method to install software and their dependencies
  - Very easy if a ready-made container is available
- Recommended particularly for software with complex dependencies

# Installation methods: Conda

- Conda is a common installation system, but it is very problematic on HPC systems
  - Creates a huge number of files and leads to poor performance on the Lustre parallel file system
  - Installations easily break when the system changes
- Containerization is required if you intend to use Conda environments on CSC supercomputers (see [usage policy](https://docs.csc.fi/computing/usage-policy/#conda-installations))
  - Wrapping Conda installations into a container alleviates problems since the number of files is dramatically decreased from the FS point of view
  - CSC has created [a tool called Tykky](https://docs.csc.fi/computing/containers/tykky/) which does the containerization automatically and transparently

# Testing -- it's important to test _first_

- Construct a [batch job script](05_batch_jobs.html) for a short and simple test run
  - Use known example/benchmark data provided, e.g., by the code developer (if you did not develop the code yourself)
  - Run a tutorial provided with the software
- Run your test in the `test` queue or in an [interactive session](https://docs.csc.fi/computing/running/interactive-usage/) directly from the command-line
- Compare performance and results to existing data (your old data, online references, etc.)

# More information 

- See the tutorials for each category for more detailed instructions
  - [Installation tutorials](https://csc-training.github.io/csc-env-eff/#8-installing-your-own-software)
- Check the Docs CSC pages:
  - [Installation overview](https://docs.csc.fi/computing/installing/)
  - Compiling applications in [Puhti](https://docs.csc.fi/computing/compiling-puhti/) and [Mahti](https://docs.csc.fi/computing/compiling-mahti/)
  - [High-performance libraries](https://docs.csc.fi/computing/hpc-libraries/)
  - [Software installation on LUMI](https://docs.lumi-supercomputer.eu/software/)
- Lots of information online
  - Try searching for any error messages you come across
  - [More about optimizing compiler options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)    
