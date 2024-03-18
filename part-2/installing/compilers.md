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

# Optimizing code performance through profiling

1. Create a directory for your code. The recommended location is under the `/projappl` directory of your project:

```bash
mkdir -p /projappl/<project>/myprog    # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 1"}
2. You need the source files of the code. Depending on the software, you can typically download them from e.g. GitHub. If you have the source code on your own computer, use e.g. [`scp`](https://docs.csc.fi/data/moving/scp/) to upload the data to the supercomputer.
3. If the source files are distributed as a zip file, use `unzip` to decompress:

```bash
unzip filename.zip    # modify the filename accordingly
```

{:style="counter-reset:step-counter 3"}
4. Read and follow any instructions on how to install. Usually, the code comes with a `README` or `INSTALL` file outlining the installation procedure.
5. When compiling, consider using the fast local disk on the login nodes (`$TMPDIR`) to move I/O load away from the parallel file system.
