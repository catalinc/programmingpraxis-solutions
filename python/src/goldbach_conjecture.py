#!/usr/bin/env python
# -*- coding: utf-8 -*-

# One of the most famous unproven conjectures in number theory is known as Goldbach’s Conjecture,
# which states that every even number greater than two is the sum of two prime numbers; for example,
# 28 = 5 + 23.
#
# Write a function that finds the two primes that add to a given even number greater than two.

import sieve


def solve(N):
    sol = []
    primes = sieve.primes(N)
    i, j = 0, len(primes) - 1
    while i <= j:
        x, y = primes[i], primes[j]
        s = x + y
        if s < N:
            i += 1
        elif s > N:
            j -= 1
        else:
            i += 1
            j -= 1
            sol.append((x, y))
    return sol

if __name__ == '__main__':
    print solve(28)
