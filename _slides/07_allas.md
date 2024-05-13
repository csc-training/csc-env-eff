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
All materials (c) 2020-2024 by CSC – IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# The Allas object storage: what is it?

- Allas is a CEPH-based object storage service for all CSC computing and cloud services
- Possible to upload data from personal laptops or organizational storage systems into Allas
- Meant for data storage during project lifetime
   - All project members have equal access to the data in Allas
   - Default quota is 10 TB per project
- Clients available on Puhti and Mahti
   - See Docs CSC for instructions on [accessing Allas from LUMI](https://docs.csc.fi/data/Allas/allas_lumi/)

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

# Allas objects

- Data is stored as **objects** within a bucket
    - Objects can contain any type of data (generally, object == file)
    - Objects have metadata that can be enriched
- In Allas, you can have 500 000 objects per bucket
- There is only one level of hierarchy of buckets (no buckets within buckets)
    - There is no hierarchical directory structure, although it sometimes looks like that

# Allas supports two protocols

- S3 (used by `s3cmd`, `rclone`, `a-tools`)
- Swift (used by `swift`, `rclone`, `a-tools`, `cyberduck`)  
- Authentication and file handling is different for the protocols
- **Avoid cross-using Swift and S3-based objects!**

# Allas clients

- **Puhti, Mahti, Linux servers, Mac:**
    - `rclone`, `swift`, `s3cmd`, `a-tools`
- **Laptops (Windows, Mac):**
    - [Cyberduck](https://cyberduck.io/), [FileZilla (pro)](https://filezilla-project.org/), [Puhti web interface](https://puhti.csc.fi), [Mahti web interface](https://mahti.csc.fi)
- **Virtual machines, small servers:**
    - In addition to the tools above, you can use FUSE-based virtual mounts

# Allas -- first steps

- Use [My CSC](https://my.csc.fi) to apply for Allas access for your project -- Allas is not automatically available
- In Puhti/Mahti, setup connection to Allas using the commands:
  ```bash
  module load allas
  allas-conf
  ```
- [Study the manual and start using Allas with `rclone` or `a-tools`](https://docs.csc.fi/data/Allas/)
- [This course](https://csc-training.github.io/csc-env-eff/part-1/allas/) includes also hands-on tutorials and a tutorial video about Allas

# Allas -- `rclone`

- Straightforward power-user tool with a wide range of features
- Fast and efficient
- Available for Linux, Mac and Windows
- **Overwrites and removes data without asking!**
   - Use with care: [`rclone` instructions at Docs CSC](https://docs.csc.fi/data/Allas/using_allas/rclone/)

# Allas -- `a-tools`

- `a-tools` provide an easy and safe way to use Allas for occasional Allas users
- Default bucket names are based on directories on Puhti/Mahti
- Unlike `rclone`, `a-tools` does not overwrite or remove data without asking!
- Developed for the CSC supercomputers, but you can install the tools in other Linux and Mac machines as well
- Automatic packing (compression can be enabled as well if needed)
- [a-commands instructions at Docs CSC](https://docs.csc.fi/data/Allas/using_allas/a_commands/)
  

# Issues with Allas

- 8-hour connection limit with `swift`
- No way to check quota
- Moving data inside Allas is not possible (`swift`)
- No way to freeze data
   - Use two projects if you need to prevent others from editing your data
- Different interfaces may work in different ways

# Questions that users should consider

- Should I store each file as a separate object, or should I collect them into bigger chunks?
    - In general: consider how you use the data
- Should I use compression?
- Who can use the data: projects and access rights?
- What will happen to my data later on?
- How to keep track of all the data I have in Allas?

# Fairdata services

- [https://www.fairdata.fi](https://www.fairdata.fi) -- Services to manage scientific data according to FAIR principles
- Suitable for all static digital research material and related metadata
- Free of charge for users in Finnish higher education institutions and research institutes
- **[IDA](https://ida.fairdata.fi):** storage for research data
- **[Qvain](https://qvain.fairdata.fi/):** Describe your dataset and get a persistent indentifier for it
- **[Etsin](https://etsin.fairdata.fi/):** Discover datasets based on metadata

# Sensitive data services

- [CSC Sensitive Data Services](https://docs.csc.fi/data/sensitive-data/) for processing sensitive data
- [**SD Desktop**](https://sd-desktop.csc.fi) is a secure virtual desktop
   - Controlled access
   - Data importing _only_ through the [**SD Connect**](https://sd-connect.csc.fi) service
   - Isolation from the Internet
   - No direct data export
- Allas could be used for sensitive data, but _only_ if the data is properly encrypted
   - The [**SD Connect**](https://sd-connect.csc.fi) procedure does the encryption
