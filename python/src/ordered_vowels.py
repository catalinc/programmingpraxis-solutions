"""
See https://programmingpraxis.com/2017/01/31/ordered-vowels/
"""
import unittest
import sys


def has_ordered_vowels(word):
    """ Checks if vowels are ordered in the specified word"""
    prev = None
    for char in word:
        if char in ('a', 'e', 'i', 'o', 'u'):
            if prev is None:
                prev = char
            else:
                if prev > char:
                    return False
            prev = char
    return not prev is None

class Test(unittest.TestCase):
    def test_has_no_vowels(self):
        test_data = ['thx', 'dst', 'bst', 'ddwrt', 'db']
        for w in test_data:
            self.assertFalse(has_ordered_vowels(w), 'failed for %s' % w)
    def test_has_ordered_vowels(self):
        test_data = ['afoot', 'out', 'faster', 'foo', 'asterisk', 'alfa']
        for w in test_data:
            self.assertTrue(has_ordered_vowels(w), 'failed for %s' % w)
    def test_has_not_ordered_vowels(self):
        test_data = ['footer', 'bear', 'sonar', 'beware', 'coerce']
        for w in test_data:
            self.assertFalse(has_ordered_vowels(w), 'failed for %s' % w)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as dict_file:
            for line in dict_file:
                if has_ordered_vowels(line):
                    print(line)
    else:
        unittest.main()
