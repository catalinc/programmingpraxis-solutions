#!/usr/bin/env python

# Given a sequence of N numbers - A[1] , A[2] , ..., A[N].
# Find the length of the longest non-decreasing sequence.

def solve(A):
    S = [1 for x in range(0, len(A))]
    for i in range(0, len(S)):
        for j in range(0, i):
            if A[j] <= A[i] and S[j] + 1 > S[i]:
                S[i] = S[j] + 1
    return S[-1]

if __name__ == '__main__':
    print "%d" % solve([5, 3, 4, 8, 6, 7])

