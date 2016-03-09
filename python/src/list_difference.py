#!/usr/bin/env python

import timeit

A = [4, 7, 12, 6, 17, 5, 13]
B = [7, 19, 4, 11, 13, 2, 15]


def difference1(a, b):
    result = []
    for i in xrange(len(a)):
        found = False
        for j in xrange(len(b)):
            if a[i] == b[j]:
                found = True
                break
        if not found:
            result.append(a[i])


def difference2(a, b):
    return list(set(a) - set(b))


def difference3(a, b):
    freq = [0 for _ in xrange(max(a) + 1)]
    for x in a:
        freq[x] += 1
    for x in b:
        if x < len(freq) and freq[x] != 0:
            freq[x] += 1
    result = []
    for i in xrange(len(freq)):
        if freq[i] == 1:
            result.append(i)
    return result

if __name__ == '__main__':
    for i in xrange(1, 4):
        print("difference%d=%f s" % (i, timeit.timeit(
            stmt="difference%d(A, B)" % i,
            setup="from __main__ import difference%d, A, B" % i,
            number=1000)))
