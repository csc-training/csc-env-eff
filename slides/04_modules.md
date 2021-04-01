---
theme: csc-2019
lang: en
---

# Module system {.title}

In this section, you will learn about module systems and how to use them in CSC supercomputers.
Same information can be found in [the module section of our user guide at docs.csc.fi](https://docs.csc.fi/computing/modules/)

# Module systems in supercomputers

- Several softwares with different (possibly conflicting) requirements are needed in one supercomputer
- The solution for managing this situation: separate the applications in *modules*
- *Environment modules* set up everything required by a particular application:
   -  Load libraries, adjust path, set environment variables 

# Module system in CSC supercomputers

- CSC uses [*Lmod*](https://lmod.readthedocs.io/en/latest/) environment modules, which are using *Lua* programming language
- Some softwares/applications have their own module (e.g. `gromacs-env`), whereas some are combined in larger modules (e.g. `biokit`, `geoconda`), and some can be found in many different modules (e.g. `gdal`)

- You can check the available applications and their respective modules in the [Application list](https://docs.csc.fi/apps/)
- These modules are used both in *interactive* and *batch jobs*

# How to use modules (1/2)

- The syntax is simple: `module command module-name`
    - For example: `module load gromacs-env`
    - [List of most common commands](https://docs.csc.fi/computing/modules/#module-commands-table)
- You can't just load all the modules because of the dependencies
- If you try to load a module that is not available, you will get an error message saying so 

# How to use modules (2/2)
 - These commands will help you figuring out the module situation:
    - `module list`: See the list of modules loaded at the moment
    - `module avail`: Modules available at the moment (due to depencies -hides modules that can't be loaded atm)
     - `module spider name`: Search for an application in the list of all existing modules
     - `module spider name/version`: Gives information on how to load the module (prerequisites etc).

# Conda enviroment
- Should we say something about the conda modules too?

# Advanced module use

- You can save your current module set (`module save filename`) and load it (`module restore filename`)
- You can also write your own module files: 
    1. Add them in your home directory (`$HOME/modulefiles`) and 
    2. Add the path to the module search path (`module use $HOME/modulefiles`)
- To study existing module files: command `module show module-name` shows also the filename of the module file