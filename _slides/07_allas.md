---
theme: csc-eurocc-2019
lang: en
---

# Allas object storage service {.title}

This topic is about using Allas and storing data.

<div class="column">
![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)
</div>
<div class="column">
<small>
All materials (c) 2020-2026 by CSC – IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# The Allas object storage: what is it?

- Allas is a Ceph-based object storage service for all CSC computing and cloud services
- Possible to upload data from personal laptops or organizational storage systems into Allas
- Meant for data storage during project lifetime
   - All project members have equal access to the data in Allas
   - Default quota is 10 TB per project
- Clients available on Roihu
   - See Docs CSC for instructions
       - [Using Allas and Lumi-O object storage services in Roihu](https://docs.csc.fi/computing/allas-in-roihu/)
       - [Tutorial for using Allas in the Roihu supercomputer](https://docs.csc.fi/data/Allas/allas-roihu/)


# The Allas object storage: what it is NOT

- **Allas is not a file system** (even though many tools try to fool you to think so)
    - It is just a place for static data objects
- **Allas is not a data management environment**
    - Tools for search, metadata, version control and access management are minimal
- **Allas is not a proper backup service**
    - Project members can delete all the data with just one command

# Storing files in Allas

- An object is stored on multiple servers
    - A disk or server failure does not cause data loss
- There is no backup, i.e. if a file is accidentally deleted, it cannot be recovered
- Data cannot be modified in the object storage
    - For computation, the data has to be typically copied to a file system on some computer
- Some data management features are built on top of Allas
- Data can be shared publicly to the Internet, which is otherwise not easily possible at CSC

# Allas buckets

- Storage space in Allas is provided per **CSC project**
- The project space can have multiple **buckets** (up to 1000)
    - Some sources refer to *buckets* as *containers*
        - Must not be confused with Docker/Apptainer containers!
- The name of the bucket must be unique within Allas
- Avoid using special characters, including _ and upper case letters in bucket names
    - Bad bucket name: `My_New_%-data`
    - Good bucket name: `my-new-percent-data`

# Allas objects

- Data is stored as **objects** within a bucket
    - Objects can contain any type of data (generally, object == file)
    - Objects have metadata that can be enriched
- In Allas, you can have 500 000 objects per bucket
- There is only one level of hierarchy of buckets (no buckets within buckets)
    - There is no hierarchical directory structure, although it sometimes looks like that
    - `123-bucket/dir1/data2.csv` means:
         - bucket name: `123-bucket`
         - object name: `dir1/data2.csv`

# Allas supports two protocols

- S3 (used by `s3cmd`, `aws s3`, `rclone`, `a-tools`, `s5cmd`, `cyberduck`)
- Swift (used by `swift`, `rclone`, `a-tools`, `cyberduck`, `https://allas.csc.fi`)  
- Authentication and file handling is different for the protocols
- **Avoid cross-using Swift and S3-based objects!**
- **In Roihu the default protocol is now S3 while in Puhti and Mahti it was swift**

# Allas clients

- **Roihu, Linux servers, Mac:**
    - `rclone`, `s3cmd`, `a-tools`, `aws`, `s5cmd`
- **Laptops (Windows, Mac):**
    - [Cyberduck](https://cyberduck.io/), [FileZilla (pro)](https://filezilla-project.org/), [Roihu web interface](https://www.roihu.csc.fi), [Allas UI](https://allas.csc.fi)
- **Virtual machines, small servers:**
    - In addition to the tools above, you can use FUSE-based virtual mounts

# Allas -- first steps

- Use [MyCSC](https://my.csc.fi) to apply for Allas access for your project. Allas is not automatically available
- In Roihu, setup connection to Allas using the commands:

  ```bash
  module load allas
  allas-conf
  ```

- In Roihu, `allas-conf` sets up a permanent S3 connection -- rerun only if you want to switch connections.
- [Study the manual and start using Allas with `rclone` or `a-tools`](https://docs.csc.fi/data/Allas/)
- [This course](https://csc-training.github.io/csc-env-eff/part-1/allas/) includes also hands-on tutorials about Allas

# Allas -- `rclone`

- Straightforward power-user tool with a wide range of features
- Fast and efficient
- Available for Linux, Mac and Windows
- **Overwrites and removes data without asking!**
- Problems occur in cases where your bucket contains tens of thousands of long object names
   - Use with care: [`rclone` instructions at Docs CSC](https://docs.csc.fi/data/Allas/using_allas/rclone/)

# Allas -- `a-tools`

- `a-tools` provide an easy and safe way to use Allas for occasional users
- Default bucket names are based on directories on Roihu
- Unlike `rclone`, `a-tools` does not overwrite or remove data without asking!
- Developed for the CSC supercomputers, but you can install the tools in other Linux and Mac machines as well
- Automatic packing (compression can be enabled as well if needed)
- In Roihu a-tools use by default S3 protocol. Add option `--swift` to a-commands if you need to use swift protocol in Roihu.
- [a-commands instructions at Docs CSC](https://docs.csc.fi/data/Allas/using_allas/a_commands/)

# Issues with Allas

- 8-hour connection limit with `swift`
- Quota can be checked only in MyCSC
- Moving data inside Allas is not possible (`swift`)
- No way to freeze data
   - Use two projects if you need to prevent others from editing your data
- Different interfaces may work in different ways
- Cross using protocols cause problems for files larger than 5 GB, see the [tips for cross usage](https://docs.csc.fi/support/faq/roihu/#12-i-uploaded-data-from-puhtimahti-to-allas-now-im-downloading-it-to-roihu-and-get-an-error-saying-corrupted-on-transfer-md5-hashes-differ)

# Questions that users should consider

- Should I store each file as a separate object, or should I collect them into bigger chunks?
    - In general: consider how you use the data
- Should I use compression?
- Who can use the data: projects and access rights?
- What will happen to my data later on?
- How to keep track of all the data I have in Allas?

# LUMI-O

- LUMI-O is object storage service for LUMI supercomputer
- Default quota: 150 TiB
- LUMI-O uses only S3 protocol and there is no https://allas.csc.fi -like web interface
- You need to apply for a LUMI-project to use LUMI-O
- LUMI projects have always a maximum duration, three years in this case, after which the project is closed and you must move your data elsewhere
- Allas is currently very full, so if you need to store large datasets (>30 TiB) we ask you to use LUMI-O instead

# SD Connect and sensitive data services

- [CSC Sensitive Data Services](https://docs.csc.fi/data/sensitive-data/) for processing sensitive data
- [**SD Desktop**](https://sd-desktop.csc.fi) is a secure virtual desktop
   - Controlled access
   - Data importing **only** through the [**SD Connect**](https://sd-connect.csc.fi) service
   - Isolation from the Internet
   - No direct data export
- Allas can be used for sensitive data, but **only** if the data is properly encrypted!
   - The [**SD Connect**](https://sd-connect.csc.fi) adds automatic encryption and decryption to Allas
   - Crypt4gh in use. Suffix: `.c4gh`

# Fairdata services

- [https://www.fairdata.fi](https://www.fairdata.fi) -- Services to manage scientific data according to FAIR principles
- Suitable for all static digital research material and related metadata
- Free of charge for users in Finnish higher education institutions and research institutes
- **[IDA](https://ida.fairdata.fi):** storage for research data
- **[Qvain](https://qvain.fairdata.fi/):** Describe your dataset and get a persistent identifier for it
- **[Etsin](https://etsin.fairdata.fi/):** Discover datasets based on metadata
