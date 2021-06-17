---
topic: Linux Prerequisites
title: Tutorial - Basic file editing
---
# Basic file editing

This tutorial requires that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
and it is a member of a project that [has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).
You have also already [logged to Puhti with ssh](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html), and [learned the basic Linux commands](https://csc-training.github.io/csc-env-eff/hands-on/linux_prerequisites/basic-linux-commands.html).

We downloaded a file called my-first-file.sh, made a copy of it (yourname-first-file.sh), and now we practise how to edit it!

These exercises are done with `nano` editor, but you can use your favorite editor too.
Here's the [nano cheet sheat](https://www.nano-editor.org/dist/latest/cheatsheet.html) 

1. Open the file with `nano`:
```bash
nano yourname-first-file.sh
```

2. Let's edit the file. Type something there!

3. Let's exit `nano` with (Ctrl + X), type Y to confirm saving and press enter to accept the filename.

4. Check that the modifications are actually there:
```bash
less yourname-first-file.sh
```
(Exit from preview with q.)

5. You can also create files with `nano`. Try simply:
```bash
nano yourname-cool-note-file.sh
```
Type something there as well, save, and close.
