---
topic: singularity
title: Tutorial - Running applications installed as containers
---

# Running applications installed as containers

💬 In this tutorial we get familiar with the basic usage of software that has been installed as a container.

💭 Some software on CSC supercomputers have been installed as containers. 
- In many cases we have tried to "hide" the container behind wrapper scripts so that there is no change in usage from the user perspective.

💭 On some cases, however, this is not practical, and in these cases there can be some differences to the standard usage as described by the software documentation. 
-Typically, this involves prefixing the commands with `singularity_wrapper exec`. 
-This will also typically be the case for software you install yourself as a container.

‼️ See the CSC documentation for each application to check any changes or considerations.

1. To run these exercises in Puhti, use `sinteractive`.
```bash
sinteractive --account project_XXXX   # Change the XXXX for the project number
```

## Example 1: A "hidden" installation

{:start="2"}
2. One example of a container-based installation that has been "hidden" behind a wrapper script is R:
    ```bash
    module load r-env-singularity
    Rscript --version
    ```
3. As you can see, `Rscript` works like normal, and in most cases you don't need to care that it is installed as container.

💭 You can see more details about using R in the [Docs page for r-env-singularity](https://docs.csc.fi/apps/r-env-singularity/).

💡 If you can't open `sinteractive` session due to high load in the course, you can try this example in the login shell instead:
```bash
module load cutadapt
cutadapt -h
```

## Example 2: Installation requiring special commands

💬 `Zonation` is one example of a software that will reguire you to prefix command with "singularity_wrapper exec".

{:start="2"}
2. So instead of e.g. `zig4 --help`, you will need to use:
    ```bash
    module load zonation
    singularity_wrapper exec zig4 --help
    ```

💭 You can see more details about the software in the [Docs page for Zonation](https://docs.csc.fi/apps/zonation).

