---
topic: allas
title: Tutorial - File transfer with Allas
---

# Allas basic usage

## Accessing Allas via web-interface

1. Open the view to the Allas service in your browser using the cPouta WWW-interface: [https://pouta.csc.fi](https://pouta.csc.fi)
2. Login with your csc user account.
3. From the upper left corner, you find a project selection pop-up menu. 
   - If you have several projects available, select the training project `project_2004306`
4. From the menu on left side of the interface, select: **Object Store -> Containers**
5. Create new container by pressing button: **➕Container**
   - Keep the container _Not public_ and name it as *2004306_YOURUSERNAME*.
6. Find the newly-created container (also called as `bucket` in S3 protocol) and open it
7. Upload one file from your computer. Any file should do, but prefer a file that you can open in Puhti.

💭 During the exercises, you can use this web-interface to get another view to the buckets and objects in Allas.

☝🏻 Note, that you need to **reload** the view in order to see the changes.

## Accessing Allas from Puhti

### Preparations (if not done already)

1. Login to puhti.csc.fi
2. In Puhti check your environment with command:
```bash
csc-workspaces
```
3. Switch to the scratch directory of your project 
```bash
cd /scratch/project_2004306    # NOTE: Here you can use also your project
```
4. Create your own sub-directory:
```bash
mkdir YOURUSERNAME      # replace YOURUSERNAME
cd YOURUSERNAME
```

### Connecting to allas

1. Open connection to Allas wih these commands:
```bash
module load allas
allas-conf 
```
2. If you have several Allas projects available, select the training project because you already created the container/bucket there.
3. Study what you have in allas with commands:
   1. With a-commands:
   ```bash
   a-list
   a-list 2004306_YOURUSERNAME                 # Name should correspond to your new container/bucket
   a-info 2004306_YOURUSERNAME/your-file-name  # replace name and your-file-name
   ```
   2. With r-tools
   ```bash
   rclone lsd allas:
   rclone ls allas:2004306_YOURUSERNAME                  # Name should correspond to your new container/bucket
   rclone lsl allas:2004306_YOURUSERNAME                 # Name should correspond to your new container/bucket
   rclone lsf allas:2004306_YOURUSERNAME                 # Name should correspond to your new container/bucket
   rclone cat allas:2004306_YOURUSERNAME/your-file-name  # replace name and your-file-name
   ```
4. Download the file you just uploaded to Allas from your local computer. You can do that in two ways: 
   1. With a-commands:
   ```bash
   a-get 2004306_YOURUSERNAME/your-file-name     # replace name and your-file-name
   ```
   2. With r-tools
   ```bash
   rclone copy allas:2004306_YOURUSERNAME/your-file-name ./ # replace name and your-file-name
   ```
5. Open/edit (+rename) the file so that you can distinguish it from the original
6. Upload the file to Allas:
   1. With a-commands:
   ```bash
   a-put --nc -b 2004306_YOURUSERNAME your-new-file-name   # replace name and your-new-file-name
   ```
   💭 Use `a-put -h` to figure out the command parameters above.

   2. With r-tools
   ```bash
   rclone copy your-new-file-name allas:2004306_YOURUSERNAME/
   ```
7. Check that the file in Puhti indeed has a counterpart in Allas:
```bash
a-check --nc -b 2004306_YOURUSERNAME your-new-file-name   # replace name and your-new-file-name
```
8. Locate the files you just uploaded in Pouta web-interface.

💬 With larger files it is feasible to omit parameter `--nc` and let the files be compressed.

### Extra: publish a file to the internet
💬 The a-tools include a basic tool for publishing files to the internet. You'll notice that the course slides use that method 🤓

‼️ NOTE: Using this command makes your entire bucket to be public! Do not use it if you don't want that to happen..

1. Select a file that has an appropriate content and publish it with command:
```bash
a-publish -b 2004306_YOURUSERNAME your-file-name   # replace name and your-file-name
```
2. The command outputs an URL. Copy it in your browser or send it to your friends 😎 

### Clean up
1. Delete the local file from Puhti so save (so much) space
```bash
rm your-file-name             # replace your-file-name
```
2. When you need your data you can download it from Allas

💭 If you don't find your file but remember the name, try `a-find`. Use `a-find -h` for help.