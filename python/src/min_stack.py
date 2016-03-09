# See http://programmingpraxis.com/2012/07/27/min-stack/

import unittest


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, item):
        self.stack.append(item)
        if not self.mins or item <= self.mins[-1]:
            self.mins.append(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.mins[-1]:
            self.mins.pop()
        return item

    def min(self):
        return self.mins[-1]

    def __len__(self):
        return len(self.stack)


class Test(unittest.TestCase):

    def test_empty(self):
        ms = MinStack()
        self.assertEqual(len(ms), 0)

    def test_push(self):
        ms = MinStack()
        ms.push(1)
        ms.push(2)
        self.assertEqual(len(ms), 2)

    def test_pop(self):
        ms = MinStack()
        ms.push(1)
        ms.push(2)
        self.assertEqual(ms.pop(), 2)
        self.assertEqual(ms.pop(), 1)
        self.assertEqual(len(ms), 0)

    def test_min(self):
        ms = MinStack()
        ms.push(2)
        ms.push(3)
        self.assertEqual(ms.min(), 2)
        ms.push(0)
        ms.push(1)
        self.assertEqual(ms.min(), 0)
        ms.push(-1)
        ms.push(4)
        self.assertEqual(ms.min(), -1)
        ms.pop()
        ms.pop()
        self.assertEqual(ms.min(), 0)


if __name__ == '__main__':
    unittest.main()
