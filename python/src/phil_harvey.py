#!/usr/bin/env python

# See http://programmingpraxis.com/2011/11/15/phil-harveys-puzzle/

def choose_iter(elements, length):
    for i in xrange(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next

def choose(l, k):
    return list(choose_iter(l, k))

def sumpow(seq, p):
	r = 0
	for x in seq:
		r += x ** p
	return r

nums = range(1, 17)
k = 8

for comb in choose(nums, k):
	rest = tuple(set(nums) - set(comb))
	found = True
	for i in xrange(1, 4):
		if sumpow(comb, i) != sumpow(rest, i):
			found = False
			break
	if found:
		print("solution: %s %s" % (comb, rest))
		break