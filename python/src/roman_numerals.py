#!/usr/bin/python

import sys
import unittest


ARABIC_TO_ROMAN = (
        (0, ''),
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
        (50, 'L'),
        (100, 'C'),
        (500, 'D'),
        (1000, 'M'))


def find_closest(n):
    diff = sys.maxint
    closest = ''
    for t in ARABIC_TO_ROMAN:
        d = n - t[0]
        if d == 0:
            return t[1], d
        else:
            if abs(d) < abs(diff):
                diff = d
                closest = t[1]
    return closest, diff


def to_roman(n):
    roman = []
    k = 10
    while n:
        unit = n % k
        n = n - unit
        k *= 10
        s = ''
        substract = False
        while unit:
            r, d = find_closest(unit)
            if substract:
                s = r + s
            else:
                s = s + r
            if d < 0:
                substract = True
            else:
                substract = False
            unit = abs(d)
        roman.append(s)
    return ''.join(reversed(roman))


class Test(unittest.TestCase):

    def test_to_roman_numeral(self):
        self.assertEqual('V', to_roman(5))
        self.assertEqual('X', to_roman(10))
        self.assertEqual('VII', to_roman(7))
        self.assertEqual('XV', to_roman(15))
        self.assertEqual('CXI', to_roman(111))
        self.assertEqual('CCL', to_roman(250))
        self.assertEqual('CDXIV', to_roman(414))
        self.assertEqual('CMXXIII', to_roman(923))
        self.assertEqual('MDCXXVII', to_roman(1627))
        self.assertEqual('MMX', to_roman(2010))

if __name__ == '__main__':
    unittest.main()
