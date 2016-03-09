#!/usr/bin/env python

# See http://programmingpraxis.com/2011/12/30/split/

import unittest


def split_list(L):
    first = []
    second = []
    if len(L) == 0:
        return first, second
    elif len(L) == 1:
        first.append(L[0])
    else:
        middle = len(L) / 2 - 1
        for i in xrange(0, len(L)):
            if i <= middle:
                first.append(L[i])
            else:
                second.append(L[i])
    return first, second


class Test(unittest.TestCase):

    def test_split_empty(self):
        L = []
        self.assertEqual(([], []), split_list(L))

    def test_split_one(self):
        L = [1]
        self.assertEqual(([1], []), split_list(L))

    def test_split_even(self):
        L = [1, 2, 3, 4]
        self.assertEqual(([1, 2], [3, 4]), split_list(L))

    def test_split_odd(self):
        L = [1, 2, 3, 4, 5]
        self.assertEqual(([1, 2], [3, 4, 5]), split_list(L))


if __name__ == '__main__':
    unittest.main()
