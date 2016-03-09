#!/usr/bin/env python

# See http://programmingpraxis.com/2012/02/14/divisors/

import unittest
import sys


def build_divisors_table(n):
    d = [[] for _ in xrange(n + 1)]
    for i in xrange(1, n + 1):
        k = 1
        m = i * k
        while m <= n:
            d[m].append(i)
            k += 1
            m = i * k
    return d


class Test(unittest.TestCase):

    def test_divisors_of_1(self):
        dtable = build_divisors_table(12)
        self.assertEqual([1], dtable[1])

    def test_divisors_of_7(self):
        dtable = build_divisors_table(12)
        self.assertEqual([1, 7], dtable[7])

    def test_divisors_of_10(self):
        dtable = build_divisors_table(10)
        self.assertEqual([1, 2, 5, 10], dtable[10])


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
        dtable = build_divisors_table(n)
        for i in xrange(1, n + 1):
            print("%d: %s" % (i, dtable[i]))
    else:
        unittest.main()
