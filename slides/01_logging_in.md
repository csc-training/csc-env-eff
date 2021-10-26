---
theme: csc-2019
lang: en
---

# Connecting to CSC Computers {.title}

This topic is about how to login on CSC supercomputers with ssh and NoMachine.

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All material (C) 2020-2021 by CSC -IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# Log in via Puhti Web Interface

- A simple way to log in to Puhti Supercomputer is via [https://puhti.csc.fi](https://puhti.csc.fi)
   - NOTE: Puhti Web Interface is still beta-version in October 2021
- Use your CSC username and password
- The web interface can eg. launch some applications and browse files
- [More in-depth documentation in Docs CSC](https://docs.csc.fi/computing/webinterface/)

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
   - Note that for example [R Studio](https://docs.csc.fi/apps/r-env-singularity/) and [Jupyter Notebooks](https://docs.csc.fi/computing/running/interactive-usage/#example-running-a-jupyter-notebook-server-via-sinteractive) can easily be run from the Puhti web interface (first slide).
- NoMachine client must be installed locally on your computer first (This may require admin privileges).
- [The client is used to connect to a server in Kajaani](https://docs.csc.fi/apps/nomachine/) and it provides faster graphical performance than X11-forwarding
- Please first consult the [Instructions on how to install and to use NoMachine](https://docs.csc.fi/support/tutorials/nomachine-usage/)

# Moving files between local computer and Puhti

- [scp](https://docs.csc.fi/data/moving/scp/) and [rsync](https://docs.csc.fi/data/moving/rsync/) are powerful command line tools to copy files
   - scp works even in Windows Powershell (but rsync is missing)
   - _e.g._ `scp filename cscusername@puhti.csc.fi:/scratch/project_xxxx`
   - _e.g._ `rsync -r foldername cscusername@puhti.csc.fi:/scratch/project_xxxx`
   - `rsync` exists in _MobaXterm_ but it removes write permissions of copied files
- Sometimes a [GUI tool for transfering files](https://docs.csc.fi/data/moving/graphical_transfer/) is more convenient
   - Nice tools are _e.g._ _FileZilla_ and _WinSCP_ (May require Admin privileges)
   - _MobaXterm_ also has a file transfer GUI (TIP: first, set persistent home directory)
   - Puhti web interface can be used to move files

# Advanced topic: Setting up SSH-keys

- Using SSH-keys is easier and safer than using password with every login
- SSH-keys can be easily used in Windows, Macs, Linux
- Consult our [tutorials on how to set up SSH-keys for your account](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)

# Advanced topic: Developing scripts remotely

- It's possible to use a local editor and push edited files easily into Puhti (or Rahti, ...) via ssh
   - For example, IDE-like _Visual Studio Code_ or a text editor like _Notepad++_
- Follow these [detailed instructions to set them up](https://docs.csc.fi/support/tutorials/remote-dev/)
