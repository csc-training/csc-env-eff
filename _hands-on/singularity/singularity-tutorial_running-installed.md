---
topic: singularity
title: Tutorial - Running applications installed as containers
---

# Running applications installed as containers

💬 In this tutorial we get familiar with the basic usage of software that has been installed as a container.

💭 Some of the software on the CSC supercomputers has been installed as containers. 
- In many cases we have tried to "hide" the container behind wrapper scripts so that there is no change in the usage from the user perspective.

💭 Sometimes, however, this is not practical, and in these cases, there can be some differences compared to the standard usage as described in the software documentation. 
- Please see CSC documentation for each software for details
- This will also typically be the case for software you install yourself as a container.

‼️  See the CSC documentation for each application to check any changes or considerations.

1. To run these exercises in Puhti, use `sinteractive`.
```bash
sinteractive --account project_xxxx   # Change the xxxx for the project number
```

## Example 1: A "hidden" installation

{:start="2"}
2. One example of a container-based installation that has been "hidden" behind a wrapper script is R:
    ```bash
    module load r-env-singularity
    Rscript --version
    ```
3. As you can see, `Rscript` works like normal, and in most cases you don't need to care that it is installed as container.

💭 You can see more details about using R in the [Docs page for r-env](https://docs.csc.fi/apps/r-env/).

💡 If you can't open `sinteractive` session due to high load in the course, you can try this example in the login shell instead:
```bash
module load cutadapt
cutadapt -h
```

## Example 2: Installation requiring special commands

💬 `Zonation` is one example of software that will require you to add a prefix command with "apptainer_exec".

{:start="2"}
2. So instead of, e.g., `zig4 --help`, you will need to use:
    ```bash
    module load zonation
    apptainer_wrapper exec zig4 --help
    ```

💭 You can see more details about the software in the [Docs page for Zonation](https://docs.csc.fi/apps/zonation).

