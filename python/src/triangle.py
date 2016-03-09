#!/usr/bin/env python

import unittest

def triangle(a, b, c):
	if a <= 0 or b <= 0 or c <= 0:
		return "invalid triangle"
	if not (a + b > c and a + c > b and b + c > a):
		return "invalid triangle"
	if a == b == c:
		return "equilateral"
	if a == b or b == c or a == c:
		return "isosceles"
	return "scalene"

class Test(unittest.TestCase):

	def test_invalid(self):
		self.assertEqual("invalid triangle", triangle(2, -1 , 4))
	
	def test_invalid_2(self):
		self.assertEqual("invalid triangle", triangle(1, 2, 3))
	
	def test_equilateral(self):
		self.assertEqual("equilateral", triangle(4, 4, 4))
	
	def test_isosceles(self):
		self.assertEqual("isosceles", triangle(3, 4, 3))
	
	def test_scalene(self):
		self.assertEqual("scalene", triangle(3, 4, 5))

if __name__ == '__main__':
	unittest.main()