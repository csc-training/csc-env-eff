import gensim
import os
import sys
import time
from parse_vrt_solution import parse_vrt_in_dir
from multiprocessing import Pool

processed_corpus = []
dirname = sys.argv[1]
n_workers = 4

corpus_lemmalists = parse_vrt_in_dir(dirname)

sys.stderr.write("Building gensim dictionary... "); sys.stderr.flush()
start_time = time.time()

# Solution to exercise 4: Parallelise computing the gensim dictionary
# In this case, we need to build one object (the dictionary) out of a
# collection of data. The object in question has a method .merge_with(other),
# which we can use to turn a collection of objects into one. But we also
# need to split the source data, which is a list, into sublists.

# Split a list into sublists of length n
# returns a generator, so we don't generate a whole new list with everything
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

dictionary = gensim.corpora.Dictionary(corpus_lemmalists)
sys.stderr.write(f"Done in {time.time() - start_time:.2f} s\n")
sys.stderr.write("Computing BOW corpus... "); sys.stderr.flush()
start_time = time.time()

# Solution to exercise 3: Parallelise computing bow_corpus
with Pool(processes = n_workers) as pool:
    bow_corpus = pool.map(dictionary.doc2bow, corpus_lemmalists)
sys.stderr.write(f"Done in {time.time() - start_time:.2f} s\n")

# Exercise 2: replace LdaModel with a parallel version
sys.stderr.write("Computing LDA model... "); sys.stderr.flush()
start_time = time.time()
# Workers should be number of physical cores, up to a limit. Good idea
# to test this if it's important.
lda = gensim.models.LdaMulticore(bow_corpus, num_topics = 10, workers = n_workers)
sys.stderr.write(f"Done in {time.time() - start_time:.2f} s\n")
for topic in enumerate(lda.show_topics(num_topics = 10,
                                       num_words = 10,
                                       formatted = False)):
    print(f"Topic {topic[0] + 1}:")
    for word, probability in topic[1][1]:
        print("  " + dictionary[int(word)])
