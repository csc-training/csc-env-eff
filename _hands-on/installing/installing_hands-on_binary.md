---
topic: installing
title: Tutorial - Installing binary applictions (essential)
---

# Installing binary applications

💬 In some cases the software developers offer ready-made binary versions of their software. 
- If the binary version runs, you don't need to compile the software yourself.

☝🏻 It should be noted that ready binary versions are typically not optimized for CSC supercomputers.
- The difference in performance will depend on the code, and on how the application was compiled. 
- Often the difference is just a few percent, but in some cases it can be more substantial.

‼️ Especially all MPI codes need to be compiled on the machine they will be run on to ensure correct operation.

## Example: Installing GCTA software

💬 In this example we install the binary release of GCTA software.

1. Go to the [GCTA download page](https://cnsgenomics.com/software/gcta/#Download).
2. Identify the Linux version. 
    - If several Linux version are offered, try find one with "x86" in the name.
    - If version are offered by Linux distribution, try first the versions made for CentOs or RedHat if present. 
    - Sometimes you may have to try different versions to find one that works.
3. Here is the link for the Linux version (accessed 19.07.21). Download the zip file by typing:
    ```bash
    wget https://cnsgenomics.com/software/gcta/bin/gcta_1.93.2beta.zip
    ```
4. Open the zip file:
    ```bash
    unzip gcta_1.93.2beta.zip
    ```
5. The software is now ready to use, but you will have to tell the computer where to find it. 
    - Trying just the following will result in a `command not found` error because you are not accessing the right folder yet.
    ```bash
    gcta64
    ```
6. Try instead:
    ```bash
    gcta_1.93.2beta/gcta64
    ```
    - Or:
    ```bash
    cd gcta_1.93.2beta
    ./gcta64
    ```
7. The result shows that the software runs.
    - The error message is just about missing arguments which is normal. 

💬 Instead of providing the path in the command line, you can also add the application to `$PATH`. 

{:start="8"}
8. Change folder into `./gcta_1.93.2beta` if not there yet!
9. To add the current directory to `$PATH`:
    ```bash
    export PATH=$PWD:$PATH
    ```
10. You should now be able to run the program from any directory with simply:
    ```bash
    cd ..
    gcta64
    ```

## Some notes: 
💡 When adding paths to `$PATH`, always remember to include the current `$PATH`, or some of your normal shell commands etc. will stop working.

☝🏻 To make the addition permanent, you can add the `export` command to your `$HOME/.bashrc`file. Instead of `$PWD` use the full path, something like:
    ```bash
    export PATH=/projappl/project_12345/gcta_1.93.2beta:$PATH
    ```

‼️ If you make changes to your environment (e.g. edit `.bashrc`), it is possible that there will be conflicts with CSC installed applications.

💭 If you have problems after making changes to your environment, it is possible to restore it to default state permanently or temporarily using the [csc-env command](https://docs.csc.fi/support/tutorials/using_csc_env/)
