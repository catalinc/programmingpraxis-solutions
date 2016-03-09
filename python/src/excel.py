#!/usr/bin/python

"""
A solution to http://programmingpraxis.com/2011/02/04/excel-columns/
"""

import unittest


def to_literal(n):
    l = []
    while n:
        n, r = n // 26, n % 26
        l.append(chr(ord('A') + r - 1))
    l.reverse()
    return ''.join(l)


def from_literal(s):
    n = 0
    for i, c in enumerate(reversed(s)):
        n += (26 ** i) * (ord(c) - ord('A') + 1)
    return n


class Test(unittest.TestCase):

    def test_to_literal(self):
        self.assertEqual('AB', to_literal(28))
        self.assertEqual('IV', to_literal(256))

    def test_from_literal(self):
        self.assertEqual(28, from_literal('AB'))
        self.assertEqual(256, from_literal('IV'))


if __name__ == '__main__':
    unittest.main()
