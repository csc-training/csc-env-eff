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

:::info (speech)
This lecture presents how to use module systems and preinstalled software in CSC supercomputers.
:::

# Module systems in supercomputers

- Several softwares with different (possibly conflicting) requirements are needed in one supercomputer
- The solution for managing this situation: separate the applications in *modules*
- *Environment modules* set up everything required by a particular application:
   -  Load libraries, adjust path, set environment variables 
- CSC uses [*Lmod*](https://lmod.readthedocs.io/en/latest/) environment modules, which are using *Lua* programming language

:::info (speech)
Applications on the supercomputer are handled a bit differently compared to a regular PC. 
A supercomputer must fulfill the needs of different applications and software, used in different scientific purposes. 
All of these software have also different dependencies and libraries, that they are linked to. 
Some of the dependencies may also be conflicting, which can create a lot of problems. 
On a supercomputer you cannot load all the applications in the start-up, as a normal PC does.
Instead we separate the applications into modules. 
Loading the module environment for a certain application sets up everything, that is needed for that software to work. 
A module loads the relevant libraries, and adjusts path and other environment variables needed for the software. 
CSC supercomputers use Lmod framework for managing environment modules. 
:::

# How to access preinstalled software in CSC supercomputers

- You can check the available applications and their respective modules in the [Application list](https://docs.csc.fi/apps/)
   - Each application docs page should contain information on usage
- You can use `module spider` to search for an application
- Use the software by loading the module: `module load modulename`
   - For example: `module spider gromacs-env`

:::info (speech)
The application list in docs.csc.fi lists all installed software on CSC supercomputers. 
Check the documentation both when: searching whether a spesific application is installed, or how to use one.
All modules are loaded with command module load, but what happens after that depends on the included software.

The command module spider – followed by a module name – finds whether that module exists.
For example to check if program called Gromacs – for molecular dynamics simulations – exists, you can type module spider gromacs-env. 
:::

# How to use modules

- The general syntax is simple: `module command modulename`   
   - [List of most common commands](https://docs.csc.fi/computing/modules/#module-commands-table)
- These modules are used both in *interactive* and *batch jobs*
   - Include `module purge` and `module load modulename` in your batch scripts to always get the same modules in consecutive batch jobs
- You can't just load all the modules because of possible conflicting dependencies

:::info (speech)
The general syntax for using modules is quite simple: module, then the command, and the module name.
Please find a list of most common commands for using modules in the documentation. 
There is commands like module load, module help, module list and so on. 
Whether you are running an interactive job, or submitting a batch job, you always need to load the appropriate modules to use your program.
Always include the module commands in your batch script.
That way you get always the same set of modules in consecutive batch jobs.
It is a good practice to start with module purge - to have a clean slate - and then issue the needed module loads.

The main idea in using modules is that you will not load all the modules simultaneously.
That would cancel the whole idea of avoiding conflicting dependencies. 
:::

# Useful commands for the module environment

- These commands will help you navigating the module environment:
   - `module list`: See the list of modules loaded at the moment
   - `module avail`: Modules available at the moment (due to depencies - hides modules that can't be loaded atm)
   - `module spider name`: Search for an application in the list of all existing modules
   - `module spider name/version`: Gives information on how to load the module (prerequisites etc).
- If you try to load a module that is not available, you will get an error message saying so 

:::info (speech)
If you want to list which modules you have loaded at the moment, you can type module list.
To check which modules are available to load right now, try module avail.
It will not show modules which you can not load. 
For example, there might still be some missing dependencies before you are able to load a particular module.
To search for a certain application and its versions, use module spider and the name of the application.
Also with module spider, you can type the application name slash the application version, to find more information on: how to load a specific version of the application. 
The system is designed so that it will give an error message, if you try to load a module, which is not available.
:::

# Various kinds of modules

- Some modules contain software that has a graphical user interface
   - For example chemistry visualisation software [Molden](https://docs.csc.fi/apps/molden/)
   - Use [Puhti Web Interface](https://puhti.csc.fi) or [other connection with GUI](https://docs.csc.fi/computing/connecting/#using-graphical-applications)
- Some modules contain software that provide a command line interface
   - For example [zstd module](https://docs.csc.fi/support/tutorials/env-guide/packing-and-compression-tools/#zstandard-compression-tool)

- A module may contain only one software/application (e.g. `gromacs-env`), and some software can be found in many different modules (e.g. `gdal`)
- Some modules provide you with a collection of softwares or eg. Python or R packages
   - For example [Bioconda](https://docs.csc.fi/apps/bioconda/), [Geoconda](https://docs.csc.fi/apps/geoconda/#using-geoconda) or [Python Data](https://docs.csc.fi/apps/python-data/)

:::info (speech)
Some software have a graphical user interface, for example Molden.
To use those, you need a graphical session in Puhti web interface, or some other way to access remote graphics.
Some software work in the command line interface, for example zstd.
You can start using them in the command line – after loading the module.

Some applications on the supercomputer have their own modules, and some applications are combined in larger modules. 
Then some applications can be found in multiple modules. 

Some modules contain packages - for example python or R packages.
You can use them with the appropriate software – after loading the module.
Avoid trial-and-errors by consulting the documentation first to find out if the application you want to use is already included in a module.
:::

# Conda, Python and R packages
- Some preinstalled software are distributed using [Conda](https://docs.conda.io/en/latest/) package management tool
   - See [Conda best practices](https://docs.csc.fi/support/tutorials/conda/) in CSC HPC environment
   - Do not create own Conda environments - run those in a [container](https://docs.csc.fi/support/tutorials/singularity-scratch/)

- Preinstalled Python packages are available in [Python-related modules](https://docs.csc.fi/apps/python/) 
   - See the Docs CSC for packages you want and the usage details
   - It is not possible to load multiple modules with Python packages at once
   - Command `pip list` shows a [list of packages](https://pip.pypa.io/en/stable/cli/pip_list/) installed within the current environment

- Instructions on [how to check installed R-libraries](https://docs.csc.fi/apps/r-env-singularity/#r-package-installations) in DocsCSC
   - RStudio shows available packages in the sidebar

:::info (speech)
Conda is a generally used package management tool for distributing and installing software. 
Some applications are installed and used in a Conda environment.
Unfortunately Conda has a really poor performance in Lustre parallel file system.
Therefore you should always check, if the software you need is already included in a module.
If you need to build an own Conda environment, put it in a container.
More information on installing software, and containers, in their own lectures.
Python-related modules have their own Docs CSC pages.
Consult those before starting, because they have different instructions on usage.
Plan your workflows such, that you do not need to load multiple modules with Python packages simultaneously.
:::

# Customizing own environment
- If you "always" use some modules, it is possible to add loading them to `.bashrc`, but **we do not recommend this**
   - This causes the modules to be loaded always, also in batch jobs and likely will cause hard-to-spot issues later
   - If you already did this, see the [`csc-env` command FAQ](https://docs.csc.fi/support/tutorials/using_csc_env/)
- If it feels cumbersome to give the `module load this and that` at the start of each session, you can put these commands in an _alias_ in your `.bashrc`
   - _e.g._ add this line in your _.bashrc_ `alias setmyenv='module load this and that'`
   - Now, you can load all those modules simply with `setmyenv` (after logging out and back in)

:::info (speech)
Eventually you as a supercomputer user will develop your own workflows, such as always loading the same modules, that you use in your research.
Usually in such cases people use a file called dot bashrc, which is executed in every login. 
But we do not recommend this for loading the modules automatically, because this might cause some hard-to-find issues later on.
You should always be aware of what modules you are loading – to avoid conflicts with the dependencies.
If you already have done this and suspect some conflicts, you can check out the csc-env command.
That allows for example resetting to the basic environment, which also resets the bashrc file.
However you can still use .bashrc to minimize the tedious typing.
Automatize module loading by creating an alias in the .bashrc.
Executing an alias will execute all the user-defined commands there.
You can come up with your own command – like for example setmyenv – and then define all the module loads you usually need.
Please keep in mind, that aliases might not work in a same way in a subshell or batch job.
:::

# [Advanced module use](https://docs.csc.fi/computing/modules/#advanced-topics)

- You can save your current module set (`module save filename`) and load it (`module restore filename`)
- You can also write your own module files: 
    1. Add them in your home directory (`$HOME/modulefiles`) and 
    2. Add the path to the module search path (`module use $HOME/modulefiles`)
- To study existing module files: command `module show module-name` shows also the filename of the module file

:::info (speech)
If you like a certain set of modules, you can also save your current module configuration, and then use module restore to load your set. 
You can also write your own module files, and put them in your home directory. 
Remember also to add the path of your modulefiles to the module search path, so that you can easily use those own modules. 
To study the existing module files, you use the command module show and the module name.
That will show for example the filename of the module file, which is a .lua file. 

The tutorials about modules continue from here. 
They cover the basic use cases with easy-to-follow examples.
Module documentation in docs.csc.fi covers also the more technical details. 
The links are in the description.
:::
