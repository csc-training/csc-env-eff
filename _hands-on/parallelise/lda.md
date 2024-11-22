---
topic: installing
title: Exercise - Fetch text in VRT format and do topic modeling
---

<!-- | 💬    | General instructions or description | -->
<!-- | 💭    | Provide extra information or insight | -->
<!-- | 💡    | Valuable information, ideas or suggestions | -->
<!-- | ☝🏻    | Notice or a side-note | -->
<!-- | ‼️ Important information    -->

# Exercise - Fetch text in VRT format and do topic modeling

💬 In this exercise we will experiment with a common task for text, topic modeling. You can go through the tutorial step by step and do all the exercises, or just read it. The exercises are in the form of Python code that you can edit to make it run faster. Solutions are included.

## A processing node and workspaces

☝🏻 First, hop into an interacive computing node with `sinteractive --time 08:00:00 --mem 32000 --cores 4`, it will prompt you to select a CSC project. `--time 08:00:00` means that the node will kick you out after 8 hours. If you exit the node before then, you will save on billing units; the reservation is more for scheduling than billing purposes. `--mem 32000` means 32000 megabytes, and `--cores 4` means you will be able to run that many processes simultaneously (for this small example).

We will organise workspaces as follows: data archives, which we don't want to download many times, go to a non-temporary location, like `/scratch/<project>/<your_username>/`. The same with dependencies and code. But we'll unpack data into `$TMPDIR`. The reason for this is that `$TMPDIR` will be a disk local to the computing node, so it will be fast for reading and writing. In this particular case with just a few files it barely matters, but it's a good habit to learn.

For dependencies and code, making a directory for this under `/scratch/<project>/<your_username>` is a good choice, since we're just trying things out. You can make sure that this directory exists with `mkdir -p /scratch/<project>/$USER`. In that directory, fetch some starter code into a new directory with `wget https://a3s.fi/hardwick-clarin-pub/lda.zip; unzip lda.zip` (assuming you don't already have a directory called `lda`. Then `cd lda` into the directory. This will be our workspace. The Python scripts ending with `_solution.py` contain solutions to the exercises.

## Dependencies

☝🏻 We need to install some dependencies. This can be done in many ways, some simpler than others, and some more efficient than others.

There are essentially three alternatives for installing Python dependencies:

1) Installing them in your home directory with `pip install --user`. This quickly becomes unmaintainable with many projects and library versions.
2) Installing in a virtual environment with `venv` or `conda`. This has some downsides on the HPC systems, causing slow startup times and unnecessary IO load on the whole system.
3) An Apptainer container, for which we have our custom tool `tykky`, which is usually the ideal option.

If you have a `requirements.txt` file, as we do here, installing them into a `tykky` environment is in principle simple, as long as your libraries support the default Python version, which at the time of writing is 3.6. Unfortunately, that's too old for us, so we'll first make a temporary `venv` in which to build the `tykky` container with python3.9. So we do:

```bash
$ mkdir tykky-env                                                                                 # the tykky environment will go here
$ python3.9 -m venv tmp-venv                                                                      # create a temporary venv with the correct Python version
$ source tmp-venv/bin/activate                                                                    # step into the venv
$ module load tykky                                                                               # load the tykky module
$ pip-containerize new --prefix /scratch/<project>/$USER/lda requirements.txt                     # or whatever directory you chose
$ deactivate                                                                                      # exit the temporary venv
$ rm -rf tmp-venv                                                                                 # not needed anymore
$ export PATH="/scratch/<project>/$USER/csc-training/lda/tykky-env/bin:$PATH"                     # make the tykky environment visible
```

For the rest of this session, your default Python environment will have the packages from `requirements.txt` installed. After logging out, things will be back to the way they were before. Then you can `export PATH` again, or set the path on every login in eg. `.bash_profile`.

## Data

