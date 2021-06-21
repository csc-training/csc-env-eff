---
topic: modules
title: Tutorial - Modules in Puhti
---

# Modules in Puhti

This tutorial requires that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
and it is a member of a project that [has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).


1. Log in to Puhti with your user credentials. (Replace your_csc_username with your CSC username!)
```bash
ssh your_csc_username@puhti.csc.fi
```

2. Let's try our first `module` command! Check out which modules are loaded as default as you login to Puhti:
```bash
module list
```

3. Let's imagine that we want to do some molecular dynamics simulations with [Gromacs](http://www.gromacs.org/About_Gromacs) application. We would start by checking [the application list at Docs](https://docs.csc.fi/apps/) to see whether this application is installed at Puhti, and how to use it. Can you spot the [Gromacs guide page](https://docs.csc.fi/apps/gromacs/) there? Skim through the manual page, and see if the license allows you to use the software, and what is the module command that you need to run to be able to use Gromacs in Puhti.

4. Let's go back to command line, and check what versions are available for Gromacs in Puhti. (Note, that this might take a while, as the command searches through all the available modules. The list can be long, you can go to next line with Enter, or stop viewing by typing ```q```).
```bash
module spider gromacs
```

5. Quite a few of them! Check the recommended versions (=versions compatible with your current environment):
```bash
module avail gromacs-env
```

6. Now, let's see which version is loaded with the default command! Do you notice any changes compared to the first command?
```bash
module load gromacs-env
module list
```

7. Just out of curiosity, let's switch to the 2020 GPU version of Gromacs, and check the situation. Do you notice any changes now?
```bash
module load gromacs-env/2020-gpu
module list
```

8. Let's clean up after ourselves, and unload all modules:
```bash
module purge
```

9. When actually starting to use Gromacs in Puhti, you would run it in the batch job system, which we hear more about later. Check however already the [example batch job script for Gromacs](https://docs.csc.fi/apps/gromacs/#example-parallel-batch-script-for-puhti) to see how the module is recommended to be loaded there (first two command lines after the `#SBATCH` commands and comments).
