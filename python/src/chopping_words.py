# See http://programmingpraxis.com/2012/07/03/chopping-words/

import time
import copy


def chop(word, dictionary):
    words = []
    for i in xrange(len(word)):
        chopped = word[0:i] + word[i + 1:]
        if chopped in dictionary:
            words.append(chopped)
    return words


def load_dictionary(filename):
    words = set()
    with open(filename) as file:
        for line in file:
            words.add(line.strip())
    return words


def chopping_chain(word, dictionary, chain=[]):
    chain.append(word)
    words = chop(word, dictionary)
    if not words:
        print(' '.join(chain))
    else:
        for w in words:
            chopping_chain(w, dictionary, copy.copy(chain))


if __name__ == '__main__':
    t0 = time.clock()
    dictionary = load_dictionary('words.lst')
    print("dictionary loaded in %.2fs" % (time.clock() - t0))
    chopping_chain('planet', dictionary)
