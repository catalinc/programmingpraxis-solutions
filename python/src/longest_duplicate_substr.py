#!/usr/bin/python

import sys
import unittest


def common_prefix(s1, s2):
    n = min(len(s1), len(s2))
    L = []
    for i in xrange(n):
        if s1[i] == s2[i]:
            L.append(s1[i])
        else:
            break
    return ''.join(L)


def find_longest_duplicate(s):
    suffix_list = [s[i:] for i in xrange(len(s) - 1, -1, -1)]
    suffix_list.sort()
    longest = ''
    for i in xrange(len(suffix_list) - 1):
        prefix = common_prefix(suffix_list[i], suffix_list[i + 1])
        if len(longest) < len(prefix):
            longest = prefix
    return longest


class Test(unittest.TestCase):

    def test_ok(self):
        self.assertEqual('ana', find_longest_duplicate('banana'))

    def test_empty(self):
        self.assertEqual('', find_longest_duplicate('abcdef'))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: longest_duplicate_substr.py <input string>")
        sys.exit(1)
    else:
        print(find_longest_duplicate(sys.argv[1]))
