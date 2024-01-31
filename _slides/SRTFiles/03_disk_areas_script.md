---
theme: csc-2019
lang: en
---

# Disk areas in CSC HPC environment {.title}
In this section, you will learn how to manage different disk areas in HPC environment at CSC

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All material (C) 2020-2021 by CSC -IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

:::info (speech)
In this section, you will learn how to manage different disk areas in HPC environment at CSC.
:::

# Overview of disk areas

- Main disk areas and their specific uses in Puhti/Mahti
- Moving data between supercomputers
- Understanding quotas (both usable space and number of files) for different disk areas
- Additional fast disk areas

:::info (speech)
CSC supercomputers have different disk areas, that have their own specific purposes.
This lecture gives insight on where to keep your files, and how to move the data between Mahti and Puhti. 
The disk areas have different quotas, which means that users cannot just create files anywhere and forget them. 
The additional fast disk areas are for applications, that require lots of file input and output. 
:::

# Disk and storage overview  

![](./img/disk-systems.svg){width=90%}

:::info (speech)
Here is a visual layout of two supercomputers, and the file storage.
The box on the left represents Puhti, and the other on the right Mahti. 
Down below is a cylinder, that represents Allas.
There are bidirectional arrows between these three objects illustrating, that data can be transferred from each service to another.
Both supercomputers have their own Lustre filesystem, that contain disk areas called home, projappl and scratch.
You can move files inside a supercomputer using commands mv and cp.
For file transfers between Puhti and Mahti, you can use rsync or scp.
And for using Allas object storage, there is a separate lecture and tutorial.
It is important to realize, that if you have your files for example in Puhti scratch area, they will not show anywhere in Mahti – unless you manually copy them there. 
:::

# Main disk areas in Puhti/Mahti

- Home directory (`$HOME`)
    - Other users cannot access you home directory
- ProjAppl directory (`/projappl/project_name`)
    - Shared with project members
    - Possible to limit access (`chmod g-rw`) in subfolders
- Scratch directory (`/scratch/project_name`)
    - Shared with project members
    - Files older than 90 days will be automatically removed
