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
All materials (c) 2020-2023 by CSC – IT Center for Science Ltd.
This work is licensed under a **Creative Commons Attribution-ShareAlike** 4.0
Unported License, [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
</small>
</div>

# How to get access to Allas service

- Use [https://my.csc.fi](https://my.csc.fi) to
    1. Create a CSC account (log in with Haka/Virtu)
        - If Haka/Virtu is not an option, contact <servicedesk@csc.fi>
    2. Set up a project at CSC (Principal Investigator)
    3. Apply for Puhti and Allas services, quota and billing units for your project
    4. Add other registered users to your project
    5. Members have to register and accept the terms of use in [My CSC](https://my.csc.fi)
- All project members have equal access to the data in Allas and Puhti (`/scratch` and `/projappl` disks)

# The Allas object storage: what is it?

- Allas is a storage service for all CSC computing and cloud services
- CEPH-based object storage
- Possible to upload data from personal laptops or organizational storage systems into Allas
- Meant for data storage during project lifetime
- Default quota is 10 TB per project
- Clients available on Puhti and Mahti

# Connections to Allas

<div class="column">
- Data can be moved to and from Allas directly without using Puhti or Mahti
    - Usage through S3 and Swift APIs are supported
- Data can be shared publicly to the Internet, which is otherwise not easily possible at CSC
</div>
<div class="column">
![](img/allas.png "Allas"){width=90%}
</div>

# The Allas object storage: what it is NOT

- **Allas is not a file system** (even though many tools try to fool you to think so)
    - It is just a place for static data objects
- **Allas is not a data management environment**
    - Tools for search, metadata, version control and access management are minimal
- **Allas is not a back up service**
    - Project members can delete all the data with just one command

# Storing files in Allas

- An object is stored on multiple servers
    - A disk or server failure does not cause data loss
- There is no backup, i.e. if a file is accidentally deleted, it cannot be recovered
- Data cannot be modified in the object storage
    - For computation, the data has to be typically copied to a file system on some computer
- Some data management features are built on top of Allas

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
- Authentication is different
    - S3: permanent key-based authentication -- nice, easy and unsecure
    - Swift: authentication based on temporary tokens -- more secure, requires authentication every 8 hours
- File handling is different
    - Metadata is handled in different ways
    - Files larger than 5 GB are managed in different ways
    - **Avoid cross-using Swift and S3-based objects!**

# Allas Clients

- **Puhti, Mahti, Linux servers, Mac:**
    - `rclone`, `swift`, `s3cmd`, `a-tools`
- **Laptops (Windows, Mac):**
    - [Cyberduck](https://cyberduck.io/), [FileZilla (pro)](https://filezilla-project.org/), [Pouta web interface](https://docs.csc.fi/cloud/pouta/launch-vm-from-web-gui/)
- **Virtual machines, small servers:**
    - In addition to the tools above, you can use FUSE-based virtual mounts

# Allas -- first steps

- Use [My CSC](https://my.csc.fi) to apply for Allas access for your project -- Allas is not automatically available
- In Puhti/Mahti, setup connection to Allas with the commands:

```bash
module load allas
allas-conf
```

- Study the manual and [start using Allas with `rclone` or `a-tools`](https://docs.csc.fi/data/Allas/)
- This [course](https://csc-training.github.io/csc-env-eff/#7-allas-and-where-to-keep-your-data) includes also hands-on tutorials and a tutorial video about Allas

# Allas -- `rclone`

- Straightforward power-user tool with a wide range of features
- Fast and efficient
- Available for Linux, Mac and Windows
- Overwrites and removes data without asking!
- The default configuration at CSC uses `swift`-protocol, but S3 can also be used
- Use with care: [`rclone` instructions at Docs CSC](https://docs.csc.fi/data/Allas/using_allas/rclone/)

# Allas -- `a-tools`

- `rclone`-based scripts for using Allas in Puhti and Mahti
- `a-tools` provide an easy and safe way to use Allas for occasional Allas users
- Default bucket names are based on directories on Puhti/Mahti
- Unlike `rclone`, `a-tools` does not overwrite or remove data without asking!
- Developed for the CSC supercomputer, but you can install the tools in other Linux and Mac machines as well
- Automatic packing (compression can be enabled as well if needed)
- [a-commands instructions at Docs CSC](https://docs.csc.fi/data/Allas/using_allas/a_commands/)

# `a-put`/`a-get`: pros and cons

<div class="column">
➕ Saving data as a tar package preserves time stamps, access settings, and internal links of the directory  
➕ Optional `zstdmt` compression reduces size  
➕ The default bucket name and the metadata reflect the directory structure on Puhti/Mahti  
➕ Checks to prevent overwriting data accidentally
</div>
<div class="column">
➖ Usage of objects created by `a-put` can be complicated when other object storage tools are used  
➖ Usage from Windows is problematic  
➖ Each object has an additional `_ameta` object
</div>

# Issues with Allas

- 8-hour connection limit with `swift`
- No way to check quota
- Moving data inside Allas is not possible (`swift`)
- No way to freeze data
    - Use two projects if you need to prevent others from editing your data
- Different interfaces may work in different ways

# Questions that users should consider

- Should I store each file as a separate object or should I collect them into bigger chunks?
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
- **[Qvain](https://qvain.fairdata.fi/):** Describe you dataset and get a persistent indentifier for it
- **[Etsin](https://etsin.fairdata.fi/):** Discover datasets based on metadata

# Sensitive data services

- [CSC Sensitive Data Services](https://docs.csc.fi/data/sensitive-data/) for processing sensitive data
- **SD Desktop** [https://sd-desktop.csc.fi](https://sd-desktop.csc.fi) is a secure virtual desktop
     - Controlled access
     - Data importing _only_ through the [**SD Connect**](https://sd-connect.csc.fi) service
     - Isolation from the Internet
     - No direct data export
- Allas could be used for sensitive data, but _only_ if the data is properly encrypted
    - The [**SD Connect**](https://sd-connect.csc.fi) procedure does the encryption
