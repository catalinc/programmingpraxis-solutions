# https://programmingpraxis.com/2017/04/11/sort-four/

import unittest


def sort_four(a, b, c, d):
    a, b = (a, b) if a < b else (b, a)
    c, d = (c, d) if c < d else (d, c)
    a, c = (a, c) if a < c else (c, a)
    b, c = (b, c) if b < c else (c, b)
    c, d = (c, d) if c < d else (d, c)
    return a, b, c, d


class Test(unittest.TestCase):
    def test_sort_four(self):
        self.assertEqual((1, 2, 3, 4), sort_four(2, 3, 1, 4))
        self.assertEqual((-1, 0, 1, 2), sort_four(2, 0, 1, -1))


if __name__ == '__main__':
    unittest.main()
