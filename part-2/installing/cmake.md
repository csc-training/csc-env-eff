---
layout: default
title: Installing using cmake
parent: 8. Installing own software
grand_parent: Part 2
nav_order: 6
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_using_cmake.html
---

# Installing using cmake

💬 CMake is an extensible, open-source system that manages the build process in an operating system and in a compiler-independent manner.


## Example: Installing OpenCV

💬 In this example we'll install an simple test C++ application `Hello World`.

1. Create a personal folder (if not done already) under your project's `/projappl` directory and move there.

2. Download the application using git:

```bash
git clone https://github.com/jameskbride/cmake-hello-world.git
```

{:style="counter-reset:step-counter 2"}
3. Move into the folder `cmake-hello-world`. Create a folder called `build` and move there:

```bash
cd cmake-hello-world
mkdir build
cd build
```

{:style="counter-reset:step-counter 3"}
4. Run `cmake` application to generate the `makefiles`. Use `-DCMAKE_INSTALL_PREFIX` flag to set installation path to the current folder:

```bash
cmake .. -DCMAKE_INSTALL_PREFIX=$PWD
```

{:style="counter-reset:step-counter 4"}
5. This will generate the needed `Makefile`. Compile and install the application using `make` command


```bash
make 
make install
```

💡 Some 'real world' applications are large and possibly require more resources for faster compilation. In these cases, use the `-j` flag to set the number of cores for compilation. *Please check the number of cores (CPUs) available for use in your system. E.g., In linux, you can find this using `lscpu` command.*

```bash
make -j 8     # will build the system using 8 cores.
```
{:style="counter-reset:step-counter 5"}
6. Check if the installation was successful:

```bash
$PWD/bin/CMakeHelloWorld
```

You should see the output `Hello, world!`
