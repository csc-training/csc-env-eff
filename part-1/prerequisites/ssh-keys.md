---
layout: default
title: Using SSH keys
parent: 1. Prerequisites
grand_parent: Part 1
nav_order: 5
permalink: /hands-on/connecting/ssh-keys.html
---

# Creating and adding SSH keys

💬 SSH keys improve security and ease-of-use.

> ☝🏻 This tutorial assumes you've already logged in and have the prerequisites covered.

## Windows

💬 On Windows, there are multiple ssh clients available, such as [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and [MobaXterm](https://mobaxterm.mobatek.net/download.html).

‼️ In this tutorial, we assume you use MobaXterm. [More examples can be found in Docs CSC](https://docs.csc.fi/computing/connecting/ssh-windows/).

💬 The MobaXterm terminal has many Linux command-line tools available, *e.g.* the ones to set up SSH keys:

1. Launch MobaXterm from the applications list (opens from the Windows logo) or search for it in the bottom bar search box.
2. Open a terminal with it (*i.e.* you'll stay on your local machine).
3. Follow these [step-by-step instructions](https://docs.csc.fi/computing/connecting/ssh-windows/#mobaxterm).

## Linux

1. Open a terminal on your **local machine**
2. Create the SSH-key in the terminal by typing:

   ```bash
   ssh-keygen -o -a 100 -t ed25519
   ```

3. Accept the default name and location (or customize them if needed).
4. Choose a secure passphrase for the SSH key.
    - It should be at least 8 characters long and should contain numbers, letters and special characters.
5. Copy the public key to Puhti (replace `cscusername` with your CSC username):

   ```bash
   ssh-copy-id cscusername@puhti.csc.fi
   ```

6. Connecting with SSH to Puhti should now proceed without the need to write your key passphrase

## macOS

1. Open a terminal on your **local machine**
2. Create the SSH key in the terminal by typing:

   ```bash
   ssh-keygen -o -a 100 -t ed25519
   ```

3. Accept the default name and location (or customize them if needed).
4. Choose a secure passphrase for the SSH key.
    - It should be at least 8 characters long and should contain numbers, letters and special characters.
5. Open `~/.ssh/config` and add the following lines into the file:

   ```bash
   Host *
       UseKeychain no
       AddKeysToAgent yes
   ```

6. Open `~/.bash_profile` (or equivalent, see below ⬇️) and add the following line:

   ```bash
   [[ -z ${SSH_AUTH_SOCK+x} ]] && eval "$(ssh-agent -s)"
   ```

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

💭 More in-depth [step-by-step instructions in Docs CSC](https://docs.csc.fi/computing/connecting/ssh-keys/).

‼️ If you make changes to your environment (e.g. edit `.bashrc`) in CSC supercomputers, it is possible that there will be conflicts with applications installed by CSC.

💭 If you have problems after making changes to your environment, it is possible to restore it to default state permanently or temporarily using the [csc-env command](https://docs.csc.fi/support/tutorials/using_csc_env/).
