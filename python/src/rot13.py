#!/usr/bin/python

import unittest

LOOKUP_TABLE = dict(
        zip('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
            'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))


def rot13(s):
    r = []
    for c in s:
        r.append(LOOKUP_TABLE.get(c, c))
    return ''.join(r)


class Test(unittest.TestCase):

    def test_inverse(self):
        self.assertEqual('abc', rot13(rot13('abc')))

    def test_encryption(self):
        self.assertEquals('Gur ohgyre qvq vg!', rot13('The butler did it!'))


if __name__ == '__main__':
    unittest.main()
