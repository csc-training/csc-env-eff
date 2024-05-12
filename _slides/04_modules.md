---
theme: csc-eurocc-2019
lang: en
---

# Modules and pre-installed software {.title}

The module system and how to use it on CSC supercomputers.
The same information can be found in [the module section of Docs CSC](https://docs.csc.fi/computing/modules/).

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

# Module systems in supercomputers

- A variety of software with different (possibly conflicting) requirements are needed on a supercomputer
- The solution for managing this situation: separating the applications into *modules*
- *Environment modules* set up everything required by a particular application:
   -  Load libraries, adjust paths, set environment variables
- CSC uses [*Lmod*](https://lmod.readthedocs.io/en/latest/) environment modules which are based on the *Lua* programming language

# How to access pre-installed software on CSC supercomputers

- You can check the available applications and their respective modules in the [application list](https://docs.csc.fi/apps/)
   - Each application page in Docs CSC contains information on basic usage
- You can use `module spider` to search for an application
  - On LUMI you need to first run `module use /appl/local/csc/modulefiles` to see modules installed by CSC
- Use the software by loading the module: `module load modulename`
   - For example: `module load gromacs-env`

# How to use modules

- The general syntax is simple: `module command modulename`
   - [List of the most common commands](https://docs.csc.fi/computing/modules/#module-commands-table)
- These modules are used both in *interactive sessions* and *batch jobs*
   - Include `module purge` and `module load modulename` in your batch scripts to always get the same modules in consecutive jobs
- You can't just load all the modules because of possibly conflicting dependencies

# Useful commands for the module environment

- These commands will help you navigate the module environment:
   - `module list`: See a list of the currently loaded modules
   - `module avail`: Modules currently available for loading (hides modules that can't be loaded at the moment due to dependencies)
   - `module spider modulename`: Search for an application in the list of all existing modules
   - `module spider modulename/version`: Gives information on how to load a specific version of a module (prerequisites *etc.*)
- If you try to load a module that is unavailable, you will get an error message

# Various kinds of modules

- Some modules contain software that have a graphical user interface
   - For example, the chemistry visualization software [VMD](https://docs.csc.fi/apps/vmd/)
   - Use the [Puhti](https://www.puhti.csc.fi) or [Mahti web interface](https://www.mahti.csc.fi), or [another method to open the GUI](https://docs.csc.fi/computing/connecting/#using-graphical-applications)
- Some modules contain software that only provide a command-line interface
   - For example, the [OpenBabel module](https://docs.csc.fi/apps/openbabel/)
- A module might contain only one program (*e.g.* `gromacs-env`), while some provide a collection of applications (*e.g.* Python or R packages)
   - For example, [Geoconda](https://docs.csc.fi/apps/geoconda/) and [Python Data](https://docs.csc.fi/apps/python-data/)

# Conda, Python and R packages

- Some pre-installed software are distributed through the [Conda](https://docs.conda.io/en/latest/) package management tool
   - Do not install Conda environments directly on the Lustre parallel file system, [containerize](https://docs.csc.fi/support/tutorials/singularity-scratch/) them instead using *e.g.* [Tykky](https://docs.csc.fi/computing/containers/tykky/)
   - See the [usage policy](https://docs.csc.fi/computing/usage-policy/#conda-installations) for further details
- Pre-installed Python packages are available in [Python-related modules](https://docs.csc.fi/apps/python/)
   - Check Docs CSC for the available packages and usage instructions 
   - It is not possible to load multiple modules with Python packages at once
   - `pip list` shows a [list of packages](https://pip.pypa.io/en/stable/cli/pip_list/) installed in the current environment
- Instructions on [how to check installed R libraries](https://docs.csc.fi/apps/r-env/#r-package-installations)
   - RStudio shows available packages in the sidebar
  
# Customizing your own environment

- If you "always" use certain modules, it is possible to load them in your `.bashrc`, but **we do not recommend this**
   - This causes the modules to be always loaded, also in batch jobs which may cause hard-to-spot issues
   - If you already did this, see the [`csc-env`](https://docs.csc.fi/support/tutorials/using_csc_env/) command
- If it feels cumbersome to run multiple `module load modulenames` at the start of each session, you can define an *alias* for these in your `.bashrc`
   - Add this line to your `.bashrc`: `alias mods="module load modulenames"`
   - Now you can load all those modules easily with `mods` (after sourcing your `.bashrc` or logging out and in again)

# [Advanced module use](https://docs.csc.fi/computing/modules/#advanced-topics)

- You can save your current set of modules with `module save filename` and load it later with `module restore filename`
- You can also write your own module files:
    1. Add them to your home directory (`$HOME/modulefiles`)
    2. Add this path to the module search path (`module use $HOME/modulefiles`)
- To see the parameters of a module file, use the command `module show modulename`
