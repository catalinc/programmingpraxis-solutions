#!/usr/bin/env python

# See http://programmingpraxis.com/2012/01/31/string-rotation/

import unittest


def is_rot(s1, s2):
    for i in xrange(2, len(s1) - 1):
        if s1[i:] + s1[0:i] == s2:
            return True
    return False


class Test(unittest.TestCase):

    def test_is_rotation(self):
        test_data = (('ProgrammingPraxis', 'PraxisProgramming'),
                     ('abcdef', 'defabc'))
        for t in test_data:
            self.assertTrue(is_rot(t[0], t[1]))

    def test_is_not_rotation(self):
        test_data = (('ProgrammingPraxis1', 'PraxisProgramming'),
                     ('abc def', 'defabc'))
        for t in test_data:
            self.assertFalse(is_rot(t[0], t[1]))


if __name__ == '__main__':
    unittest.main()
