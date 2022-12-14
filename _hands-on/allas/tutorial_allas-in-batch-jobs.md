---
topic: allas
title: Tutorial - Allas in batch jobs
---

# Using Allas in batch jobs

## Preparations

💬 The allas-conf command opens an Allas connection that is valid for eight hours. 
   - In case of interactive usage this eight-hour limit is not problematic as allas-conf can be executed again to extend the validity of the connection.
   - In case of batch jobs, the situation is different, as it may take more than eight hours before the job even starts. 

1. To be able to use Allas in a batch job, run `allas-conf` again with option `-k`:

```bash
allas-conf -k 
```
- Here the option `-k` indicates that the password will be stored in an environment variable `$OS_PASSWORD`. 
   - With this variable defined, you no longer need to define the password when you re-execute `allas-conf` with the `-k` option and the Allas project name. 

☝🏻 Note that if you mistype your password when using the `-k` option, you must use command `unset OS_PASSWORD` before you can try again.

{:start="2"}
2. Refresh the connection with command:

```bash
allas-conf -k project_xxxxxxx      # replace xxxxxxx
```

☝🏻 When OS_PASSWORD is set, the a-commands (a-put, a-get, a-list, a-delete) automatically refresh the Allas connection when the commands are executed in a batch job.

{:start="3"}
3. Choose a file from Allas. The file should have text in it.

```bash
a-list xxxxxxx_yourcscusername   # replace the name to match your bucket
```

4. Create a new batch job script. First open a new text file with command:

```bash
nano allas_xxxx.sh    # replace xxxx with a custom name for your job
```

5. Copy the batch job script from below to the text file you are editing.

**Option 1: a-commands**

```bash
#!/bin/bash
#SBATCH --job-name=my_allas_job        # Name of the job visible in the queue.
#SBATCH --account=project_xxxxxxx      # Choose the billing project. Has to be defined!
#SBATCH --time=00:05:00                # Maximum duration of the job. Max: depends of the partition. 
#SBATCH --mem-per-cpu=1G               # How much RAM is reserved for one processor.
#SBATCH --partition=test               # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --output=allas_output_%j.txt   # Name of the output-file.
#SBATCH --error=allas_errors_%j.txt    # Name of the error-file.

a-get xxxxxxx_yourcscusername/your-file-name                  # Bucket name / File name
wc -l your-file-name > your-file-name.num_rows     # File name
a-put -b xxxxxxx_yourcscusername your-file-name.num_rows # Bucket name / File name
```

{:start="6"}
6. Replace `xxxxxxx_yourcscusername` to match your bucket name and `your-file-name` with the name of the file you have in Allas. 

**Option 2: rclone**  

💭 If you use rclone or swift instead of the a-commands, you need to add _source allas_conf_ commands to your script. 

```bash
#!/bin/bash
#SBATCH --job-name=my_allas_job        # Name of the job visible in the queue.
#SBATCH --account=project_xxxxxxx      # Choose the billing project. Has to be defined!
#SBATCH --time=00:05:00                # Maximum duration of the job. Max: depends of the partition. 
#SBATCH --mem-per-cpu=1G               # How much RAM is reserved for one processor.
#SBATCH --partition=test               # Job queues: test, interactive, small, large, longrun, hugemem, hugemem_longrun
#SBATCH --output=allas_output_%j.txt   # Name of the output-file.
#SBATCH --error=allas_errors_%j.txt    # Name of the error-file.

#make sure connection to Allas is open
source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
rclone copy allas:xxxxxxx_yourcscusername/your-file-name ./        # Bucket name / File name

wc -l your-file-name > your-file-name.num_rows          # File name

#make sure connection to Allas is open
source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
rclone copy your-file-name.num_rows allas:xxxxxxx_yourcscusername  # File name / Bucket name
```

{:start="6"}
6. Replace `xxxxxxx_yourcscusername` to match your bucket name and `your-file-name` with the name of the file you have in Allas. 

7. Submit the batch job with command:

```bash
sbatch allas_xxxx.sh                   # This was the custom name you created earlier
```

8. Monitor the progress of your batch job:

```bash
squeue -u $USER
sacct -u $USER
a-list xxxxxxx_yourcscusername            # Bucket name
```
