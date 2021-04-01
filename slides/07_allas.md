---
theme: csc-2019
lang: en
---

# Allas object storage service {.title}

# How to get access to Allas

Use [https://my.csc.fi](https://my.csc.fi) to 

1. Register to CSC (haka)
2. Set up a project at CSC (Principal Investigator)
3. Apply for Puhti and Allas service, quota and billing units for your project
4. Add other registered users to your project
5. Members have to register and accept the services in [https://my.csc.fi](https://my.csc.fi)

All project members have equal access to the data in Puhti and Allas.

# Allas – object storage: what it is for?

*  Allas is a new storage service for all computing and cloud services
*  CEPH based object storage
*  Meant for data during project lifetime
*  Default quota 10 TB / Project.
*  Possible to upload data from personal laptops or organizational storage systems into Allas
*  Clients available in Puhti and Mahti
*  Data can also be shared via Internet

# Allas – object storage: what it is for?

<br>

<div class="column">
*  Data can be moved to and from Allas directly without using Puhti or Mahti.
*  For computation the data has to be typically copied to a file system in some computer
*  Data can be shared publicly to Internet, which is otherwise not easily possible at CSC.
</div>
<div class="column">
!["Allas"](img/allas.png "Allas"){width=90%}
</div>

# Allas – object storage: what it is NOT

*  **Allas is not a file system** (even though many tools try to fool you to think so). It is just a place for a pile of static data objects.
*  **Allas is not a data management environment**. Tools for etc. search, metadata,version control and access management are minimal.
*  **Allas is not a back up service**. Project mebers can delete all the data with just one command.

# Allas - storage 

* An object is stored in multiple servers so a disk or server break does not cause data loss.
* There is no backup i.e. if a file is deleted, it cannot be recovered
* Data cannot be modified while it is in the object storage – data is immutable.
* Rich set of data management features are to be built on top of it.
* Usage through S3 and Swift APIs are supported

# Allas – object storage: terminology

*  Storage space in Allas is provided per **CSC project**
*  Project space can have multiple *buckets* ( up to 1000)
*  There is only one level of hierarchy of buckets (no buckets within buckets)
*  Data is stored as **objects** within a bucket
*  Objects can contain can contain any type of data (generally, object = file)
*  In Allas you can have 500 000 objects / bucket
*  Name of the bucket must be unique within Allas
*  Objects have metadata that can be enriched 
*  In reality, there is no hierarcical directory structure, although it sometimes looks like that.

# Allas supports two protocols

*  S3  (used by: s3cmd)
*  Swift (used by: swift, rclone, a-tools, cyberduck)  

*   Authentication is different
    * S3: permanent key based authentication – nice, easy and unsecure
*   Swift: authentication based on temporary tokens – more secure, requires authentication every 8 hours
    * Metadata is handled in different ways
    * Over 5G files are managed in different ways
*   → **Avoid cross-using Swift and S3 based objects!**


# Allas Clients: read, write, delete

**Puhti, Mahti, Linux servers, Macs:**
*  rclone, swift, s3cdm, a-tools

**Virtual machines, small servers:**
* In addition to the tools above, you can use FUSE based virtual mounts

**Laptops (Windows, Mac):**
* Cyberduck, FileZilla(pro), pouta-www interface
FIXME: links to these / detailed instructions?

# Allas – first steps for Puhti 

*  Use [https://my.csc.fi](https://my.csc.fi) to apply Allas access for your project – Allas is not automatically available
*  In Puhti and Mahti, setup connection to Allas with commands:
```bash
module load allas
allas-conf
```
*  Study the manual and [Start using Allas with rclone or a-tools instructions](https://docs.csc.fi/data/Allas/)

# Allas – rclone

*  Straight-forward power-user tool with wide range of features.
*  Fast and effective.
*  Available for Linux, Mac and windows.
*  Overwrites and removes data without asking!
*  The default configuration at CSC uses swift-protocol but S3 can be used too.
Use with care: [rclone instructions in Docs CSC](https://docs.csc.fi/#data/Allas/using_allas/rclone/)


# Allas – a-tools

*  Rclone based scripts for using Allas in Puhti and Mahti
*  A-tools try to provide easy and safe way to use Allas for occasional Allas user users.
*  Developed for CSC server environmnet (Puhti, Mahti) but you can install the tools in other linux and mac machines too.
*  Unlike rclone, a-tools do not overwrite and remove data without asking!
*  Automatic packing and compression.
*  Default bucket names based on directories of Puhti
*  [a-commands instructions in Docs CSC](https://docs.csc.fi/#data/Allas/using_allas/a_commands/)


# A-put/a-get: pros and cons

+ Saving data as a tar package preserves time stamps, accession settings, and internal links of the directory.
+ `zstdmt` compression reduces size
+ Default bucket name and metadata reflect the directory sturctures of Puhti and Mahti
+ Checks to prevent over writing data accidentally

- Usage of objects, created by `a-put` can be complicated when other object storage tools are used
- Especially usage from windows is problematic
- Each object has an additional _ameta object

# Allas problems

*   8 hour connection limit with swift
*   No way to check quota
*   Moving data inside Allas is not possible (swift)
*   No way to freeze data (use two projects if needed).
*   Different interfaces may work in diffrent ways


# Things that users should consider 

*   Should I store files as one object or as bigger chunks?
*   Should I use compression?
*   Who can use the data: Projects and accession permissions?
*   What will happen to my data later on?
*   How to keep track of all the data I have in Allas?
