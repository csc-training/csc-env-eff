---
layout: default
title: Optimizing compiler options
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 7
has_children: false
has_toc: false
permalink: /hands-on/installing/compiler_options.html
---

# Code performance based on compiler options

Create a directory for the code. The recommended location is under the `/projappl` directory of your project:

```bash
mkdir -p /projappl/<project>/laplacian    # replace <project> with your CSC project, e.g. project_2001234
```

This exercise examines two different programming languages (`cpp` and `fortran`) and their corresponding compilers (`gcc` and `gfortran`). **Please choose one option (`cpp` or `fortran`) for the exercise**

Create subdirectories for the programs.

```bash
mkdir -p /projappl/<project>/laplacian/cpp

## OR

mkdir -p /projappl/<project>/laplacian/fortran
```

## Option 1 : CPP

1. Migrate to the `cpp` subdirectory and download the code from GitHub.

```bash
cd /projappl/<project>/laplacian/cpp

wget https://raw.githubusercontent.com/csc-training/node-level-optimization/master/math/solution/laplacian.cpp
```

2. Compile the code using gcc and the following options:
   
**Note:** 

**`-fopenmp` flag is needed for compiling the code. Do not forget to add it.**

### Exercise 

1. Compare how the compilation statistics (`usr` and `GGC`) varies with the choice of compiler flag.

2. Compare also how the time taken for execution (during `srun`) varies with the choice of compiler flag.

#### Options

- No compiler flags

```bash
gcc -fopenmp laplacian.cpp -o laplacian_no_opt -ftime-report &> lap_no_opt.log  # &> redirects the terminal output to the file 'lap_no_opt.log'. This is optional.

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_no_opt &>> lap_no_opt.log   # &>> appends the terminal output to 'lap_no_opt.log'. This is optional.
```

- flag `O2`

```bash
gcc -fopenmp -O2 laplacian.cpp -o laplacian_opt_O2 -ftime-report &> lap_opt_O2.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_O2 &>> lap_opt_O2.log
```

- flag `O3`

```bash
gcc -fopenmp -O3 laplacian.cpp -o laplacian_opt_O3 -ftime-report &> lap_opt_O3.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_O3 &>> lap_opt_O3.log
```

- flag `Os`

```bash
gcc -fopenmp -Os laplacian.cpp -o laplacian_opt_Os -ftime-report &> lap_opt_Os.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_Os &>> lap_opt_Os.log
```

- flag `Og`

```bash
gcc -fopenmp -Og laplacian.cpp -o laplacian_opt_Og -ftime-report &> lap_opt_Og.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_Og &>> lap_opt_Og.log
```

- flag `Ofast`

```bash
gcc -fopenmp -Ofast laplacian.cpp -o laplacian_opt_Ofast -ftime-report &> lap_opt_Ofast.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_Ofast &>> lap_opt_Ofast.log
```


## Option 2 : Fortran

1. Migrate to the `fortran` subdirectory and download the code from GitHub.

```bash
cd /projappl/<project>/laplacian/fortran

wget https://raw.githubusercontent.com/csc-training/node-level-optimization/master/math/solution/laplacian.F90
```

2. Compile the code using gfortran and the following options:
   
**Note:** 

**`-fopenmp` flag is needed for compiling the code. Do not forget to add it.**

### Exercise 

1. Compare how the compilation statistics (`usr` and `GGC`) varies with the choice of compiler flag.

2. Compare also how the time taken for execution (during `srun`) varies with the choice of compiler flag.

#### Options

- No compiler flags

```bash
gfortran -fopenmp laplacian.F90 -o laplacian_no_opt.out -ftime-report &> lap_no_opt.log  

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_no_opt.out &>> lap_no_opt.log  
```

- flag `O2`

```bash
gfortran -fopenmp -O2 laplacian.F90 -o laplacian_opt_O2.out -ftime-report &> lap_opt_O2.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_O2.out &>> lap_opt_O2.log
```

- flag `O3`

```bash
gfortran -fopenmp -O3 laplacian.F90 -o laplacian_opt_O3.out -ftime-report &> lap_opt_O3.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_O3.out &>> lap_opt_O3.log
```

- flag `O5`

```bash
gfortran -fopenmp -O5 laplacian.F90 -o laplacian_opt_O5.out -ftime-report &> lap_opt_O5.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_O5.out &>> lap_opt_O5.log
```

- flag `Os`

```bash
gfortran -fopenmp -Os laplacian.F90 -o laplacian_opt_Os.out -ftime-report &> lap_opt_Os.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_Os.out &>> lap_opt_Os.log
```

- flag `Og`

```bash
gfortran -fopenmp -Og laplacian.F90 -o laplacian_opt_Og.out -ftime-report &> lap_opt_Og.log

srun --account <project> --partition small --time 00:05:00 --nodes 1 --ntasks-per-node 1 --cpus-per-task 1 ./laplacian_opt_Og.out &>> lap_opt_Og.log
```
