---
topic: allas
title: Tutorial - Allas file transfer 
---

# Allas web-interface

- Open the view to the Allas service in your browser using the cPouta WWW-interface: [https://pouta.csc.fi](https://pouta.csc.fi)
- Login with your csc user account.
- From the upper left corner, you find a project selection pop-up menu. 
   - If you have several projects available, select the training project: **project_2004306**
- From the menu on left side of the interface, select: **Object Store -> Containers**
- Create new container by pressing button: **➕Container**
   - Keep the container _Not public_ and name it as 2004306_xxxx ( replace xxxx with your user account).
- Find the newly-created container (also called as `bucket` in S3 protocol) and open it
   - Upload one file from your computer. Any file should do, but prefer a file that you can open in Puhti.

💭 During the exercises, you can use this web-interface to get another view to the buckets and objects in Allas.
> Note, that you need to **reload** the view in order to see the changes.

## Accessing Allas in Puhti

**Do these preparations if not done already:**

- Login to puhti.csc.fi and move to scratch.
   - In Puhti check your environment with command:
```text
csc-workspaces
```
   - Switch to the scratch directory of your project 
```text
cd /scratch/project_2004306    # NOTE: Here you can use also your project
```
- Create your own sub-directory:
```text
mkdir XXXX      # replace XXXX with eg. username
cd XXXX
```

**Then let's connect to allas:**

- Open connection to Allas wih these commands:
```text
module load allas
allas-conf 
```
   - If you have several Allas projects available, select the training project because you created the container/bucket there.
- Study what you have in allas with commands
   1. With a-commands:
```text
a-list
a-list 2004306_xxxx     # replace xxxx so that the name corresponds to your new container/bucket
```
   2. With r-tools
```text
rclone lsd allas:
rclone ls allas:2004306_xxxx     # replace xxxx so that the name corresponds to your new container/bucket
rclone lsl allas:2004306_xxxx    # replace xxxx so that the name corresponds to your new container/bucket
rclone lsf allas:2004306_xxxx    # replace xxxx so that the name corresponds to your new container/bucket
```
- Download the file you just uploaded to Allas from your local computer. You can do that in two ways: 
   1. With a-commands:
```text
a-get 2004306_xxxx/your-file-name         # replace xxxx and your-file-name
```
   2. With r-tools
```
rclone copy allas:2004306_xxxx/your-file-name ./ # replace xxxx and your-file-name
```
- Open/edit (+rename) the file so that you can distinguish it from the original
- Upload the file to Allas:
   1. With a-commands:
```text
a-put --nc -b 2004306_xxxx your-file-name   # replace xxxx and your-file-name
```
💭 Use `a-put -h` to figure out the command parameters above.

   2. With r-tools
Then do the upload with rclone:
```text
rclone copy your-file-name allas:2004306_xxxx/
```
- Locate the files you just uploaded in Pouta web-interface.
