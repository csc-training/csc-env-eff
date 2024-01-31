---
layout: default
title: Finding where you have lots of data
parent: 3. Disk areas
grand_parent: Part 1
nav_order: 2
has_children: false
has_toc: false
permalink: /hands-on/disk-areas/disk-areas-tutorial-lue.html
---
# Where do I have a lot of data?

> In this tutorial you
   - Familiarize yourself with efficient ways to check where you have a lot of files and data on Puhti.

💬 CSC has developed a tool called [LUE](https://docs.csc.fi/support/tutorials/lue/) for keeping track of much data/files one has on the disk. Conventional tools such as `stat` or `du` are slow and heavy on the parallel file system, while `lue` is significantly faster. This comes with a slight loss in accuracy, although this is usually not a problem. See [Docs CSC](https://docs.csc.fi/support/tutorials/lue/#short-prelude) for a list of possible caveats.

☝🏻 Keeping track of how much data/files one has on the disk and (re)moving it in a timely manner (e.g. to [Allas](https://docs.csc.fi/data/Allas/)) is very important to ensure a more performant file system for all users.

## Querying where you have a lot of files and data

1. On Puhti, start by loading the `lue` module:

```bash
module load lue
```

{:style="counter-reset:step-counter 1"}
2. Check out the different available options with:

```bash
lue --help
```

{:style="counter-reset:step-counter 2"}
3. See how much data you have in your `$HOME` directory (i.e. `/users/$USER`):

```bash
lue $HOME
```

💡 You can also try some other directory e.g. in your project's `/scratch`. However, **don't run the tool on the whole project folder** (e.g. `/scratch/project_2001234`), but choose instead a smaller subdirectory where you think you might have a lot of files or data. Some operations can be both slow and heavy on the file system! By default, the tool will only fetch size data for 30 mins before quitting. Alternatively, you can [limit the runtime of the tool as instructed in Docs CSC](https://docs.csc.fi/support/tutorials/lue/#limiting-the-runtime).

{:style="counter-reset:step-counter 3"}
4. The first lines of the output should look like:

```text
Rerunning find for /users/$USER
Total size: 922595190 Processed files: 14036 Permission denied: 0 Missing size: 2, Other err: 0
path, total size, in dir size, % of total, % of dir
---------------------------------------------------
/users/$USER        910MB  384KB 100.0 100.0
...
```

{:style="counter-reset:step-counter 4"}
5. You can see the total number of files in the directory on the second line after `Processed files` and a breakdown of the subdirectory sizes in the following table. How many files do you have in total in your `$HOME`? Which directory is the largest in size?
6. Rerun `lue` with the `--count` flag to display the number of files in each directory instead of the size. Which directory in `$HOME` contains most files?

```bash
lue --count $HOME
```

💡 To get more detailed information, use the `--display-level=<n>` flag to show a deeper directory hierarchy. Alternatively, rerun the query for individual subdirectories.

☝🏻 LUE stores a very simple cache of runs in `$TMPDIR`. This means that you can run a query on any subdirectories without actually re-querying anything from the file system. To rerun the query from scratch, add the flag `--refresh`. This might be needed to get a more accurate estimate of the file count e.g. if the cache file is old.

## More information

💡 See Docs CSC for more information about [managing data on Puhti and Mahti `/scratch` disks](https://docs.csc.fi/support/tutorials/clean-up-data/) and [using LUE](https://docs.csc.fi/support/tutorials/lue/) (e.g. how to fix `NOSIZE`/`NOPERM` errors).