The Language Bank of Finland keeps its analyzed text data in a format called [VRT](https://www.kielipankki.fi/development/korp/corpus-input-format/). VRT is used because it's the format of the [IMG Open Corpus Workbench](http://cwb.sourceforge.net/) (CWB), so it's not exactly a common standard, but it's easy enough to use for many purposes. We will fetch some VRT files, extract the lemmas, and use the lemmas as input to a topic modeling package.

The Language Bank maintains a [directory of corpora](https://www.kielipankki.fi/corpora/) which you can browse for corpora available to you. Each corpus is listed with license information: PUB means available to everyone, ACA means available for users affiliated with an academic institution, RES means you have to apply for access.

💡 If you are a member of the `kieli` group on `puhti`, you can find read-only VRT data under `/appl/data/kielipankki/`. Otherwise, you can follow download links from the corpus directory.

The rest of this example will use the YLE news in Finnish corpus, which can be downloaded [here](https://korp.csc.fi/download/YLE/fi/2011-2018-s-vrt/).

```bash
$ wget https://korp.csc.fi/download/YLE/fi/2019-2021-s-vrt/ylenews-fi-2019-2021-s-vrt.zip

$ unzip ylenews-fi-2019-2021-s-vrt.zip -d $TMPDIR
   creating: /local_scratch/<username>/ylenews-fi-2019-2021-s-vrt/
   ...
```

We should now have three VRT files under `ylenews-fi-2019-2021-s-vrt/vrt` of roughly two gigabytes each.

### Data format

💭 Let's take a quick look at the files so we have some idea of what we're dealing with:

```bash
$ head $TMPDIR/ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2019_s.vrt 
<!-- #vrt positional-attributes: word ref lemma lemmacomp pos msd dephead deprel lex/ -->
<!-- #vrt info: VRT generated from CWB data for corpus "ylenews_fi_2019_s" (2022-08-24 11:38:39 +0300) -->
<!-- #vrt info: A processing log at the end of file -->
<text datetime_content_modified="2018-12-31T23:46:26+0200" datetime_json_modified="2020-09-23T12:41:54+0300" datetime_published="2018-12-31T23:46:26+0200" datefrom="20181231" dateto="20181231" departments="|Näkökulmat|" id="20-280865" main_department="Näkökulmat" publisher="yle-aihe" timefrom="234626" timeto="234626" url="https://yle.fi/aihe/artikkeli/2018/12/31/matkakertomuksia-osa-vi-v-tilanne-verhon-edessa-osa-a">
<sentence id="1" type="text" paragraph_type="text">
Kun	1	kun	kun	C	SUBCAT_CS|CASECHANGE_Up	2	mark	|kun..kn.1|
käännyin	2	kääntyä	kääntyä	V	PRS_Sg1|VOICE_Act|TENSE_Prt|MOOD_Ind	5	advcl	|kääntyä..vb.1|
katsomaan	3	katsoa	katsoa	V	NUM_Sg|CASE_Ill|VOICE_Act|INF_Inf3	2	xcomp	|katsoa..vb.1|
,	4	,	,	Punct	_	2	punct	|,..xx.1|
huomasin	5	huomata	huomata	V	PRS_Sg1|VOICE_Act|TENSE_Prt|MOOD_Ind	0	ROOT	|huomata..vb.1|
```

VRT is a pseudo-xml format. By pseudo I mean that it doesn't have a root node, but is instead a sequence of `text` elements. (There are some other differences but that's not important right now.) The leaf nodes which contain text (here, `sentence`), have one token per line, with fields separated by tabs. So it's a TSV (tab-separated values) format inside an XML-like format. The first line indicates what the fields mean; the first one is `word`, for word form, the second is `ref`, for token number, `lemma` for lemma and so on.

💭 You may notice that the `text` element has some interesting attributes, like `departments`, `main_department` and `publisher`. Unfortunately the `main_department` is usually empty (the commands are `unix` tools available on every system):

```bash
$ grep --only-matching 'main_department="[^"]*' $TMPDIR/ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2019_s.vrt | sed 's/main_department="//' | sort | uniq -c | sort -nr
  62104 
    319 Yle TV1
    263 Klassinen
    184 Yleisradio
    164 Luonto
    160 Strömsö
    160 Kulttuuricocktail
...
```

The `publisher` never is:

```bash
$ grep --only-matching 'publisher="[^"]*' $TMPDIR/ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2019_s.vrt | sed 's/publisher="//' | sort | uniq -c | sort -nr
  38110 Yle Uutiset
  14104 Yle Urheilu
   8882 Yle Uutiset - lyhyet
   1301 yle-aihe
...
```
The attributes come from the data source, and there's no general rule as to what you can rely on. Clearly here `publisher` is somewhat meaningful and very reliable, `main_department` has more detail, but is very sparse (perhaps we could fill it in ourselves!).

## Data processing

💬 Moving on, we can try to run `parse_vrt.py`, which by default builds lists of lemmas of each text, and then does nothing with them. It should look something like this:

```bash
$ python3 parse_vrt.py $TMPDIR/ylenews-fi-2019-2021-s-vrt/vrt
Running parse_vrt_in_dir...
  Reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2019_s.vrt
  Finished reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2019_s.vrt, 65811 texts and 25772447 tokens
  Reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2020_s.vrt
  Finished reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2020_s.vrt, 63004 texts and 27871609 tokens
  Reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2021_s.vrt
  Finished reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2021_s.vrt, 56543 texts and 25374938 tokens
...finished in 136.04 s
```

### First task

☝🏻 Your first task, should you choose to accept it, is to replace the sequential processing of VRT files in `parse_vrt.py` with parallel processing, and then verify that you are able to accomplish this step faster with parallel than sequential processing.

<details><summary>Hint 1</summary>

There are several files to read and process, so you can process different files separately and combine the results afterwards.

</details>

<details><summary>Hint 2</summary>

The standard library module `multiprocessing` has helpful facilities for this, such as `multiprocessing.Pool`, which can be used to `map` inputs to outputs in parallel.

</details>

<details><summary>

One possible solution for this is included in `parse_vrt_solution.py`, or you can expand this line to see some code.
</summary>

In `parse.vrt`:
```python
    # Exercise 1: parallelise parsing the corpora
    # Hint: you can use the Python standard library for this
    retval = []
    for filename in os.listdir(dirname):
        if not filename.endswith('.vrt'):
            continue
        retval += vrt2lemmalists(os.path.join(dirname, filename))
```

Solution:
```python
    # Exercise 1 solution (one possible one): we map each filename to a
    # vrt2lemmalists call using multiprocessing.Pool
    from multiprocessing import Pool
    retval = []
    # First we get the valid file names
    filenames = [os.path.join(dirname, filename) for filename in os.listdir(dirname) if filename.endswith('.vrt')]
    # Then we initialize a Pool object
    with Pool() as pool: # by default, processes = number of cores
        for result in pool.map(vrt2lemmalists, filenames):
        # We add the result lists together
        retval += result
```

This should run in 50-60 seconds instead of 130-140 seconds.
</details>

## Topic modelling

💬 Next we will use `gensim` to do some topic modeling. The Python script `topics.py` uses `parse_vrt.py` to get data, and processes it in various ways. Try running it with the same argument:

```bash
$ python3 topics.py $TMPDIR/ylenews-fi-2019-2021-s-vrt/vrt
Running parse_vrt_in_dir...
  Reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2019_s.vrt
  Finished reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2019_s.vrt, 65811 texts and 25772447 tokens
  Reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2020_s.vrt
  Finished reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2020_s.vrt, 63004 texts and 27871609 tokens
  Reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2021_s.vrt
  Finished reading ylenews-fi-2019-2021-s-vrt/vrt/ylenews_fi_2021_s.vrt, 56543 texts and 25374938 tokens
...finished in 133.57 s
Building gensim dictionary... Done in 21.49 s
Computing BOW corpus... Done in 14.11 s
Computing LDA model... Done in 114.99 s
Computing model coherence... 
  Coherence with 10 topics was -1.8115932174225207
Done in 1.53 s
[topic printout]
```

After the one step from the previous section, we have added three more sections. All of them can be parallelised, but not all of them offer the same potential. If you are interested in parallelising code, they are all interesting examples, but the most important practical skill is to recognise at this point that these steps represent 47%, 7%, 5% and 41% of the runtime respectively, so that is the ceiling to how much can be accomplished by speeding them up. It is also often the case that relatively fast tasks also have relatively little to gain from parallelisation. We will tackle them in reverse order, from most to least useful.

### Second task

☝🏻 Replace the LdaModel class with something else to accomplish the same result, but quicker.

<details><summary>Hint 1</summary>

Go to the `gensim` [API reference](https://radimrehurek.com/gensim/apiref.html) and search the page for "models.lda".
</details>

<details><summary>Hint 2</summary>

Try the `gensim.models.LdaMulticore` class.
</details>

<details><summary>Solution</summary>

Change this:
```python
lda = gensim.models.LdaModel(bow_corpus, num_topics = n_topics)
```
To this:
```python
lda = gensim.models.LdaMulticore(bow_corpus, num_topics = n_topics, workers = n_workers)
```
</details>

### Third Task

☝🏻 Parallelise computing the BOW corpus. This means replacing the texts (or in this case, lists of lemmas) with bag-of-words representations. Each text will undergo the same transformation, so this should be possible to parallelise.

<details><summary>Hint 1</summary>

You can use `multiprocessing.Pool.map` like in the first exercise, but in an even simpler way: the result is simply the map.
</details>

<details><summary>Solution</summary>

Change this:
```python
bow_corpus = [dictionary.doc2bow(text) for text in corpus_lemmalists]
```
To this:
```python
with Pool(processes = n_workers) as pool:
    bow_corpus = pool.map(dictionary.doc2bow, corpus_lemmalists)
```

This doesn't really save any processing time, due to communication overhead being similar to the processing time. You can experiment with values of `n_workers` and `chunk_size`, an argument to `map()`.
</details>

### Fourth task

☝🏻 Parallelise computing the `gensim` dictionary.    This exercise is the trickiest one, and least useful to implement.

<details><summary>Hint 1</summary>

The `Dictionary` object has a method .merge_with(other), which we can use to turn a collection of dictionaries into one. But to do this we also need to split the source data, which is a list, into sublists.
</details>

<details><summary>Hint 2</summary>

You can make sublists with a generator comprehension like this:
```python
def split_list(l, n):
    return (l[i:i+n] for i in range(0, len(l), n))
```
</details>

<details><summary>Solution</summary>

```python
def split_list(l, n):
    return (l[i:i+n] for i in range(0, len(l), n))

dictionary = None
with Pool(processes = n_workers) as pool:
    for sub_dictionary in pool.map(gensim.corpora.Dictionary,
                                   split_list(corpus_lemmalists, 5000)):
        if dictionary is None:
            dictionary = sub_dictionary
        else:
            dictionary.merge_with(sub_dictionary)
```
</details>

## Finally

We have focused on getting dependencies installed on CSC's HPC systems and on parallelism, but of course there are more general things that could be done to speed up a process like this. If a system like this is run many times with a lot of data, data preprocessing need not be done at every step. You can do it once and use that result as a cache. Later steps depend on earlier steps, so you could set up a Makefile-like system to only redo steps that have changed or depend on those changes. The more times something is run, the more it pays to optimize it.
