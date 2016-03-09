#!/usr/bin/env python

# See http://programmingpraxis.com/2012/02/17/hailstones/

import sys


def hailstone(n):
    while n > 1:
        yield n
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    yield 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: %s N" % sys.argv[0])
        sys.exit(1)
    for x in hailstone(int(sys.argv[1])):
        print x,
