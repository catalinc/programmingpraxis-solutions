#!/usr/bin/python

import unittest


def _min(iterable):
    min_val = None
    min_idx = -1
    for i, v in enumerate(iterable):
        if not min_val or min_val > v:
            min_val = v
            min_idx = i
    return min_val, min_idx


def sliding_win_min(L, k):
    queue = []
    mins = []
    first_min, start = _min(L[0:k])
    queue.append((first_min, start + k))
    for i in xrange(start + 1, len(L)):
        mins.append(queue[0][0])
        queue_copy = queue[:]
        for e in queue_copy:
            if e[0] > L[i]:
                queue.remove(e)
        queue.append((L[i], i + k))
        if queue[0][1] <= i:
            queue.pop(0)
        if i == len(L) - 1:
            mins.append(queue[0][0])
    return mins


class Test(unittest.TestCase):

    def setUp(self):
        self.test_data = [4, 3, 2, 1, 5, 7, 6, 0, 9]
        self.test_result = [2, 1, 1, 1, 5, 0, 0]

    def test_sliding_win_min(self):
        self.assertEqual(self.test_result, sliding_win_min(self.test_data, 3))


if __name__ == '__main__':
    unittest.main()
