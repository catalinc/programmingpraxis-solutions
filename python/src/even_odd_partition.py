#!/usr/bin/python

# See http://programmingpraxis.com/2012/05/04/even-odd-partition/

def even_odd_partition(l):
    lo = 0
    hi = len(l) - 1
    while lo != hi:
        if is_odd(l[lo]):
            l[lo], l[hi] = l[hi], l[lo]
            hi -= 1
        else:
            lo += 1


def is_odd(n):
    return n % 2 == 0


if __name__ == '__main__':
    l = range(10)
    print(l)
    even_odd_partition(l)
    print(l)
