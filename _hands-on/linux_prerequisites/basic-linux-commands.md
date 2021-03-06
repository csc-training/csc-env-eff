---
topic: Linux Prerequisites
title: Tutorial - Basic linux commands
---

# Basic Linux commands

> ‼️ To begin make sure that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/) and it is a member of a project that [has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).

> ☝🏻 You should also have already [logged to Puhti with ssh](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html).

### Navigating folders

1. Now that you have logged in Puhti, check in which folder you are in: type `pwd` and hit Enter.
    ```bash
    pwd
    ```
2. Check if there are any files:
    ```bash
    ls
    ```
3. Make a directory and see if it appears:
    ```bash
    mkdir YourNameTestFolder    # replace YourName
    ls
    ```
4. Go to that folder. 
    ```bash
    cd YourNameTestFolder       # replace YourName
    ```

💡 Note, that if you just type `cd` and the first letter of the folder name,  then hit 'tab' key, the terminal completes the name. Handy!
    

### Exploring files 

1. Download a file into this new folder. Use the command `wget` for downloading from an URL:
    ```bash
    wget https://github.com/csc-training/csc-env-eff/raw/master/_hands-on/linux_prerequisites/my-first-file.txt
    ```
2. Check what kind of file did you get and what size it is using `ls` command with some extra parameters:
    ```bash
    ls -lth         # parameters are l for long format, t for sorting by time and h for convenient size units. Anything that starts with a hashtag is a comment and is not executed
    ```
3. Use `less` command to check out what the file looks like:
    ```bash
    less my-first-file.txt
    ```
4. Exit `less` preview of the file, hit 'q'.  

💡 Tip: Instead of `less` you can use `cat` which prints the content of the file(s) straight into command line. For long texts `less` is recommended.

{:start="5"}
5. Make a copy of this file:
    ```bash
    cp my-first-file.txt YourName-first-file.txt  # replace YourName
    ls -lth
    less YourName-first-file.txt                 # replace YourName
    ```
6. Remove the file we originally downloaded (leave your own copy). 
    ```bash
    rm my-first-file.txt
    ls
    ```

💡 Tip: If you don't want to have duplicate files you can use `mv` to 'move/rename' the file. Syntax is the same: `mv [path/source] [path/destination]`.

## More information
- Learn [how to edit that file](https://csc-training.github.io/csc-env-eff/hands-on/linux_prerequisites/basic-file-editing.html) in the next tutorial!

💡 More information of a given command line `command`: type `man command` or `command --help` where `command` is replaced with the one that you need help with.

💡 Pro-tip: if you remember *a part of a command* that you have used you can input it as `'string'` into command `history | grep 'string'` to see all your used commands that include the `'string'`.