from os import sys
import random
from collections import defaultdict

#Anagrams
def load_anagram_words(filename='/usr/share/dict/words'):
    with open(filename) as f:
        for word in f:
            yield word.rstrip()

def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        key = "".join(sorted (word))
        d[key].append(word)
    return d

def print_anagrams(word_source):
    d = get_anagrams(word_source)
    for key, anagrams in d.iteritems():
        if len(anagrams) > 1:
            print(key, anagrams)

if __name__ == '__main__':
    arguments = sys.argv[1:]
    input = sys.argv
    word_source = load_anagram_words()
    print_anagrams(word_source)
