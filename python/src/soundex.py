#!/usr/bin/env python

import unittest
import re

PATTERNS = (
    (re.compile('[aehiouwy]', re.I), ''),
    (re.compile('[bfpv]', re.I), '1'),
    (re.compile('[cgjkqsxz]', re.I), '2'),
    (re.compile('[dt]', re.I), '3'),
    (re.compile('[l]', re.I), '4'),
    (re.compile('[mn]', re.I), '5'),
    (re.compile('[r]', re.I), '6')
    )


def soundex(name):
    
    if len(name) == 0:
        return ''

    s = name.upper()
    first, s = s[0], s[1:]

    for p in PATTERNS:
        s = p[0].sub(p[1], s)

    l = len(s)
    if l < 3:
        s += "0" * (3 - l)
    elif l > 3:
        s = s[0:3]

    return first + s


class TestSoundex(unittest.TestCase):

    def test_encode(self):
        self.assertEquals('C300', soundex('cata'))
        self.assertEquals('P365', soundex('PETRONELA'))

if __name__ == "__main__":
    unittest.main()
