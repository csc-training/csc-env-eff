---
theme: csc-eurocc-2019
lang: en
---

# Connecting to CSC Computers {.title}

This topic is about how to login to the CSC supercomputers.

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All materials (c) 2020-2023 by CSC – IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# Login via the Puhti Web Interface

- A simple way to log in the Puhti supercomputer is via [www.puhti.csc.fi](https://www.puhti.csc.fi)
- Use your CSC username and password
- The web interface can be used, _e.g._, to launch GUI applications and browse files
- [More in-depth documentation in Docs CSC](https://docs.csc.fi/computing/webinterface/)

# Login with SSH

- SSH is a terminal program that gives you command-line access on the CSC supercomputer
- It is a versatile main interface to a supercomputer
   - Laptop &harr; Toyota, Supercomputer &harr; F1. F1 needs a specialist interface.
- Please read this page for an introduction on [how to log in with SSH](https://docs.csc.fi/computing/connecting/)
   - Mac and Linux come with SSH. On Windows, Powershell can be used, but we recommend applications like MobaXterm, Putty, CMDer
   - Note the [prerequisites to be able to access Puhti](https://docs.csc.fi/support/faq/how-to-get-puhti-access/)
- Plain SSH will not allow displaying remote graphics
   - Puhti Web Interface is usually best option for this, but can be enabled also by tunneling (additional installations required on Windows, see link above)

# Moving files between a local computer and Puhti

- [`scp`](https://docs.csc.fi/data/moving/scp/) and [`rsync`](https://docs.csc.fi/data/moving/rsync/) are powerful command-line tools to copy files
   - `scp` works even in Windows Powershell (but `rsync` is missing)
   - _e.g._ `scp filename cscusername@puhti.csc.fi:/scratch/project_xxxx`
   - _e.g._ `rsync -r foldername cscusername@puhti.csc.fi:/scratch/project_xxxx`
   - `rsync` exists in _MobaXterm_ but it removes write permissions of copied files
- Sometimes a [GUI tool for transferring files](https://docs.csc.fi/data/moving/graphical_transfer/) is more convenient
   - Nice tools are _e.g._ _FileZilla_ and _WinSCP_ (may require admin privileges)
   - _MobaXterm_ also has a file transfer GUI (Tip: first, set persistent home directory)
   - Puhti Web Interface can also be used to move files

# Advanced topic: Setting up SSH keys

- Using SSH keys is easier and safer than using a password with every login
- SSH keys can be easily used in Windows, Mac, Linux
- Consult our [tutorials on how to set up SSH keys for your account](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)

# Advanced topic: Developing scripts remotely

- It's possible to use a local editor and push edited files easily into Puhti (or Rahti, ...) via ssh
   - For example, an IDE like _Visual Studio Code_ or a text editor like _Notepad++_
- Follow these [detailed instructions to set them up](https://docs.csc.fi/support/tutorials/remote-dev/)
