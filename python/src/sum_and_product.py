#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

def good_nums():
    return [x for x in range(2, 100)]

def good_factors(p):
    """
    Given a number p, we want to find all its good factors a and b, with a ≥ b, 
    and return them (the pairs of factors) in a list
    """
    return [(a, b) for a in good_nums() for b in good_nums() if a >= b and a * b == p]

def good_summands(s):
    """
    Given a number s, we want to find all its good summands a and b, with a ≥ b, 
    and return them (the pairs of factors) in a list
    """
    return [(a, b) for a in good_nums() for b in good_nums() if a >= b and a + b == s]

def is_singleton(l):
    """
    A singleton list has only one element
    """
    return len(l) == 1        

def fact1(ab):
    """
    The first fact is that Mr. P. doesn’t know the numbers.
    But Mr. P. would have know the numbers if the product had had a unique good factorization
    """
    return not is_singleton(good_factors(_prod(ab)))

def fact2(ab):
    """The second fact is similar; Mr. S. doesn’t know the numbers either"""
    return not is_singleton(good_summands(_sum(ab)))

def fact3(ab):
    """
    The third fact is that Mr. S. knows that Mr. P. doesn’t know the numbers.
    In other words, for all possible summands that make a+b, Mr. P. cannot be certain of the numbers
    """
    return _all(fact1, good_summands(_sum(ab)))

def fact4(ab):
    """
    Mr. S. now knows that Mr. P. doesn’t know the numbers. Thus, the fourth fact is that of all 
    factorizations of a×b there exists only one that makes the third fact true
    """
    return is_singleton(filter(fact3, good_factors(_prod(ab))))

def fact5(ab):
    """
    The fifth fact is that Mr. S. knows that Mr. P. found the numbers.
    Thus, only one decomposition of a+b makes the fourth fact true
    """
    return is_singleton(filter(fact4, good_summands(_sum(ab))))    

def sum_and_prod():
    nums = [(a, b) for a in good_nums() for b in good_nums() if a >= b]
    return filter(is_solution, nums)

def is_solution(ab):
    for fact in [fact1, fact2, fact3, fact4, fact5]:
        if not fact(ab):
            return False
    return True    

def _all(predicate, iterable):    
    for element in iterable:
        if not predicate(element):
            return False
    return True

def _sum(iterable):
    return reduce(lambda x, y: x + y, iterable, 0)

def _prod(iterable):
    return reduce(lambda x, y: x * y, iterable, 1)
    
class SumAndProductTestCase(unittest.TestCase):
    
    def test_calculator(self):
        self.assertEqual([(13, 4)], sum_and_prod())
