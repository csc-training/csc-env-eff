---
topic: allas
title: Tutorial - Allas in batch jobs
---

# Allas web-interface

- Open the view to the Allas service in your browser using the cPouta WWW-interface: [https://pouta.csc.fi](https://pouta.csc.fi)
- Login with your csc user account.
- From the upper left corner, you find a project selection pop-up menu. 
   - If you have several projects available, select the training project: **project_2004306**
- From the menu on left side of the interface, select: **Object Store -> Containers**
- Create new container by pressing button: **➕Container**
   - Keep the container _Not public_ and name it as 2004306_xxxx ( replace xxxx with your user account).
- Find the newly-created container (also called as `bucket` in S3 protocol) and open it
   - Upload one file from your computer. Any file should do, but prefer a file that you can open in Puhti.

💭 During the exercises, you can use this web-interface to get another view to the buckets and objects in Allas.
> Note, that you need to **reload** the view in order to see the changes.

## Using Allas in batch jobs

The allas-conf command opens an Allas connection that is valid for eight hours. In the case of interactive usage this eight-hour limit is not problematic as allas-conf can be executed again to extend the validity of the connection.

In the case of batch jobs, the situation is different, as it may take more than eight hours before the job even starts. 
To be able to use Allas in a batch job, run _allas-conf_ again with option **-k**.
```text
allas-conf -k 
```
Here the option -k indicates that the password will be stored in the environment variable $OS_PASSWORD. With this variable defined, you no longer need to define the password when you re-execute allas-conf with the -k option and the Allas project name. Note that if you mistype your password when using the -k option, you must use command **unset OS_PASSWORD** before you can try again.

Refresh the connection with command:

```text
allas-conf -k project_2004306
```
When OS_PASSWORD is set, the a-commands (a-put, a-get, a-list, a-delete) automatically refresh the Allas connection when commands are ececuted in batch job.

To test this, create a new batch job script. First open a new text file with command (relace xxxx  here too):

```text
nano allas_xxxx.sh
```
Then copy the batch job script sample lines from below to the text file you are editing.
Replace _xxxx_ with your user account and _your-file-name_ with the name of the file you 
previously uploaded to Allas. When you are ready, save the changes with _Ctrl-o_ and exit nano with _Ctrl-x_ . 

```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2004306
#SBATCH --time=00:05:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=test
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

a-get 2004306_xxxx/your-file-name
wc -l your-file-name > your-file-name.num_rows
a-put -b 2004306_xxxx --nc your-file-name.num_rows
```
Submit the batch job with command:
```text
sbatch allas_xxxx.sh
```

Use commands below to monitor the progress of your batch job.
```text
squeue -u $USER
sacct -u $USER
a-list 2004306_xxxx
```

If you use rclone or swift instead of the a-commands, you need to add _source allas_conf_ commands to your script. 
In this case, the batch job script for Puhti could look like:
```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2004306
#SBATCH --time=00:05:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=test
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

#make sure connection to Allas is open
source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
rclone copy allas:2004306_xxxx/your-file-name ./

wc -l your-file-name > your-file-name.num_rows

#make sure connection to Allas is open
source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
rclone copy your-file-name.num_rows allas:2004306_xxxx
```
