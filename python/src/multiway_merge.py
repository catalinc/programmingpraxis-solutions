import unittest
import heapq


# Solution to https://programmingpraxis.com/2016/03/29/multi-way-merge/

def merge_sort(a, b):
    i, j, r = 0, 0, []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            r.append(a[i])
            i += 1
        else:
            r.append(b[j])
            j += 1
    while i < len(a):
        r.append(a[i])
        i += 1
    while j < len(b):
        r.append(b[j])
        j += 1
    return r


def merge_sort_multiple(*args):
    r = None
    for l in args:
        if r is None:
            r = l
        else:
            r = merge_sort(r, l)
    return r


def merge_sort_multiple_pq(*args):
    h = []
    for l in args:
        heapq.heappush(h, l)
    r = []
    while h:
        t = heapq.heappop(h)
        if t:
            r.append(t[0])
            t = t[1:]
            if t:
                heapq.heappush(h, t)
    return r


class Test(unittest.TestCase):
    def test_merge_sort_with_empty(self):
        self.assertEqual([1, 2], merge_sort([1, 2], []))

    def test_merge_sort(self):
        self.assertEqual([1, 2, 3, 4, 5], merge_sort([2, 5], [1, 3, 4]))

    def test_merge_sort_multiple(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8],
                         merge_sort_multiple([6, 8], [2, 5, 7], [1, 3, 4]))

    def test_merge_sort_multiple_pq(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8],
                         merge_sort_multiple_pq([6, 8], [2, 5, 7], [1, 3, 4]))


if __name__ == '__main__':
    unittest.main()
