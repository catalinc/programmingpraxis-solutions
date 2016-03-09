#!/usr/bin/env python

import random
import pprint

def partition(arr):
    k = random.choice(arr)
    smaller = [x for x in arr if x <= k]
    bigger = [x for x in arr if x > k]
    return smaller, bigger, k

def random_array(nelems=100, min=0, max=100):
    return [random.randint(min, max) for x in range(0, nelems)]

def select(arr, kth):
    """select smallest kth element"""
    smaller, bigger, elem = partition(arr)
    len_smaller = len(smaller)
    if len_smaller > kth:
        return select(smaller, kth)
    elif len_smaller < kth:
        return select(bigger, kth - len_smaller)
    else:
        return elem

if __name__ == "__main__":
    arr = random_array(10)
    print "input data:"
    pprint.pprint(arr)
    kth = random.randint(1, len(arr)-1)
    el = select(arr, kth)
    print "%d smaller is: %s" % (kth, str(el))
