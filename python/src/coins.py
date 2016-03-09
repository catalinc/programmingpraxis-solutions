#!/usr/bin/env python

# Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S.
# Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want),
# or report that it's not possible to select coins in such a way that they sum up to S. 

import sys

INF = sys.maxint

def solve(V, S):
    Min = [INF for x in range(0, S+1)]
    Min[0] = 0
    for i in range(1, S+1):
        for j in range(0, len(V)):
            if V[j] <= i and Min[i-V[j]] + 1 < Min[i]:
                Min[i] = Min[i-V[j]] + 1
    return Min[S]

if __name__ == "__main__":
    print "%d" % solve([1,3,5], 11)
