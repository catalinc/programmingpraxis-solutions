#!/usr/bin/python

import unittest


def hamming_weight(n):
    count = 0
    while n:
        if n & 1:
            count += 1
        n >>= 1
    return count


def hamming_weight_2(n):
    p = 0
    while n:
        p += 1
        n &= n - 1
    return p


class Test(unittest.TestCase):

    def test_hamming_weight(self):
        self.assertEqual(4, hamming_weight(23))

    def test_hamming_weight_2(self):
        self.assertEqual(4, hamming_weight_2(23))


if __name__ == '__main__':
    unittest.main()
