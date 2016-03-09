#!/usr/bin/env python

import sys

def factors(n):
    d = 2
    L = []
    while d <= n:
        if n % d == 0:
            L.append(d)
            n /= d
        d += 1
    return L

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: factors.py N1 N2...")
        sys.exit(1)
    for n in map(int, sys.argv[1:]):
        print("%d -> %s" % (n, " ".join(map(str, factors(n)))))