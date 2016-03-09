#!/usr/bin/python

# coding: utf-8

import unittest


def politness(n):
    politness = 0
    consecutive = []
    for d in divisors(n):
        if odd(d) and d > 1:
            politness += 1
            L = [n / d]
            while sum(L) < n:
                L.insert(0, L[0] - 1)
                L.append(L[-1] + 1)
            tmp = L[:]
            for x in L:
                if x == 0:
                    tmp.remove(0)
                elif -1*x in tmp:
                    tmp.remove(x)
                    tmp.remove(-1*x)
            consecutive.append(tmp)
    return politness, consecutive


def divisors(n):
    L = [k for k in xrange(1, n / 2 + 1) if n % k == 0]
    L.append(n)
    return L


def odd(n):
    return n % 2 != 0


class Test(unittest.TestCase):

    def test_politness(self):
        self.assertEqual((0, []), politness(64))
        self.assertEqual((1, [[1, 2, 3, 4, 5, 6, 7]]), politness(28))
        self.assertEqual((3, [[10, 11, 12], [3, 4, 5, 6, 7, 8], [16, 17]]), politness(33))

if __name__ == '__main__':
    unittest.main()
