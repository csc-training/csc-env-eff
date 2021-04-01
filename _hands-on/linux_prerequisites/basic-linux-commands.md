---
topic: Linux Prerequisites
title: Tutorial - Basic linux commands
---
# Basic Linux commands

This tutorial requires that you have a [user account at CSC](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
and it is a member of a project that [has access to Puhti service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/).
You have also already [logged to Puhti with ssh](ssh-puhti.md).


1. Now that you have logged in Puhti, let's check in which folder we are in! Type pwd and hit Enter.
```bash
pwd
```

2. Are there any files there? 
```bash
ls
```

3. Let's make a directory (replace YourName with your name, for example: MariasTestFolder)! Try `ls` to see if the folder is now there!
```bash
mkdir YourNameTestFolder 
ls
```

4. Go to that folder. Note, that if you just type `cd` and the first letter of the folder name,  then hit 'tab' key, the terminal completes the name. Handy!
```bash
cd YourNameTestFolder
```

5. Let's download a file into this new folder. `wget` is the command for downloading from URL.
```bash
wget https://github.com/CSCfi/csc-env-eff/raw/master/hands-on/linux_prerequisites/my-first-file.sh
```

6. What kind of file did you get? What's in that file now? What size is it? Let's use `ls` command with some extra parameters, and `less`  command to check out how the file looks like. 
```bash
ls -lth
less my-first-file.sh
```
To exit the `less` preview of the file, hit 'q'. 

7. Let's make a copy of this file (again, replace YourName with your name).
```bash
cp my-first-file.sh YourName-first-file.sh
ls -lth
less YourName-first-file.sh
```

8. Let's remove the file we originally downloaded (leave your own copy). 
```bash
rm my-first-file.sh
ls
```

Next, let's learn [how to edit that file](basic-file-editing.md)!