- These directories reside on [Lustre parallel file system](https://docs.csc.fi/computing/lustre/)
- Default quotas and more info on [disk areas section](https://docs.csc.fi/computing/disk/)

:::info (speech)
As pictured in the previous slide: the main disk areas in both Puhti and Mahti, are the user's home directory, scratch and projappl. 
The home directory is personal, but projappl and scratch are for the project's use, and they are shared with your project members. 
In scratch disk area there will be an automatic file removal system. 
To keep your data and results safe, move them for example to Allas during the lifetime of your project.
These disk areas reside in the Lustre parallel file system, which makes them visible in both the login nodes and the compute nodes. 
If you want to know how the Lustre file system works, you can find the link to Lustre documentation in the slides. 
Lustre is good in handling lots of data at once, but not well suited for repeatedly searching and reading small chunks of files.
The documentation in docs.csc.fi covers also the default quotas for the disk areas.
:::

Switch to # [Disk Areas docs](https://docs.csc.fi/computing/disk/)

:::info (speech)
There you can find more information about the default quotas.
For example in home directory you can not have more than 10 GiB of space and you can only have less than hundred thousand files in there.
:::

# Moving data between and to/from supercomputers

- Puhti and Mahti have their own disk systems
- Data can be moved between the supercomputers 
    - [directly with rsync](https://docs.csc.fi/data/moving/rsync/) 
    - via [Allas object storage](https://docs.csc.fi/data/Allas/)
- There are [many ways to transfer data to/from CSC and your local computer](https://docs.csc.fi/data/moving/)

:::info (speech)
Puhti and Mahti do not share any disk space. 
You can copy your files to a different supercomputer using rsync and scp commands.
You can also put your data in Allas, and download it from there to other supercomputers. 
You will learn more about Allas in the later presentations and tutorials.
:::

# Displaying current status of disk areas

- use `csc-workspaces` command to display available projects and quotas 

![](./img/disk_status.png)

:::info (speech)
You can check the status of the disk areas, that you have with command csc-workspaces.
It prints a list of your disk areas with current capacity, and the number of files used. 
Each project have their own projappl and scratch areas, and they all will be printed out for you.
The first line is your own personal project.
In this example the user has 8 GB of files against 11 GB of quota, and 17000 files against the 100000 files that is allowed.
Be aware that you may reach this 100000 file limit, if you install software with many files.
Please pay attention to the disk usage – as well as the number of files – that you are using in your disk areas. 
Note that with this command you can also check the paths to your projappl and scratch areas.
:::

# Disk and storage overview (revisited) 

![](./img/disk-systems.svg){width=90%}

:::info (speech)
Here is the visual layout of two supercomputers and their file storage again.

In addition to the main disk areas the supercomputers have fast local disk areas. 
These mean the temp directories in login nodes and then NVMe directories on some compute nodes in Puhti.
:::

# Additional fast local disk areas 

- `$TMPDIR` on Login nodes
    - Each of the login nodes have 2900 GiB of fast local storage `$TMPDIR`
    - The local storage is meant for temporary storage and is cleaned frequently
- NVMe on part of compute nodes in Puhti
    - Interactive batch job nodes, IO- and gpu-nodes have [local fast storage (NVMe)](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage) as `$LOCAL_SCRATCH`
    - You must copy data in and out during your batch job. NVMe is accessible only during your job allocation.
    - If your job reads or writes a lot of small files, using this can give 10x performance boost

:::info (speech)
Remember that the Lustre filesystem is not good in reading or writing a lot of small files? 
That is what the local fast disk areas are for.
In login nodes it is called temporary directory, and you can access it from the login node with command cd $TMPDIR.
The temp directory is meant for preprocessing of your files. 
For example if you have too many files, and you want to merge them.
Don't do any heavy computing in the login nodes. 
In some Puhti compute nodes, the fast local disk areas have NVMe-based disks, which means SSD-disks. 
You can use them as part of an interactive job, or a batch job. 
The environment variable – used for accessing the NVMe-disks during a job – is $LOCAL_SCRATCH. 
You must copy the data to and from the NVMe space during your batch job, because the fast local disk areas are not part of the Lustre filesystem. 
Otherwise the data and results produced during the batch job, will be not be accessible to you after the job has finished.
You should consider using the NVMe space, if your job reads or writes lots of small files.
Depending on the amount of files, you might get up to 10 times faster performance – if you use the local fast disk area – compared to the Lustre filesystem.
:::

# What are the different disk areas for?

- [Allas](https://docs.csc.fi/data/Allas/) - for data which is not actively used
- [HOME](https://docs.csc.fi/computing/disk/#home-directory) - small, thus only for most important (small) files, personal access only
- [scratch](https://docs.csc.fi/computing/disk/#scratch-directory) - main working area, can be used to share with project members
- [projappl](https://docs.csc.fi/computing/disk/#projappl-directory) - not cleaned up, e.g. for shared binaries 
- [Login node local tmp](https://docs.csc.fi/computing/disk/#login-nodes) - compiling, temporary, fast IO 
- [NVMe](https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage) - fast IO in batch jobs

:::info (speech)
This slide shows a summary of the disk areas, and their specific usecases.
Allas is for storing data that is not used in any computational analysis at that moment.
Home directory is especially meant for storing your personal information, and some scripts that you would like to use later. 
Other users cannot access your home folder.
In projappl users can store and share their scientific programs, binaries and packages with colleagues in the same project. 
The scratch area should be your main working space, and it is also shared with project members. 
The temp directory in login node is used for compiling code, and fast file I/O in lightweight processing.
NVMe nodes are used in heavy computing with fast file I/O in batch jobs, or interactive jobs. 
:::

# Some best practice tips

- Don't put databases on Lustre (projappl, scratch, home) 
    - use other CSC services like [kaivos](https://docs.csc.fi/data/kaivos/overview/) or mongoDB in cPouta
- Don't create a lot of files in one folder
- Don't create overall a lot of files (if you're creating tens of thousands of files, you should probably rethink the workflow)
- Take backups of important files. Data on CSC disks is not backed up even if systems are fault tolerant.
- When working with the large number of smaller files, consider using fast local disks
- [Best practice performance tips for using Lustre](https://docs.csc.fi/computing/lustre/#best-practices)

:::info (speech)
Do not put any databases on the Lustre filesystem.
It is not good to have too many files, and Lustre is inefficient in reading small bits of a single file. 
For databases we recommend, that you use our services like Kaivos and MongoDB in cPouta.
Don't create a lot of files in one folder – or actually: don't create overall a lot of files in Lustre filesystem. 
If that is needed, you have to rethink the workflow. 
Please note, that CSC does not backup your data. 
The disks are fault tolerant, but that does not stop you or your colleaques accidentally deleting everything.
A pro-tip: modify the usage rights to files with command chmod.

If your workflow requres reading or writing lot of files, use the fast local disks.
That will increase the performance for your computation, as well as decrease the load on Lustre filesystem. 
The documentation in docs.csc.fi contains best practice tips for performance when using Lustre.

The tutorials about disk areas continue from here. 
They cover the basic use cases with easy-to-follow examples.
Check the links in the description!
:::
