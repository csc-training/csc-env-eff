---
topic: allas
title: Tutorial - Allas mini tutorial
---

# Allas Mini tutorial

Open the view to the Allas service in your browser using the cPouta WWW-interface.

Open: https://pouta.csc.fi

And login with your csc user account.

From the upper left corner, you find a project selection pop-up menu. If you have several projects available, select the
training project: **project_2002389**

Then from the menu on left side of the interface, select:

**Object Store -> Containers**

And create new container by pressing button: **+Container**

Keep the container _Not public_ and name it as 2002389_xxxx ( replace xxxx with your user account).

Open the new bucket (that is here called as container) and upload one file from your computer. 
Any file should do, but prefer a file that you can open in Puhti.

During the exercises, you can use this interface to get another view to the buckets and objects in Allas.
> Note, that you need to **reload** the view in order to see the changes.


## Log in Puhti and use scratch

1. Login to puhti.csc.fi and move to scratch:

**Linux/Mac/MobaXterm on Windows**
```text
ssh XXXX@puhti.csc.fi   (replace XXXX with your csc user account)
```

**Windows/PuTTY**

   **host:* puhti.csc.fi
 
   **login as:** XXXX  (replace XXXX with your csc user account)


In Puhti check your environment with command:
```text
csc-workspaces
```
Switch to the scratch directory of your project 
```text
cd /scratch/project_2002389  # note! replace the text here (and below) with your project
```
And create your own sub-directory, named after your training account (if this directory does not yet exist):
```text
mkdir XXXX 
```
(replace XXXX with your user account)

move to the directory.
```text
cd XXXX
```

## Using Allas

Open connection to Allas. 
```text
module load allas
allas-conf 
```
If you have several Allas projects available, select the training project we are currently using.

Study what you have in allas with commands
```text
a-list
rclone lsd allas:

a-list 2002389_xxxx
rclone ls allas:2002389_xxxx
```

Download the file you just uploaded to Allas from your local computer.
You can do that in two ways (replace _your-file-name_ with the name of the file you uploaded):
```text
a-get 2002389_xxxx/your-file-name
```
or
```
rclone copy allas:2002389_xxxx/your-file-name ./
```

Upload the file back to Allas.

Try commands:

```text
a-put your-file-name
a-put --nc -b 2002389_xxxx 
```
Use use `a-put -h` to figure out the difference between the two commands above.

Then do the upload with rclone:
```text
rclone copy your-file-name allas:2002389_xxxx/
```
Locate the files you just uploaded in Pouta www-interface.




