---
theme: csc-2019
lang: en
---

# Allas object storage service {.title}

This topic is about using Allas and storing data.

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

# How to get access to Allas

Use [https://my.csc.fi](https://my.csc.fi) to 

1. Register to CSC (haka)
2. Set up a project at CSC (Principal Investigator)
3. Apply for Puhti and Allas service, quota and billing units for your project
4. Add other registered users to your project
5. Members have to register and accept the services in [https://my.csc.fi](https://my.csc.fi)

All project members have equal access to the data in Puhti and Allas.

# Allas – object storage: what it is for?

- Allas is a storage service for all computing and cloud services
- CEPH based object storage
- Meant for data during project lifetime
- Default quota 10 TB / Project 
- Possible to upload data from personal laptops or organizational storage systems into Allas
- Clients available in Puhti and Mahti
- Data can also be shared via Internet

# Allas – object storage: what it is for?

<br>

<div class="column">
- Data can be moved to and from Allas directly without using Puhti or Mahti.
- For computation the data has to be typically copied to a file system in some computer
- Data can be shared publicly to Internet, which is otherwise not easily possible at CSC.
</div>
<div class="column">
!["Allas"](img/allas.png "Allas"){width=90%}
</div>

# Allas – object storage: what it is NOT

- **Allas is not a file system** (even though many tools try to fool you to think so). It is just a place for a pile of static data objects.
- **Allas is not a data management environment**. Tools for etc. search, metadata,version control and access management are minimal.
- **Allas is not a back up service**. Project members can delete all the data with just one command.

# Allas - storage 

- An object is stored in multiple servers so a disk or server break does not cause data loss
- There is no backup i.e. if a file is deleted, it cannot be recovered
- Data cannot be modified while it is in the object storage – data is immutable.
- Rich set of data management features are to be built on top of it.
- Usage through S3 and Swift APIs are supported

# Allas – object storage: terminology

<div class="column">
- Storage space in Allas is provided per **CSC project**
- Project space can have multiple *buckets* ( up to 1000)
- There is only one level of hierarchy of buckets (no buckets within buckets)
- Data is stored as **objects** within a bucket
- Objects can contain any type of data (generally: object = file)
</div>
<div class="column">
- In Allas you can have 500 000 objects / bucket
- Name of the bucket must be unique within Allas
- Objects have metadata that can be enriched 
- In reality, there is no hierarcical directory structure, although it sometimes looks like that.
</div>

# Allas supports two protocols

- S3  (used by: s3cmd, rclone, a-tools)
- Swift (used by: swift, rclone, a-tools, cyberduck)  

- Authentication is different
    - S3: permanent key based authentication – nice, easy and unsecure
    - Swift: authentication based on temporary tokens – more secure, requires authentication every 8 hours
        - Metadata is handled in different ways
        - Over 5G files are managed in different ways
- **Avoid cross-using Swift and S3 based objects!**


# Allas Clients: read, write, delete

**Puhti, Mahti, Linux servers, Macs:**

- rclone, swift, s3cdm, a-tools

**Virtual machines, small servers:**

- In addition to the tools above, you can use FUSE based virtual mounts

**Laptops (Windows, Mac):**

- [Cyberduck](https://cyberduck.io/), [FileZilla(pro)](https://filezilla-project.org/), [Pouta-www interface](https://docs.csc.fi/cloud/pouta/launch-vm-from-web-gui/)

# Allas – first steps for Puhti 

- Use [https://my.csc.fi](https://my.csc.fi) to apply Allas access for your project – Allas is not automatically available
- In Puhti and Mahti, setup connection to Allas with commands:
```bash
module load allas
allas-conf
```
- Study the manual and [Start using Allas with rclone or a-tools instructions](https://docs.csc.fi/data/Allas/)

# Allas – rclone

- Straight-forward power-user tool with wide range of features.
- Fast and effective.
- Available for Linux, Mac and windows.
- Overwrites and removes data without asking!
- The default configuration at CSC uses swift-protocol but S3 can be used too.
Use with care: [rclone instructions in Docs CSC](https://docs.csc.fi/#data/Allas/using_allas/rclone/)


# Allas – a-tools

- Rclone based scripts for using Allas in Puhti and Mahti
- A-tools try to provide easy and safe way to use Allas for occasional Allas user users.
- Developed for CSC server environment (Puhti, Mahti) but you can install the tools in other linux and mac machines too.
- Unlike rclone, a-tools do not overwrite and remove data without asking!
- Automatic packing and compression.
- Default bucket names based on directories of Puhti and Mahti
- [a-commands instructions in Docs CSC](https://docs.csc.fi/#data/Allas/using_allas/a_commands/)


# A-put/a-get: pros and cons

<div class="column">
➕ Saving data as a tar package preserves time stamps, accession settings, and internal links of the directory  
➕ `zstdmt` compression reduces size  
➕ Default bucket name and metadata reflect the directory sturctures of Puhti and Mahti  
➕ Checks to prevent over writing data accidentally  
</div>
<div class="column">
➖ Usage of objects, created by `a-put` can be complicated when other object storage tools are used  
➖ Especially usage from windows is problematic  
➖ Each object has an additional _ameta object  
</div>

# Allas problems

- 8 hour connection limit with swift
- No way to check quota
- Moving data inside Allas is not possible (swift)
- No way to freeze data (use two projects if needed).
- Different interfaces may work in diffrent ways


# Things that users should consider 

- Should I store each file as a separate object or should I collect it into bigger chunks?
- Should I use compression?
- Who can use the data: Projects and accession permissions?
- What will happen to my data later on?
- How to keep track of all the data I have in Allas?

# Fairdata services

- [https://fairdata.fi](https://fairdata.fi) - Services to manage scientific data according to FAIR principles.
- Suitable for all static digital research material and related metadata
- Free of charge for users in Finnish higher education institutions and research institutes
- **[IDA](https://ida.fairdata.fi)** : storage for research data 
- **[Quvain](https://qvain.fairdata.fi/)** : Descibe you dataset and gent a persistent indentifier for it
- **[Etsin](https://etsin.fairdata.fi/)** : Discover datasets based on metadata

# Sensitive data services

- [CSC Sensitive Data Services](https://docs.csc.fi/data/sensitive-data/) were launched on last June. 
- **SD Desktop** [https://sd-desktop.csc.fi](https://sd-desktop.csc.fi) is a secure virtual desktop for processing data.
     - Security is based on controlled access, controlled data import, and isolation from internet.
     - Data import _only_ through **SD Connect** service. No direct data export.
- **SD Connect** [https://sd-connect.csc.fi](https://sd-connect.csc.fi) is based on Allas. 
- At the moment Allas and SD-Connect are in practice the same service.
- Allas can be used for sensitive data, _only_ if it is properly encrypted. (SD-Connect procedure does that)

