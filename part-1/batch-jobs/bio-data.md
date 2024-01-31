---
layout: default
title: Retrieving data from bio data repositories
parent: 5. Batch queue system and interactive use
grand_parent: Part 1
nav_order: 4
has_children: false
has_toc: false
permalink: /hands-on/batch_jobs/exercise_retrieving-bio-data.html
---
# Exercise: Retrieving data from bio data repositories

> This exercise covers retrieving data from various commonly used bio data repositories.

1. We will do these exercises in an interactive session launched using the [sinteractive](https://docs.csc.fi/computing/running/interactive-usage/) command:

```bash
sinteractive --account <project>   # replace <project> with your CSC project, e.g. project_2001234
```

{:style="counter-reset:step-counter 1"}
2. Alternatively, open a compute node shell through the [Puhti web interface](https://www.puhti.csc.fi).
3. To access the applications in parts 2 and 3, we will need to load the `biokit` module:

```bash
module load biokit
```

{:style="counter-reset:step-counter 3"}
4. Create a directory for yourself under the `/scratch` directory of your project and move there:

```bash
mkdir -p /scratch/<project>/$USER   # replace <project> with your CSC project, e.g. project_2001234
cd /scratch/<project>/$USER         # replace <project> with your CSC project, e.g. project_2001234
```

💭 Everyone in a project shares the same `/scratch` directory, so it is a good idea to use subdirectories for each user and task to avoid accidentally deleting or overwriting others' files.

🗯 In normal usage it may be a good idea to use the `chmod` command to alter file access rights so that only you have write access to your own subfolder, but please do not do this if you are using a CSC course project, as it will make clean-up after the course harder.

💡 You can find more information about this on the [Disk areas page in Docs CSC](https://docs.csc.fi/computing/disk/).

## 1. Downloading data with `curl`

1. `curl` and `wget` are general tools to download data from an URL.
2. Download a dataset from internet using `curl` and uncompress it. The dataset contains some *Pythium* genomes with related BWA indexes.

```bash
curl https://a3s.fi/course_12.11.2019/pythium.tgz > pythium.tgz
ls
tar -zxvf pythium.tgz  
ls
```

## 2. Downloading data with NCBI edirect

1. Create directory `cellulose_synthase` and move to this new directory:

```bash
mkdir cellulose_synthase
cd cellulose_synthase
```

{:style="counter-reset:step-counter 1"}
2. Next we use the [NCBI edirect tool](https://docs.csc.fi/apps/edirect/) to retrieve some data.
3. Check how many proteins are found in the NCBI protein database for *Pythium* species (`count` row in the results):

```bash
esearch -db protein -query "Pythium [ORGN]" 
```

{:style="counter-reset:step-counter 3"}
4. Check the number of proteins for **cellulose synthase 1**, **cellulose synthase 2** and **cellulose synthase 3** that are found for *Pythium* species.
5. For cellulose synthase 1 this can be done with:

```bash
esearch -db protein -query "Pythium [ORGN] AND cellulose synthase 1 [PROT]"
```

{:style="counter-reset:step-counter 5"}
6. Do the same for the other proteins.
7. Retrieve the cellulose synthase 3 sequences in Fasta format

```bash
esearch -db protein -query "Pythium [ORGN] AND cellulose synthase 3 [PROT]" | efetch -format fasta > cesy3.fasta
```

{:style="counter-reset:step-counter 7"}
8. Run the `esearch` command that tells how many **cellulose synthase 3** sequences there are in total in the NCBI protein database?

### Extra exercise for fast ones

{:style="counter-reset:step-counter 8"}
9. Align the cellulose synthase 3 set with `mafft`

```bash
mafft cesy3.fasta > cesy3_aln.fasta
```

{:style="counter-reset:step-counter 9"}
10. Study the results:

```bash
infoalign cesy3_aln.fasta
showalign cesy3_aln.fasta
```

## 3. Downloading with enaDataGet

1. Check the options of `enaDataGet` with command:

```bash
enaDataGet -h
```

{:style="counter-reset:step-counter 1"}
2. Download a file (Pythium iwayamai genome assembly)

```bash
enaDataGet AKYA02000000 -f fasta
gunzip AKYA02.fasta.gz 
ls
```

### Extra exercise for fast ones

{:style="counter-reset:step-counter 2"}
3. Study the downloaded file:

```bash
head -20 AKYA02.fasta
tail AKYA02.fasta
infoseq_summary AKYA02.fasta
```

## 4. Finishing up

1. Close the interactive session when you are done by typing `exit`.
