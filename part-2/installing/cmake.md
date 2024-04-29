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

# Installing using CMake

💬 CMake is an extensible, open-source system that manages the build process in an operating system and in a compiler-independent manner.

💬 CMake uses simple configuration files placed in each source directory (called CMakeLists.txt files) to generate standard build files (e.g., Makefiles).

💬 CMake generates a native build environment that will compile source code, create libraries, generate wrappers and build executable binaries in arbitrary combinations. 

💬 CMake supports in-place and out-of-place builds, and can therefore support multiple builds from a single source tree.

## Example: Installing a test C++ application

💬 In this example we'll install an simple test C++ application `Hello World`.

1. Create a personal folder (if not done already) under your project's `/projappl` directory and move there.

2. Download the application using git:

```bash
git clone https://github.com/jameskbride/cmake-hello-world.git
```

{:style="counter-reset:step-counter 2"}
3. Move into the folder `cmake-hello-world`. Run `cmake` command. Set the source directory (`-S`) and the build directory (`-B`). This will generate the `Makefile`:

```bash
cd cmake-hello-world
cmake -S . -B build        # Here we create a build directory named `build`. If the build directory does not exist already, cmake creates it.
```

{:style="counter-reset:step-counter 3"}
4. Now invoke the build system

```bash
cmake --build build
```

💡 Some 'real world' applications are large and possibly require more resources for faster compilation. In these cases, use the `-j` flag to set the number of cores for compilation. *Please check the number of cores (CPUs) available for use in your system. E.g., In linux, you can find this using `lscpu` command.*

```bash
cmake --build build -j 8     # This will build the system using 8 cores.
```

{:style="counter-reset:step-counter 4"}

5. Check if the installation was successful:

```bash
$PWD/build/CMakeHelloWorld
```

You should see the output `Hello, world!`

💡 For 'real world' applications, the binary file is usually created in a default `bin` folder.

```bash
$PWD/build/bin/application_binary_file
```

### Alternate method : Using make command

1. Move into the folder `cmake-hello-world` and create a build directory (`build`)


```bash
cd cmake-hello-world
mkdir build
```

{:style="counter-reset:step-counter 1"}

2. Move into the `build` folder and run cmake. Set the installation path to the current directory (`build`)

```bash
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$PWD
```

{:style="counter-reset:step-counter 2"}

3. Now compile and install using the `make` command

```bash
make
make install
```

💡 For 'real world' applications, set the number of cores to be used for compilation using the `-j` flag.

```bash
make -j 8     
```
