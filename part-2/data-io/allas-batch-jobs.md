---
layout: default
title: Using Allas in batch jobs
parent: 8. Working efficiently with data
grand_parent: Part 2
nav_order: 2
has_children: false
has_toc: false
permalink: /hands-on/data-io/tutorial_allas-in-batch-jobs.html
---

# Using Allas in batch jobs

## Preparations

💬 On Roihu, `allas-conf` sets up a **persistent S3 connection** by default.
Unlike the older Swift protocol (which is only valid for eight hours), the S3
connection does not expire, so there is no need to worry about a batch job
starting late or running longer than eight hours.

1. Load the Allas module and open a connection to Allas interactively
   **before** submitting your batch job:

   ```bash
   module load allas
   allas-conf
   ```

   ‼️ Re-running `allas-conf` later (e.g. to switch to a different project)
   updates the generic `s3allas:` rclone endpoint to point at the new
   project. This can affect batch jobs that are still queued or running! To
   avoid this, prefer the project-specific endpoint `s3allas-project_<id>:`
   (also created by `allas-conf`) in your batch scripts instead of
   `s3allas:`.

   💡 If you specifically need the Swift protocol instead (e.g. to access
   multiple projects from the same session), see
   [Using the legacy Swift protocol](#using-the-legacy-swift-protocol) below.

2. Choose a file from Allas. The file should have text in it. You can use the
   one you created in
   [one of the earlier tutorials](../../part-1/allas/allas-usage.md),
   or then any other text file you have in Allas:

   ```bash
   a-list <project_number>_$USER  # replace <project_number> with your CSC project number, e.g. 2001234, to match the bucket you created earlier
   ```

3. Create a new batch job script. First open a new text file with the command:

   ```bash
   nano allas_job.sh
   ```

4. **Option 1:** `a-commands`
   1. Copy the batch job script below to the text file you are editing:

      ```bash
      #!/bin/bash
      #SBATCH --job-name=my_allas_job          # Name of the job visible in the queue
      #SBATCH --account=<project>              # Choose the billing project. Has to be defined!
      #SBATCH --time=00:05:00                  # Maximum duration of the job. Max: depends of the partition
      #SBATCH --mem-per-cpu=1G                 # How much RAM is reserved for one processor
      #SBATCH --partition=test                 # Job queues (CPU): interactive, test, small, medium, large, longrun, hugemem, hugemem_longrun
      #SBATCH --output=allas_output_%j.txt     # Name of the output-file
      #SBATCH --error=allas_errors_%j.txt      # Name of the error-file
        
      bucketname=<project_number>_$USER        # Replace with your bucket name, e.g. 2001234_username
      filename=<filename>                      # Replace with your file name
        
      a-get $bucketname/$filename              # Bucket name / file name
      wc -l $filename > $filename.num_rows     # file name
      a-put -b $bucketname $filename.num_rows
      ```

   2. In the script, replace `<project_number>_$USER` to match your bucket name
   and `<filename>` to the name of the file you have in Allas. Remember to also
   define your billing project (`--account`).

5. **Option 2:** `rclone`

   ☝🏻 Since the S3 connection set up in [Preparations](#preparations) is
   persistent, no extra connection code is needed inside the batch script --
   just make sure you have run `allas-conf` interactively beforehand.

   1. Copy the batch job script below to the text file you are editing:   

      ```bash
      #!/bin/bash
      #SBATCH --job-name=my_allas_job          # Name of the job visible in the queue.
      #SBATCH --account=<project>              # Choose the billing project. Has to be defined!
      #SBATCH --time=00:05:00                  # Maximum duration of the job. Max: depends of the partition. 
      #SBATCH --mem-per-cpu=1G                 # How much RAM is reserved for one processor.
      #SBATCH --partition=test                 # Job queues (CPU): interactive, test, small, medium, large, longrun, hugemem, hugemem_longrun
      #SBATCH --output=allas_output_%j.txt     # Name of the output-file.
      #SBATCH --error=allas_errors_%j.txt      # Name of the error-file.
      
      bucketname=<project_number>_$USER        # Replace with your bucket name, e.g. 2001234_username
      filename=<filename>                      # Replace with your file name
      
      rclone copy s3allas:$bucketname/$filename ./
      
      wc -l $filename > $filename.num_rows
      
      rclone copy $filename.num_rows s3allas:$bucketname
      ```

   2. Replace `<project_number>_$USER` to match your bucket name and `<filename>`
   to the name of the file you have in Allas. Remember to also define your
   billing project (`--account`).

   💡 If you're running multiple batch jobs across different projects at the
   same time, use the project-specific endpoint (`s3allas-project_<id>:`)
   instead of `s3allas:` to avoid a later `allas-conf` run changing which
   project your job's `rclone` commands point to.

6. Submit the batch job with the command:

   ```bash
   sbatch allas_job.sh
   ```

7.  Monitor the progress of your batch job:

    ```bash
    squeue -u $USER
    a-list <project_number>_$USER    # replace <project_number> with your CSC project number, e.g. 2001234, to match your bucket
    ```

## Using the legacy Swift protocol

☝🏻 Roihu defaults to S3, so the steps above are the recommended approach for
most users. Use this section only if you specifically need Swift, e.g. to
access multiple projects within the same eight-hour session.

💬 The `allas-conf --swift` command opens a Swift-based Allas connection that
is valid for eight hours. In interactive use this is not a problem, since
`allas-conf` can simply be run again to extend the connection. In batch jobs,
however, the job may still be queuing or running once the connection expires.

1. Load the Allas module and open a Swift connection with the `-k` option:

   ```bash
   module load allas
   allas-conf --swift -k
   ```

   - The `-k` option stores your password in the environment variable
     `$OS_PASSWORD`. With this variable defined, you no longer need to input
     your password when you re-execute `allas-conf` with the `-k` option and
     the Allas project name.

   ☝🏻 Note that if you mistype your password when using the `-k` option, you
   must use the command `unset OS_PASSWORD` before you can try again.

2. Refresh the connection with the command:

   ```bash
   allas-conf --swift -k <project>  # replace <project> with your CSC project, e.g. project_2001234
   ```

   ☝🏻 When `$OS_PASSWORD` is set, the `a-commands` (`a-put`, `a-get`, `a-list`,
   `a-delete`) automatically refresh the Allas connection when the commands
   are executed in a batch job, so the **Option 1: `a-commands`** batch
   script above works with Swift as-is, once the connection has been opened
   this way.

3. If you use `rclone` instead of the `a-commands`, you need to explicitly
   refresh the Swift connection inside the batch script itself, since the
   `$OS_PASSWORD` auto-refresh only applies to `a-commands`:

   ```bash
   #!/bin/bash
   #SBATCH --job-name=my_allas_job          # Name of the job visible in the queue.
   #SBATCH --account=<project>              # Choose the billing project. Has to be defined!
   #SBATCH --time=00:05:00                  # Maximum duration of the job. Max: depends of the partition. 
   #SBATCH --mem-per-cpu=1G                 # How much RAM is reserved for one processor.
   #SBATCH --partition=test                 # Job queues (CPU): interactive, test, small, medium, large, longrun, hugemem, hugemem_longrun
   #SBATCH --output=allas_output_%j.txt     # Name of the output-file.
   #SBATCH --error=allas_errors_%j.txt      # Name of the error-file.
   
   bucketname=<project_number>_$USER        # Replace with your bucket name, e.g. 2001234_username
   filename=<filename>                      # Replace with your file name
   
   # Make sure the connection to Allas is open
   source /appl/soft/manual/general/common/allas/allas-cli-utils/allas_conf --swift -f -k $OS_PROJECT_NAME
   rclone copy allas:$bucketname/$filename ./
   
   wc -l $filename > $filename.num_rows
   
   # Make sure the connection to Allas is open
   source /appl/soft/manual/general/common/allas/allas-cli-utils/allas_conf --swift -f -k $OS_PROJECT_NAME
   rclone copy $filename.num_rows allas:$bucketname
   ```

   💡 Note that the Swift-configured `rclone` remote is named `allas:`, not
   `s3allas:` (which is reserved for the S3 connection).

## More information

- Docs CSC: [Using Allas in batch jobs](https://docs.csc.fi/data/Allas/allas_batchjobs/)
