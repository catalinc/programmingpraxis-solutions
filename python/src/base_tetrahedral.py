#!/usr/bin/env python

import sys


def triangular():
    n = 0
    b = 0
    while True:
        b += 1
        n += b
        yield n


def tetrahedral():
    n = 0
    gen = triangular()
    while True:
        t = gen.next()
        n += t
        yield n


def base_tetrahedral(n):
    for i, t in enumerate(tetrahedral()):
        if t == n:
            return i
        if t > n:
            break

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: base_tetrahedral.py N1 N2...")
        sys.exit(1)
    for n in map(int, sys.argv[1:]):
        print("base for %d is %s" % (n, base_tetrahedral(n)))
