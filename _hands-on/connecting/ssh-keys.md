---
topic: connecting
title: Advanced tutorial - Use SSH-keys to authenticate connection
---

# Ssh-keys improve security and facilitate use

This tutorial assumes you've already logged in and have the prerequisites covered.

## Windows10

On Windows 10, there are multiple ssh clients available, but here we cover only
[Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), and
[MobaXterm](https://mobaxterm.mobatek.net/download.html).

In this tutorial, we assume you use MobaXterm. [More examples can be found
in docs](https://docs.csc.fi/computing/connecting/).

### Create ssh keys

The MobaXterm terminal has many linux commandline tools available, e.g. the ones
to set up ssh keys.

1. Launch MobaXterm from the applications list (opens from the windows logo) or search for it
in the bottom bar search box.
2. Open a terminal with it (i.e. you'll stay on your local machine)
3. Follow these [step-by-step instructions](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)

### Set up MobaXterm to use the keys for Puhti

Some additional steps are needed to make connecting to Puhti and using e.g. Jupyter Notebooks and R-servers
from interactive batch jobs via your browser. The next steps show how to edit your local ssh config
file and how to use an ssh-agent to use your key securely to access Puhti.

4. Continue the previous [guide at CSC docs](https://docs.csc.fi/computing/connecting/#using-ssh-keys-with-mobaxterm)
5. You will likely be asked to restart MobaXterm, do so.
6. Select puhti.csc.fi from your left connections menu and try launching e.g. 
[Jupyter Notebook interactively and access it via your browser](https://docs.csc.fi/computing/running/interactive-usage/#example-running-a-jupyter-notebook-server-via-sinteractive)

## MacOS and Linux

1. Open a terminal on your local machine
2. Follow these [step-by-step instructions](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)
3. Start a local ssh-agent and add your new ssh key to it
4. ssh to Puhti should now proceed without the need to write your key passphrase
5. Login to puhti and try launching e.g. 
[Jupyter Notebook interactively and access it via your browser](https://docs.csc.fi/computing/running/interactive-usage/#example-running-a-jupyter-notebook-server-via-sinteractive)


