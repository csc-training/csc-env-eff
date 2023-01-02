---
topic: modules
title: Tutorial - Modules in Puhti (essential)
---

# Modules in Puhti

> ☝🏻 This tutorial requires that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) and it is a member of a project that [has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

## Checking the default modules

1. Log in to Puhti with your user credentials. (Replace your_csc_username with your CSC username!)

```bash
ssh your_csc_username@puhti.csc.fi
```

2. Try a `module` command! Check out which modules are loaded as default as you login to Puhti:

```bash
module list
```

## More module commands with Gromacs-module as an example 

💬 Let's imagine that you want to do some molecular dynamics simulations with [Gromacs](https://www.gromacs.org/about.html) application. 
- Always a good idea to start by checking [the application list at Docs](https://docs.csc.fi/apps/) to see whether this application is installed at Puhti, and how to use it. 

1. Check out the [Gromacs guide page](https://docs.csc.fi/apps/gromacs/) 
2. Skim through the manual page, and see if the license allows you to use the software, and what is the module command that you need to run to be able to use Gromacs in Puhti.

3. Back in the command line, check what versions are available for Gromacs in Puhti. 

```bash
module spider gromacs
```

- This might take a while, as the command searches through all the available modules. 
- The list can be long, you can go to next line with Enter, or stop viewing by typing ```q```).
    
4. Check if some versions can be loaded right away ie. are compatible with currently loaded modules:

```bash
module avail gromacs
```

5. Which version is loaded with the default command? Is it the newest version? Try:

```bash
module load gromacs-env
```

6. Do you notice any changes in the output of ```module list``` compared to the first try? Try this again:

```bash
module list
```  

☝🏻 If no version is given in the module command, the default version is loaded. 

- The default version is typically the latest **stable** version of the program.
- If the program version matters, it is best to give it in module load command, as the default version may change.

{:start="7"}
7. Let's try and load the 2021 version:

```bash
module load gromacs-env/2021
module list
```

8. If you wanted to do something else in the same session, it can be useful to reset the module environment to the default settings. This can be done by first removing all loaded modules and then loading the defaults.

```bash
module purge            # Clear all modules
module list             # List the modules in use
module load StdEnv      # Load the default modules
module list             # List the modules in use
```

## More information

💭 When actually starting to use Gromacs in Puhti, you would run it in the batch job system, which we hear more about later. 

💭 Check out the [example batch job script for Gromacs](https://docs.csc.fi/apps/gromacs/#example-parallel-batch-script-for-puhti) to see how the module is recommended to be loaded there (the first two command lines after `#SBATCH` commands and comments).

### Loading an older version of a module

💬 Using an older version of a module is usually possible

💬 As an example you can try to use an old version of Gromacs from 2020. 

1. The older versions do not have "environment module" (because the usage is not encouraged) so check with ```spider``` command which other modules are needed for the old version

```bash
module spider gromacs/2020.5
```

2. Load all of the required modules manually.

```bash
module load gcc/9.4.0  
module load openmpi/4.1.4
module load gromacs/2020.5
module list
```
    
    
