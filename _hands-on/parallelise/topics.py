# Comments beginning with "Exercise" mark places to edit the code

import gensim
import os
import sys
import time
from parse_vrt import parse_vrt_in_dir

n_topics = 10

processed_corpus = []
dirname = sys.argv[1]

start_time = time.time()
sys.stderr.write(f"Running parse_vrt_in_dir...\n");
corpus_lemmalists = parse_vrt_in_dir(dirname)
sys.stderr.write(
    f"...finished in {time.time() - start_time:.2f} s\n")

sys.stderr.write("Building gensim dictionary... "); sys.stderr.flush()
start_time = time.time()

# Exercise 4: Parallelise building the dictionary
# Hint: the dictionary has a merge_with(other) method
dictionary = gensim.corpora.Dictionary(corpus_lemmalists)
sys.stderr.write(f"Done in {time.time() - start_time:.2f} s\n")
sys.stderr.write("Computing BOW corpus... "); sys.stderr.flush()
start_time = time.time()

# Exercise 3: Parallelise computing bow_corpus
# Hint: send the corpus in suitable-sized chunks to processes that map
# the corpus with the function dictionary.doc2bow
bow_corpus = [dictionary.doc2bow(text) for text in corpus_lemmalists]
sys.stderr.write(f"Done in {time.time() - start_time:.2f} s\n")
sys.stderr.write("Computing LDA model... "); sys.stderr.flush()
start_time = time.time()

# Exercise 2: replace LdaModel with a parallel version
# Hint: you can simply replace the model name, but do look at the API,
# choose a number of processes, and test which one works best. Warning:
# memory consumption will grow with number of processes, it's possible to run
# out if you have a lot of cores!
lda = gensim.models.LdaModel(bow_corpus, num_topics = n_topics)
sys.stderr.write(f"Done in {time.time() - start_time:.2f} s\n")

sys.stderr.write("Computing model coherence... \n")
start_time = time.time()
cm = gensim.models.coherencemodel.CoherenceModel(
    model=lda, corpus=bow_corpus, dictionary=dictionary, coherence='u_mass')
print(f"  Coherence with {n_topics} topics was {cm.get_coherence()}")
sys.stderr.write(f"Done in {time.time() - start_time:.2f} s\n")

for topic in enumerate(lda.show_topics(num_topics = n_topics,
                                       num_words = 10,
                                       formatted = False)):
    print(f"Topic {topic[0] + 1}:")
    for word, probability in topic[1][1]:
        print("  " + dictionary[int(word)])
