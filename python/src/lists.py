#!/usr/bin/python

import unittest


def unnest(x):
    if not isinstance(x, list):
        return [x]
    elif len(x) == 0:
        return x
    return unnest(x[0]) + unnest(x[1:])


class Node(object):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList(object):

    def __init__(self):
        self.root = None

    def add(self, node):
        if not self.root:
            self.root = node
        else:
            n = self.root
            while n.next_node:
                n = n.next_node
            n.next_node = node

    def nth_to_last(self, i):
        if self.root:
            n = self.root
            count = 1
            while n.next_node:
                n = n.next_node
                count += 1
            j = 1
            n = self.root
            while j < count - i:
                n = n.next_node
                j += 1
            return n.value


class Test(unittest.TestCase):

    def test_unnest(self):
        self.assertEqual([], unnest([]))
        self.assertEqual([1, 2, 3, 4, 5], unnest([1, [2, 3, [4]], [5]]))

    def test_nth_to_last(self):
        ll = LinkedList()
        for x in xrange(10):
            ll.add(Node(x))
        self.assertEqual(9, ll.nth_to_last(0))
        self.assertEqual(7, ll.nth_to_last(2))
        self.assertEqual(0, ll.nth_to_last(9))


if __name__ == '__main__':
    unittest.main()
