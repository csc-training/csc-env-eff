---
layout: default
title: Title that is shown in the navigation and breadcrumbs
parent: Parent page
grand_parent: Grand parent page
nav_order: Order in navigation
permalink: /set/permanent/link/if/needed.html
---

# Descriptive Headline

💬 This document contains general style guide for hands-on tutorials and exercises. 

> The prerequisites/learning outcomes: Sometimes there are many, but list if there's something essential but not obvious. 

1. Use numbered list to describe actual steps that a student does
    ```bash
    echo 'project_xxxx/yourcscusername'   # Use commented code whenever clarification is necessary
    ```
    - Try to get the code block indented nicely in the rendered product

## Get started

💬 This is the first phase of this tutorial e.g. a preparation.  

💡 It is recommended to structure the content with second level headlines.

2. A code block can contain multiple lines
    ```bash
    export SCRATCH=/scratch/project_xxxx    # Use xxxx for projectnumber
    mkdir yourcscusername                   # Use yourcscusername if student should use their own
    echo $USER                              # Or use the environment variable
    ```

{:style="counter-reset:step-counter 2"}
3. A step does not need to contain a code block, but instead make a point that student should notify
    - Further explanation can be provided with indented list element

☝🏻 A list element cannot start with indented block
- Meaning that it starts after regular text like this

### 1. Further structuring

1. Feel free to add more headlines if it supports the understandability of the content 
2. The goal is to reduce the effort in following the material

## Usage of Emojis

💡 The emojis are meant to structure text and to improve its readability. 

1. Look for the symbols-option from your computer
    - Usually the emojis are there.
2. Copy the existing emojis if you don't find them anywhere else

| Emoji | Purpose |
|-------|:--------|
| 💬    | General instructions or description |
| 💭    | Provide extra information or insight |
| 🗯    | Emphasise the message a bit |
| 💡    | Valuable information, ideas or suggestions |
| ☝🏻    | Notice or a side-note |
| ‼️     | Very important notice. Failing to comply with this will result in error of some kind |

## Usage of images

1. Add images to the `/_slides/img/`-folder
    - Or in the respective section folders under `/part-1` and `/part-2`
2. Provide the path like this:
`![terminal-icon](../_slides/img/terminal_icon1.png)`
1. The image should show like this: ![terminal-icon](../_slides/img/terminal_icon1.png)

## Providing batch job files

💬 [Batch job files](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#a-basic-batch-job-script) are scripts for Slurm queueing system used in CSC supercomputers.

1. Provide necessary job-files commented like this:
    ```bash
    #!/bin/bash
    #SBATCH --job-name=test           # Name of the job visible in the queue.
    #SBATCH --account=project_xxxx    # Choose the billing project. Has to be defined!
    #SBATCH --partition=test          # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
    #SBATCH --time=00:01:00           # Maximum duration of the job. Max: depends of the partition. 
    #SBATCH --mem=1G                  # How much RAM is reserved for job per node.
    #SBATCH --ntasks=1                # Number of tasks. Max: depends on partition.
    #SBATCH --cpus-per-task=1         # How many processors work on one task. Max: Number of CPUs per node.

    apptainer exec tutorial.sif hello_world
    ```

💭 For more information on batch jobs, please see [Docs CSC pages](https://docs.csc.fi/computing/running/getting-started/).

## More information

💡 It is a good practice to provide more information on topics, but it is not mandatory.

💬 This tutorial is meant as a brief introduction to get you started.

💭 When searching the internet for instructions, pay attention that the instructions are for the same version of Apptainer that you are using. There have been some command syntax changes etc. between the versions, so older instructions may not work with copy-paste.

💡 Always a good idea to link to [Docs CSC](https://docs.csc.fi/).

### About Markdown

📝 Ordered lists reset numbering if there's stuff in between.  
Options:
- Manually reset counter if needed with {:style="counter-reset:step-counter 2"}
- Indent code blocks, and make sure they appear directly "under" the list item, and the numbering goes on nicely
