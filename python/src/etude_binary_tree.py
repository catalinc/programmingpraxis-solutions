# Solution to https://programmingpraxis.com/2017/04/25/etude-on-a-binary-tree/

import unittest


class BinaryTree(object):
    def __init__(self, root=None):
        self.levels = [[0]]
        self.pos = 0

    def insert(self, x):
        current = self.levels[-1]
        current[self.pos] = x
        self.pos += 1
        if self.pos == len(current):
            self.levels.append([0 for _ in range(2 * len(current))])
            self.pos = 0

    def odd_even_sum(self):
        total = 0
        for i, level in enumerate(self.levels):
            level_total = sum(level)
            if i % 2 == 0:
                total += level_total
            else:
                total -= level_total
        return total


class Test(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()
        for x in range(1, 16):
            self.tree.insert(x)

    def test_odd_even_sum(self):
        self.assertEqual(-74, self.tree.odd_even_sum())


if __name__ == '__main__':
    unittest.main()
