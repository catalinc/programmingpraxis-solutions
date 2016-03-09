#!/usr/bin/env python

# See http://programmingpraxis.com/2011/12/16/majority-voting/

import unittest


def winner(iterable):
    freq = {}
    most_common = (None, 0)
    count = 0
    for x in iterable:
        count += 1
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
        if freq[x] > most_common[1]:
            most_common = (x, freq[x])
    if most_common[1] > count / 2:
        return most_common
    return (None, 0)


class Test(unittest.TestCase):

    def test_winner_exists(self):
        self.assertEqual(("C", 7), winner("AAACCBBCCCBCC"))

    def test_no_winner(self):
        self.assertEqual((None, 0), winner("ABCABCA"))


if __name__ == '__main__':
    unittest.main()
