#!/usr/bin/env python

import time
import bitarray
import unittest

def benchmark(fn):
	def wrapped(*args, **kwargs):
		start = time.time()
		res   = fn(*args, **kwargs)
		print("%.2f s" % (time.time()-start))
		return res
	return wrapped


@benchmark
def find_dup(a):
	seen = set()
	for x in a:
		if x in seen:
			return x
		seen.add(x)

@benchmark
def find_dup_bitarray(a, max):
	bits = bitarray.bitarray(max+1)
	bits.setall(False)
	for x in a:
		if bits[x]:
			return x
		bits[x] = True

class Test(unittest.TestCase):

	def setUp(self):
		self.dup = 42
		self.min = 1
		self.max = 1000000
		self.array = range(self.min, self.max+1)
		self.array.append(self.dup)

	def test_find_dup(self):
		self.assertEqual(self.dup, find_dup(self.array))
	
	def test_find_dup_bitarray(self):
		self.assertEqual(self.dup,
						 find_dup_bitarray(self.array, self.max))

if __name__ == '__main__':
	unittest.main()