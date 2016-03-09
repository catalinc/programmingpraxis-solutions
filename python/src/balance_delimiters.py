#!/usr/bin/env  python

# See http://programmingpraxis.com/2012/03/02/balanced-delimiters/

import unittest

DELIMITERS = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def is_balanced(s):
    if not s:
        return True
    prev = None
    stack = []
    in_string = False
    string_start = None
    for char in s:
        if prev != "\\":
            if char in "'\"":
                if not in_string:
                    string_start = char
                    in_string = True
                else:
                    if char != string_start:
                        return False
                    else:
                        in_string = False
            elif not in_string:
                if char in DELIMITERS.values():
                    stack.append(char)
                elif char in DELIMITERS:
                    if len(stack) == 0:
                        return False
                    prev_delim = stack.pop()
                    if prev_delim != DELIMITERS[char]:
                        return False
        prev = char
    return len(stack) == 0


class Test(unittest.TestCase):

    def test_None(self):
        self.assertTrue(is_balanced(None))

    def test_empty_string(self):
        self.assertTrue(is_balanced(''))

    def test_balanced(self):
        balanced_strings = ('({abc}def)',
                            '<(0{abc}def)[ <ghi>]>',
                            '((abc)def(ghi))',
                            '{a (b \( ) \[ {[cde \<]}}',
                            '(abc "(((def \\"{{))\{" {ghi<>})')
        for s in balanced_strings:
            self.assertTrue(is_balanced(s), '%s should be balanced' % s)

    def test_unbalanced(self):
        unbalanced_strings = ('({abcdef)',
                            '(0{abc}def)[ <ghi>]>',
                            '((abc)"def(ghi))',
                            '{a (b \( )> \[ {[cde \<]}}',
                            '(a "((def {{))\{"> {ghi<>})',
                            "'abd \"(dfafaf'")
        for s in unbalanced_strings:
            self.assertFalse(is_balanced(s), '%s should NOT be balanced' % s)

if __name__ == '__main__':
    unittest.main()
