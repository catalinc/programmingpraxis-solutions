# See http://programmingpraxis.com/2012/11/16/list-intersection-and-union/

import timeit

L1 = [4, 7, 12, 6, 17, 5, 13]
L2 = [7, 19, 4, 11, 13, 2, 15]


def intersection1(l1, l2):
    result = []
    for x in l1:
        if x in l2:
            result.append(x)
    return result


def union1(l1, l2):
    result = l1[:]
    for x in l2:
        if not x in l1:
            result.append(x)
    return result


def intersection2(l1, l2):
    d = freq(l1 + l2)
    return [k for k in d.keys() if d[k] > 1]


def union2(l1, l2):
    d = freq(l1 + l2)
    return d.keys()


def freq(l):
    d = {}
    for x in l:
        d.setdefault(x, 0)
        d[x] += 1
    return d


def intersection3(l1, l2):
    l = freq2(l1 + l2)
    return[i for i in xrange(len(l)) if l[i] > 1]


def union3(l1, l2):
    l = freq2(l1 + l2)
    return[i for i in xrange(len(l)) if l[i] > 0]


def freq2(l):
    max_val = max(l)
    fl = [0 for _ in xrange(max_val + 1)]
    for x in l:
        fl[x] += 1
    return fl

if __name__ == '__main__':
    for i in xrange(1, 4):
        print("intersection%d: %f" %
             (i, timeit.timeit(
              stmt="intersection%d(L1, L2)" % i,
              setup="from __main__ import intersection%d, freq, L1, L2" % i,
              number=1000)))
        print("union%d: %f" %
             (i, timeit.timeit(
              stmt="union%d(L1, L2)" % i,
              setup="from __main__ import union%d, freq, L1, L2" % i,
              number=1000)))
