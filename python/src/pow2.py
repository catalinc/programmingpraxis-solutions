#!/usr/bin/python

import unittest

def is_power_of_2(n):
	return n != 0 and n & (n-1) == 0

class Test(unittest.TestCase):

	def test_0(self):
		self.assertFalse(is_power_of_2(0))
	
	def test_power_of_2(self):
		candidates = [1, 8, 16, 32, 64, 128, 256, 512, 1024]
		for x in candidates:
			self.assertTrue(is_power_of_2(x))
	
	def test_non_power_of_2(self):
		candidates = [10, 13, 54, 102, 133, 190]
		for x in candidates:
			self.assertFalse(is_power_of_2(x))

if __name__ == "__main__":
	unittest.main()