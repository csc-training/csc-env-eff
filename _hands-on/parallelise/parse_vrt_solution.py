import os
import sys
import time
from lxml import etree

# process-based parallelism
from multiprocessing import Pool

# a list of common semantically useless lemmas
stopwords = set([line.strip() for line in open('stopwords.txt')])

def is_content_word(lemma):
    return lemma.isalpha() and lemma not in stopwords

def parse_vrt_in_dir(dirname):
    '''
    Parse each file ending in .vrt in dirname in parallel, and return their concatenation.
    '''
    start_time = time.time()
    sys.stderr.write(f"Running parse_vrt_in_dir...\n");
    
    # Exercise 1 solution (one possible one): we map each filename to a
    # vrt2lemmalists call using multiprocessing.Pool
    retval = []
    # First we get the valid file names
    filenames = [os.path.join(dirname, filename) for filename in os.listdir(dirname) if filename.endswith('.vrt')]
    # Then we initialize a Pool object
    with Pool() as pool: # by default, processes = number of cores
        for result in pool.map(vrt2lemmalists, filenames):
            retval += result
    # How long did we take?
    sys.stderr.write(
        f"...finished in {time.time() - start_time:.2f} s\n")
    return retval

def vrt2lemmalists(filename, max_texts = None, lemma_col = 3):
    '''
    Parse each text in a VRT file into a list of lemmas, and return a list of those lists.
    '''

    sys.stderr.write(f"Reading {filename}\n")
    retval = []
    fobj = open(filename, "rb")
    parser = etree.XMLParser(recover = True)
    
    text_count = 0
    token_count = 0
    for line in fobj:
        if max_texts and text_count >= max_texts:
            break
        parser.feed(line)
        if line.strip() != b'</text>':
            continue
        # A text has ended
        text_count += 1
        text = parser.close()
        this_text = []
        for leaf in text.iter():
            tokens = leaf.text.strip()
            if tokens != "":
                for token in tokens.split('\n'):
                    token_count += 1
                    lemma = token.split('\t')[lemma_col-1]
                    if is_content_word(lemma):
                        this_text.append(lemma)
        retval.append(this_text)
    sys.stderr.write(f"Finished reading {filename}, {text_count} texts and {token_count} tokens\n")
    return retval

if __name__ == '__main__':
    parse_vrt_in_dir(sys.argv[1])
