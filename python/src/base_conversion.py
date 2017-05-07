# Solution to https://programmingpraxis.com/2017/05/02/base-conversion/

import unittest


def convert(s, base, new_base):
    n, p = 0, 1
    for i in range(len(s) - 1, -1, -1):
        n += int(s[i]) * p
        p *= base
    res = []
    while n > 0:
        n, r = divmod(n, new_base)
        res.append(str(r))
    res.reverse()
    return ''.join(res)


class Test(unittest.TestCase):
    def test_convert_from_base_2_to_4(self):
        self.assertEqual("3120", convert("11011000", 2, 4))

    def test_convert_from_base_4_to_2(self):
        self.assertEqual("11011000", convert("3120", 4, 2))

    def test_convert_from_base_2_to_10(self):
        self.assertEqual("216", convert("11011000", 2, 10))


if __name__ == '__main__':
    unittest.main()
