---
theme: csc-eurocc-2019
lang: en
---

# Working Efficiently with Data {.title}
         
<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All materials (c) 2020-2023 by CSC – IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>


# Outline

- Using Allas in batch scripts 
- Moving data across Allas, IDA and LUMI-O
- Cleaning and backing up of data 
- File I/O in HPC systems
- Working with remote mounts
- Transferring data in sensitive data computing


# Using Allas in Batch Scripts

- SWIFT (all projects; 8-hour) *vs.* S3 protocol (fixed for a project; persistent)
- *allas-conf* needs setting up CSC password interactively
   - Jobs may start late and actual job may take longer than 8 hrs
- Use *allas-conf -k*
   - stores password in variable $OS_PASSWORD to generate a new token automatically
   - a-tools regenerate a token from $OS_PASSWORD automatically
   - rclone requires explicit setting of env variable in batch jobs:
       - *source /appl/opt/allas-cli-utils/allas_conf -f –k  $OS_PROJECT_NAME *


# Configuring Allas for S3 Protocol

- Opening Allas connection in s3mode
  - *source allas_conf --mode  s3cmd *
- Connection is persistent
- Usage:
   - s3cmd with endpoint *s3:*
   - rclone with endpoint *s3allas:*
   - a-put/a-get with -S flag


# How to Use LUMI-O from Puhti/Mahti

- LUMI-O is very similar to Allas but it uses only S3 protocol
- In Puhti and Mahti, connection to Lumi-O can be opened with command:
  - allas-conf  `--lumi`

- Usage:
  - Using LUMI-O with rclone (endpoint is lumi-o: )
    - e.g., rclone lsd lumi-o:
  - One can use a-tools with option `--lumi`
    - e.g., a-list  `--lumi`

- Using [Allas and LUMI-O from LUMI](https://docs.csc.fi/data/Allas/allas_lumi/)


# Moving Data Between LUMI-O and Allas 

- Activate connections to both Lumi-O and Allas  
    - *allas-conf --mode s3cmd* 
    - *allas-conf --lumi*

- Use rclone with *s3allas:* as endpoint for Allas and *lumi-o:* for LUMI-O
    - e.g.,*rclone copy -P lumi-0:lumi-bucket/object s3allas:allas-bucket/ * 


# Moving Data Between IDA and Allas 

- Needs transfer of data *via* supercomputer (e.g., Puhti)
- First, [configure IDA in CSC supercomputers](https://docs.csc.fi/data/ida/using_ida/) 
    - commands: module load ida and ida_configure 
    - e.g., ida upload /test123/data1 test_data 
    - e.g., ida download /project1 project1_data.zip 
- Move data between Allas and Puhti


# Cleaning and Backing up of Data (1/3)

- Disk cleaning
  - Cleaning in force for scratch areas of projects
  - Files older than 180 days will be removed
- Best practice tips
  - Avoid cross-using SWIFT and S3-based protocols!
  - Don't save everything automatically
  - You can keep important data in Allas
  - Use *[lue](https://docs.csc.fi/support/tutorials/lue/)* tool for managing disk space


# Cleaning and Backing up of Data (2/3)

- Allas-backup command uses *restic* back-up tool
- Backing up differs from normal storing:
  - Incremental (effective) and version control (no overriding)
  - Based on hashes and requires more computing
  - Effective way to store different versions of a dataset


# Cleaning and Backing up of Data (3/3) 

- Please note that Allas is intended for storing active data 
- Project lifetime is usually 1-5 years
- Commands for backing up data:
     - allas-backup –help
     - allas-backup [add] file-or-directory 
     - allas-backup list 
     - allas-backup restore snapshot-id


# Understanding File I/O on HPC System

<div class="column">

<style>
p.ex1 {
  font-size: 40px;
}
</style>

- Metadata servers (MDS) with metadata targets (MDT) that store the file system metadata.
- Object storage servers (OSS) with object data targets that store the actual file system contents.
- Accessing a file involves:  
    - <p class="ex1"> Sending metadata request </p>
    - <p class="ex1"> Responding e with metadata </p>
    - <p class="ex1"> Requesting data </p>
    - <p class="ex1"> Responding with actual data </p>
</div>

<div class="column">
<p align="left"> ![](img/fileio1.png){width=70%} </p>
</div>


# Managing File I/O in HPC System (1/3)

- Shared storage (Lustre): 
   - shared across all nodes in the cluster (e.g., /scratch)
   - slow when accessing huge number of files!
- Temporary local storage:
   - available to running jobs on some compute nodes
   - varies depending on the supercomputer (Puhti vs. Mahti vs. LUMI)
   - automatically purged after the job finishes
   - accessible to job using $TMPDIR/$LOCAL_SCRATCH 
    

# Managing File I/O in HPC System (2/3)

- Avoid reading lots of small files from shared disks
   - Shared file system (Lustre) separates actual data and metadata (file info, including on which file server the file is stored
   - Optimized for parallel I/O of large files
- Use efficient file formats when possible
   - TensorFlow’s solution in ML/AI: TFRecords - a simple record-oriented binary format
   - Use high-level I/O libraries and portable file formats like HDF5 or NetCDF. These enable fast I/O through a single file format and parallel operations. 


# Managing File I/O in HPC System (3/3)

- Use the fast local disk (NVMe) to handle file I/O with lots of small files 
   - Requires staging and unstaging of data
   - e.g., tar xf /scratch/<project>/big_dataset.tar.gz -C $LOCAL_SCRATCH

- Process data in memory when possible instead of writing to and reading from the disk
   - Files are saved in memory, allowing for better performance than using disk.
   - e.g., Use local /dev/shm directory (on Mahti) for large-scale I/O
- Avoid using databases on /scratch. Consider hosting DBs on cloud resources (e.g., [Pukki-DBaaS](https://docs.csc.fi/cloud/dbaas/))

# Working with Remote Disk Mounts

- Using *sshfs* command in Linux/MacOS
   - *mkdir csc_home* 
   - *sshfs kayttaja@puhti.csc.fi:/users/kayttaja csc_home*

- To unmount the file system, give the command: 
   - *fusermount -u mountpoint*


# Transferring Data for Sensitive Data Computing

- CSC sensitive data services: SD Connect and SD Desktop, use service specific encryption.
- If you want to make your data available for SD Desktop you need to encrypt the data with the CSC public key before data is uploaded to Allas.
- SD Desktop is able to read this encrypted data from Allas
- Use a-put with option –sdx to or command a-encrypt to make your Allas data compatible with SD Desktop.
- New version of SD Connect will change the situation next fall, but the new server will be compatible with data uploaded for the current SD Connect.


# Questions That Users Should Consider

- Should I store each file as a separate object or should I collect them into bigger chunks? 
- In general: consider how you use the data
- Should I use compression?
- Who can use the data: projects and access rights?
- What will happen to my data later on?
- How to keep track of all the data I have in Allas?

