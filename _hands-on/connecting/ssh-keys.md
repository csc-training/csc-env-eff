---
topic: connecting
title: Advanced tutorial - Use SSH-keys to authenticate connection
---

# Creating and adding SSH-keys

💬 SSH-keys improve security and the ease of use.

☝🏻 This tutorial assumes you've already logged in and have the prerequisites covered.

## Windows10

💬 On Windows 10, there are multiple ssh clients available, but here we cover only [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and [MobaXterm](https://mobaxterm.mobatek.net/download.html).

‼️ In this tutorial, we assume you use MobaXterm. [More examples can be found in docs](https://docs.csc.fi/computing/connecting/).

### Create SSH-keys

💬 The MobaXterm terminal has many linux commandline tools available, e.g. the ones to set up ssh keys.

1. Launch MobaXterm from the applications list (opens from the windows logo) or search for it in the bottom bar search box.
2. Open a terminal with it (i.e. you'll stay on your local machine)
3. Follow these [step-by-step instructions](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)

### Set up MobaXterm to use the keys for Puhti

☝🏻 Some additional steps are needed to make connecting to Puhti and using e.g. Jupyter Notebooks and R-servers from interactive batch jobs via your browser. 

💬 The next steps show how to edit your local ssh config file and how to use an ssh-agent to use your key securely to access Puhti.

4. Continue the previous [guide at CSC docs](https://docs.csc.fi/computing/connecting/#using-ssh-keys-with-mobaxterm)
5. You will likely be asked to restart MobaXterm, do so.
6. Select puhti.csc.fi from your left connections menu and try launching e.g. 
[Jupyter Notebook interactively and access it via your browser](https://docs.csc.fi/computing/running/interactive-usage/#example-running-a-jupyter-notebook-server-via-sinteractive)

## Linux

1. Open a terminal on your local machine
2. Create the SSH-key in Terminal by typing:
```bash
ssh-keygen -t rsa -b 4096
```
3. Accept the default name and location (or customize them if needed).
4. Choose a secure passphrase for the SSH key. 
    - It should be at least 8 characters long and should contain numbers, letters and special characters.
5. Copy the public key to Puhti:
```bash
ssh-copy-id YOURUSERNAME@puhti.csc.fi   # replace YOURUSERNAME
```
6. Connecting with SSH to Puhti should now proceed without the need to write your key passphrase

### Optional step: launch Jupyter Notebook in Puhti
7. Login to puhti and try launching e.g. 
[Jupyter Notebook interactively and access it via your browser](https://docs.csc.fi/computing/running/interactive-usage/#example-running-a-jupyter-notebook-server-via-sinteractive)


## macOS

1. Open a terminal on your local machine
2. Create SSH key in Terminal by typing: 
```bash
ssh-keygen -t rsa -b 4096
```
3. Accept the default name and location (or customize them if needed).
4. Choose a secure passphrase for the SSH key. 
    - It should be at least 8 characters long and should contain numbers, letters and special characters.
5. Open `~/.ssh/config` and add the following rows into the file:
```bash
Host *
    UseKeychain no
    AddKeysToAgent yes
```
6. Open `~/.bash_profile` (or equivalent, see below ⬇️) and add the following row:
```bash
[[ -z ${SSH_AUTH_SOCK+x} ]] && eval "$(ssh-agent -s)"
```
7. Copy the SSH public key to Puhti by typing in Terminal
```bash
ssh-copy-id YOURUSERNAME@puhti.csc.fi
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

💭 More in-depth [step-by-step instructions in CSC docs.](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys)
