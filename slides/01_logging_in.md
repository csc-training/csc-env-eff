---
theme: csc-2019
lang: en
---

# Connecting to CSC Computers {.title}

In this section, you will learn how to login on CSC supercomputers with ssh and NoMachine.

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png)
</div>
<div class="column">
<small>
All material (C) 2020-2021 by CSC -IT Center for Science Ltd. and the authors.
This work is licensed under a **Creative Commons Attribution-NonCommercial-ShareAlike** 3.0
Unported License, [http://creativecommons.org/licenses/by-nc-sa/3.0/](http://creativecommons.org/licenses/by-nc-sa/3.0/)
</small>
</div>


# Log in with SSH

- SSH is a terminal program that will give you access to the command line on the CSC supercomputer
- It is the versatile main interface to a supercomputer
   - Laptop <-> Toyota, Supercomputer <-> F1. F1 needs a specialist interface.
- Please read this page for an introduction on [how to login with ssh](https://docs.csc.fi/computing/connecting/)
   - Mac and Linux come with ssh, Windows Powershell can be used, but we recommend applications like MobaXterm, Putty, CMDer
   - Note the [prerequisites to be able to access Puhti](https://docs.csc.fi/support/faq/how-to-get-puhti-access/)
- Plain ssh will not allow displaying remote graphics
   - It can be enabled by tunneling, but on Windows it will require additional installations, see the link above. 

# Log in via NoMachine

- NoMachine is a software that makes remote graphics easier, like using a graphical user interface (GUI)
   - Note, [R Studio](https://docs.csc.fi/apps/r-env-singularity/) and [Jupyter Notebooks](https://docs.csc.fi/computing/running/interactive-usage/#example-running-a-jupyter-notebook-server-via-sinteractive) have a better way via client server approach
- NoMachine client must be installed locally on your computer first (This may require admin privileges).
- [The client is used to connect to a server in Kajaani](https://docs.csc.fi/apps/nomachine/) and it provides faster graphical performance than X11-forwarding
- Please first consult the [Instructions on how to install and to use NoMachine](https://docs.csc.fi/support/tutorials/nomachine-usage/)

# Moving files between local computer and Puhti

- [scp](https://docs.csc.fi/data/moving/scp/) and [rsync](https://docs.csc.fi/data/moving/rsync/) are powerful command line tools to copy files
   - scp works even in Windows Powershell (but rsync is missing)
   - e.g. `scp filename cscusername@puhti.csc.fi:/scratch/project_xxxx`
   - e.g. `rsync -r foldername cscusername@puhti.csc.fi:/scratch/project_xxxx`
   - `rsync` is available in MobaXterm but it removes write permissions of copied files
- Sometimes a [GUI tool for transfering files](https://docs.csc.fi/data/moving/graphical_transfer/) is more convenient
   - Nice tools are e.g. FileZilla and WinSCP 
   - Installing such tools may require Admin privileges

# Advanced topic: Setting up SSH-keys

- Using SSH-keys is easier and safer than using password with every login.
- SSH-keys can be easily used in Windows, Macs, Linux
- Consult our [tutorials on how to set up SSH-keys for your account](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)

# Advanced topic: Developing scripts remotely

- It's possible to use a local editor and push edited files easily into Puhti (or Rahti, ...) via ssh
   - For example IDE like Visual Studio Code or a text editor like Notepad++
- Follow these [detailed instructions to set it up](https://docs.csc.fi/support/tutorials/remote-dev/)
