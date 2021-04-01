---
theme: csc-2019
lang: en
---

# Installing own software {.title}

In this section you will learn about installing your own software on CSC servers.

# Code categories
- It is possible to install software on CSC servers
- Start by reading the software documentation
  - Installation method depends on code type (or category)
  - Instructions found on the web rarely work "copy/paste" in HPC environment
- Before doing a lot of work, check if an alternative software is already available in [CSC application list](https://docs.csc.fi/apps/)

# Binares
- If you have ready made binaries, you can just try to run them
- The problem with ready made binaries is that they are hardly ever optimal for the computer they are used on
  - Especially MPI codes should always be re-compiled
- Ready binaries can be considered if
  - Source code not available
  - Software is compiled on an identical computer 
  - Software is for relatively light (serial or threaded) computation

# Interpreted languages
- Examples of High-level interpreted languages are
  -  Python, Java, Perl, R etc. 
- These languages do not need to be compiled, but they often can be. 
- These languages are often quite easy and efficient to program and therefore to get a result, but for very extensive computations they are rarely optimal (and can easily be very far from optimal). 
- An efficient code should be constructed so that heavy computations utilize libraries and/or subroutines written in High-Performance-Computing programming languages

# High-Performance-Computing languages
- Programming languages that need a compiler 
   - Typical examples are _e.g._ C, C++, and Fortran. 
- These languages are not easy to program and for complicated tasks need quite a lot of experience and much work.
- Most of the resource intensive software have been programmed with these
- As a researcher, you typically _only_ need to compile them (unless already available) 

# Basic requirements
- You need a computer with a decent internet connection.
- You need a CSC account and need to be [part of a project](https://research.csc.fi/accounts-and-projects)
- You need to [log in to a CSC computer](https://docs.csc.fi/computing/connecting/)
- You need to know, at least basic, Unix/Linux line commands 
  - CSC's [Linux basics tutorial](https://docs.csc.fi/support/tutorials/env-guide/using-linux-in-command-line/)
  - [Linux Command line quick reference / Cheat Sheet](https://docs.csc.fi/img/csc-quick-reference.pdf)


# Installation how-to 
- See tutorials for each category for more detailed instructions
  - [GitHub link for interpreted language tutorials](https://github.com/CSCfi/csc-env-eff/blob/master/hands-on/installing/README.md)
  - [GitHub link for High-Performance-Computing language tutorials](https://github.com/CSCfi/csc-env-eff/blob/master/hands-on/installing/README.md)
  - Applications may also be available as [containers](09_singularity.html), which can be used in CSC environment.

# Testing - it's important to test _first_
- Construct a batch script (see Chapter 3)
- Make a short and simple test run
  - Use known test data, e.g. test data provided by the code developer if you use a ready made code.
  - Run a tutorial provided with the code
- Run your test in the `test` queue or in an [interactive session](https://docs.csc.fi/computing/running/interactive-usage/) directly from the command line
- Compare performance to existing data (your old data, reference from the web, ...)
