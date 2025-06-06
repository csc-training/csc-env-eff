---
theme: csc-eurocc-2019
lang: en
---

# Connecting to CSC Supercomputers {.title}

This topic is about how to login to the CSC supercomputers.

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All materials (c) 2020-2025 by CSC – IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# Login via the web interfaces

- A simple way to login to the Puhti supercomputer is via <https://www.puhti.csc.fi>
- Use your CSC username and password
- The web interface can be used, _e.g._, to launch GUI applications, browse files or open a command-line shell
   - The latter is useful if your computer does not have an SSH client, but you need command-line access to the supercomputer
- Similar web interfaces are also available for Mahti and LUMI
  - More in-depth documentation in [Docs CSC](https://docs.csc.fi/computing/webinterface/) and [Docs LUMI](https://docs.lumi-supercomputer.eu/runjobs/webui/)

# Login with SSH

- SSH is a terminal program that gives you command-line access on the CSC supercomputer
- It is a versatile main interface to a supercomputer
   - Laptop &harr; Toyota, Supercomputer &harr; F1. F1 needs a specialist interface.
- Please read this page for an introduction on [how to log in with SSH](https://docs.csc.fi/computing/connecting/#using-an-ssh-client)
   - Example: `ssh cscusername@puhti.csc.fi`
   - Mac and Linux have SSH. On Windows, PowerShell can be used, but we recommend the web interfaces, or clients like MobaXterm or PuTTY
- Plain SSH will not allow displaying remote graphics
   - The web interfaces are often best for this, but can be enabled also by X11-tunneling (additional installations required on Windows, see link above)

# Moving files between a local computer and Puhti

- [`scp`](https://docs.csc.fi/data/moving/scp/) and [`rsync`](https://docs.csc.fi/data/moving/rsync/) are powerful command-line tools to copy files
   - `scp` works even in Windows PowerShell (but `rsync` is missing)
   - _e.g._ `scp filename cscusername@puhti.csc.fi:/scratch/project_xxxx`
   - _e.g._ `rsync -r foldername cscusername@puhti.csc.fi:/scratch/project_xxxx`
   - `rsync` exists in _MobaXterm_ but it removes write permissions of copied files
- Sometimes a [GUI tool for transferring files](https://docs.csc.fi/data/moving/graphical_transfer/) is more convenient
   - Nice tools are _e.g._ _FileZilla_ and _WinSCP_ (may require admin privileges)
   - _MobaXterm_ also has a file transfer GUI (Tip: first, set persistent home directory)
   - The web interfaces can also be used to easily upload/download files

# Setting up SSH keys

- Using SSH keys is easier and safer than using a password with every login
   - A key pair is created and the **public** key is uploaded to the supercomputer
- SSH keys can be easily used in Windows, Mac, Linux
- Consult our [tutorials on how to set up SSH keys for your account](https://docs.csc.fi/computing/connecting/ssh-keys/)
   - [Logging in to LUMI](https://docs.lumi-supercomputer.eu/firststeps/getstarted/) requires setting up an SSH key pair _and_ registering the public key in [MyCSC](https:/my.csc.fi)
   - Adding SSH keys in MyCSC for Puhti and Mahti is also possible, but not yet a requirement for connecting
