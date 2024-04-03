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

💬 In this example we'll install an computer vision library, OpenCV.

1. Create a personal folder (if not done already) under your project's `/projappl` directory and move there.

2. Download the software using git:

```bash
git clone https://github.com/opencv/opencv.git
```

{:style="counter-reset:step-counter 2"}
3. Move into the folder `opencv`. Create a folder called `build` and move there:

```bash
cd opencv
mkdir build
cd build
```

{:style="counter-reset:step-counter 3"}
4. Run `cmake` application to generate the `makefiles`. Use `-DCMAKE_INSTALL_PREFIX` flag to set installation path to the current folder:

```bash
cmake .. -DCMAKE_INSTALL_PREFIX=$PWD
```

💡 This will generate the needed `Makefile`. Now invoke the build system using `make` command. To speed up the process, you can use the flag `-j` to set the number of cores for the build process.

```bash
make -j 8     # set the flag `-j` to 8 cores. 
```
