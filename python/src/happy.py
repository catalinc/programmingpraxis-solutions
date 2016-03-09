#!/usr/bin/python

import unittest

def sum_squares_digits(n):
    s = 0
    while n:
        n, d = n // 10, n % 10
        s += d**2
    return s

def is_happy(n):
    ns = set()
    while True:
        n = sum_squares_digits(n)
        if n == 1:
            return True
        elif n in ns:
            return False
        else:
            ns.add(n)

class Test(unittest.TestCase):

    def test_sum_squares_digits(self):
        self.assertEqual(14, sum_squares_digits(123))

    def test_is_happy(self):
        self.assertTrue(is_happy(7))
        self.assertFalse(is_happy(17))

if __name__ == '__main__':
    unittest.main()

