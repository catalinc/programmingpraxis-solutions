#!/usr/bin/python

# Solution to http://programmingpraxis.com/2014/02/21/anagrams-within-words/

import itertools

__author__ = 'cata'


def anagram(a, b):
    for p in itertools.permutations(a, len(a)):
        if b.find(''.join(p)) >= 0:
            return True
    return False


if __name__ == '__main__':
    for w1, w2 in (('cat', 'actor'), ('car', 'actor')):
        print("%s %s -> %s" % (w1, w2, anagram(w1, w2)))
