---
topic: Linux Prerequisites
title: Tutorial - Basic file editing
---

# Basic file editing

> ‼️ To begin make sure you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) that is a member of a project which [has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

> ☝🏻 You should also have already [logged in to Puhti with SSH](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html).

> ☝🏻 Note: For graphical output to work you need to log in with `ssh -X cscusername@puhti.csc.fi`. Another option is to use a remote desktop via the Puhti web interface, although this tutorial assumes you are working with SSH and X11-tunneling.

In the [previous tutorial](https://csc-training.github.io/csc-env-eff/hands-on/linux_prerequisites/basic-linux-commands.html) we downloaded a file called `my-first-file.txt`, made a copy of it named `YourName-first-file.txt`, and now we practice how to edit it!

💬 These exercises are done with the `nano` editor, but you can use your favorite editor too.

💡 Here's a [nano cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html)

## Processing text files

1. Open the file with `nano`:

```bash
nano YourName-first-file.txt      # replace YourName
```

{:start="2"}
2. Edit the file. Type something there!
3. Exit `nano` with `Ctrl+X`, type `Y` to confirm saving and press enter to accept the filename.
4. Check that the modifications are actually there:

```bash
less YourName-first-file.txt      # replace YourName
```

{:start="5"}
5. Exit the preview with `q`.

## Processing images and pdf files

1. Download an image and a pdf:

```bash
wget https://github.com/csc-training/csc-env-eff/raw/master/slides/img/terminal_icon.png
wget https://github.com/csc-training/csc-env-eff/raw/master/slides/img/schrodingerscat.pdf
```

{:start="2"}
2. Open the image with:

```bash
eog terminal_icon.png
```

{:start="3"}
3. Close the preview window.
4. Open the pdf with:

```bash
evince schrodingerscat.pdf
```

{:start="5"}
5. Close the preview window with your mouse or by pressing `Ctrl+C` when the Terminal window is selected.

## Create text files

1. You can also create files with `nano`. Try simply:

```bash
nano YourName-markdown-file.md
```

{:start="2"}
2. In the text file, write something (*e.g.* instructions for others how to replicate your file creation process), then save and close.
    - May I interest you with the [basic Markdown guide](https://www.markdownguide.org/basic-syntax/)?
3. Use `pwd` and copy the path of your current working directory
4. Copy the text file to your personal computer for example with `scp`

‼️ Note: The following has to be typed in your personal computer's terminal (not Puhti):

```bash
scp cscusername@puhti.csc.fi:/path/to/your/filename.md /path/to/local/folder
```

{:start="5"}
5. Look for the file on your personal computer and check that the contents match.

## More information

💡 You can read more about `scp` and moving files from [Docs CSC: Copying files using scp](https://docs.csc.fi/data/moving/scp/)

💬 One way to display `html` files on Puhti is to go through the Allas object storage service. After configuring Allas there's `a-commands` which enable publishing files on the internet. This is instructed in the [Allas tutorial](https://csc-training.github.io/csc-env-eff/hands-on/allas/tutorial_allas-file-transfer.html).
