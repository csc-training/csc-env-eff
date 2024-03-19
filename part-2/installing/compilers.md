---
layout: default
title: Compiler options : Performance Optimization
parent: 8. Installing own software
grand_parent: Part 2
nav_order: 7
has_children: false
has_toc: false
permalink: /hands-on/installing/compiler_options.html
---

# Code performance based on compiler options

1. Create a directory for the code. The recommended location is under the `/projappl` directory of your project:

```bash
mkdir -p /projappl/<project>/laplacian    # replace <project> with your CSC project, e.g. project_2001234
```

2. Download the code from GitHub.

```bash
wget https://raw.githubusercontent.com/csc-training/node-level-optimization/master/math/solution/laplacian.cpp
```

3. Compile the code using gcc and the following options:
   
**Note: `-fopenmp` flag is needed for compiling the code. Do not forget to add it**

- a. No compiler flags

```bash
gcc -fopenmp laplacian.cpp -o laplacian_no_opt -ftime-report &> lap_no_opt.log  # &> redirects the terminal output to the file 'lap_no_opt.log'. This is optional.

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_no_opt &>> lap_no_opt.log   # &>> appends the terminal output to 'lap_no_opt.log'. This is optional.
```

- b. flag `O2`

```bash
gcc -fopenmp -O2 laplacian.cpp -o laplacian_opt_O2 -ftime-report &> lap_opt_O2.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_O2 &>> lap_opt_O2.log
```

- c. flag `O3`

```bash
gcc -fopenmp -O3 laplacian.cpp -o laplacian_opt_O3 -ftime-report &> lap_opt_O3.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_O3 &>> lap_opt_O3.log
```

- d. flag `Os`

```bash
gcc -fopenmp -Os laplacian.cpp -o laplacian_opt_Os -ftime-report &> lap_opt_Os.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_Os &>> lap_opt_Os.log
```

- e. flag `Og`

```bash
gcc -fopenmp -Og laplacian.cpp -o laplacian_opt_Og -ftime-report &> lap_opt_Og.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_Og &>> lap_opt_Og.log
```

- c. flag `Ofast`

```bash
gcc -fopenmp -Ofast laplacian.cpp -o laplacian_opt_Ofast -ftime-report &> lap_opt_Ofast.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_Ofast &>> lap_opt_Ofast.log
```

