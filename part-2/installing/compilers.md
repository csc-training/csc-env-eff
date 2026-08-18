---
layout: default
title: Optimizing compiler options
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 8
has_children: false
has_toc: false
permalink: /hands-on/installing/compiler_options.html
---

# Compiling using optimizing compiler options

> This tutorial is done on **Roihu**, which requires that:
  - You have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
  - Your account belongs to a project [that has access to the Roihu service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

‼️ Roihu has separate **CPU** and **GPU** partitions with different processor architectures,
AMD (x86) on Roihu-CPU and NVIDIA Grace (ARM) on Roihu-GPU. Binaries built on one side are
**not** compatible with the other, so always compile on the login node matching where you
intend to run. This tutorial covers **Roihu-CPU** only. Refer to
[Compiling applications in Roihu](https://docs.csc.fi/computing/compiling-roihu/) for 
detailed information.

## Overview

💭 Without any optimization options, a compiler tries to reduce the
computational cost of compiling and to make debugging produce the expected
results. Turning on optimization flags makes the compiler attempt to improve
the performance and/or code size at the expense of compilation time and
possibly the ability to debug the program.

☝🏻 It is recommended to start with safe (basic) optimization, and then move up
to intermediate, or even aggressive, while ensuring that results produced by
the program remain correct and that the performance actually improves.

On Roihu-CPU, "safe" optimization also includes an architecture flag, since the
compiler needs to be told which CPU to target to generate the most efficient 
instructions:

| Optimization level | GNU (`gcc`/`g++`/`gfortran`)                   | AMD AOCC (`clang`/`clang++`/`flang`) |
| ------------------ | ---------------------------------------------- | ------------------------------------ |
| **Safe**           | `-O2 -march=znver5`                            | `-O2 -march=znver5`                  |
| **Intermediate**   | `-O3 -march=znver5`                            | `-O3 -march=znver5`                  |
| **Aggressive**     | `-O3 -march=znver5 -ffast-math -funroll-loops` | -                                    |

`-march=znver5` tells the compiler to target the AMD Zen 5 architecture used in Roihu-CPU nodes, enabling
instruction sets (e.g. wider vector extensions) that generic `-O2`/`-O3` alone will not use.

## Compare different optimization flags

💬 This tutorial examines a simple C++ code that computes the Laplacian for a
two-dimensional field. We'll use `gcc` to compile the code with different
optimization options and observe how they affect performance. Understanding
the details of the program is not important for completing this tutorial, just
consider it an illustrative example.

1. Create and enter a suitable scratch directory on Roihu (replace `<project>`
   with your CSC project, e.g. `project_2001234`):

   ```bash
   mkdir -p /scratch/<project>/$USER/laplacian
   cd /scratch/<project>/$USER/laplacian
   ```

   ☝🏻 Own software should normally be installed under `/projappl`, but for the
   sake of this exercise it is sufficient to use `/scratch`.

2. Download the source code from Allas:

   ```bash
   wget https://a3s.fi/CSC_training/laplacian.cpp
   ```

3. To avoid causing unnecessary load on the login node, launch an interactive
   session on a compute node:

   ```bash
   sinteractive --account <project> --time 00:15:00 # replace <project> with your CSC project, e.g. project_2001234
   ```

4. First, compile the code using `gcc` without optimizing compiler options:
   
   ```bash
   gcc -fopenmp -o laplacian laplacian.cpp
   ```

   - `-o laplacian` instructs the compiler to name the executable output as
     `laplacian`.
   - `-fopenmp` flag is needed for this code since it uses OpenMP directives.

5. Run the code as (should take about two minutes):

   ```bash
   ./laplacian
   ```

6. Recompile the code using safe (`-O2 -march=znver5`), intermediate (`-O3 -march=znver5`)
   and aggressive (`-O3 -march=znver5 -ffast-math -funroll-loops`) optimization options.
   For example:

   ```bash
   gcc -O2 -march=znver5 -fopenmp laplacian.cpp -o laplacian_O2
   ```

7. Re-run the program for each optimization level.
   - How much does the performance improve in each case?
   - Do the results remain the same for all optimization levels?
   - Does adding `-march=znver5` change anything compared to
     using `-O2`/`-O3` alone?

☝🏻 Aggressive optimization may result in programs producing less precise or
even incorrect results. Please be aware of this and thoroughly benchmark your
code when using aggressively optimizing compiler flags.

💡 As the example code here is so small, it is not necessary to compile on the
fast local disk to move I/O load away from the shared file system. However,
when building a larger, more realistic software package, please use `$TMPDIR`
to avoid stressing Lustre.

☝🏻 If your code uses MPI, use the compiler wrappers `mpicc`, `mpicxx` or `mpif90`
instead of calling `gcc`/`g++`/`gfortran` directly. These wrappers automatically
call the right underlying compiler from your loaded suite and add the necessary
MPI flags.

## Bonus: Fortran version

1. Re-run the previous steps for a similar program written in Fortran instead
of C++. You may download the source code from Allas:

   ```bash
   wget https://a3s.fi/CSC_training/laplacian.F90
   ```

1. Use `gfortran` compiler instead of `gcc`. The previous options are the same
   for both compilers.

💭 How does the performance and results compare with the C++ code? Does
`gfortran` deliver similar improvements as `gcc`?

## More information

- Docs CSC: [Compiling on Roihu](https://docs.csc.fi/computing/compiling-roihu/)
- Docs LUMI: [Compiling on LUMI](https://docs.lumi-supercomputer.eu/development/)
