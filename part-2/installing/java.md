---
layout: default
title: Installing Java applications
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 6
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_hands-on_java.html
---

# Installing Java applications (on Puhti)

💬 Java applications do not typically require special installation.

- You just need to download the distribution package, typically a `.jar` file.

💡 Compute nodes do not have a default Java installation, so you need to load a
suitable Java module.

You can check the available modules with the command:

```bash
module spider java
```

💬 Despite their name, modules named `biojava` are just normal Java
installations, which can be used with any software, not just bio applications.

☝🏻 Some java applications fail to run on the login nodes. Try running them
using `sinteractive` instead (or by opening a compute node shell in the
[Puhti web interface](https://www.puhti.csc.fi)).

‼️ Naturally, computationally heavy tasks should be never ran on the login
nodes.

💡 The compute nodes have very limited `/tmp` space. If you have to set the
temporary file location for a Java application, you can use:

```bash
export _JAVA_OPTIONS=-Djava.io.tmpdir=/path/to/tmp  # replace with the actual path 
```

## Example: Installing ABRA2

💬 In this example we'll install and run the Java application ABRA2.

1. Create a personal folder (if not done already) under your project's
   `/projappl` directory and move there. Then create (and move to) a new
   directory for the installation:

   ```bash
   cd /projappl/<project>  # replace <project> with your CSC project, e.g. project_2001234
   mkdir -p $USER
   cd $USER
   mkdir abra2
   cd abra2
   ```

2. Download the software:

   ```bash
   wget https://github.com/mozack/abra2/releases/download/v2.24/abra2-2.24.jar
   ```

3. Load a Java module:

   ```bash
   module load biojava
   ```

   💡 If you get error messages or warnings about the Java version, try loading
   another Java module.

4. Run the application:

   ```bash
   java -jar abra2-2.24.jar
   ```

   💡 If you are not in the same directory as the `.jar` file, you need to
   include the full path to the file, e.g.

   ```bash
   java -jar /projappl/<project>/$USER/abra2/abra2-2.24.jar  # replace <project> with your CSC project, e.g. project_2001234, and ensure that the path corresponds to the true path
   ```

## Example 2: Java application with a shell wrapper script

💬 Some Java applications come with shell scripts that are used to launch them
instead of calling Java directly. See the documentation of each software for
details.

💡 One example of such an application is BEAST:

```bash
sinteractive --account <project>  # replace <project> with your CSC project, e.g. project_2001234
module load beast
beast -help
```

☝🏻 BEAST will fail to run on the login nodes. Try running it in an interactive
session instead (using `sinteractive` or a compute node shell in the
[Puhti web interface](https://www.puhti.csc.fi)).
