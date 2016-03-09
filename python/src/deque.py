#!/usr/bin/env python

import unittest

class Node(object):

	def __init__(self, value):
		super(Node, self).__init__()
		self.value = value
		self.next = None
		self.prev = None

class Deque(object):

	def __init__(self, *args):
		super(Deque, self).__init__()
		self.head = None
		self.tail = None
		self.size = 0
		for x in args:
			self.push_back(x)
	
	def is_empty(self):
		return self.size == 0

	def push_back(self, x):
		n = Node(x)
		if self.is_empty():
			self.head = self.tail = n
		else:
			n.prev = self.tail
			self.tail.next = n
			self.tail = n
		self.size += 1
	
	def pop_back(self):
		if self.is_empty():
			return None
		n = self.tail
		if self.size == 1:
			self.head = self.tail = None
		else:
			self.tail = n.prev
			self.tail.next = None
		self.size -= 1
		return n.value			

	def push_front(self, x):
		n = Node(x)
		if self.is_empty():
			self.head = self.tail = n
		else:
			n.next = self.head
			self.head.prev = n
			self.head = n
		self.size += 1
	
	def pop_front(self):
		if self.is_empty():
			return None
		n = self.head
		if self.size == 1:
			self.head = self.tail = None
		else:
			self.head = n.next
			self.head.prev = None
		self.size -= 1
		return n.value
	
	def as_list(self):
		L = []
		n = self.head
		while n:
			L.append(n.value)
			n = n.next
		return L

	def __str__(self):
		return str(self.as_list())
	
	def __len__(self):
		return self.size

class Test(unittest.TestCase):

	def test_init_with_seq(self):
		d = Deque(1, 2, 3)
		self.assertEqual([1, 2, 3], d.as_list())

	def test_empty(self):
		d = Deque()
		self.assertEqual(0, len(d))
		self.assertTrue(d.is_empty())
		self.assertTrue(d.pop_back() is None)
		self.assertTrue(d.pop_front() is None)
	
	def test_push_back(self):
		d = Deque()
		d.push_back(1)
		d.push_back(2)
		self.assertEqual(2, len(d))
		self.assertEqual([1, 2], d.as_list())
	
	def test_pop_back(self):
		d = Deque(1, 2)
		self.assertEqual(2, d.pop_back())
		self.assertEqual(1, d.pop_back())
		self.assertTrue(d.is_empty())
	
	def test_push_front(self):
		d = Deque()
		d.push_front(1)
		d.push_front(2)
		self.assertEqual(2, len(d))
		self.assertEqual([2, 1], d.as_list())
	
	def test_pop_front(self):
		d = Deque(1, 2)
		self.assertEqual(1, d.pop_front())
		self.assertEqual(2, d.pop_front())
		self.assertTrue(d.is_empty())

if __name__ == '__main__':
	unittest.main()