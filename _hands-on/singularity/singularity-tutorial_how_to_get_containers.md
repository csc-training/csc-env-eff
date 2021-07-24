---
topic: singularity
title: Advanced tutorial - How to get containers
---

# How to get containers
💬 Building containers from scratch requires root access, so it can not be done on Puhti. Instead, you will have to import a ready image file. There are various option to do this.

### 1. Run or pull an existing Singularity container from a repository
- It is possible to run containers directly from repository:
```bash
singularity run shub://vsoch/hello-world:latest
```
- This can, however, lead to a batch job failing if there are network problems.
- Usually it is preferable to pull the container first and use the image file.
```bash
singularity pull shub://vsoch/hello-world:latest
singularity run hello-world_latest.sif
```

### 2. Convert an existing Docker container to Singularity

💬 Docker images are downloaded as layers. These layers are stored in the cache directory. Default location for this is `$HOME/.singularity/cache`. Since the home directory has limited capacity, and some images can be large, it's best to set `$SINGULARITY_CACHE` to point to some other location with more space.

➖ If you're running on a node with no local storage, you can use e.g. /scratch.
```bash
export SINGULARITY_TMPDIR=/scratch/project_XXXX/YOURUSERNAME      # Replace XXXX and YOURUSERNAME
export SINGULARITY_CACHEDIR=/scratch/project_XXXX/YOURUSERNAME    # Replace XXXX and YOURUSERNAME
```

➖ If you're running with `sinteractive`, or as batch job on an IO node, you can use the fast local storage:
```bash
export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH
```

- You can avoid some unnecessary warnings by unsetting a variable:
```bash
unset XDG_RUNTIME_DIR
```
- You can now run `singularity build`:
```bash
singularity build alpine.sif docker://library/alpine:latest
```
- You can find more detailed instructions for converting Docker images in Docs CSC: 
[Running existing containers](https://docs.csc.fi/computing/containers/run-existing/)

### 3. Build the image on another system and transfer the image file to Puhti
‼️ To do this you will need an access to system where you have root access and that has Singularity installed.

- Singularity version does not need to be exactly same, but it should be same major version e.g. (3.x as opposed to 2.x).
- You can check the current version on Puhti with:
```bash
singularity --version
```
- After creating an image file, you can transfer it to Puhti to use.

## More information

This tutorial is meant as a brief introduction to get you started.

When searching the internet for instruction, pay attention that the instructions are
for the same version of Singularity that you are using. There has been some command 
syntax changes etc. between the versions, so older instructions may not work with copy-paste.

For authoritative instructions see [Singularity documentation](https://sylabs.io/docs/).
