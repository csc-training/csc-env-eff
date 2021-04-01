---
theme: csc-2019
lang: en
---

# Logging in CSC Computers {.title}

In this section, you will learn how to login on CSC supercomputers with ssh and NoMachine.

# Log in with SSH

- SSH is a terminal program that will give you access to the command line on the CSC supercomputer
- It is the versatile main interface to a supercomputer
- Please read this page for an introduction on [how to login with ssh](https://docs.csc.fi/computing/connecting/)
   - Mac and Linux come with ssh, Windows Powershell can be used, but we recommend applications like MobaXterm, Putty, CMDer
- Note the [prerequisites to be able to access Puhti](https://docs.csc.fi/support/faq/how-to-get-puhti-access/)
- Plain ssh will not allow displaying remote graphics
   - It can be enabled by tunneling, but on Windows it will require additional installations, see the link above. 

# Log in via NoMachine

- NoMachine is a software that makes remote graphics easier, like using a graphical user interface (GUI)
   - Note, [R software](https://docs.csc.fi/apps/r-env-singularity/) and [Jupyter Notebooks](https://docs.csc.fi/computing/running/interactive-usage/#example-running-a-jupyter-notebook-server-via-sinteractive) have a better way via client server approach
- NoMachine client must be installed locally on your computer first (This may require admin privileges).
- [The client is used to connect to a server in Kajaani](https://docs.csc.fi/apps/nomachine/) and it provides faster graphical performance than X11-forwarding
- Please first consult the [Instructions on how to install and to use NoMachine](https://docs.csc.fi/support/tutorials/nomachine-usage/)

# Moving files between local computer and Puhti

- [scp](https://docs.csc.fi/data/moving/scp/) and [rsync](https://docs.csc.fi/data/moving/rsync/) are powerful command line tools to copy files
   - scp works even in Windows Powershell (but rsync is missing)
   - e.g. `scp filename cscusername@puhti.csc.fi:/scratch/project_xxxx`
- Sometimes a [GUI tool for transfering files](https://docs.csc.fi/data/moving/graphical_transfer/) is more convenient
   - Nice tools are e.g. FileZilla and WinSCP 
   - Installing such tools may require Admin privileges

# Advanced topic: Setting up SSH-keys

- Using SSH-keys is easier and safer than using password with every login.
- SSH-keys can be easily used in Windows, Macs, Linux
- Consult our [tutorials on how to set up SSH-keys for your account](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)
