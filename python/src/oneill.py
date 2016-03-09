#!/usr/bin/env python

# See http://programmingpraxis.com/2011/10/14/the-first-n-primes/

import sys
from heapq import *


def oneill(n):
    queue = []
    primes = [2]
    odd_number = 3
    next_composite, skip = 9, 6
    while len(primes) < n:
        if odd_number < next_composite:
            primes.append(odd_number)
            heappush(queue, (odd_number**2, 2*odd_number))
        else:
            while odd_number == next_composite:
                next_composite, skip = heappushpop(queue, (next_composite+skip, skip))
        odd_number += 2
    return primes

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: %s NUM_PRIMES" % sys.argv[0])
        sys.exit(1)
    print(oneill(int(sys.argv[1])))
