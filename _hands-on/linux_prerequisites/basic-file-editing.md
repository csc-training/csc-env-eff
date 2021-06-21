---
topic: Linux Prerequisites
title: Tutorial - Basic file editing
---
# Basic file editing

This tutorial requires that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
and it is a member of a project that [has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).
You have also already [logged to Puhti with ssh](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html), and [learned the basic Linux commands](https://csc-training.github.io/csc-env-eff/hands-on/linux_prerequisites/basic-linux-commands.html).

| ☝️ | NOTE: For graphical output to work you need to log in with `ssh -X account@puhti.csc.fi` |
|----|:------------------|

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

5. Let's download an image and a pdf
```bash
wget https://github.com/CSCfi/csc-env-eff/raw/master/slides/img/terminal_icon.png
wget https://github.com/CSCfi/csc-env-eff/raw/master/slides/img/schrodingerscat.pdf
```

6. Open the image with
```bash
eog terminal_icon.png
```
(Close the preview window.)

7. Open the pdf with
```bash
evince schrodingerscat.pdf
```
(Close the preview window.)

Now that we can open and edit files let's try to create one

8. You can also create files with `nano`. Try simply:
```bash
nano yourname-cool-note-file.sh
```

#### Extra steps for the Text-file expo -activity in Basic CLI -course

1. In the text-file: write instructions for others how to replicate your file-creation process, save and close.

2. Use `pwd` and copy the path to your current working directory

3. 10. Copy the text-file to your personal computer for example with scp:

| ☝️ | NOTE: This has to be typed in your personal computer's Terminal! |
|----|:------------------|

```bash
scp account@puhti.csc.fi:[path-to-your-wrkdir+the-file-name.txt] [path-to-local-folder-in-your-PC]
```

4. Submit your file into eLena course page
