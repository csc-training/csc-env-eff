---
topic: allas
title: Tutorial - File transfer with Allas (essential)
---

# Allas basic usage

## Accessing Allas via web-interface

1. Open a view to the Allas service in your browser using the cPouta WWW-interface: [https://pouta.csc.fi](https://pouta.csc.fi)
2. Login with your CSC user account.
3. From the upper left corner, you find a project selection pop-up menu. If you have several projects available, select one that you use in this exercise.
4. From the menu on the left side of the interface, select: **Object Store -> Containers**

   💡 A "container" in cPouta WWW-interface is called a "bucket" in S3 protocol. 

{:start="5"}
5. Create new _bucket_ by pressing button: **➕Container**
   - Keep the bucket _Not public_ and name it as *xxxxxxx_yourcscusername*, in which *xxxxxxx* is the number in your project id (project_xxxxxxx) and *yourcscusername* is your CSC username.
6. Find the newly-created bucket and open it.
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

3. Switch to the scratch directory of your project:

```bash
cd /scratch/project_xxxxxxx    # replace xxxxxxx with your project number
```

4. Create your own sub-directory:

```bash
mkdir yourcscusername      # replace yourcscusername
cd yourcscusername
```

### Connecting to allas

1. Open connection to Allas with these commands:

```bash
module load allas
allas-conf 
```

💡 It might take a while with `module load allas`

{:start="2"}
2. If you have several Allas projects available, select the same one where you just created a bucket using cPouta.

3. Study what you have in Allas with [a-commands](https://docs.csc.fi/data/Allas/using_allas/a_commands/) and with [r-clone](https://docs.csc.fi/data/Allas/using_allas/rclone/):

- With a-commands:

```bash
a-list
a-list xxxxxxx_yourcscusername                 # replace xxxxxxx_yourcscusername so that it corresponds to your new bucket
a-info xxxxxxx_yourcscusername/your-file-name  # replace xxxxxxx_yourcscusername and your-file-name
```
    
- With r-clone:
      
```bash
rclone lsd allas:
rclone ls allas:xxxxxxx_yourcscusername                  # replace xxxxxxx_yourcscusername so that it corresponds to your new bucket
rclone lsl allas:xxxxxxx_yourcscusername                 # replace xxxxxxx_yourcscusername
rclone lsf allas:xxxxxxx_yourcscusername                 # replace xxxxxxx_yourcscusername
rclone cat allas:xxxxxxx_yourcscusername/your-file-name  # replace xxxxxxx_yourcscusername and your-file-name
```
   
4. Download to Puhti the file that you just uploaded to Allas from your local computer. You can do that in two ways:

- With a-commands:
      
```bash
a-get xxxxxxx_yourcscusername/your-file-name     # replace xxxxxxx_yourcscusername and your-file-name
```
      
- With r-clone:
      
```bash
rclone copy allas:xxxxxxx_yourcscusername/your-file-name ./    # replace xxxxxxx_yourcscusername and your-file-name
```
      
5. Open/edit (+rename) the file so that you can distinguish it from the original

6. Upload the new file to Allas:

- With a-commands:

```bash
a-put -b xxxxxxx_yourcscusername your-new-file-name   # replace xxxxxxx_yourcscusername and your-new-file-name
```

💭 Use `a-put -h` to figure out the command parameter above and to find more options. 
💬 With larger files it is feasible to include parameter `-c` to compress the files.

- With r-clone:

```bash
rclone copy your-new-file-name allas:xxxxxxx_yourcscusername/   # replace your-new-file-name and xxxxxxx_yourcscusername
```

7. Check that the file in Puhti indeed has a counterpart in Allas:

```bash
a-check -b xxxxxxx_yourcscusername your-new-file-name   # replace xxxxxxx_yourcscusername and your-new-file-name
```

8. Locate the files you just uploaded to Allas in the Pouta web-interface. Look for the bucket name.

### Clean up

1. Delete the local file from Puhti:

```bash
rm your-file-name             # replace your-file-name
```

2. When you need your data you can download it from Allas

💭 If you don't find your file but remember the name, try `a-find`. Use `a-find -h` for help.

## Extra: publish a file to the internet

💬 The a-commands include basic tools for publishing files to the internet. You might notice that the course slides use one of those 🤓

‼️ NOTE: Using these commands makes your **entire bucket** public! Do not engage if you don't want that to happen. All files that you `a-put` in the bucket later, will also be accessible from internet, since the _bucket_ is accessible.

### Option 1: `a-publish`

1. Select a file that has an appropriate content and publish it with command:

```bash
a-publish -b xxxxxxx_yourcscusername your-file-name   # replace xxxxxxx_yourcscusername and your-new-file-name
```

2. The command outputs an URL. Copy it in your browser or send it to your friends 😎 

### Option 2: `a-flip`

💬 `a-flip` is meant for files that need to be published only temporarily for example for one time share. 

1. Select a file that has an appropriate content and publish it with command:

```bash
a-flip your-file-name         # replace your-file-name
```

2. The command outputs an URL. Copy it in your browser or send it to your friends 😎 
