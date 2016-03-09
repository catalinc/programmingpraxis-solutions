#!/usr/bin/python

import unittest

graph = {1: (6, 8),
         2: (7, 9),
         3: (4, 8),
         4: (3, 9, 0),
         6: (1, 7, 0),
         7: (2, 6),
         8: (1, 3),
         9: (2, 4),
         0: (4, 6)}


def count_paths(length, start):
    if length == 1:
        return 1
    sum = 0
    for next in graph[start]:
        sum += count_paths(length - 1, next)
    return sum


class Test(unittest.TestCase):

    def test_10_length_paths(self):
        self.assertEqual(1424, count_paths(10, 1))

if __name__ == '__main__':
    unittest.main()
