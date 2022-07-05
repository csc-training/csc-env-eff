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

# How to get access to Allas service

Use [https://my.csc.fi](https://my.csc.fi) to 

1. Register to CSC (haka)
2. Set up a project at CSC (Principal Investigator)
3. Apply for Puhti and Allas service, quota and billing units for your project
4. Add other registered users to your project
5. Members have to register and accept the services in [https://my.csc.fi](https://my.csc.fi)

All project members have equal access to the data in Puhti and Allas.

:::info (speech)
Allas is a CSC service, and to use it you need to have a CSC user account – which is a member in a CSC project.
And then just like for Puhti and Mahti, you apply for the Allas service. 
Allas is available for all project members – after they accept the Allas terms of use.
Note that you can use Allas without Puhti or Mahti, if you only want to store files for your project.
:::

# Allas – object storage: what it is?

- Allas is a storage service for all computing and cloud services
- CEPH based object storage
- Possible to upload data from personal laptops or organizational storage systems into Allas
- Meant for data during project lifetime
- Default quota 10 TB / Project 
- Clients available in Puhti and Mahti

:::info (speech)
Allas is a general purpose storage system, where files are stored as objects.
It is developed at CSC to provide a long term data storage space for computing and cloud services.
It is a CEPH-based data storage system - in case anyone asks.
Allas is accessible from the CSC computing environment, and personal computers as well.
It is meant for storing your datasets during your project lifetime. 

The default Allas storage quota for one CSC project is 10 terabytes. 
If you need to have more quota, and you have good reasons for that, you can apply for more. 
For that you need to send email to the CSC servicedesk – but don't be shy to let us know, if you really need the space. 
At the moment, the biggest projects have several hundreds of terabytes of data stored in Allas. 
It is better to use Allas for storing large datasets – rather than for example, applying for more scratch space for just having some data available for you.

Puhti and Mahti have clients for accessing Allas, but Allas not in any way bound to other CSC services. 
You can upload data and use Allas directly from your PC, or from your organization's own computing system. 
Just note that there you have to install yourself the clients that you use.
:::

# Connections to Allas

<div class="column">
- Data can be moved to and from Allas directly without using Puhti or Mahti.
    - Usage through S3 and Swift APIs are supported
- Data can be shared publicly to Internet, which is otherwise not easily possible at CSC.
</div>
<div class="column">
!["Allas"](img/allas.png "Allas"){width=90%}
</div>

:::info (speech)
So Allas is in a sense a some kind of data hub of CSC. 
The illustration shows that you can access Allas from Puhti and Mahti.
Other examples are: a weather measurement station – where the sensors send the data directly to Allas, an university computer server, a Virtual Machine in cPouta, a personal computer, a mobile phone, and a web page.
So it does not need to be CSC involved in the process of moving data.
As long as you are connected to internet, you can use Allas.

The usual workflow is to have the static dataset stored all the time in Allas, and copy it to a computer to do some analyses.
And then put a new or another version of the dataset to Allas – if it had been modified somehow. 

Files in Allas can be shared publicly to Internet.
For example these slides are stored in Allas.
Check the URL from the video description.
:::

# Allas – object storage: what it is NOT

- **Allas is not a file system** (even though many tools try to fool you to think so). 
    - It is just a place for a pile of static data objects.
- **Allas is not a data management environment**. 
    - Tools for etc. search, metadata, version control and access management are minimal.
- **Allas is not a back up service**. 
    - Project members can delete all the data with just one command.

:::info (speech)
Allas is not a file system or disk. 
Many of the interfaces represent the data like it had some hierarchy – directories, subdirectories and files – but in practice it is just a pile of static data objects.
You can add, read and delete objects, but you are not modifying any data there.
There is no real hierarchy - it is just a place where you have some data blobs stored. 

Allas is also not a data management environment.
The tools for searching data, doing version controlling, or metadata management are minimal. 
The basic Allas command line tools can handle maybe some hundreds of objects in Allas.
Workflows that automatically collect data to Allas – and store it for a long time – will end up having hundreds of thousands of small files.
They will need some other tools to keep track of the data stored in Allas. 
You can store huge amounts of data to Allas, but we recommend to set up some support service – like a database that tells you later on what data is where, and how to access it from Allas. 

Also, Allas is not a backup service.
If you ask where to copy of your important files from ProjAppl, we will suggest you to make a copy to Allas.
Nevertheless we want to point out, that it is not a full backup, because you or your colleagues can still accidentally delete the data from Allas. 
All the project members have equal rights to the project's data in Allas.
You have to make sure that your project members know how to use the service, and agree on files that should not be deleted.
Note that all it takes is just one erratic command - from you or your project members - and the data is lost.
Always keep important backups in a safe place - for example in a separate local hard drive.
Allas is not a final resting place of your data - the point is that you can have your data there while you are actively working with that data - which is sometimes several years. 
:::

# Allas: File storing

- An object is stored in multiple servers 
    - A disk or server break does not cause data loss
- There is no backup i.e. if a file is deleted, it cannot be recovered
- Data cannot be modified while it is in the object storage
    - For computation the data has to be typically copied to a file system in some computer
- Some data management features are built on top of it.

:::info (speech)
Technical-wise Allas is quite secure.
Data is stored into several servers in Allas. 
Individual disc or server breaks will not result to data losses, because other discs or servers have another copies. 
Note that even these multiple copies of data do not help, if the user deletes the file or object.
We at CSC cannot recover your deleted data from Allas.

Storing data as static objets means that they can not be modified while they are in Allas. 
If you want to edit a file you have to download it to some other environment, for example to your local laptop. 
Then after you edit the document you can overwrite the file in Allas. 

You can use some data management and metadata tools included in Allas, but they have somewhat limited features. 
:::

# Allas buckets

- Storage space in Allas is provided per **CSC project**
- Project space can have multiple **buckets** (up to 1000)
    - Some sources refer to *buckets* as *containers*
        - Must not be confused with Docker/Singularity containers!
- Name of the bucket must be unique within Allas

:::info (speech)
Allas storage space is given for a CSC project - sometimes referred as Allas project. 
If your project has only one user, then the data is accessible by you only, but that is rarely the case.
Each project can have up to 1000 of so-called buckets. 
A bucket is kind of a root directory in Allas.
Some interfaces may refer to buckets as containers, but that confuses easily with Docker containers!

Each of the bucket names must be unique throughout all Allas. 
This is because the bucket names are used, if you generate public URLs for your buckets. 
Therefore two projects cannot have the same bucket name in use. 
Keep this in mind when creating buckets, and include for example your project number in the bucket name
Then you can be quite sure no one else has a bucket with the same name. 
If you try to use already used bucket name, the system gives you an error message. 
:::

# Allas objects

- Data is stored as **objects** within a bucket
    - Objects can contain any type of data (generally: object = file)
    - Objects have metadata that can be enriched 
- In Allas you can have 500 000 objects / bucket
- There is only one level of hierarchy of buckets (no buckets within buckets)
    - There is no hierarcical directory structure, although it sometimes looks like that.

:::info (speech)
Data is stored in a way that is called as an object, which is like a static blob of data.
In general you can think that one file is one object. 
That means that in a normal bucket: an object name equals to a file name, and you can pull the file to you environment by pointing the object name.
Then for example larger files might be automatically stored as several objects in Allas, but in practice you don't have to worry about that. 
Objects have metadata and users can add or edit their own metadata.
Each bucket can have half a million objects. 
It sure sounds a lot at first, but if you have an automatic data collection service, you may end up having these many files. 
We ask you not to have these many objects in your buckets, because it will make the system very slow. 
It is better to create more buckets and spread the files among those.

The one level of hierarchy means, that there can be only objects inside buckets, not buckets inside buckets. 
You can have object names which look like that there were some directory structure. 
For example: if the object name is maindir/dataset/data – where maindir and dataset are like pseudofolders.
Still there is no real directory structure there - instead it is a long object name with directory names and slashes. 
All in all you may think your project's Allas space as a home folder.
In there you have up to 1000 folders (here buckets) that have files - but not real subdirectories. 
:::

# Allas supports two protocols

- S3  (used by: s3cmd, rclone, a-tools)
- Swift (used by: swift, rclone, a-tools, cyberduck)  

- Authentication is different
    - S3: permanent key based authentication – nice, easy and unsecure
    - Swift: authentication based on temporary tokens – more secure, requires authentication every 8 hours
- File handling is different        
    - Metadata is handled in different ways
    - Over 5G files are managed in different ways
    - **Avoid cross-using Swift and S3 based objects!**

:::info (speech)
There are several tools to interface with Allas.
Those tools use either S3, or Swift protocol, for uploading and downloading data. 
Both of them have their pros and cons, and you can use either one of them. 

For the end user the biggest difference between S3 and Swift is in the authentication. 
When you open the connection to Allas, you have to authenticate first. 
S3 protocol creates a permanent key for accessing your project's data in Allas. 
These keys are always project specific and permanent.
The same can be used from any client to access the project's data in Allas, until you delete the key from the system. 
It is convenient for a user, but also very unsecure. 
If anybody steals your key - which is just a two random character strings - they can access all the data in your project. 
It means they can also delete all the data, and you won't even notice it. 
Swift protocol also has a random string used for authentication, but it is a temporary token. 
The key is valid only for a limited time - currently eight hours. 
After eight hours, or if you close the terminal session, you need to generate new key with your CSC password.
It is perfectly fine to initiate a new connection – already before eight hours have passed.
If somebody gets access to your Allas keys used by Swift protocol, they have only eight hours time to do something.
Then if someone gets your CSC password - well that is not good for many different reasons!
In Puhti and Mahti environment we are preferring Swift for its safer authentication. 

The two protocols also manage metadata a little bit different way. 
And they handle large files also a little bit differently. 
Swift protocols split your data in smaller pieces, so that you can easily read only part of it if needed.
S3 instead stores everything in a one big object. 
Because of these differencies you should avoid cross-using Swift and S3 based objects. 
That means if you have uploaded the data to Allas with one protocol, it is better to also read it using the same protocol.
:::

# Allas Clients:

**Puhti, Mahti, Linux servers, Macs:**
- rclone, swift, s3cmd, a-tools

**Laptops (Windows, Mac):**
- [Cyberduck](https://cyberduck.io/), [FileZilla(pro)](https://filezilla-project.org/), [Pouta-www interface](https://docs.csc.fi/cloud/pouta/launch-vm-from-web-gui/)

**Virtual machines, small servers:**
- In addition to the tools above, you can use FUSE based virtual mounts

:::info (speech)
These Allas clients listed in this slide use either Swift or S3 protocol. 
Many of these tools can actually use both of the protocols. 
In Puhti and Mahti, we are mostly using command line clients – like rclone, swift, s3cmd and a-tools. 
In your local Mac or Linux computer, you can also use the same tools in Terminal. 
In Windows and Mac you can use at least Cyberduck, FileZilla pro, Pouta web-interface or SD-Connect.

You can also use FUSE-based virtual mounts, which makes one bucket in Allas to be shown as a directory.
That is handy especially in virtual machines.
It is also very prone for errors, and we suggest you use only the Read-Only mode with this kind of approach.
:::

# Allas – first steps for Puhti 

- Use [https://my.csc.fi](https://my.csc.fi) to apply Allas access for your project – Allas is not automatically available
- In Puhti and Mahti, setup connection to Allas with commands:
```bash
module load allas
allas-conf
```
- Study the manual and [Start using Allas with rclone or a-tools instructions](https://docs.csc.fi/data/Allas/)
- The [material bank](https://csc-training.github.io/csc-env-eff/#7-allas-and-where-to-keep-your-data) includes hands-on tutorials and a tutorial video about Allas

:::info (speech)
First you have to enable Allas service in my CSC. 
In Puhti or Mahti environment Allas is available as a module, which includes the Allas tools.
Load the Allas module with command module load allas. 
Then run the command allas-conf, which by default opens a swift-based connection.
The configuration process asks you to specify a project. 
The connection stays for eight hours, so you have time to figure out what was the command to see your buckets and files.
Check out the material bank for tutorials and a hands-on Allas tutorial video.
:::

# Allas – rclone

- Straight-forward power-user tool with wide range of features.
- Fast and effective.
- Available for Linux, Mac and windows.
- Overwrites and removes data without asking!
- The default configuration at CSC uses swift-protocol but S3 can be used too.
Use with care: [rclone instructions in Docs CSC](https://docs.csc.fi/#data/Allas/using_allas/rclone/)

:::info (speech)
A straight-forward command line interface, that can be used with Allas is rclone.
It works fast and provides functions like move, copy, tree and cat.
You can install it to all operating systems.
Be mindful that rclone overrides and removes data without asking. 
That means you have to know: which copy of your file is the newer version.
Rclone does not ask that "do you want to override this new file with this older one" - it just copies what you write in the command.
And if you have a very large sets of objects, then it does not always function properly. 
We have found that rclone has difficulties to list for example datasets, which have tens of thousands of objects in a one bucket.
By default at CSC rclone is configured to use swift, but S3 can be used as well.
:::

# Allas – a-tools

- Rclone based scripts for using Allas in Puhti and Mahti
- A-tools try to provide easy and safe way to use Allas for occasional Allas user users.
- Default bucket names based on directories of Puhti and Mahti
- Unlike rclone, a-tools do not overwrite and remove data without asking!
- Developed for CSC server environment (Puhti, Mahti) but you can install the tools in other linux and mac machines too.
- Automatic packing and compression.
- [a-commands instructions in Docs CSC](https://docs.csc.fi/#data/Allas/using_allas/a_commands/)

:::info (speech)
We at CSC have created a wrapper around the native rclone.
The aim is to make the scripts more easy to use in Puhti and Mahti. 
For example it uses default bucket names so you don't have to. 
If you do not define a bucket name, it checks where your data is coming – for example from Scratch directory of Puhti - and it creates a corresponding bucket for your project, and puts the data there.
A-tools also do ask before overwriting or removing data.
The basic use case is that you use data from Puhti or Mahti, make a copy to Allas, and later on download the data back to Puhti or Mahti. 
You can install these tools to other Linux and Mac machines as well. 
But note that a-tools are developed with CSC environment in mind.
For example it collects the files in one tar package and does compression before uploading to Allas. 
If you want to then push the data out to some other service, it may require extra steps for uncompressing and unpacking the data before you can access the files. 
:::

# A-put/a-get: pros and cons

<div class="column">
➕ Saving data as a tar package preserves time stamps, accession settings, and internal links of the directory  
➕ `zstdmt` compression reduces size  
➕ Default bucket name and metadata reflect the directory sturctures of Puhti and Mahti  
➕ Checks to prevent over writing data accidentally  
</div>
<div class="column">
➖ Usage of objects, created by `a-put` can be complicated when other object storage tools are used  
➖ Especially usage from Windows is problematic  
➖ Each object has an additional _ameta object  
</div>

:::info (speech)
This is also a comparison of a-tools and rclone.
As stated in the previous slide, a-tools work nicely in the CSC environment.
It packages the data nicely, and allows you to store and move it in a bigger chunks – instead of file by file. 
The file size is reduced with compression, so you can store more data consuming less billing units.
With a-tools you don't need to think about bucket names.
The default bucket names refer to Puhti and Mahti directory structures. 
A-tools also prevent you from accidentally overwriting your data. 

The downsides of a-tools are mainly related to the usage in other that CSC environments.
Trying to read an object that is created with some other tool is usually complicated.
Objects created with a-tools have an additional ameta metadata object.
A-tools put them in your bucket in addition to the object itself.
:::

# Issues with Allas

- 8 hour connection limit with swift
- No way to check quota
- Moving data inside Allas is not possible (swift)
- No way to freeze data 
    - Use two projects if you need to prevent others editing your data
- Different interfaces may work in different ways

:::info (speech)
Then some practical good-to-know issues concerning Allas in general. 
First of all is this eight hour connection limit with Swift. 
It usually is not an issue in normal interactive work, but in batch jobs you need to take that into account.
It might be that your batch job does not even start before the eight-hour limit has gone. 
In batch jobs you should configure Allas so that it stores your password in an environment variable in the session.
Then the Allas connection can be refreshed by the batch job – by using the password from the environmental variable.
Check the material bank for a tutorial on how to achieve this.

In Allas you cannot check the quota to see the maximum amount of data you can have in Allas. 
If you increase your quota from the 10TB default, there is no way to check the quota in Allas. 
You can check the emails from CSC telling that you have been granted 50 terabytes of quota. 
If you try to put there data that exceeds the quotas, it will tell that object is too large.
Then you might guess that you have hit the size limit of the Allas area. 

Moving data inside Allas is not possible, at least with the swift protocol. 
If you want to move a dataset from one bucket to another – or from one project to another, you have to download it to – for example Puhti Scratch – and then push it to the new location in Allas. 
That is of course more time consuming that it would be to move the data only inside Allas.

Freezing the data means such a read-only mode, that would prevent others modifying the data. 
To achieve that in Allas, you could use a so-called "two project protocol" as a workaround. 
The first Allas project is the hosting project. 
The managers has full access rights to data under that project.
They can set up another project for the users of the data. 
The users don't belong to the data hosting project, so they don't have full access to all the data.
The managers can grant access for a selected users – for example to one single bucket.
This way you can have more secure way of sharing your data with your project members.
Another option is that you create a separate front server inside or outside Allas.
With the server you can control the access to data that you have in Allas. 
For example you can set up a NextCloud server in cPouta, and use that to share data to your external collaborators somewhere else.

It is a good idea to learn one Allas interface like a-tools, and stick with that as much as possible.
If you need to use many different interfaces, keep in mind that they may work in a little bit different ways.
For example different CyberDuck versions show the data in little bit different ways. 
You may not always see the same buckets and objects there - even though you should - because the interfaces interpret the pseudofolders differently.
:::

# Things that users should consider 

- Should I store each file as a separate object or should I collect it into bigger chunks?
    - In general: consider how you use tha data
- Should I use compression?
- Who can use the data: Projects and access rights?
- What will happen to my data later on?
- How to keep track of all the data I have in Allas?

:::info (speech)
Whenever you plan to store something in Allas, you should think whether to store individual files, or to collect them in larger chunks.
Think about how you will use the data.
If you use a set of scripts that consist of three files, you should collect those files to a one tar package, and upload the package as one object to Allas. 
Then you can download the files as one object, which puts less stress to the system.
Consider also using compression to reduce the space needed to store the data.
It also reduces the time needed to move the data in and out of Allas. 
That is especially good thing, if you have a slow or unstable internet connection.
Compression of course takes time, so it may not always bring time efficiency.

You should also think of who can use the data.
By default all project members have equal access to the data. 
Usually that is the ideal situation.
If not, then consider using two projects or another server to manage access.

Note that Allas is not the final resting place of your data. 
When you start a CSC project, you should already consider: what will happen to the project's data when the project ends.
Remember that the project lifetime has to be extended yearly, if the project still continues.
After the project is finished, you need to save everything in somewhere else, because everything will be removed from the CSC environment - which means from Allas as well.
  
In time you start to accumulate large amounts of data in Allas.
It will get difficult to keep track of all the data you have.
You should plan and make rules on how to store the data in the Allas project – already before starting to use Allas.
Especially if there is a whole group pushing files and datasets to Allas, it will get messy after a while.
:::

# Fairdata services

- [https://fairdata.fi](https://fairdata.fi) - Services to manage scientific data according to FAIR principles.
- Suitable for all static digital research material and related metadata
- Free of charge for users in Finnish higher education institutions and research institutes
- **[IDA](https://ida.fairdata.fi)** : storage for research data 
- **[Quvain](https://qvain.fairdata.fi/)** : Descibe you dataset and gent a persistent indentifier for it
- **[Etsin](https://etsin.fairdata.fi/)** : Discover datasets based on metadata

:::info (speech)
A few words about other data services at CSC. 
Allas is not the only place where you can store data. 
The Fairdata services are more focused services developed with datasets in mind.
You can use them when you have a ready static data set – that you want to store for longer time, and make it available for other researchers as well. 
Fairdata services consist of three main services. 
IDA is the storage service, where you can do things like data freezing and backup copies. 
Linking to IDA, there is Quvain for describing the data.
There are rich metadata features, and a possibility to create a persistent identifier for your data, which you can use in your publications. 
Then there is the Etsin service, which allows external users to look for the datasets stored in IDA and described with Quvain. 
The datasets do not need to be accessible to everybody. 
People can see that the dataset is there in IDA, and who has access to it.
Then they can contact the manager to ask for access to use the dataset.
:::

# Sensitive data services

- [CSC Sensitive Data Services](https://docs.csc.fi/data/sensitive-data/) for processing sensitive data
- **SD Desktop** [https://sd-desktop.csc.fi](https://sd-desktop.csc.fi) is a secure virtual desktop
     - Controlled access, 
     - Data import _only_ through [**SD Connect**](https://sd-connect.csc.fi) service
     - Isolation from internet
     - No direct data export
- Allas could be used for sensitive data, but _only_ if data is properly encrypted
    - [**SD Connect**](https://sd-connect.csc.fi) procedure does the encryption

:::info (speech)
Sensitive data services at CSC are intended for working with datasets that contain sensitive or secret material. 
In the core of the service is SD Desktop - Sensitive Data Virtual Desktop.
You can use that to work with sensitive data secure way. 
The data is imported to the system through interface called SD-Connect.
The fact that you cannot access internet – or pull out data from SD Desktop – makes it more secure.
It is possible to have a collaboration project, where you let your collaborators do analyses with your data, but never get the data out of your control. 
In practice you can use Allas for storing sensitive data, but you have to always encrypt the data before you upload it to Allas.
SD-Connect does encryption automatically, and in a way which is compatible with the SD-Desktop.

The tutorials about Allas continue from here. 
They cover the basic use cases with easy-to-follow examples.
Allas documentation covers the introduction to Allas and the technical details.
:::

