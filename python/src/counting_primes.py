#!/usr/bin/python

import itertools
import unittest


def gen_primes():
    """Primes generator"""
    D = {}
    q = 2
    while True:
        if not q in D:
            D[q * q] = [q]
            yield q
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def prime_pi(n):
    """Count primes less or equal to n"""
    return len(list(itertools.takewhile(lambda x: x <= n, gen_primes())))


def nth_prime(n):
    """Return nth prime"""
    return next(itertools.islice(gen_primes(), n - 1, None))


class Test(unittest.TestCase):

    def test_prime_pi(self):
        self.assertEqual(25, prime_pi(100))

    def test_nth_prime(self):
        self.assertEqual(97, nth_prime(25))

    def test_prime_pi_nth_prime(self):
        self.assertEqual(25, prime_pi(nth_prime(25)))


if __name__ == '__main__':
    unittest.main()
