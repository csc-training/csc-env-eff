---
layout: default
title: Running containerized applications
parent: 9. Containers and Apptainer
grand_parent: Part 2
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/singularity/singularity-tutorial_running-installed.html
---

# Running containerized applications

💬 In this tutorial we will get familiar with the basic usage of containerized software.

💭 Some software on CSC supercomputers have been installed as containers.

- Usually, we try to make the containers as transparent as possible using wrapper scripts. This way, there should be little to no change in usage from the users' perspective.

💭 Sometimes, however, this is impractical and there might be slight differences compared to the standard usage as described in the documentation.

- Typically, this will also be the case for software you containerize yourself. You can, however, use [Tykky](https://docs.csc.fi/computing/containers/tykky/) to create wrapper scripts to facilitate use of containers.

‼️ Please see the software documentation in [Docs CSC](https://docs.csc.fi/apps/) for details and other considerations.

1. To run these exercises on Puhti, use `sinteractive` or open a compute node shell in the [Puhti web interface](https://www.puhti.csc.fi)

```bash
sinteractive --account <project>   # replace <project> with your CSC project, e.g. project_2001234
```

## Example: A "hidden" installation

{:start="2"}
2. An example of a container-based installation that has been "hidden" behind a wrapper script is R:

```bash
module load r-env
Rscript --version
```

{:start="3"}
3. As you can see, `Rscript` works as expected and in most cases you don't need to care about the fact that it is installed as a container.

💭 You can find more details about using R in the [Docs CSC page of the `r-env` module](https://docs.csc.fi/apps/r-env/).

💡 If you're unable to open an interactive session due to high load during the course, you can try this example in a login shell instead:

```bash
module load cutadapt
cutadapt -h
```
