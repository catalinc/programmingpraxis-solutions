#!/usr/bin/env python

# See http://programmingpraxis.com/2012/02/10/find-in-an-ascending-matrix/

import unittest


def matrix(s):
    m = [[int(c) for c in r.split()]
            for r in s.strip().split('\n')]
    return m


def find(k, m):
    if not m:
        return None
    rows, cols = len(m), len(m[0])
    if k < m[0][0] or k > m[rows - 1][cols - 1]:
        return None
    row = 0
    while row < rows:
        first, last = m[row][0], m[row][cols - 1]
        if k < first:
            return None
        if k > last:
            row += 1
            continue
        col = 0
        while k > m[row][col] and col < cols:
            col += 1
        if k == m[row][col]:
            return row, col
        row += 1
    return None


class Test(unittest.TestCase):

    def setUp(self):
        self.m = matrix("""
 1  5  7  9
 4  6 10 15
 8 11 12 19
14 16 18 21
""")

    def test_matrix(self):
        self.assertEqual(10, self.m[1][2])

    def test_empty_matrix(self):
        self.assertEqual(None, find(1, []))

    def test_found(self):
        self.assertEqual((0, 0), find(1, self.m))
        self.assertEqual((3, 3), find(21, self.m))
        self.assertEqual((2, 1), find(11, self.m))
        self.assertEqual((3, 0), find(14, self.m))

    def test_not_found(self):
        self.assertEqual(None, find(-1, self.m))
        self.assertEqual(None, find(13, self.m))
        self.assertEqual(None, find(52, self.m))


if __name__ == '__main__':
    unittest.main()
