#!/usr/bin/env python

import unittest


def next_perm(n):
    digits = _digits(n)
    last = len(digits) - 1
    for k in xrange(last - 1, -1, -1):
        if digits[k] < digits[k + 1]:
            for l in xrange(last, k, -1):
                if digits[l] > digits[k]:
                    digits[k], digits[l] = digits[l], digits[k]
                    break
            digits[k + 1:] = reversed(digits[k + 1:])
            return int(''.join(map(str, digits)))
    return n


def _digits(n):
    digits = []
    while n != 0:
        n, r = divmod(n, 10)
        digits.insert(0, r)
    return digits


class Test(unittest.TestCase):
    
    def test_digits(self):
        self.assertEqual([1, 2, 3], _digits(123))

    def test_next_perm(self):
        self.assertEqual(38627, next_perm(38276))

    def test_next_perm_final(self):
        self.assertEqual(87632, next_perm(87632))


if __name__ == '__main__':
    unittest.main()
