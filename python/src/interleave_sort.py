import unittest

# Solution to
# https://programmingpraxis.com/2016/05/13/interleaved-increasing-decreasing-sort/


def interleave_increase_decrease_sort(L):
    even = []
    odd = []
    for i in range(len(L)):
        if i % 2 == 0:
            even.append(L[i])
        else:
            odd.append(L[i])
    even.sort()
    odd.sort(reverse=True)
    result = []
    while even and odd:
        result.append(even.pop(0))
        result.append(odd.pop(0))
    if even:
        result.append(even.pop(0))
    if odd:
        result.append(odd.pop(0))
    return result


class Test(unittest.TestCase):

    def test_interleave_sort_empty(self):
        self.assertEqual([], interleave_increase_decrease_sort([]))

    def test_interleave_sort_increase_decrease(self):
        self.assertEqual([0, 9, 2, 7, 4, 5, 6, 3, 8, 1],
                         interleave_increase_decrease_sort(range(10)))

if __name__ == '__main__':
    unittest.main()
