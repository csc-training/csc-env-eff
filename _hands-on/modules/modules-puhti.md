---
topic: modules
title: Tutorial - Modules in Puhti
---

# Modules in Puhti

This tutorial requires that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
and it is a member of a project that [has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).


1. Log in to Puhti with your user credentials. (Replace <your_csc_username> with your CSC username, withouth the < > brackets!)
```bash
ssh <your_csc_username>@puhti.csc.fi
```

2. Check out which modules are loaded:
```bash
module list
```

3. Check what versions are available for Gromacs. (Note, that this might take a while, as the command searches through all the available modules. The list can be long, you can go to next line with Enter, or stop viewing by typing ```q```).
```bash
module spider gromacs
```

4. Check the recommended versions (=versions compatible with your current environment):
```bash
module avail gromacs-env
```

5. Load the gromacs-env module, and check the loaded modules list again. Do you notice any changes?
```bash
module load gromacs-env
module list
```

6. Switch to the GPU version of Gromacs, and check the situation. Do you notice any changes?
```bash
module load gromacs-env/2020-gpu
module list
```

7. Unload all modules:
```bash
module purge
```

8. Check the [example batch job script for Gromacs](https://docs.csc.fi/apps/gromacs/#example-parallel-batch-script-for-puhti) to see how the module is recommended to be loaded there (first two lines after the `#SBATCH` commands and comments).
