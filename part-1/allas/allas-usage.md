---
layout: default
title: Basic usage of Allas
parent: 7. Allas
grand_parent: Part 1
nav_order: 1
has_children: false
has_toc: false
permalink: /hands-on/allas/tutorial_allas-file-transfer.html
---

# Basic usage of Allas

## Accessing Allas via the Puhti web interface

1. Go to the Puhti web interface: <https://www.puhti.csc.fi>.
2. Login with your CSC user account (or Haka).
3. Select *Cloud storage configuration* from the *Pinned Apps* view on the dashboard.
4. Enter your CSC password to authenticate, then create an Allas S3 connection for the project you want to use for this exercise.
   - You may skip the previous step if you've already configured a connection.

💡 Now you'll be able to browse your _buckets_ and _objects_ in Allas using the *Files* app!

{:style="counter-reset:step-counter 4"}
1. From the *Files* dropdown menu in the top navigation bar, select `s3allas-project_<id>` where `<id>` is the number of your project (e.g. 2001234).
2. Create a new bucket by pressing the *New Directory* button.
   - Name it as `<id>_<username>`, in which `<id>` is again the number of your project and `<username>` is your CSC username. Note that you cannot use a bucket name that already exists!
3. Open the created bucket by clicking it.
4. Upload one file from your computer into the bucket (any file should do, but prefer a file that you can open in Puhti, e.g. a text file).

💭 During the exercises, you can use this web interface to get another view to your buckets and objects in Allas.

## Accessing Allas from Puhti

### Preparations (if not done already)

1. Login to `puhti.csc.fi` (open a login node shell if using the web interface)
2. In Puhti, check your environment with the command

```bash
csc-workspaces
```

{:style="counter-reset:step-counter 2"}
3. Move to the scratch directory of your project:

```bash
cd /scratch/<project>   # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 3"}
4. Create your own subdirectory named as your username (tip! your username is automatically stored in the environment variable `$USER`):

```bash
mkdir -p $USER
cd $USER
```

### Connecting to Allas

1. Open a connection to Allas with these commands:

```bash
module load allas
allas-conf 
```

💡 It might take a while to run `module load allas`

{:style="counter-reset:step-counter 1"}
2. If you have several projects with access to Allas available, select the one where you just created a bucket using the Puhti web interface
3. Study what you have in Allas with [`a-commands`](https://docs.csc.fi/data/Allas/using_allas/a_commands/) and with [rclone](https://docs.csc.fi/data/Allas/using_allas/rclone/):

- With `a-commands`:

```bash
a-list
a-list <id>_$USER             # replace <id> with your CSC project number, e.g. 2001234
a-info <id>_$USER/<filename>  # replace <id> with your CSC project number, e.g. 2001234, and <filename> with the file you uploaded
```

- With `rclone`:

```bash
rclone lsd allas:
rclone ls allas:<id>_$USER
rclone lsl allas:<id>_$USER
rclone lsf allas:<id>_$USER
rclone cat allas:<id>_$USER/<filename>
```

{:style="counter-reset:step-counter 3"}
4. Download to Puhti the file that you just uploaded from your local computer to Allas. This can be done in two ways:

- With `a-commands`:

```bash
a-get <id>_$USER/<filename>     # replace <id> with your CSC project number, e.g. 2001234, and <filename> with the file you uploaded
```

- With `rclone`:

```bash
rclone copy allas:<id>_$USER/<filename> ./    # replace <id> with your CSC project number, e.g. 2001234, and <filename> with the file you uploaded
```

{:style="counter-reset:step-counter 4"}
5. Open, edit and rename the file so that you can distinguish it from the original one
6. Upload the new file to Allas:

- With `a-commands`:

```bash
a-put -b <id>_$USER <newfilename>   # replace <id> and <newfilename> accordingly
```

💭 Try running `a-put -h` to understand the command-line switch above and to find more information on options.

💬 With larger files it is good to include the option `-c` to enable `zstdmt` compression of the files.

- With `rclone`:

```bash
rclone copy <newfilename> allas:<id>_$USER/   # replace <newfilename> and <id> accordingly
```

{:style="counter-reset:step-counter 6"}
7. Check that the file in Puhti indeed has a counterpart in Allas:

```bash
a-check -b <id>_$USER <newfilename>   # replace <id> and <newfilename>
```

{:style="counter-reset:step-counter 7"}
8. Locate the files you just uploaded to Allas in the Puhti web interface (search for the bucket name)

### Clean up

1. Delete the local file from Puhti:

```bash
rm <filename>             # replace <filename>
```

{:style="counter-reset:step-counter 1"}
2. Whenever you need your data again, you can download it from Allas

💭 If you can't find your file but remember the name, try `a-find`. Use `a-find -h` for help.

## Extra: publish a file to the internet

💬 The `a-commands` include basic tools for publishing files to the internet. You might notice that the course slides use one of these! 🤓

‼️ Note: Using these commands makes your **entire bucket** public! Do not engage if you don't want that to happen. All files that you `a-put` in the bucket later will also be accessible from internet, since the _bucket_ is accessible.

### Option 1: `a-publish`

1. Select a file that has an appropriate content and publish it with the command:

```bash
a-publish -b <id>_$USER <filename>   # replace <id> and <filename>
```

{:style="counter-reset:step-counter 1"}
2. The command outputs a URL (public link). Copy it to your browser or send it to your friends 😎

### Option 2: `a-flip`

💬 `a-flip` is meant for files that need to be published only temporarily, for example for a one-time share.

1. Select a file that has an appropriate content and publish it with the command:

```bash
a-flip <filename>         # replace <filename>
```

{:style="counter-reset:step-counter 1"}
2. The command outputs an URL (public link). Copy it to your browser or send it to your friends 😎

‼️ Note: `a-flip` takes just the file name, not the bucket name like many of the previous commands.
