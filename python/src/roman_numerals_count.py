#!/usr/bin/env python

# See http://programmingpraxis.com/2012/02/03/roman-numeral-puzzle/

from src.roman_numerals import to_roman


def solve(limit=10000):
    count = 0
    for i in xrange(1, limit + 1):
        if no_duplicates(to_roman(i)):
            count += 1
    return count


def no_duplicates(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        else:
            seen.add(c)
    return True

if __name__ == '__main__':
    print solve()
