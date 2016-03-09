#!/usr/bin/env python

"""
Word cube is game in which players form words from the nine letters in a cube.
Words must have four or more letters and must use the central letter from the cube;
at least one word will use all nine letters in the cube.
"""
import sys


def read_dictionary(filename):
    """
    Load words dictionary
    """
    words = {}
    with open(filename) as file:
        for line in file:
            word = line.strip().lower()
            words.setdefault(word[0], {}).setdefault(len(word), set()).add(word)
    return words


def query_dictionary(dictionary, letter, min, max):
    """
    Return a list of words starting with given letter and length between min and max
    """
    result = []
    scope = dictionary[letter]
    for i in range(min, max +1):
        if i in scope:
            result.extend(scope[i])
    return result


def read_word_cube(filename):
    """
    Load word cube
    """
    letters = []
    with open(filename) as file:
        for line in file:
            letters.extend(line.lower().split())
    return letters


def solve(dictionary, word_cube):
    """
    For each distinct letter in word_cube query the dictionary for all the
    words starting with the letter and length between 2 and 9.
    From this list of candidates collect only the words that can be composed
    with the existing letters in the word_cube.
    """
    sorted_word_cube = ''.join(sorted(word_cube))
    central_letter = word_cube[4]

    words = []
    letters = set(word_cube)
    for c in letters:
        candidates = query_dictionary(dictionary, c, 2, 9)
        for word in candidates:
            sorted_word = ''.join(sorted(word))
            if sorted_word in sorted_word_cube and central_letter in sorted_word:
                words.append(word)
    return words

if __name__ == '__main__':
    if len(sys.argv) == 3:
        dictionary = read_dictionary(sys.argv[1])
        word_cube = read_word_cube(sys.argv[2])
        words = solve(dictionary, word_cube)
        if words:
            for w in words:
                print w,
        else:
            print "no solutions"
    else:
        print >> sys.stderr, "usage: ./word_cube.py dictionary word_cube"
        sys.exit(1)
