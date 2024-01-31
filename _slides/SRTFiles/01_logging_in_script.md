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

:::info (speech)
This lecture introduces you to different ways to interface with a supercomputer.
:::

# Log in via Puhti Web Interface

- A simple way to log in to Puhti Supercomputer is via [https://puhti.csc.fi](https://puhti.csc.fi)
   - NOTE: Puhti Web Interface is still beta-version in October 2021
- Use your CSC username and password
- The web interface can eg. launch some applications and browse files
- [More in-depth documentation in Docs CSC](https://docs.csc.fi/computing/webinterface/)

:::info (speech)
There is a new web interface, that can be used to access Puhti directly from a web browser.
Note that the web interface is still a beta-version, which means there might be further changes.
Use you CSC username to log in.
From there you can access your files in Puhti, and launch some applications.
More in-depth documentation is available in Docs CSC.
:::

# Log in with SSH

- SSH is a terminal program that will give you access to the command line on the CSC supercomputer
- It is the versatile main interface to a supercomputer
   - Laptop <-> Toyota, Supercomputer <-> F1. F1 needs a specialist interface.
- Please read this page for an introduction on [how to login with ssh](https://docs.csc.fi/computing/connecting/)
   - Mac and Linux come with ssh, Windows Powershell can be used, but we recommend applications like MobaXterm, Putty, CMDer
   - Note the [prerequisites to be able to access Puhti](https://docs.csc.fi/support/faq/how-to-get-puhti-access/)
- Plain ssh will not allow displaying remote graphics
   - It can be enabled by tunneling, but on Windows it will require additional installations, see the link above. 

:::info (speech)
The usual way to log in to CSC supercomputers is using a secure shell (SSH). 
SSH can be opened for example in the Command Line Interface. 
In Linux and Mac that is known as Terminal.
We recommend to get familiar with the basics of a Command Line Interface, which is a little more spesific interface, that lets you use the full power of a supercomputer. 
We have documentation and an introductory tutorial on how to SSH to Puhti. 
The links are in the description.
Mac and Linux come with an SSH client in the Terminal by default. 
In Windows 10, there's something called the PowerShell. 
It can be used as well, but it might not be fully compatible with our setup. 
Therefore we recommend another software called MobaXTerm, which is free to use.
Putty or CMDer can also be used.
Installing these software may require admin privileges, so you might need your IT support to do this for you.
If you do plain SSH, by default it might not allow displaying remote graphics. 
On Linux or Mac you can just add a capital X or Y to your SSH command, and it will tunnel the remote graphics from Puhti. 
In Windows MobaXTerm has a way to do that, or then you would need to install some other tools. 
:::

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

:::info (speech)
Sometimes you may edit files in your local computer - and want to copy the files to a supercomputer or vice versa.
You can use secure copy and RSync directly from the command line. 
The basic syntax is scp or RSync, then source path, then target path.
The path in another computer needs to include the domain and the username at that machine.
RSync is available in MobaXTerm, which is one reason we recommend MobaXTerm for Windows users. 
Sometimes a graphical user interface for transferring files is much more convenient.
For Windows FileZilla and WinSCP are good examples. 
Installing them might require admin privileges.
MobaXTerm also has a file transfer functionality. 
When downloading files they go by default to a home folder, which is in a weird place. 
The tip is to first choose this home directory from the Settings tab.
Also Puhti web interface can be used to move files between Puhti and a local computer.
:::

# Advanced topic: Setting up SSH-keys

- Using SSH-keys is easier and safer than using password with every login
- SSH-keys can be easily used in Windows, Macs, Linux
- Consult our [tutorials on how to set up SSH-keys for your account](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)

:::info (speech)
SSH-keys are used for example in some RStudio, or Jupyter Notebook workflows.
You don't need SSH-keys for logging in to CSC supercomputers, but they can make your workflows easier at some point. 
A tutorial covers the setup for SSH-keys.
The link is in the materials index page.
:::

# Advanced topic: Developing scripts remotely

- It's possible to use a local editor and push edited files easily into Puhti (or Rahti, ...) via ssh
   - For example, IDE-like _Visual Studio Code_ or a text editor like _Notepad++_
- Follow these [detailed instructions to set them up](https://docs.csc.fi/support/tutorials/remote-dev/)

:::info (speech)
The default workflow of editing files is to open an editor on Puhti. 
With lot of files - for example when coding - that is not so convenient.
For these purposes you can install a suitable editor – like Visual Studio code, or configure Notepad++, so that they sync the files to Puhti. 
We have some detailed documentation in docs.csc.fi, with instructions on how to set up such environment.

The tutorials about Accounts and Connecting continue from here. 
They cover the basic use cases with easy-to-follow examples. 
Check the links in the description!
:::
