---
theme: csc-2019
lang: en
---

# Modules and preinstalled software {.title}

Module systems and how to use them in CSC supercomputers.
Same information can be found in [the module section of our user guide at docs.csc.fi](https://docs.csc.fi/computing/modules/)

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

# Module systems in supercomputers

- Several softwares with different (possibly conflicting) requirements are needed in one supercomputer
- The solution for managing this situation: separate the applications in *modules*
- *Environment modules* set up everything required by a particular application:
   -  Load libraries, adjust path, set environment variables 
- CSC uses [*Lmod*](https://lmod.readthedocs.io/en/latest/) environment modules, which are using *Lua* programming language

# How to access preinstalled software in CSC supercomputers

- You can check the available applications and their respective modules in the [Application list](https://docs.csc.fi/apps/)
   - Each application docs page should contain information on usage
- You can use `module spider` to search for an application
- Use the software by loading the module: `module load modulename`
   - For example: `module spider gromacs-env`

# How to use modules (1/2)

- The general syntax is simple: `module command modulename`   
   - [List of most common commands](https://docs.csc.fi/computing/modules/#module-commands-table)
- These modules are used both in *interactive* and *batch jobs*
   - Include `module purge` and `module load modulename` in your batch scripts to always get the same modules in consecutive batch jobs
- You can't just load all the modules because of possible conflicting dependencies

# How to use modules (2/2)

- These commands will help you navigating the module environment:
   - `module list`: See the list of modules loaded at the moment
   - `module avail`: Modules available at the moment (due to depencies - hides modules that can't be loaded atm)
   - `module spider name`: Search for an application in the list of all existing modules
   - `module spider name/version`: Gives information on how to load the module (prerequisites etc).
- If you try to load a module that is not available, you will get an error message saying so 

# Various kinds of modules

- Some modules contain software that has a graphical user interface
   - For example chemistry visualisation software [Molden](https://docs.csc.fi/apps/molden/)
   - Use [Puhti Web Interface](https://puhti.csc.fi) or [other connection with GUI](https://docs.csc.fi/computing/connecting/#using-graphical-applications)
- Some modules contain software that provide a command line interface
   - For example [zstd module](https://docs.csc.fi/support/tutorials/env-guide/packing-and-compression-tools/#zstandard-compression-tool)

- A module may contain only one software/application (e.g. `gromacs-env`), and some software can be found in many different modules (e.g. `gdal`)
- Some modules provide you with a collection of softwares or eg. Python or R packages
   - For example [Bioconda](https://docs.csc.fi/apps/bioconda/), [Geoconda](https://docs.csc.fi/apps/geoconda/#using-geoconda) or [Python Data](https://docs.csc.fi/apps/python-data/)

# Conda, Python and R packages
- Some preinstalled software are distributed using [Conda](https://docs.conda.io/en/latest/) package management tool
   - See [Conda best practices](https://docs.csc.fi/support/tutorials/conda/) in CSC HPC environment
   - Do not create own Conda environments - run those in a [container](https://docs.csc.fi/support/tutorials/singularity-scratch/)

- Preinstalled Python packages are available in [Python-related modules](https://docs.csc.fi/apps/python/) 
   - See the Docs CSC for packages you want and the usage details
   - it is not possible to load multiple modules with Python packages at once
   - Command `pip list` shows a [list of packages](https://pip.pypa.io/en/stable/cli/pip_list/) installed within the current environment

- Instructions on [how to check installed R-libraries](https://docs.csc.fi/apps/r-env-singularity/#r-package-installations) in DocsCSC
   - RStudio shows available packages in the sidebar
  
# Customizing own environment
- If you "always" use some modules, it is possible to add loading them to `.bashrc`, but **we do not recommend this**
   - This causes the modules to be loaded always, also in batch jobs and likely will cause hard-to-spot issues later
   - If you already did this, see the [`csc-env` command FAQ](https://docs.csc.fi/support/tutorials/using_csc_env/)
- If it feels cumbersome to give the `module load this and that` at the start of each session, you can put these commands in an _alias_ in your `.bashrc`
   - _e.g._ add this line in your _.bashrc_ `alias setmyenv='module load this and that'`
   - Now, you can load all those modules simply with `setmyenv` (after logging out and back in)

# [Advanced module use](https://docs.csc.fi/computing/modules/#advanced-topics)

- You can save your current module set (`module save filename`) and load it (`module restore filename`)
- You can also write your own module files: 
    1. Add them in your home directory (`$HOME/modulefiles`) and 
    2. Add the path to the module search path (`module use $HOME/modulefiles`)
- To study existing module files: command `module show module-name` shows also the filename of the module file
