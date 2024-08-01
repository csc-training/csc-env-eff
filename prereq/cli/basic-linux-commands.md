---
layout: default
title: Basic Linux commands
parent: 2. Command-line basics
grand_parent: Prerequisites
nav_order: 1
permalink: /hands-on/linux_prerequisites/basic-linux-commands.html
---

# Basic Linux commands

> ‼️ To begin make sure you have a
> [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
> that is a member of a project which
> [has access to the Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

> ☝🏻 You should also have already
> [logged in to Puhti with SSH](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html)
> or via the Puhti web interface (and opened a login node shell).

## Briefly about Linux commands

CSC supercomputers use Linux operating systems. The traditional, and typically
most efficient, way of interacting with a Linux operating system is through a
text-based command-line interface (CLI), also called a *shell*. The user inputs
lines of text (commands), which are interpreted by the shell as directives for
the computer to execute a specific task.

The general syntax of Linux commands is:

```bash
command parameter1 parameter2 ... parameterN
```

The parameters correspond to options or input arguments provided by the user
that alter the behavior of the command. They may be optional or mandatory.
Options are usually denoted by a single hyphen and a single character (e.g.
`command -o`). Some options may also have a longer, more descriptive
alternative prefixed by two hyphens (e.g. `command --option`).

Some commands allow single-character options to be combined. For example,
`command -o -p` could be written more succinctly as `command -op`. Otherwise,
any letter following an option would be interpreted as an argument for it.

Most Linux commands have their own manual page. If you at any point need help
with using a certain command, you can study its reference manual on the
command-line using `man`:

```bash
man command
```

## Navigating folders

1. Now that you have logged in to Puhti, check which folder (a.k.a. directory)
   you are in by typing `pwd` (**p**rint **w**orking **d**irectory) and
   hitting `Enter`:

   ```bash
   pwd
   ```

2. Probably you got `/users/<username>` as the result (with `<username>`
   replaced by your actual CSC username). This is your *home* directory.
   Different levels in the hierarchical directory tree are distinguished by the
   forward-slash character `/`. The first `/` denotes the *root directory* --
   all other files and directories are located in subdirectories of this
   directory so that each file has a unique combination of a name and a
   directory path.

3. Check if there are any files or subdirectories in your home directory by
   typing the `ls` command (**l**i**s**t):

   ```bash
   ls
   ```

4. Create a new directory using the `mkdir` command (**m**a**k**e
   **dir**ectory) and see if it appears:

   ```bash
   mkdir my-test-folder
   ls
   ```

5. Go to that folder using the `cd` command (**c**hange **d**irectory).

   ```bash
   cd my-test-folder
   ```

   💡 Note: if you just type `cd` and the first few letters of the folder name,
   then hit `Tab` key, the terminal completes the name. Handy!

6. Various shorthand arguments are available for navigating directories. Return
   to the *parent directory* (i.e. move one level up in the hierarchy) by using
   the shorthand `../`:

   ```bash
   cd ../
   ```

   💡 To move multiple directories up, you would just repeat the pattern, e.g.
   `cd ../../` to move two levels up. Note that a single dot `./` is used to
   represent the current directory.

7. Another useful shorthand is `~/` which denotes your home directory. Move
   again into your new directory `my-test-folder` with:

   ```bash
   cd ~/my-test-folder
   ```

   💡 The previous command would work from any directory as it is essentially a
   shorthand for giving the full path, `/users/<username>/my-test-folder`.

## Exploring files

1. Download a file into the `my-test-folder` directory. The command `wget` is a
   convenient tool for downloading from a URL:

   ```bash
   wget https://a3s.fi/CSC_training/my-first-file.txt
   ```

2. Check what kind of file you got and what size it is using the `ls` command
   with some extra options:

   ```bash
   ls -lth
   ```

   - `-l` is for long listing format
   - `-t` is for sorting by time (most recently edited file first)
   - `-h` is for convenient human-readable size units (also `--human-readable`)

3. Use the `less` command to check out what the file looks like:

   ```bash
   less my-first-file.txt
   ```

4. To exit the `less` preview of the file, hit `q`.

   💡 Tip: Instead of `less` you can use `cat` which prints the content of the
   file(s) directly on the command-line. For long texts `less` is recommended.

5. Make a copy of this file:

   ```bash
   cp my-first-file.txt my-second-file.txt
   ls -lth
   less my-second-file.txt
   ```

6. Remove the file we originally downloaded (leave your own copy).

   ```bash
   rm my-first-file.txt
   ls
   ```

   💡 Tip: If you don't want to have duplicate files you can use `mv` to
   **m**o**v**e and, optionally, rename files. The syntax is similar:

   ```bash
   mv /path/to/source/oldname /path/to/destination/newname
   ```

## More information

* Learn
  [how to edit that file](https://csc-training.github.io/csc-env-eff/hands-on/linux_prerequisites/basic-file-editing.html)
  in the next tutorial!
* [Linux guide in Docs CSC](https://docs.csc.fi/support/tutorials/env-guide/)

💡 For more information of a given command-line `command`: type `man command`
or `command --help` where `command` is replaced with the one that you need help
with.

💡 Tip: If you remember *a part of a command* that you have used recently you
can search for it with the command `history | grep string`. This will show all
your used commands that have included the string `string` (replace this with
the pattern you are searching for).
