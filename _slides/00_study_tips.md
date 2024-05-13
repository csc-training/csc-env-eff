---
theme: csc-eurocc-2019
lang: en
---
# Study tips and problem solving {.title}

How to use the material and how to solve common problems.

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

# Using these materials

- The material is organized by topics of increasing complexity
   - Feel free to jump if you know the basics already
- Read the slides / watch the videos first
- Complete the tutorials to make sure you've got the steps right
- Try out one or more of the exercises to verify your new skills
- If you get stuck, consult [Docs CSC](https://docs.csc.fi) linked to the topic slides
- Press `shift` to open links with additional information in a new window
- Left-click on slides and you can then navigate them with the arrow keys

# General problem solving

1. Go to [docs.csc.fi](https://docs.csc.fi) and check in the right section in the _navigation_
2. Try the [FAQ](https://docs.csc.fi/support/faq/)
3. Try the search function in CSC Docs or search the web
   - Type a keyword in CSC Docs, copy/paste the error message in your favorite search engine
4. Send an email to [servicedesk@csc.fi](mailto:servicedesk@csc.fi) containing:
   - A descriptive title
   - What you wanted to achieve and on which which computer
   - Which commands you have given
   - What error messages resulted
   - [More tips to help us quickly solve your issue](https://docs.csc.fi/support/support-howto/)

# Running a new application in Puhti 1/2

- If it comes with tutorials, do at least one
   - This will likely be the fastest way forward
   - Naturally, read the manual/instructions
- Check if there's a page about it in [Docs CSC](https://docs.csc.fi/apps/)
   - If there is, use the batch script example from _there_
   - Otherwise, use a [general template](https://docs.csc.fi/computing/running/example-job-scripts-puhti/)
- Try first running interactively (**not** on a login node)
   - Perhaps it is easier to find the correct command line options
   - Use the `top` command to get rough estimate of memory use, _etc_.
   - If developers provide some test or example data, run it first and make sure results are correct

# Running a new application in Puhti 2/2

- You can use the _test_ queue to check that your batch job script is correct
   - Limits : 15 min, 2 nodes
   - Job turnaround usually very fast even if machine is "full"
   - Can be useful to spot typos, missing files, _etc_. before submitting a job that will idle in the queue
- Before large runs, it's a good idea to do a smaller trial run
   - Check that results are as expected
   - Check the resource usage after the test run and adjust accordingly
- How many cores to allocate?
   - This depends on many things, so you have to try, see our [instructions about a scaling test](https://docs.csc.fi/support/tutorials/cmdline-handson/#scaling-test-for-an-mpi-parallel-job)

# What if your job fails? Troubleshooting checklist 1/2

1. Did the job run out of time?
2. Did the job run out of memory?
3. Did the job actually use the resources you specified?
   - Problems in the batch job script can cause parameters to be ignored and default values are used instead
4. Did it fail immediately or did it run for some time?
   - Jobs failing immediately are often due to something simple like typos, missing inputs, bad parameters, _etc_.

# What if your job fails? Troubleshooting checklist 2/2

5. Check the error file captured by the batch job script
6. Check any other error files and logs the your program may have produced
7. Error messaged can sometimes be long, cryptic and a bit intimidating, but ...
   - Try skimming through them and see if you can spot something "human-readable"
   - Often you can spot the actual problem easily if you go through the whole message. Something like "required input file so-and-so missing" or "parameter X out of range", _etc_.
8. Consult the [FAQ on common Slurm issues](https://docs.csc.fi/support/faq/why-does-my-batch-job-fail/) in the CSC Docs

# Document your discoveries

- When you've successfully solved an issue, make it easy to rediscover it
- Set up a file in your `$HOME` and add your commands there
   - It's quick to copy/paste from the screen to the end of the file

```bash
cat >> $HOME/vault
<copy/paste>
Ctrl-C
```

- ... and finding _them_ with `grep` later is quick (`grep them $HOME/vault`)
   - `bash` history is nice, but it keeps also the commands that didn't work...
   - Note, don't overwrite your vault file (_e.g._, with `cat > $HOME/vault`)
- Store scripts in `$HOME/bin` and take backups
