---
theme: csc-2019
lang: en
---
# Study tips and problem solving {.title}

How to use the material and hot to solve the common problems.

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

:::info (speech)
This Lecture gives insructions on how to use the material and how to solve problems.
:::

# Using these materials

- The material is organized by topics in increasing complexity
   - Feel free to jump if you know the basics already
- Read the slides / watch the video (to appear) first
- Complete the tutorial to make sure you've got the steps right
- Try out one or more of the exercises to verify your new skill
- If you get stuck, consult [the docs](https://docs.csc.fi) linked to the topic slides
- Press *ctrl* to open additional information links to a new window
- Left-click on slides and you can then navigate them with arrow-keys

:::info (speech)
This is how the course material is organised.
The material involves slides, videos, hands-on tutorials and exercises.
The material often links to the documentation at docs.csc.fi.
These tips help you to navigate within the slides and other material.
:::

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

:::info (speech)
This is the general procedure of solving problems.
First try looking at the docs. 
The pages are organised hierarchically.
There is also a FAQ-section that covers many topics.
You might try the search button in the docs 
or googling the keywords or the error message.
If you can't find the answer, then send an email to servicedesk at csc.fi.
A descriptive title helps us direct the message to the right people.
Explain what you wanted to achieve and on which computer, what commands you gave, and what error messages resulted.
There is a rather detailed help specifying how to compose a good support request.
It will help us to solve your issue faster, and you will get more quickly to do the work.
:::

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

:::info (speech)
Some applications come with a tutorial.
Doing those will be the fastest way forward.
There are also instructions or documentation for installed applications.
The documentation sometimes contains application spesific batch scripts.
If they are not available, you may use the general batch script template.
You can try to run the application interactively.
Do not do this in the login node, but instead use for example sinteractive.
It is a one easy way to see that things are running correctly.
:::

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

:::info (speech)
You can also try to run the application in a test queue.
Usually the results come quickly.
It helps you to tweak your batch script before longer runs.
It is not nice to wait in a long queue - just to see that there is a typo in the script.

Always before you launch any big projects, you should run a small trial
to make sure, that the results are expected.
You may use the results to adjust the resource usage.
It benefits all users when the resources are used efficiently.
:::

# What if your job fails? Troubleshooting checklist 1/2

   1. Did the job run out of time?
   2. Did the job run out of memory?
   3. Did the job actually use resources you specified?
      * Problems in batch job script can cause parameters to be ignored and default values are used instead
   4. Did it fail immediately or did it run for some time?
      * Jobs failing immediately are often due to something simple like typos in command line, missing inputs, bad parameters etc.

:::info (speech)
If your job fails, you should first check for these issues.
Usually the job runs out of allocated time or memory.
If the job fails immediately, there is usually a typo in the script.
:::

# What if your job fails? Troubleshooting checklist 2/2

   5. Check the error file captured by batch job script
   6. Check any other error files and logs the program may have produced
   7. Error messaged can sometimes be long, cryptic and a bit intimidating, but ...
      * Try skimming through them and see if you can spot something ”human readable”  instead of ”nerd readable”
      * Often you can spot the actual problem easily if you go through the whole message. Something like ”required input file so-and-so missing” or ”parameter X out of range” etc.
   8. Consult the [FAQ on common Slurm issues](https://docs.csc.fi/support/faq/why-does-my-batch-job-fail/) in docs.csc.fi

:::info (speech)
The error files provide useful information on why the job failed.
Sometimes they may be difficult to interpret, but sometimes there is a clear answer.
If you have difficulties to understand the error file, please send us the error file, and we will take a look at that.
You may also look at the FAQ on common Slurm issues.
:::

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

:::info (speech)
When you have solved or discovered something, we recommend you document it for yourself - so that you can easily rediscover it later.
Here is one way to do it.
You can use cat command, to save text in a file - for example in your home folder.
After entering the first line, you can copy paste commands or other text - like a description.
Press control and C when you are finished typing.
You can use grep to look for content in that file.

Try the links in the slides, tutorials and video descriptions to discover relevant documentation or more content. We wish you happy learning!
:::
