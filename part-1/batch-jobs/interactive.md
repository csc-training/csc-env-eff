---
layout: default
title: Interactive batch jobs
parent: 5. Batch queue system and interactive use
grand_parent: Part 1
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/batch_jobs/interactive.html
---

# Batch job tutorial - Interactive jobs

> In this tutorial we'll get familiar with the basic usage of the Slurm batch queue system at CSC
- The goal is to learn how to request resources that **match** the needs of a job

💬 A job consists of two parts: resource requests and the job step(s)

☝🏻 Examples are done on Puhti. If using the web interface, you can either open a login node shell and follow the steps below or, even better, open a compute node shell directly and skip to step 3.

💡 The benefit of running an interactive session through the Puhti web interface is that the shell is *persistent*, i.e. the session will stay open and any programs started there will keep running even if you would happen to lose internet connection or close the browser tab.

## Interactive jobs

💬 In an interactive batch job, an interactive shell session is launched on a compute node.

- For heavy interactive tasks one can request specific resources (time, memory, cores, disk).

💡 You can also use tools with graphical user interfaces in an interactive shell session.

- For such usage the [Puhti web interface](https://www.puhti.csc.fi/) remote desktop often provides an improved experience.
- Check also [how to use RStudio and Jupyter Notebooks in Puhti](https://docs.csc.fi/support/tutorials/rstudio-or-jupyter-notebooks/)

### A simple interactive job

1. Start an interactive job using one core for ten minutes:

```bash
sinteractive --account <project> --time 00:10:00         # replace <project> with your CSC project, e.g. project_2001234
```

💡 You can list your projects with `csc-projects`

{:style="counter-reset:step-counter 1"}
2. You should see that the command prompt (initial text on each row on the command-line) has changed from e.g. `puhti-login11` to e.g. `r07c51` which refers to a compute node.
3. Once on the compute node, you can run commands directly from the command-line without `srun`. You can e.g. load the `python-data` module (e.g. for running Python scripts interactively on Puhti):

```bash
module load python-data
```

{:style="counter-reset:step-counter 3"}
4. Quit the interactive batch job with `exit`.

💬 This way you can work interactively for an extended period, using e.g. lots of memory without creating load on the login nodes. Running heavy/long tasks on the login nodes is forbidden according to our [Usage Policy](https://docs.csc.fi/computing/usage-policy/).

‼️ Note that above you asked only for 10 minutes of time.

- Once that is up, you will be automatically logged out from the compute node.

💡 From the command-line prompt you can see whether you're on a compute node (e.g. `r07c51`) or on the login node (e.g. `puhti-login12`).

- Running `exit` on the login node will log you out from Puhti.

## More information

💡 Documentation at Docs CSC on [Interactive usage](https://docs.csc.fi/computing/running/interactive-usage/)

💡 [FAQ on CSC batch jobs](https://docs.csc.fi/support/faq/#batch-jobs) in Docs CSC
