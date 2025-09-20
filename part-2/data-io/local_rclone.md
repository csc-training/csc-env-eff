---
layout: default
title: Using Allas with local rclone
parent: 8. Working efficiently with data
grand_parent: Part 2
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/data-io/allas-local-rclone.html
---

# Using Allas with rclone from your local computer

💭 The graphical user interfaces of Allas can normally manage data transfers
between Allas and your local computing environment as long as the amount of
data and number of files is small. However, if you need to move large amounts
of data, then using command-line tools like `rclone` or `allas-cli-utils` could
be a more efficient way to use Allas.

💬 In this exercise, we'll study how you can use Allas from your own computer
using `rclone`, which is available for all common operating systems including
Windows and macOS. Note that in macOS and Linux machines you can also install
the whole allas-cli-utils repository locally.

## Step 1. Installing rclone

☝🏻 If you already have `rclone` command available, skip to [Step 2](#step-2-configuring-rclone-swift-connection-in-local-machine).

1. Download `rclone` executable to your own machine. Executables can be found
   from <https://rclone.org/downloads/>.
2. In case of Windows, if you don’t know which version to choose, try the
   [Intel/AMD 64 bit version](https://downloads.rclone.org/v1.66.0/rclone-v1.66.0-windows-amd64.zip).

## Step 2. Configuring rclone-Swift connection in local machine

1. Start the process by opening a command shell and executing command:
    1. Windows: `.\rclone.exe config`
    2. Linux and macOS: `./rclone config`
2. The configuration process in now done interactively in your command shell.
   In case of Allas, you need to do the following selections:
    1. Select **n** to create a *New remote*
    2. Name the remote as: `allas`
    3. From the list of storage protocols, select the number corresponding to:
       *OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)*
    4. Select authentication option **2**: *Get swift credentials from
       environment vars*.
    5. Select the default blank setting for all the remaining settings until
       you are back in the starting menu of the configuration process. 
    6. Finally, choose **q** to stop the configuration process.
3. You need to do this configuration only once.

## Step 3. Authentication

💭 In addition to the configuration, you must define a set of environment
variables to authenticate your Allas connection each time you start using
`rclone`. If you have access to Puhti, you can use it as an easy way to
generate a list of commands to set the authentication:

1. Open a terminal connection to Puhti and activate there a connection to the
   Allas project you wish to use so that you add option `--show-powershell`
   (Windows) or option `--show-shell` (macOS and Linux) to the `allas-conf` 
   command.
2. With these options, the configuration process prints out environment
   variable setting commands that you can run in your local machine to enable
   authentication to Allas.

### Windows PowerShell

1. If your local machine is running Windows, execute the following commands in
   Puhti:
   ```bash
   module load allas
   allas-conf --show-powershell
   ```
2. Copy the last four lines, starting with `$Env:`, to the local PowerShell and
   execute them. Then, test the `rclone` connection with command:
   ```console
   .\rclone.exe lsd allas:
   ```
3. Note that also in this case the connection will work only for the next 8
   hours. 

### macOS and Linux (bash and zsh)

1. If your local machine is running macOS or Linux, then the default shell is
   often `bash` or `zsh`. To activate Allas connection in these cases, run the
   following commands in Puhti:
   ```bash
   module load allas
   allas-conf --show-shell
   ```
2. Copy the last four lines, starting with `export`, to the local shell session
   and execute them. Then, test the `rclone` connection with command:
   ```bash
   ./rclone lsd allas:
   ```
3. Note that also in this case the connection will work only for the next 8
   hours.

## Step 4. Upload and download from local computer

💬 Use `rclone` to upload a small directory from your local computer to Allas.
The sample commands below are written for Windows PowerShell. In macOS and
Linux you should replace `rclone.exe` with `rclone` and `.\` in the directory
paths with `./`.

☝🏻 For this test, choose some unimportant directory that contains only a small
amount of data (less than 1 GiB).

1. First check what would be copied by running `rclone` command with option
   `--dry-run`. Prefix the target bucket name in Allas with your username to
   make it unique. So in the sample commands below you should replace
   `local-directory` and `username` with you own values.
   ```console
   .\rclone.exe copy -P --dry-run .\local-directory allas:username_local-directory
   ```
2. If the test command above works, then run the same command without
   `--dry-run` to actually copy the data:
   ```console
   .\rclone.exe copy -P .\local-directory allas:username_local-directory
   ```
3. What was the speed of transfer? Calculate how long time it would take to
   copy 10 GiB of data with the same speed?
4. Check the results with command:
   ```console
   .\rclone.exe ls allas:username_local-directory
   ```
5. Finally, copy the same data to a new directory on your local computer:
   ```console
   .\rclone.exe copy -P  allas:username_local-directory .\username_local-directory
   ```
6. What was the speed of transfer? Calculate how long time it would take to
   copy 10 GiB of data with the same speed?

## More information

💡 Docs CSC: [Local `rclone` configuration for Allas](https://docs.csc.fi/data/Allas/using_allas/rclone_local/)
