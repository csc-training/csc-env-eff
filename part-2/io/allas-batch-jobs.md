---
layout: default
title: Allas in batch jobs
parent: 8. Working efficiently with data
grand_parent: Part 2
nav_order: 3
has_children: false
has_toc: false
permalink: /hands-on/allas/tutorial_allas-in-batch-jobs.html
---


# Using Allas in batch jobs

## Preparations

💬 The `allas-conf` command opens an Allas connection that is valid for eight hours.

- In case of interactive usage, this eight-hour limit is not problematic as `allas-conf` can be executed again to extend the validity of the connection.
- In case of batch jobs, the situation is different, as it may take more than eight hours before the job even starts.

1. To be able to use Allas in a batch job, run `allas-conf` again with the `-k` option:

```bash
allas-conf -k 
```

- Here, the option `-k` indicates that the password will be stored in an environment variable `$OS_PASSWORD`.
   - With this variable defined, you no longer need to input your password when you re-execute `allas-conf` with the `-k` option and the Allas project name.

☝🏻 Note that if you mistype your password when using the `-k` option, you must use the command `unset OS_PASSWORD` before you can try again.

{:style="counter-reset:step-counter 1"}
2. Refresh the connection with the command:

```bash
allas-conf -k <project>    # replace <project> with your CSC project, e.g. project_2001234
```

☝🏻 When `$OS_PASSWORD` is set, the `a-commands` (`a-put`, `a-get`, `a-list`, `a-delete`) automatically refresh the Allas connection when the commands are executed in a batch job.

{:style="counter-reset:step-counter 2"}
3. Choose a file from Allas. The file should have text in it.

```bash
a-list <project number>_$USER   # replace <project number> with your CSC project number, e.g. 2001234, to match the bucket you created earlier
```

{:style="counter-reset:step-counter 3"}
4. Create a new batch job script. First open a new text file with the command:

```bash
nano allas_<myjobname>.sh    # replace <myjobname> with a custom name for your job
```

{:style="counter-reset:step-counter 4"}
5. Copy the batch job script below to the text file you are editing:

- Option 1: `a-commands`

```bash
#!/bin/bash
#SBATCH --job-name=my_allas_job        # Name of the job visible in the queue.
#SBATCH --account=<project>            # Choose the billing project. Has to be defined!
#SBATCH --time=00:05:00                # Maximum duration of the job. Max: depends of the partition. 
#SBATCH --mem-per-cpu=1G               # How much RAM is reserved for one processor.
#SBATCH --partition=test               # Job queues: test, interactive, small, large, longrun, hugemem, $
#SBATCH --output=allas_output_%j.txt   # Name of the output-file.
#SBATCH --error=allas_errors_%j.txt    # Name of the error-file.

bucketname=<project number>_$USER      # Replace with your bucket name, e.g. 2001234_username
filename=<filename>                    # Replace with your file name

a-get $bucketname/$filename            # Bucket name / file name
wc -l $filename > $filename.num_rows   # file name
a-put -b $bucketname $filename.num_rows
```

{:style="counter-reset:step-counter 5"}
6. In the script, replace `<project number>_$USER` to match your bucket name and `<filename>` to the name of the file you have in Allas. Remember to also define your billing project (`--account`).

- Option 2: `rclone`  

💭 If you use `rclone` or `swift` instead of the `a-commands`, you need to add `source allas_conf` commands to your script.

```bash
#!/bin/bash
#SBATCH --job-name=my_allas_job        # Name of the job visible in the queue.
#SBATCH --account=<project>            # Choose the billing project. Has to be defined!
#SBATCH --time=00:05:00                # Maximum duration of the job. Max: depends of the partition. 
#SBATCH --mem-per-cpu=1G               # How much RAM is reserved for one processor.
#SBATCH --partition=test               # Job queues: test, interactive, small, large, longrun, hugemem, $
#SBATCH --output=allas_output_%j.txt   # Name of the output-file.
#SBATCH --error=allas_errors_%j.txt    # Name of the error-file.

bucketname=<project number>_$USER      # Replace with your bucket name, e.g. 2001234_username
filename=<filename>                    # Replace with your file name

# Make sure the connection to Allas is open
source /appl/opt/csc-cli-utils/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
rclone copy allas:$bucketname/$filename ./

wc -l $filename > $filename.num_rows

# Make sure the connection to Allas is open
source /appl/opt/csc-cli-utils/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
rclone copy $filename.num_rows allas:$bucketname
```

{:style="counter-reset:step-counter 5"}
6. Replace `<project number>_$USER` to match your bucket name and `<filename>` to the name of the file you have in Allas. Remember to also define your billing project (`--account`).
7. Submit the batch job with the command:

```bash
sbatch allas_<myjobname>.sh
```

{:style="counter-reset:step-counter 7"}
8. Monitor the progress of your batch job:

```bash
squeue -u $USER
a-list <project number>_$USER    # replace <project number> with your CSC project number, e.g. 2001234, to match your bucket
```
