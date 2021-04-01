---
topic: Batch jobs
title: Exercise - Retrieving data from the net
---

# Exercise: Retrieving data from the net

These exercises cover retrieving data from various commonly used 
bio data repositories.

We will do these exercises using the [sinteractive](https://docs.csc.fi/computing/running/interactive-usage/)
command (substitute xxxx with correct project number):
```text
sinteractive --account project_xxxxx
```
To use the applications in exercises2 and 3, we will need to load 
the biokit module:
```text
module load biokit
```
Move to `/scratch` directory area of the course project (substitute
xxxx with correct project number):
```text
cd /scratch/project_xxxx
```
Create a directory for yourself and move to it:
```text
mkdir $USER
cd $USER
```
Everyone in the project shares the same `/scratch` directory, so
it is a good idea to use subdirectories for each user and task, so 
you won't accidentally delete or overwrite each others files.

In normal usage it may be a good idea to even use `chmod` command 
to alter file access rights so that only you have write access to
your own subfolder, but please do not do this in the course project, 
as it would make clean-up after course harder.

You can find more information about this in [Disk areas](https://docs.csc.fi/computing/disk/)
page in the Docs.

## 1. Downloading data with curl

`Curl` and `wget` are general tools to download data from an URL.

Download a dataset from internet using `curl` and uncompress it. The 
dataset contains some *Pythium* genomes with  related BWA indexes.
```text
curl https://a3s.fi/course_12.11.2019/pythium.tgz > pythium.tgz
ls -ltr
tar zxvf pythium.tgz  
ls -ltr
tree pythium
```

## 2. Downloading data with NCBI edirect

Create directory `cellulose_synthase` and move to this new directory:
```text
mkdir cellulose_synthase
cd cellulose_synthase
```
Next we use [NCBI edirect tool](https://docs.csc.fi/apps/edirect/) 
to retrieve some data.

Check how many proteins are found the NCBI protein databanks for 
*Pythium* species (`count` row in the results):
```text
esearch -db protein -query "Pythium [ORGN]" 
```
Then check the nuber of proteins: cellulose synthase 1, cellulose 
synthase 2 and cellulose synthase 3 that are found for Pythium species.

For cellulose synthase 1 this can be done with:
```text
esearch -db protein -query "Pythium [ORGN] AND cellulose synthase 1 [PROT]"
```
do the same for the other proteins.

Retrive the cellulose synthase 3 sequenses in Fasta format
```text
esearch -db protein -query "Pythium [ORGN] AND cellulose synthase 3 [PROT]" | efetch -format fasta > cesy3.fasta
```
Then run esearch command that tells how many  cellulose synthase 3 
sequences there are in total in NCBI protein database?

### Extra exercises for the fast ones: Align the cellulose synthase 3 set with mafft
```text
mafft cesy3.fasta > cesy3_aln.fasta
```
And study the results:
```text
infoalign cesy3_aln.fasta
showalign cesy3_aln.fasta
```

## 3. Downloading with enaDataGet

Check the options of enaDataGet with command:
```text
enaDataGet -h
```
Download a file (Pythium iwayamai  genome assembly)
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
Then compare the cellulose synthase 3 sequences against the genome using BLAST
```text
pb tblastn -query cesy3.fasta -dbnuc AKYA02.fasta -out blast_result.txt
```

 
