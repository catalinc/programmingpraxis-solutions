#!/usr/bin/python

import random
import sys


def randoms_gt_one():
    S = 0
    count = 0
    while S < 1:
        S += random.random()
        count += 1
    return count


if __name__ == '__main__':
    N = 100
    count = 0
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    for _ in xrange(N):
        count += randoms_gt_one()
    print("Avg: %f" % (float(count) / N))
