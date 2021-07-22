---
topic: Linux Prerequisites
title: Tutorial - Basic file editing
---
# Basic file editing

This tutorial requires that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
and it is a member of a project that [has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).
You have also already [logged to Puhti with ssh](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html), and [learned the basic Linux commands](https://csc-training.github.io/csc-env-eff/hands-on/linux_prerequisites/basic-linux-commands.html).

☝️ NOTE: For graphical output to work you need to log in with `ssh -X account@puhti.csc.fi`

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
wget https://github.com/csc-training/csc-env-eff/raw/master/slides/img/terminal_icon.png
wget https://github.com/csc-training/csc-env-eff/raw/master/slides/img/schrodingerscat.pdf
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
nano yourname-cool-note-file.txt
```

9. In the text-file: write something eg. instructions for others how to replicate your file-creation process, save and close.

10. Use `pwd` and copy the path to your current working directory

11. Copy the text-file to your personal computer for example with scp:

☝️ NOTE: This has to be typed in your personal computer's Terminal!

```bash
scp account@puhti.csc.fi:[path-to-your-wrkdir+the-file-name.txt] [path-to-local-folder-in-your-PC]
```

12. Look for the file in your personal computer and check that the contents match.

## EXTRA: Open `html`-files in Puhti**  
**Alternative 1: Firefox**  
- Download a html-file to your folder in Puhti:
```bash
wget https://a3s.fi/mjaskeli-2004306-pub/index.html
```
- Load Bioconda-module which includes Firefox:
```bash
module load Bioconda
```
- The message says that you need to set the `PROJAPPL` environment variable.
    - To do so, run command (you can check the XXXXXXX of your project(s) with command `csc-workspaces`):
```bash
export PROJAPPL=/projappl/project_XXXXXXX
```
- Re-run the ```module load Bioconda``` command:
```bash
module load bioconda
```
- Open the file with Firefox
```bash
firefox index.html
```

**Alternative 2: Allas**  
- After configuring Allas there's a-commands which include publishing files to the internet. This is instructed in [Allas-tutorial](https://csc-training.github.io/csc-env-eff/hands-on/allas/tutorial_allas-file-transfer.html)