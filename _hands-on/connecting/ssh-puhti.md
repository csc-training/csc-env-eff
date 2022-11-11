---
topic: connecting
title: Tutorial - Login to Puhti with browser or SSH (essential)
---

# Log in to Puhti

> ‼️ To begin make sure you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) that is a member of a project which [has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/). Note that there's a small delay before one can login to Puhti after creating a new project and adding services.

## Puhti Web Interface

💬 Connecting via the Puhti Web Interface is an easy way to access the Puhti supercomputer.

1. Open a web browser and go to [www.puhti.csc.fi](https://www.puhti.csc.fi)
2. Login with your CSC account
3. You have connected to Puhti

💡 From the top menus you can e.g. access your files and open some applications.

## Connecting with SSH from the Command Line

💬 The basic Command Line Interface (CLI) in Unix-based systems is the Terminal. Find the Terminal on your computer:  
![terminal-icon](../../slides/img/terminal_icon1.png)

💡 Different operating systems have slightly different CLIs and SSH-clients (programs that you can use for connecting to the supercomputers).

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

### Connecting from Windows10

💬 On Windows 10, you have different options:

- You can use the *Windows Power Shell*
- You can [download PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- You can [download and install MobaXterm](https://mobaxterm.mobatek.net/download.html).

‼️ In this tutorial, we assume you use MobaXterm. [More examples can be found in Docs CSC](https://docs.csc.fi/computing/connecting/).

1. Launch MobaXterm from the applications list (opens from the windows logo) or search for it in the bottom bar search box.
2. Click "SSH" icon at top left corner.
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

### Remote graphics

💬 By default remote graphics may not work. Try the following if you want to use any graphical tools in Puhti.

#### In Linux/macOS

1. Add X11-tunneling to your ssh-connection by adding `-X` or `-Y` to your command like this (replace `cscusername` with your CSC username):

```bash
ssh -X cscusername@puhti.csc.fi
```

#### In Windows

1. MobaXterm will actually tunnel the connection by default.

☝🏻 For intensive remote graphics we recommend using the [Web Interface](https://www.puhti.csc.fi/).

## More information

💭 [Docs: Connecting](https://docs.csc.fi/computing/connecting/)
