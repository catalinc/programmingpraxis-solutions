#!/usr/bin/env python

# See http://programmingpraxis.com/2011/10/11/tower-of-hanoi/

def hanoi(source, target, helper, n):
	if n == 1:
		print("Moving 1 ring from %s to %s" % (source, target))
	else:
		hanoi(source, helper, target, n-1)
		print("Moving 1 ring from %s to %s" % (source, target))
		hanoi(helper, target, source, n-1)

if __name__ == '__main__':
	hanoi('A', 'B', 'C', 3)