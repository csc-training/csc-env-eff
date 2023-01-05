---
topic: allas
title: Tutorial - File transfer with Allas (essential)
---

# Basic usage of Allas

## Accessing Allas via the cPouta web interface

1. Open a view to the Allas service in your browser using the cPouta web interface: <https://pouta.csc.fi>
2. Login with your CSC user account
3. From the upper left corner, you'll find a project selection pop-up menu
   - If you have several projects available, select one that you want use in this exercise
4. From the menu on the left side of the interface, select `Object Store > Containers`

💡 A "container" in the cPouta web interface is called a "bucket" within the S3 protocol. Don't confuse this with Docker/Apptainer containers.

{:start="5"}
5. Create a new _bucket_ by pressing the button: **➕ Container**
   - Keep the bucket _Not public_ and name it as `<project number>_<username>`, in which `<project number>` is the number of your project (e.g. 2001234) and `<username>` is your CSC username
6. Find the newly created bucket and open it
7. Upload one file from your computer (any file should do, but prefer a file that you can open in Puhti, e.g. a text file)

💭 During the exercises, you can use this web interface to get another view to the buckets and objects in Allas.

☝🏻 Note, that you need to **reload** the view in order to see any recent changes.

## Accessing Allas from Puhti

### Preparations (if not done already)

1. Login to `puhti.csc.fi` (open a login node shell if using the web interface)
2. In Puhti, check your environment with the command

```bash
csc-workspaces
```

{:start="3"}
3. Move to the scratch directory of your project:

```bash
cd /scratch/<project>   # replace <project> with your CSC project, e.g. project_2001234
```

{:start="4"}
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

{:start="2"}
2. If you have several projects with access to Allas available, select the one where you just created a bucket using the cPouta web interface
3. Study what you have in Allas with [`a-commands`](https://docs.csc.fi/data/Allas/using_allas/a_commands/) and with [rclone](https://docs.csc.fi/data/Allas/using_allas/rclone/):

- With `a-commands`:

```bash
a-list
a-list <project_number>_$USER             # replace <project number> with your CSC project number, e.g. 2001234
a-info <project_number>_$USER/<filename>  # replace <project number> with your CSC project number, e.g. 2001234, and <filename> with the file you uploaded
```

- With `rclone`:

```bash
rclone lsd allas:
rclone ls allas:<project number>_$USER
rclone lsl allas:<project number>_$USER
rclone lsf allas:<project number>_$USER
rclone cat allas:<project number>_$USER/<filename>
```

{:start="4"}
4. Download to Puhti the file that you just uploaded from your local computer to Allas. This can be done in two ways:

- With `a-commands`:

```bash
a-get <project number>_$USER/<filename>     # replace <project number> with your CSC project number, e.g. 2001234, and <filename> with the file you uploaded
```

- With `rclone`:

```bash
rclone copy allas:<project number>_$USER/<filename> ./    # replace <project number> with your CSC project number, e.g. 2001234, and <filename> with the file you uploaded
```

{:start="5"}
5. Open, edit and rename the file so that you can distinguish it from the original one
6. Upload the new file to Allas:

- With `a-commands`:

```bash
a-put -b <project number>_$USER <newfilename>   # replace <project number> and <newfilename> accordingly
```

💭 Try running `a-put -h` to understand the command-line switch above and to find more information on options.

💬 With larger files it is good to include the option `-c` to enable `zstdmt` compression of the files.

- With `rclone`:

```bash
rclone copy <newfilename> allas:<project number>_$USER/   # replace <newfilename> and <project number> accordingly
```

{:start="7"}
7. Check that the file in Puhti indeed has a counterpart in Allas:

```bash
a-check -b <project number>_$USER <newfilename>   # replace <project number> and <newfilename>
```

{:start="8"}
8. Locate the files you just uploaded to Allas in the cPouta web interface (search for the bucket name)

### Clean up

1. Delete the local file from Puhti:

```bash
rm <filename>             # replace <filename>
```

{:start="2"}
2. Whenever you need your data again, you can download it from Allas

💭 If you can't find your file but remember the name, try `a-find`. Use `a-find -h` for help.

## Extra: publish a file to the internet

💬 The `a-commands` include basic tools for publishing files to the internet. You might notice that the course slides use one of these! 🤓

‼️ Note: Using these commands makes your **entire bucket** public! Do not engage if you don't want that to happen. All files that you `a-put` in the bucket later will also be accessible from internet, since the _bucket_ is accessible.

### Option 1: `a-publish`

1. Select a file that has an appropriate content and publish it with the command:

```bash
a-publish -b <project number>_$USER <filename>   # replace <project number> and <filename>
```

{:start="2"}
2. The command outputs a URL (public link). Copy it to your browser or send it to your friends 😎

### Option 2: `a-flip`

💬 `a-flip` is meant for files that need to be published only temporarily, for example for a one-time share.

1. Select a file that has an appropriate content and publish it with the command:

```bash
a-flip <filename>         # replace <filename>
```

{:start="2"}
2. The command outputs an URL (public link). Copy it to your browser or send it to your friends 😎
