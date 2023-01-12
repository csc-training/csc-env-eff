---
topic: connecting
title: Tutorial - Login to Puhti with a browser or SSH (essential)
---

# Log in to Puhti

> ‼️ To begin make sure you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) that is a member of a project which [has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/) and perhaps [Allas](https://docs.csc.fi/data/Allas/). Note that there's a small delay before one can login to Puhti after creating a new project and adding services.

## Puhti web interface

💬 Connecting via the Puhti web interface is an easy way to access the Puhti supercomputer.

1. Open a web browser and go to <https://www.puhti.csc.fi>
2. Login with your CSC account (or Haka/Virtu)
3. You have now connected to Puhti!

💭 The Puhti web interface landing page looks like this:  
![Puhti web interface](../../slides/img/ood.png)

💡 From the pinned apps and top menus you can *e.g.* access your files and open some applications or a command-line interface.

## Connecting with SSH from the command-line

💬 The basic Command Line Interface (CLI) in Unix-based systems is the Terminal. Find the Terminal on your computer:  
![terminal-icon](../../slides/img/terminal_icon1.png)

💡 Different operating systems have slightly different CLIs and SSH-clients (programs that you can use to connect to the supercomputers).

### Connecting from Linux

💬 Laptops and workstations running Linux typically have SSH installed:

1. Open a terminal and type (replace `cscusername` with your CSC username):

```bash
ssh cscusername@puhti.csc.fi
```

{:start="2"}
2. Scroll down to [In Puhti](#in-puhti)

### Connecting from macOS

💬 In macOS, you can use Terminal similarly to Linux machines:

1. Open the Terminal application and type (replace `cscusername` with your CSC username):

```bash
ssh cscusername@puhti.csc.fi
```

{:start="2"}
2. Scroll down to [In Puhti](#in-puhti)

### Connecting from Windows

💬 On Windows you have different options:

- You can use the [Puhti web interface](https://www.puhti.csc.fi) to connect with your browser ([see above](#puhti-web-interface))
- You can use the *Windows Power Shell*
- You can [download PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- You can [download and install MobaXterm](https://mobaxterm.mobatek.net/download.html).

‼️ The following steps assume you use MobaXterm. [More examples can be found in Docs CSC](https://docs.csc.fi/computing/connecting/).

1. Launch MobaXterm from the applications list (opens from the Windows logo), or search for it in the bottom bar search box.
2. Click the "SSH" icon in the top left corner.
3. In the Basic SSH settings section Remote host field write "puhti.csc.fi"
4. Tick the "specify username" box and in the box write your CSC username (leave port in the default setting 22).
5. Click "OK" at the bottom.
6. MobaXterm will now login to puhti.csc.fi and ask you for your password.

💡 The next time you want to login to Puhti, just select it from the "session" menu on the left.

💭 The MobaXterm window looks like this:  
![terminal-icon](../../slides/img/mobaxterm-login.png)

## In Puhti

1. If you're connecting to Puhti (or a specific Puhti login node) for the first time, SSH will ask you if you trust the authenticity of the host, *e.g.*:

```text
The authenticity of host 'puhti-login14.csc.fi' can't be established.
ECDSA key fingerprint is SHA256:kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

{:start="2"}
2. The first time you connect, you need to accept, but the key should not change for the next login.
3. Pay attention whether you logged in `login11`, `login12`, `login14` or `login15`.
4. Once you've logged in you'll see a greeting starting something like this:

```text
┌─ Welcome ───────────────────────────────────────────────────────────────────┐
│         CSC - Tieteen tietotekniikan keskus - IT Center for Science         │
│            ____        __    __  _                                          │
│           / __ \__  __/ /_  / /_(_)   - -  -   -                            │
│          / /_/ / / / / __ \/ __/ /   - -  -   -                             │
│         / ____/ /_/ / / / / /_/ /   - -  -   -                              │
│        /_/    \__,_/_/ /_/\__/_/   - -  -   -                               │
│                                                                             │
│      Puhti.csc.fi - Atos BullSequana X400 - 682 CPU nodes - 80 GPU nodes    │
├─ Contact ───────────────────────────────────────────────────────────────────┤
│ Servicedesk : 09-457 2821, servicedesk@csc.fi   Switchboard : 09-457 2001   │
├─ User Guide ────────────────────────────────────────────────────────────────┤
│ https://docs.csc.fi                                                         │
├─ Manage my account ─────────────────────────────────────────────────────────┤
│ https://my.csc.fi/                                                          │
├─ Software ──────────────────────────────────────────────────────────────────┤
...
└─────────────────────────────────────────────────────────────────────────────┘
[cscusername@puhti-login14 ~]$
```

{:start="5"}
5. Now, you're ready to go.
6. Let's do our first small task in Puhti: let's check our projects and that we have a one with access to Allas service! 
```bash
csc-projects
module load allas
allas-conf
```

{:start="7"}
7. The first command `csc-projects` lists your projects. The second command `module load allas` loads the Allas tools in your use. The third command `allas-conf` sets up the connection to Allas: it will ask for your CSC password, and then you need to select which project you want to use (by typing the number of the project, for example `2`). If you don't see a project here, please return to [CSC account and project](credentials.md) tutorial and see that you have a project with access to Allas service. Please note, that it can take up to 1h after accepting the terms of use before the service is in use.

### Remote graphics

💬 Remote graphics may not work by default. Try the [Puhti web interface](https://docs.csc.fi/computing/webinterface/) for running graphical applications. Another option is to enable X11-tunneling as follows.

#### On Linux/macOS

1. Add X11-tunneling to your SSH connection by adding `-X` or `-Y` to your `ssh` command like this (replace `cscusername` with your CSC username):

```bash
ssh -X cscusername@puhti.csc.fi
```

#### On Windows

1. MobaXterm will actually tunnel the connection by default.

☝🏻 For intensive remote graphics we recommend using the [Puhti web interface](https://www.puhti.csc.fi/).

## More information

💭 [Docs: Connecting](https://docs.csc.fi/computing/connecting/)
