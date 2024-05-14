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

> This tutorial is done on **Puhti**, which requires that:
  - You have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
  - Your account belongs to a project [that has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

## Overview

💭 Without any optimization options, a compiler tries to reduce the
computational cost of compiling and to make debugging produce the expected
results. Turning on optimization flags makes the compiler attempt to improve
the performance and/or code size at the expense of compilation time and
possibly the ability to debug the program.

☝🏻 It is recommended to start with safe (basic) optimization, and then move up
to intermediate, or even aggressive, while ensuring that results produced by
the program remain correct and that the performance actually improves.

## Compare different optimization flags

💬 This tutorial examines a simple C++ code that computes the Laplacian for a
two-dimensional field. We'll use `gcc` to compile the code with different
optimization options and observe how they affect performance. Understanding
the details of the program is not important for completing this tutorial, just
consider it an illustrative example.

1. Create and enter a suitable scratch directory on Puhti (replace `<project>`
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
   sinteractive --account <project> --time 00:15:00 --tmp 0  # replace <project> with your CSC project, e.g. project_2001234
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

6. Recompile the code using safe (`-O2`), intermediate (`-O3`) and aggressive
   (`-Ofast`) optimization options. For example:

   ```bash
   gcc -O2 -fopenmp laplacian.cpp -o laplacian_O2
   ```

7. Re-run the program for each optimization level.
   - How much does the performance improve in each case?
   - Do the results remain the same for all optimization levels?

💡 In this case `-Ofast` increases code size by roughly 10% compared to using
no optimization flags. Although the absolute difference for such a small code
is insignificant (only about 2 KB), it is good to keep in mind that
optimization may affect output program size. Similarly, more aggressive
optimization typically increases compilation time and may worsen debugging
experience.

☝🏻 Aggressive optimization may result in programs producing less precise or
even incorrect results. Please be aware of this and thoroughly benchmark your
code when using aggressively optimizing compiler flags.

💡 As the example code here is so small, it is not necessary to compile on the
fast local disk to move I/O load away from the shared file system. However,
when building a larger, more realistic software package, please use `$TMPDIR`
to avoid stressing Lustre.

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

- Docs CSC: [Compiling on Puhti](https://docs.csc.fi/computing/compiling-puhti/)
- Docs CSC: [Compiling on Mahti](https://docs.csc.fi/computing/compiling-mahti/)
- Docs LUMI: [Compiling on LUMI](https://docs.lumi-supercomputer.eu/development/)
