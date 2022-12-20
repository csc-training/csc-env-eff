---
topic: Batch jobs
title: Exercise - Retrieving data from bio data repositories (advanced)
---

# Exercise: Retrieving data from bio repositories

> These exercises cover retrieving data from various commonly used bio data repositories.

- We will do these exercises using the [sinteractive](https://docs.csc.fi/computing/running/interactive-usage/) command:

```text
sinteractive --account project_xxxx   # replace xxxx with your project number
```

- To use the applications in steps 2 and 3, we will need to load the biokit module:

```text
module load biokit
```

- Move to `/scratch` directory area of your project (unless there already):

```text
cd /scratch/project_xxxx   # replace xxxx with your project number
```

- Create a directory for yourself and move to it (unless there already):

```text
mkdir $USER
cd $USER
```

💭 Everyone in a project shares the same `/scratch` directory, so
it is a good idea to use subdirectories for each user and task, so 
you won't accidentally delete or overwrite each others files.

🗯 In normal usage it may be a good idea to even use `chmod` command 
to alter file access rights so that only you have write access to
your own subfolder, but please do not do this if you are using a CSC course project,
as it would make clean-up after the course harder.

- You can find more information about this in [Disk areas](https://docs.csc.fi/computing/disk/)
page in the Docs.

## 1. Downloading data with curl

- `curl` and `wget` are general tools to download data from an URL.

- Download a dataset from internet using `curl` and uncompress it. The dataset contains some *Pythium* genomes with related BWA indexes.

```text
curl https://a3s.fi/course_12.11.2019/pythium.tgz > pythium.tgz
ls -ltr
tar -zxvf pythium.tgz  
ls -ltr
```

## 2. Downloading data with NCBI edirect

- Create directory `cellulose_synthase` and move to this new directory:

```text
mkdir cellulose_synthase
cd cellulose_synthase
```

- Next we use [NCBI edirect tool](https://docs.csc.fi/apps/edirect/) to retrieve some data.

- Check how many proteins are found the NCBI protein databanks for *Pythium* species (`count` row in the results):

```text
esearch -db protein -query "Pythium [ORGN]" 
```
- Then check the number of proteins: **cellulose synthase 1**, **cellulose synthase 2** and **cellulose synthase 3** that are found for *Pythium* species.

- For cellulose synthase 1 this can be done with:

```text
esearch -db protein -query "Pythium [ORGN] AND cellulose synthase 1 [PROT]"
```

- Do the same for the other proteins.

- Retrive the cellulose synthase 3 sequenses in Fasta format

```text
esearch -db protein -query "Pythium [ORGN] AND cellulose synthase 3 [PROT]" | efetch -format fasta > cesy3.fasta
```

- Then run `esearch` command that tells how many **cellulose synthase 3** sequences there are in total in the NCBI protein database?

### Extra exercises for the fast ones: Align the cellulose synthase 3 set with mafft

```text
mafft cesy3.fasta > cesy3_aln.fasta
```

- And study the results:

```text
infoalign cesy3_aln.fasta
showalign cesy3_aln.fasta
```

## 3. Downloading with enaDataGet

- Check the options of enaDataGet with command:

```text
enaDataGet -h
```

- Download a file (Pythium iwayamai genome assembly)

```text
enaDataGet AKYA02000000 -f fasta
gunzip AKYA02.fasta.gz 
ls -ltr
```

### Extra exercise for the fast ones: study the downloaded file:

```text
head -20 AKYA02.fasta
tail AKYA02.fasta
infoseq_summary  AKYA02.fasta
```

- Then compare the cellulose synthase 3 sequences against the genome using BLAST

```text
pb tblastn -query cesy3.fasta -dbnuc AKYA02.fasta -out blast_result.txt
```
