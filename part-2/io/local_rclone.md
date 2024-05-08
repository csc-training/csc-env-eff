---
layout: default
title: Using Allas with local rclone
parent: 8. Working efficiently with data
grand_parent: Part 2
nav_order: 4
has_children: false
has_toc: false
permalink: /hands-on/disk-areas/disk-areas-exercise-fastdisks.html
---

# Using Allas with Rclone from your local computer.

The graphical user interfaces of Allas can normally manage data transfers between Allas and your local computing environment as long as the amount of data and files is small. However if you need transfer large amounts of data, then using command lines tools like `rclone` or `allas-cli-utils` could be more effective way to use Allas.

In this exercise we study how you can use Allas from your own computer using rclone, that is available for all common operating systems including Windows and Mac. Not that in Mac and Linux machines you can also install the whole allas-cli-utils repository to your machine.


## 1 Installing Rclone


If you  don’t  have  Rclone in you local machine, dowload rclone executable to your own machine.

Executables can  be found from:

[https://rclone.org/downloads/](https://rclone.org/downloads/)

In case of Windows , if you don’t know, which version to choose, try the Intel/AMD 64 bit version:

   [https://downloads.rclone.org/v1.66.0/rclone-v1.66.0-windows-amd64.zip](https://downloads.rclone.org/v1.66.0/rclone-v1.66.0-windows-amd64.zip)


## 2 Configuring rclone-Swift connection in local machine

Start the process by opening commmand shell and executing command;
Windows:

```text
   .\rclone.exe config
```   
Mac and Linux

```text
   ./rclone config
```
Configuration procerss in now done interactivelu in your command shell.
In the case of Allas you need to do following selections:
    1. Select *n* to create a New remote 
    2. Name the remote as: *allas* 
    3. From the list of storage protocols, select the number that defines: *OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)* 
    4. Select authentication option *2 Get swift credentials from environment vars*. 
    5. After that select the default blank setting for all the remaining settings until you are back in the starting menu of the configuration process. 
    6. Finally, choose *q* to stop the configuration process. 

You need to do this configuration only once. 


## 3. Authentication

In addition to the configuration, you must define a set of environment variables to autenticate your Allas connection each time you start using rclone. If you have access to Puhti, you can use it as an easy way to generate a list of commands to set the authentication. 

Open terminal connection to Puhti and activate there connection to the Allas project you wish to use so that you add option `--show-powershell` (Windows) or option `--show-shell` (Mac and linux) to the `allas-conf` command. 

With these options, the configuration process prints out environment variable setting commands that you can run in your local machine, to enable authentication to Allas

### 3.1 Windows PowerShell

If your local machine is running on Windows. Execute following commands in Puhti:
```text
module load allas
allas-conf --show-powershell
```
Copy the last four lines, starting with `$Env:`, to the local powershell and execute them. Then test the rclone connection with command :

```text
  .\rclone lsd allas:
```

Note that also in this case the connection will work only for the next 8 hours. 

### 3.2. Mac and Linux (bash and zsh )
If your local machine is running on Mac or Linux then the default command shell is often `bash` or `zsh`. To actuivate Allas connection in these cases run following commands in Puhti:

```text
  module load allas
  allas-conf --show-shell
```
Copy the last four lines, starting with word `export`, to the local shell session and execute them. Then test the rclone connection with command:

```text
  .\rclone.exe lsd allas:
```

Note that also in this case the connection will work only for the next 8 hours.

## 4. Upload and Download from local computer

Use rclone to upload a small directory from your local comuter to Allas. The sample commands below are written for Windows PowerShell. In Mac and linux machine you should replace _.\rclone.exe_ with _rclone_
and _.\\_ in the directory paths with _./_ .

For this test, choose some unimportant derectory that contains only small amount of data ( less than 1 GiB).

First check what would be copied by runing rclone command with option `--dry-run`. In the Allas side, name the target bucket so that you add your user name in front of the directory name. So in the sample commads below you shiuld replace _local-directory_ and _username_ with you own values.

```text
   .\rclone.exe copy -P --dry-run .\local-directory allas:username_local-directory
```
If the test command above works, then run the same command without _--dry-run_ to actually copy the data:

```text
    .\rclone.exe copy -P  .\local-directory allas:username_local-directory
```

What was the speed of transfer? Calculate how long time it would take to copy 10 GiB of data with the same speed?

Check the results with command:

```text
   .\rclone.exe ls allas:username_local-directory
```

Finally copy the same data to new directory in your local computer.    

```text
   .\rclone.exe copy -P  allas:username_local-directory .\username_local-directory
```

What was the speed of transfer? Calculate how long time it would take to copy 10 GiB of data with the same speed?