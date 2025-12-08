---
layout: default
title: Basic file editing
parent: 1. Prerequisites
grand_parent: Part 1
nav_order: 5
permalink: /hands-on/linux_prerequisites/basic-file-editing.html
---

# Basic file editing

> ‼️ To begin, make sure you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) that is a member of a project which [has access to the Roihu service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).
>
> ☝🏻 You should also have already [logged in to Roihu with SSH](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-Roihu.html).
>
> ☝🏻 Note: For graphical output to work you need to log in with `ssh -X cscusername@roihu.csc.fi`. On Windows/macOS you also need to have an X server installed and running. [See details in the previous tutorial](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-roihu.html#remote-graphics). Another option is to use the Roihu web interface.

In the [previous tutorial](https://csc-training.github.io/csc-env-eff/hands-on/linux_prerequisites/basic-linux-commands.html) we downloaded a file called `my-first-file.txt`, made a copy of it named `YourName-first-file.txt`, and now we practice how to edit it!

💬 These exercises are done with the `nano` editor, but you can use your favorite editor too.

💡 Here's a [nano cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html)

## Processing text files

1. Open the file with `nano`:

   ```bash
   nano YourName-first-file.txt      # replace YourName
   ```

2. Edit the file. Type something there!
3. Exit `nano` with `Ctrl+X`, type `Y` to confirm saving and press enter to accept the filename.
4. Check that the modifications are actually there:

   ```bash
   less YourName-first-file.txt      # replace YourName
   ```

5. Exit the preview with `q`.

## Processing images and pdf files

☝🏻 Note! In case you are using the Roihu web interface, you need to open the files below from the file browser.

1. Download an image and a pdf:

   ```bash
   wget https://raw.githubusercontent.com/csc-training/csc-env-eff/master/_slides/img/terminal_icon.png
   wget https://raw.githubusercontent.com/csc-training/csc-env-eff/master/_slides/img/schrodingerscat.pdf
   ```

2. Open the image with `eog` or using the file browser of the Roihu web interface.

   ```bash
   eog terminal_icon.png
   ```

3. Close the preview window.
4. Open the pdf with `evince` or using the file browser of the Roihu web interface.

   ```bash
   evince schrodingerscat.pdf
   ```

5. Close the preview window with your mouse or by pressing `Ctrl+C` when the Terminal window is selected.

## Create text files

1. You can also create files with `nano`. Try simply:

   ```bash
   nano YourName-markdown-file.md
   ```

2. In the text file, write something (*e.g.* instructions for others how to replicate your file creation process), then save and close.
    - May I interest you with the [basic Markdown guide](https://www.markdownguide.org/basic-syntax/)?
3. Use `pwd` and copy the path of your current working directory
4. Copy the text file to your personal computer for example with `scp`

   ‼️ Note: The following has to be typed in your personal computer's terminal (not Roihu):

   ```bash
   scp cscusername@roihu.csc.fi:/path/to/your/filename.md /path/to/local/folder
   ```

5. Look for the file on your personal computer and check that the contents match.

## More information

💡 You can read more about `scp` and moving files from [Docs CSC: Copying files using scp](https://docs.csc.fi/data/moving/scp/)

💬 One way to display `html` files on Roihu is to go through the Allas object storage service. After configuring Allas there's `a-commands` which enable publishing files on the internet. This is instructed in the [Allas tutorial](https://csc-training.github.io/csc-env-eff/hands-on/allas/tutorial_allas-file-transfer.html).
