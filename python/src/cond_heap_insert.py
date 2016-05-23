import unittest
from heapq import *


def cond_heap_insert(heap, item):
    if item in heap:
        return
    heappush(heap, item)


class Test(unittest.TestCase):

    def setUp(self):
        self.h = [4, 2, 8]
        heapify(self.h)

    def test_cond_insert_already_in_heap(self):
        cond_heap_insert(self.h, 8)
        self.assertEqual(3, len(self.h))

    def test_cond_insert_not_in_heap(self):
        cond_heap_insert(self.h, 16)
        self.assertEqual(4, len(self.h))
        self.assertTrue(16 in self.h)

if __name__ == '__main__':
    unittest.main()
