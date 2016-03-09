#!/usr/bin/python 

# Problem description is located at
# http://programmingpraxis.com/2011/09/02/two-string-exercises/

import unittest

def delstrdup(s):
	ret = []
	seen = set()
	for x in s:
		if not x in seen:
			ret.append(x)
			seen.add(x)
	return "".join(ret)

def compactspaces(s):
	ret = []
	for x in s:
		if x == " ":
			if ret and ret[-1] == " ":
				continue
			ret.append(x)
		else:
			ret.append(x)
	return "".join(ret)

class Test(unittest.TestCase):

	def test_delstrdup_empty_str(self):
		self.assertEqual("", delstrdup(""))
	
	def test_delstrdup_no_dups(self):
		self.assertEqual("abc", delstrdup("abc"))

	def test_delstrdup_consecutives(self):
		self.assertEqual("ab", delstrdup("aaabbb"))
	
	def test_delstrdup_random(self):
		self.assertEqual("abcd", delstrdup("abcbd"))		
	
	def test_compactspaces_empty_str(self):
		self.assertEqual("", compactspaces(""))

	def test_compactspace_no_consec_spaces(self):
		self.assertEqual("a b c", compactspaces("a b c"))
	
	def test_compactspaces_consec_spaces(self):
		self.assertEqual("a bc d", compactspaces("a  bc   d"))

if __name__ == '__main__':
	unittest.main()