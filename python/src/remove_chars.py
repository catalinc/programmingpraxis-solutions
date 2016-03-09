#!/usr/bin/env python

import unittest


def remove_chars(s, chars):
    ret = []
    for c in s:
        if not c in chars:
            ret.append(c)
    return ''.join(ret)


class Test(unittest.TestCase):

    def test_no_chars_to_remove(self):
        self.assertEqual('abc', remove_chars('abc', ''))

    def test_remove_chars(self):
        self.assertEqual('Prgrmmng Prxs', remove_chars('Programming Praxis', 'aeiou'))


if __name__ == '__main__':
    unittest.main()
