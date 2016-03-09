#!/usr/bin/env python

import unittest
from sieve import primes
from math import sqrt, ceil

def prime_factors(n):
    sqrtn = int(ceil(n))
    trial_divisors = primes(sqrtn)
    trial_divisors.append(sqrtn)
    
    k = 0
    factors = []
    while n > 1:
        d = trial_divisors[k]
        q, r = divmod(n, d)
        
        if r == 0:
            factors.append(d)
            n = q
        else:
            if q > d:
                k += 1
            else:
                factors.append(n)
                break
    
    return factors

class PrimeFactorsTest(unittest.TestCase):
    
    def test_prime_factors(self):
        self.assertEqual(prime_factors(15), [3, 5])