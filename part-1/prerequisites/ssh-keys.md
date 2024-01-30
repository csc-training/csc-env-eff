---
layout: default
title: Using SSH keys
parent: 1. Prerequisites
grand_parent: Part 1
nav_order: 5
permalink: /hands-on/connecting/ssh-keys.html
---

# Creating and adding SSH keys

💬 SSH keys improve security and ease of use.

> ☝🏻 This tutorial assumes you've already logged in and have the prerequisites covered.

## Windows 10

💬 On Windows 10, there are multiple ssh clients available, such as [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and [MobaXterm](https://mobaxterm.mobatek.net/download.html).

‼️ In this tutorial, we assume you use MobaXterm. [More examples can be found in Docs CSC](https://docs.csc.fi/computing/connecting/).

### Create SSH keys

💬 The MobaXterm terminal has many Linux command line tools available, *e.g.* the ones to set up ssh keys:

1. Launch MobaXterm from the applications list (opens from the windows logo) or search for it in the bottom bar search box.
2. Open a terminal with it (*i.e.* you'll stay on your local machine)
3. Follow these [step-by-step instructions](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)

### Set up MobaXterm to use the keys for Puhti

☝🏻 Some additional steps are needed to enable connecting to Puhti and using *e.g.* Jupyter Notebooks and R-servers from interactive batch jobs via your browser.

💬 The next steps show how to edit your local ssh config file and how to use an ssh-agent to use your key securely to access Puhti.

1. Continue the previous [guide at Docs CSC](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)
2. You will likely be asked to restart MobaXterm, do so.
3. Select puhti.csc.fi from your left connections menu and try launching *e.g.*
[Jupyter Notebook interactively and access it via your browser](https://docs.csc.fi/support/tutorials/rstudio-or-jupyter-notebooks/)

## Linux

1. Open a terminal on your **local machine**
2. Create the SSH-key in the terminal by typing:

```bash
ssh-keygen -o -a 100 -t ed25519
```

{:style="counter-reset:step-counter 2"}
3. Accept the default name and location (or customize them if needed).
4. Choose a secure passphrase for the SSH key.
    - It should be at least 8 characters long and should contain numbers, letters and special characters.
5. Copy the public key to Puhti (replace `cscusername` with your CSC username):

```bash
ssh-copy-id cscusername@puhti.csc.fi
```

{:style="counter-reset:step-counter 5"}
6. Connecting with SSH to Puhti should now proceed without the need to write your key passphrase

## macOS

1. Open a terminal on your **local machine**
2. Create the SSH key in the terminal by typing:

```bash
ssh-keygen -o -a 100 -t ed25519
```

{:style="counter-reset:step-counter 2"}
3. Accept the default name and location (or customize them if needed).
4. Choose a secure passphrase for the SSH key.
    - It should be at least 8 characters long and should contain numbers, letters and special characters.
5. Open `~/.ssh/config` and add the following lines into the file:

```bash
Host *
    UseKeychain no
    AddKeysToAgent yes
```

{:style="counter-reset:step-counter 5"}
6. Open `~/.bash_profile` (or equivalent, see below ⬇️) and add the following line:

```bash
[[ -z ${SSH_AUTH_SOCK+x} ]] && eval "$(ssh-agent -s)"
```

{:style="counter-reset:step-counter 6"}
7. Copy the SSH public key to Puhti by typing in the terminal (replace `cscusername` with your CSC username):

```bash
ssh-copy-id cscusername@puhti.csc.fi
```

☝🏻 Equivalent files for configuring profile in step 6.

- `~/.bashrc`
- `~/.bash_rc`
- `~/.bash_profile`

And with `zsh`-shell

- `~/.zshrc`
- `~/.zsh_rc`
- `~/.zsh_profile`

## More information

💭 More in-depth [step-by-step instructions in Docs CSC](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys).

‼️ If you make changes to your environment (e.g. edit `.bashrc`) in CSC supercomputers, it is possible that there will be conflicts with applications installed by CSC.

💭 If you have problems after making changes to your environment, it is possible to restore it to default state permanently or temporarily using the [csc-env command](https://docs.csc.fi/support/tutorials/using_csc_env/).
