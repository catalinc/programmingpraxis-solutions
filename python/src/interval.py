#!/usr/bin/python

import unittest


class Interval(object):

    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __add__(self, other):
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def __sub__(self, other):
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def __mul__(self, other):
        ll = self.lower * other.lower
        lu = self.lower * other.upper
        ul = self.upper * other.lower
        uu = self.upper * other.upper
        return Interval(min(ll, lu, ul, uu), max(ll, lu, ul, uu))

    def __div__(self, other):
        try:
            ll = self.lower / other.lower
            lu = self.lower / other.upper
            ul = self.upper / other.lower
            uu = self.upper / other.upper
            return Interval(min(ll, lu, ul, uu), max(ll, lu, ul, uu))
        except ZeroDivisionError:
            return None

    def __eq__(self, other):
        return self.lower == other.lower and self.upper == other.upper

    def __str__(self):
        return '[%s, %s]' % (self.lower, self.upper)


class Test(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(Interval(2, 3), Interval(2, 3))

    def test_add(self):
        self.assertEqual(Interval(3, 5), Interval(1, 2) + Interval(2, 3))

    def test_sub(self):
        self.assertEqual(Interval(-2, 0), Interval(1, 2) - Interval(2, 3))

    def test_multiply(self):
        self.assertEqual(Interval(2, 6), Interval(1, 2) * Interval(2, 3))

    def test_division(self):
        self.assertEqual(Interval(0, 1), Interval(1, 2) / Interval(2, 3))
        self.assertTrue(Interval(1, 2) / Interval(0, 1) is None)


if __name__ == '__main__':
    unittest.main()
