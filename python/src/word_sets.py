# Solution to https://programmingpraxis.com/2017/03/17/word-sets/

import unittest


def test_word_with_dupes(word, letters):
    for c in word:
        if not c in letters:
            return False
    return True


def test_word_no_dupes(word, letters):
    used = set()
    for c in word:
        if not c in letters:
            return False
        else:
            if c in used:
                return False
            used.add(c)
    return True


def word_sets(words, letters, test_word=test_word_with_dupes):
    r = []
    for w in words:
        if test_word(w, letters):
            r.append(w)
    return r


class Test(unittest.TestCase):

    def setUp(self):
        self.letters = set('act')
        self.words = ['cat', 'act', 'def',
                      'tac', 'blah', 'atac', 'tcca', 'acf']

    def test_words_sets_with_dupes(self):
        self.assertEqual(['cat', 'act', 'tac', 'atac', 'tcca'],
                         word_sets(self.words, self.letters, test_word=test_word_with_dupes))

    def test_words_sets_no_dupes(self):
        self.assertEqual(['cat', 'act', 'tac'],
                         word_sets(self.words, self.letters, test_word=test_word_no_dupes))

if __name__ == '__main__':
    unittest.main()
