#!/usr/bin/python

import unittest


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lca(node, n, m):
    if node:
        if n < node.value and m < node.value:
            return lca(node.left, n, m)
        elif n > node.value and m > node.value:
            return lca(node.right, n, m)
        else:
            return node


class Test(unittest.TestCase):

    def setUp(self):
        self.root = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))),
                            Node(10, None, Node(14, Node(13), Node(15))))

    def test_lca(self):
        self.assertEqual(6, lca(self.root, 4, 7).value)
        self.assertEqual(3, lca(self.root, 1, 3).value)
        self.assertEqual(8, lca(self.root, 4, 10).value)
        self.assertEqual(3, lca(self.root, 1, 7).value)
        self.assertEqual(14, lca(self.root, 13, 15).value)
        self.assertEqual(8, lca(self.root, 4, 13).value)


if __name__ == '__main__':
    unittest.main()
