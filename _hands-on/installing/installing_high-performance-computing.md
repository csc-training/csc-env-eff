---
topic: installing
title: Exercise - installing own C, C++, or Fortran
---

# installing, making and making your own C, C++, or Fortran program in the CSC environment

## scenario A: you have a code already, you want to install it and run it.
 - Create a proper directory for your code (command: mkdir dir-name)
 - You need the codes sources files. Download from e.g. GitHub or use e.g. scp to upload a .zip file to the directory (https://docs.csc.fi/data/moving/scp/)
 - Unzip you code (line command: unzip code-name.zip)
 - Follow any instructions on how to install. Usually comes with the code in form of a ‘readme’ or ’how to install’ file.

   ### Install scenario A1: the code comes with cmake
 - Load the module cmake with line command: module load cmake, and load also any other e.g. libraries the code needs (avilable modules: module spider), or try download and install also needed libraries.
 - Create a ‘build’ directory, and go to that directory (line commad: mkdir build, then: cd build)
 - Run cmake ..
 - If error messages, try to fix. If it becomes really messed up, remove all and start again from the .zip file
 - Run ‘make’ to compile the specific codes you want to use
 - Ask help from servicedesk if you really get stuck (mail to: servcedesk@csc.fi)

   ### Install scenario A2: the code comes with a makefile
 - Module load or install separately any needed libraries (check available modules with line command: module spider. Load module with: module load name-of-module)
 - Edit the ‘makefile’ and replace compile and link commands with proper ones for Mahti (https://docs.csc.fi/computing/compiling-mahti/) or Puhti ( https://docs.csc.fi/computing/compiling-puhti/)
 - Run the command ‘make’
 - Read error messages and try to fix
 - Ask help from servicedesk if not successfull (mail to: servicedesk@csc.fi)

## Scenario B: you want to write your own code
 - You need an editor https://docs.csc.fi/support/tutorials/env-guide/text-and-image-processing/
 - Launch an editor and write the code
 - Compile your code (on puhti:https://docs.csc.fi/computing/compiling-puhti/, and on Mahti: https://docs.csc.fi/computing/compiling-mahti/)
 - Fix bugs until compiler accepts code
 
## Exercise
 - Write your own simple code, compile it if necessary and run it.
