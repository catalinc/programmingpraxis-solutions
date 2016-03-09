#!/usr/bin/python

import unittest
import sys
import math


def kaprekar(k):
    k2 = k * k
    n = int(math.log10(k2)) / 2 + 1
    q, r = divmod(k2, (10 ** n))
    return q + r == k


class Test(unittest.TestCase):

    def test_kaprekar(self):
        self.assertTrue(kaprekar(9))
        self.assertTrue(kaprekar(297))

    def test_not_kaprekar(self):
        self.assertFalse(kaprekar(3))
        self.assertFalse(kaprekar(100))
        self.assertFalse(kaprekar(8))


if __name__ == '__main__':
    N = 1000
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    L = []
    for n in xrange(1, N + 1):
        if kaprekar(n):
            L.append(n)
    print('Kaprekar numbers under %d: %s' % (N, L))
