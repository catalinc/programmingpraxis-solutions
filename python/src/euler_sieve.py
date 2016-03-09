#!/usr/bin/python


import unittest
import math


def euler_sieve(n):
    L = [2]
    L.extend([x for x in xrange(3, n + 1) if x % 2 != 0])
    primes = []
    sqrtn = int(math.sqrt(n))
    while L[0] <= sqrtn:
        p = L.pop(0)
        primes.append(p)
        i = len(L)
        while i != 0:
            i -= 1
            if L[i] % p == 0:
                del L[i]
    primes.extend(L)
    return primes


class Test(unittest.TestCase):

    def test_euler_sieve(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
                         euler_sieve(30))

if __name__ == '__main__':
    unittest.main()
