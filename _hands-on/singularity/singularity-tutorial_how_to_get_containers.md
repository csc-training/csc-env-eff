---
topic: singularity
title: Advanced tutorial - How to get containers
---

# How to get containers
💬 Building containers from scratch requires root access, so it can not be done on Puhti. 
- Instead, you will have to import a ready image file. There are various option to do this.

### 1. Run or pull an existing Singularity container from a repository
1. It is possible to run containers directly from repository:
    ```bash
    apptainer run shub://vsoch/hello-world:latest
    ```
    - This can, however, lead to a batch job failing if there are network problems.
2. Usually it is preferable to pull the container first and use the image file:
    ```bash
    apptainer pull shub://vsoch/hello-world:latest
    apptainer run hello-world_latest.sif
    ```

### 2. Convert an existing Docker container to apptainer

💬 Docker images are downloaded as layers. These layers are stored in the cache directory. 
- Default location for this is `$HOME/.singularity/cache`. 
- Since the home directory has limited capacity, and some images can be large, it's best to set `$SINGULARITY_CACHE` to point to some other location with more space.

**Option 1.**  
1. If you're running on a node with no local storage, you can use e.g. /scratch:
```bash
export APPTAINER_TMPDIR=/scratch/project_xxxx/yourcscusername      # Replace xxxx and yourcscusername
export APPTAINER_CACHEDIR=/scratch/project_xxxx/yourcscusername    # Replace xxxx and yourcscusername
```

**Option 2.**  
1. If you're running with `sinteractive`, or as batch job on an IO node, you can use the fast local storage:
```bash
export APPTAINER_TMPDIR=$LOCAL_SCRATCH
export APPTAINER_CACHEDIR=$LOCAL_SCRATCH
```

{:start="2"}
2. Avoid some unnecessary warnings by unsetting a variable:
    ```bash
    unset XDG_RUNTIME_DIR
    ```
3. You can now run `singularity build`:
    ```bash
    apptainer build alpine.sif docker://library/alpine:latest
    ```

💡 You can find more detailed instructions for converting Docker images in CSC Docs: [Running existing containers](https://docs.csc.fi/computing/containers/run-existing/)

### 3. Build the image on another system and transfer the image file to Puhti
‼️ To do this you will need an access to system where you have root access and that has Apptainer installed.

1. You can check the current version on Puhti with:
    ```bash
    apptainer --version
    ```
2. After creating an image file, you can transfer it to Puhti to use.

## More information

💬 This tutorial is meant as a brief introduction to get you started.

☝🏻 When searching the internet for instruction, note that the instructions are for the same version of Apptainer that you are using. There has been some command syntax changes, etc., between the versions, so older instructions may not work with copy-paste. Also note that Apptainer used to be called Singularity.

💡 For more details, see [Apptainer documentation](https://apptainer.org/docs/user/latest/).
