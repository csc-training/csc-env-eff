---
layout: default
title: Installing binary applications
parent: 9. Installing own software
grand_parent: Part 2
nav_order: 1
has_children: false
has_toc: false
permalink: /hands-on/installing/installing_hands-on_binary.html
---

# Installing binary applications

> This tutorial is done on **Puhti**, which requires that:
  - You have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/).
  - Your account belongs to a project [that has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

💬 In some cases software developers offer ready-made binary versions of their
software.

- If the binary version runs, you don't need to compile the software yourself.

☝🏻 It should be noted that ready binary versions are typically not optimized
for CSC supercomputers.

- The performance difference will depend on the code and on how the application
  was compiled.
- Often the difference is just a few percent, but in some cases it can be more
  substantial.

‼️ Especially all MPI codes need to be compiled on the machine they will be run
on to ensure correct operation.

## Make the installation in your own folder in the `/projappl` directory of your project

1. Move to the `/projappl` directory of your project:

   ```bash
   cd /projappl/<project>   # replace <project> with your CSC project, e.g. project_2001234
   ```

2. If not done already, create your own folder under your project's `/projappl`
   directory:

   ```bash
   mkdir -p $USER
   ```

3. Move to your folder:

   ```bash
   cd $USER
   ```

## Example: Installing the GCTA software

💬 In this example we'll install the binary release of the GCTA software.

1. Go to the [GCTA download page](https://yanglab.westlake.edu.cn/software/gcta/#Download).
2. Identify the Linux version.
   - If several Linux versions are offered, try to find one with "x86" in the
     name.
   - If versions are offered by Linux distribution, try first the versions made
     for CentOS or RedHat if present.
   - Sometimes you may have to try different versions to find one that works.
3. Here is the link for the Linux version. Download the `.zip` file by running:

   ```bash
   wget https://yanglab.westlake.edu.cn/software/gcta/bin/gcta-1.94.1-linux-kernel-3-x86_64.zip
   ```

4. Unzip the file:

   ```bash
   unzip gcta-1.94.1-linux-kernel-3-x86_64.zip
   ```

5. The software is now ready to use, but you will have to tell the computer
   where to find it.
6. Trying just the following will result in a `command not found` error because
   you are not accessing the right folder yet.

   ```bash
   gcta64
   ```

7. Try instead:

   ```bash
   gcta-1.94.1-linux-kernel-3-x86_64/gcta64
   ```

8. Or:

   ```bash
   cd gcta-1.94.1-linux-kernel-3-x86_64
   ./gcta64
   ```

9. The result shows that the software runs.
   - The error message is just about missing arguments, which is normal.

💡 Instead of providing the full path in the command line, you can also add the
application to your `$PATH`.

10. Move to `./gcta-1.94.1-linux-kernel-3-x86_64` if not there yet.
11. Add the current working directory to `$PATH`:

    ```bash
    export PATH=$PWD:$PATH
    ```

12. You can now run the program from any directory simply with:

    ```bash
    gcta64
    ```

## Some notes

💡 When adding paths to `$PATH`, always remember to *append* the current
`$PATH`, otherwise some of your normal shell commands etc. will stop working.

☝🏻 To add paths automatically, you can add the `export` command to your
`$HOME/.bashrc` file. Instead of `$PWD`, use the full path:

```bash
export PATH=/projappl/<project>/$USER/gcta-1.94.1-linux-kernel-3-x86_64:$PATH   # replace <project> with your CSC project, e.g. project_2001234
```

‼️ If you make changes to your environment (e.g. edit `.bashrc`), it is possible
that there will be conflicts with applications pre-installed by CSC.

💭 If you encounter problems after modifying your environment, it is possible
to restore it to the default state permanently or temporarily using the
[`csc-env` command](https://docs.csc.fi/support/tutorials/using_csc_env/).
