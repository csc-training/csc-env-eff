---
topic: allas
title: Tutorial - Allas in batch jobs
---

# Using Allas in batch jobs

**Preparations**  
- The allas-conf command opens an Allas connection that is valid for eight hours. 
   - In the case of interactive usage this eight-hour limit is not problematic as allas-conf can be executed again to extend the validity of the connection.
   - In the case of batch jobs, the situation is different, as it may take more than eight hours before the job even starts. 
- To be able to use Allas in a batch job, run _allas-conf_ again with option **-k**.
```text
allas-conf -k 
```
   - Here the option -k indicates that the password will be stored in the environment variable $OS_PASSWORD. 
      - With this variable defined, you no longer need to define the password when you re-execute allas-conf with the -k option and the Allas project name. 
      - Note that if you mistype your password when using the -k option, you must use command **unset OS_PASSWORD** before you can try again.

- Refresh the connection with command:
```text
allas-conf -k project_2004306
```
   - When OS_PASSWORD is set, the a-commands (a-put, a-get, a-list, a-delete) automatically refresh the Allas connection when commands are executed in batch job.
- Choose a file from Allas. The file should have text in it.
```text
a-list 2004306_xxxx   # replace xxxx to match your training bucket/container name
```
- Create a new batch job script. First open a new text file with command:
```text
nano allas_xxxx.sh    # replace xxxx with custom name
```
- Copy the batch job script from below to the text file you are editing.
   - Replace _xxxx_ to match your bucket/container name and _your-file-name_ with the name of the file you have in Allas. 

**Option 1: a-commands**

```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2004306
#SBATCH --time=00:05:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=test
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

a-get 2004306_xxxx/your-file-name                  # Bucket name / File name
wc -l your-file-name > your-file-name.num_rows     # File name
a-put -b 2004306_xxxx --nc your-file-name.num_rows # Bucket name / File name
```

**Option 2: rclone**  
💭 If you use rclone or swift instead of the a-commands, you need to add _source allas_conf_ commands to your script. 

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
rclone copy allas:2004306_xxxx/your-file-name ./        # Bucket name / File name

wc -l your-file-name > your-file-name.num_rows          # File name

#make sure connection to Allas is open
source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
rclone copy your-file-name.num_rows allas:2004306_xxxx  # File name / Bucket name
```

- Submit the batch job with command:
```text
sbatch allas_xxxx.sh          # This was your custom name
```
- Monitor the progress of your batch job:
```text
squeue -u $USER
sacct -u $USER
a-list 2004306_xxxx           # Bucket name
```
