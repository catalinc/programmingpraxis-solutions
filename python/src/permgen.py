#!/usr/bin/env python

import sys


def perm(s):
    p = sorted(s)
    n = len(p)
    while True:
        yield ''.join(p)
        k = -1
        for i in xrange(n - 2, -1, -1):
            if p[i] < p[i + 1]:
                k = i
                break

        if k > 0:
            for l in xrange(n - 1, k, -1):
                if p[k] < p[l]:
                    p[k], p[l] = p[l], p[k]
                    i = k + 1
                    j = n - 1
                    while i < j:
                        p[i], p[j] = p[j], p[i]
                        i += 1
                        j -= 1
                    break
        else:
            break

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage %s STRING" % sys.argv[0])
        sys.exit(1)
    for i, p in enumerate(perm(sys.argv[1])):
        print("%d: %s" % (i, p))
