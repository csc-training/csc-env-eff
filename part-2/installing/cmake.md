---
layout: default
title: Installing using CMake
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 7
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_cmake.html
---

# Installing using CMake

💬 CMake is an extensible, open-source software build system. CMake uses simple
`CMakeLists.txt` configuration files placed in each source directory to 
generate standard `Makefile` build files. CMake generates a native build 
environment that will compile source code, create libraries, generate wrappers
and build executable binaries in arbitrary combinations.

## Preparations

💬 In this tutorial we'll use CMake to install a simple C++ Hello World
application.

1. It is recommended to use the fast local disk when compiling software on CSC
   supercomputers to move I/O load away from the parallel file system. Go there
   and download the source code from Allas:

   ```bash
   cd $TMPDIR
   wget https://a3s.fi/CSC_training/hello-cmake.tgz
   ```

2. Extract the package and move into the `hello-cmake` directory:

   ```bash
   tar xvf hello-cmake.tgz
   cd hello-cmake
   ```

3. Most codes ship with a `README` or `INSTALL` file outlining the installation
   procedure. When compiling other codes, start by reading these carefully. In
   this case, the `README` just points to this tutorial page.
4. Before compiling, one should ensure all the dependencies needed by the
   software are available. Remember to always first check whether these can be
   found on the CSC supercomputers as pre-installed modules. This example
   depends on the Boost library, so check if it is available:

   ```bash
   module spider boost
   ```

5. Load the module with:

   ```bash
   module load boost/1.79.0
   ```

## Building with CMake

💡 When your build generates files, they have to go somewhere. An *in-source*
build puts them in your source tree, while an *out-of-source* build puts them
in a completely separate directory. The latter alternative, which is covered
below, is typically recommended, as you can build multiple variants of the code
in separate directories.

1. Load the `cmake` module:

   ```bash
   module load cmake
   ```

2. Create and move to a `build` directory in the root of the source code:

   ```bash
   mkdir build
   cd build
   ```

3. It is recommended to install own software under the `/projappl` directory
   of your project. The installation directory can be specified using the
   CMake flag `-DCMAKE_INSTALL_PREFIX=<path to install dir>`. CMake also
   requires you to specify the source code root directory, so run the `cmake`
   command as:

   ```bash
   cmake .. -DCMAKE_INSTALL_PREFIX=/projappl/<project>/$USER/hello-cmake  # replace <project> with your CSC project, e.g. project_2001234
   ```
4. If you get errors, try to fix the problems. For example, if you did not load
   the `boost` module, you'll get an error `Could NOT find Boost`. Often it is
   easiest to delete everything in the `build` directory and start from the
   beginning after fixing all issues.
5. After running `cmake`, run `make` to compile the application:

   ```bash
   make
   ```
   
   💡 `make` can also be run in parallel. For example, to run using 8 cores,
   use `make -j 8`. However, do not compile in parallel on the login node,
   but use instead an interactive session. See CSC's
   [usage policy](https://docs.csc.fi/computing/usage-policy/) for details.

6. Finally, install into the specified directory under `/projappl` with:

   ```bash
   make install
   ```

7. Check what was installed and where:

   ```bash
   cat install_manifest.txt
   ```

## Test the installed application

1. Own software installations are not automatically added to your `PATH`, which
   means that the installed binaries (commands) cannot be used without
   specifying the full path. To access the commands directly from anywhere, the
   directory containing the binaries should be added to `PATH`:

   ```bash
   export PATH="/projappl/<project>/$USER/hello-cmake/bin:$PATH"  # replace <project> with your CSC project, e.g. project_2001234
   ```

2. Try to run the program by typing:

   ```bash
   hi
   ```

3. You probably got an error like:

   ```bash
   hi: error while loading shared libraries: libhello.so: cannot open shared object file: No such file or directory
   ```
   
4. This happens because the program depends on a library file `libhello.so` and
   does not know where to look for it. This is a quite common issue with
   self-installed software. To fix the situation, add the `lib` path to the
   `LD_LIBRARY_PATH` environment variable:

   ```bash
   export LD_LIBRARY_PATH="/projappl/<project>/$USER/hello-cmake/lib:$LD_LIBRARY_PATH"  # replace <project> with your CSC project, e.g. project_2001234
   ```

5. Retry running the program, it should now work!

## Bonus: Create your own module for the program

💡 Users can create their own modules for self-installed applications. See the
["Module system" section](../../part-1/modules/index.md) for more details about
the CSC module system.

💬 CSC uses the [Lmod](https://lmod.readthedocs.io/en/latest/) module system
in which the Lua language is used to write modulefiles.

1. Create a directory for your own modulefiles:

   ```bash
   mkdir -p /projappl/<project>/$USER/my-modules  # replace <project> with your CSC project, e.g. project_2001234
   cd /projappl/<project>/$USER/my-modules        # replace <project> with your CSC project, e.g. project_2001234
   ```

2. In this directory, create a directory for the "Hello World" program and move
   there:

   ```bash
   mkdir -p hello-cmake
   cd hello-cmake
   ```

3. Let's assume this is version 0.0.1 of the "Hello World" program. Create a
   file `0.0.1.lua` and paste the contents below to it (using e.g. `nano`).
   Remember to change `<project>` and `<user>` to match your CSC project and
   username:

   ```lua
   -- This is an example modulefile for hello-cmake module
   -- Edit <project> and <user> below as needed to match the installation root directory
   local root = '/projappl/<project>/<user>/hello-cmake'
   local version = '0.0.1'

   load('boost/1.79.0')
   prepend_path('PATH', pathJoin(root, 'bin'))
   prepend_path('LD_LIBRARY_PATH', pathJoin(root, 'lib'))

   if (mode() == 'load') then
      LmodMessage('Hello World version', version, 'loaded.')
   end
   ```

4. The example highlights a few Lmod/Lua features:
   - Comments are specified with `--`.
   - `local` is used to declare local variables, in this case for the version
     number and installation path.
   - `load()` is used to load modules the program depends on.
   - `PATH` and `LD_LIBRARY_PATH` are modified using `prepend_path()`, and
     `pathJoin()` function is used together with `root` variable to compose the
     full paths to the `bin` and `lib` directories.
   - A message is printed to the standard output when the module is loaded
     using an `if` clause and `LmodMessage`.
5. To make your own modules available you need to modify your `MODULEPATH`
   variable. This can be done by hand or using `module use <path>` command, and
   is required each time you start a new shell session:

   ```bash
   module use /projappl/<project>/$USER/my-modules                     # replace <project> with your CSC project, e.g. project_2001234
   # or
   export MODULEPATH=/projappl/<project>/$USER/my-modules:$MODULEPATH  # replace <project> with your CSC project, e.g. project_2001234
   ```

6. Now that the module system knows where to search for your own modules, you
   can check if the module you created is available:

   ```bash
   module avail hello-cmake
   ```

7. Load the module and check if you can run `hi` command:

   ```bash
   module load hello-cmake/0.0.1
   hi
   ```

## More information

- Not all software use CMake build system. For an example how to build software
  using the traditional configure-make procedure, see
  [this tutorial](https://csc-training.github.io/csc-env-eff/hands-on/installing/installing_hands-on_mcl.html).
- If you get stuck when compiling your own software, don't hesitate to ask for
  help from [CSC Service Desk](https://docs.csc.fi/support/contact/)
- Documentation on how to compile on
  [Puhti](https://docs.csc.fi/computing/compiling-puhti/),
  [Mahti](https://docs.csc.fi/computing/compiling-mahti/) and
  [LUMI](https://docs.lumi-supercomputer.eu/development/).
