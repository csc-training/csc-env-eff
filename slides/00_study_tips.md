---
theme: csc-2019
lang: en
---
# Study tips and problem solving {.title}

# Using these materials

- The material is organized by topics in increasing complexity
   - Feel free to jump if you know the basics already
- Read the slides / watch the video (to appear) first
- Complete the tutorial to make sure you've got the steps right
- Try out one or more of the exercises to verify your new skill
- If you get stuck, consult [the docs](https://docs.csc.fi) linked to the topic slides
- Press *ctrl* to open additional information links to a new window

# General problem solving

1. Try looking in [docs.csc.fi](https://docs.csc.fi) in the right section in the *hierarchy*
2. Try in the [FAQ](https://docs.csc.fi/support/faq/)
3. Try the search in docs or google for it
   - Start typing a keyword in docs, Copy/paste the error message in google
4. Send an email to [servicedesk@csc.fi](mailto:servicedesk@csc.fi) containing:
   - A descriptive title
   - What you wanted to achieve, and on which which computer
   - Which commands you had given
   - What error messages resulted
   - [More tips to help us quickly solve your issue](https://docs.csc.fi/support/support-howto/)

# Running a new application in Puhti 1/2

- If it comes with tutorials, do at least one
   - This will likely be the fastest way forward
   - Naturally, read the manual / instructions
- Check if there's a page for it in [docs CSC](https://docs.csc.fi/apps/)
   - If there is, use the batch script example from _there_
   - Otherwise, use a general template
- Try first running interactively (**not** in login node)
   - Perhaps easier to find the correct command line options
   - Use `top` command to get rough estimate on memory use etc.
   - If developers provide some test or example data, run it first and make sure results are correct

# Running a new application in Puhti 2/2

- You can use *test* queue to check your batch job script correctness
   - Limits : 15 min, 2 nodes
   - Job turnaround usually very fast even if machine "full"
   - Can be useful to spot typos, missing files etc. before submitting a job that will spend long in the queue
- Before large runs, it’s a good idea to do a smaller trial run
   - Check that results are as expected
   - Check resource usage after test run and adjust accordingly
- How many cores to allocate?
   - This depends on many things so you must try, see our [instructions on a scaling test](https://docs.csc.fi/support/tutorials/cmdline-handson/#scaling-test-for-an-mpi-parallel-job)


# What if your job fails? Troubleshooting checklist 1/2

   1. Did the job run out of time?
   2. Did the job run out of memory?
   3. Did the job actually use resources you specified?
      * Problems in batch job script can cause parameters to be ignored and default values are used instead
   4. Did it fail immediately or did it run for some time?
      * Jobs failing immediately are often due to something simple like typos in command line, missing inputs, bad parameters etc.

# What if your job fails? Troubleshooting checklist 2/2

   5. Check the error file captured by batch job script
   6. Check any other error files and logs the program may have produced
   7. Error messaged can sometimes be long, cryptic and a bit intimidating, but ...
      * Try skimming through them and see if you can spot something ”human readable”  instead of ”nerd readable”
      * Often you can spot the actual problem easily if you go through the whole message. Something like ”required input file so-and-so missing” or ”parameter X out of range” etc.
   8. Consult the [FAQ on common Slurm issues](https://docs.csc.fi/support/faq/why-does-my-batch-job-fail/) in docs.csc.fi

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
   - `bash` history is nice, but keeps also the ones that didn't work...
   - Note, don't overwrite your vault file (_e.g._ with `cat > $HOME/vault`)
- Store scripts in `$HOME/bin` and take backups
