#!/usr/bin/env python

import sys
import unittest

# See http://programmingpraxis.com/2011/04/01/maximum-difference-in-an-array/

def maxdiff(a):
	min_i = i = j = 0
	d = -sys.maxint
	for k in xrange(1, len(a)):
		if a[k] < a[min_i]:
			min_i = k
		elif a[k] - a[min_i] > d:
			d = a[k] - a[min_i]
			i = min_i
			j = k
	return i, j, d


class Test(unittest.TestCase):

	def test_1(self):
		self.assertEqual((3, 4, 7), maxdiff([4, 3, 9, 1, 8, 2, 6, 7, 5]))
	
	def test_2(self):
		self.assertEqual((1, 2, 7), maxdiff([4, 2, 9, 1, 8, 3, 6, 7, 5]))

	def test_3(self):
		self.assertEqual((3, 7, 7), maxdiff([4, 3, 9, 1, 2, 6, 7, 8, 5]))

if __name__ == '__main__':
	unittest.main()
