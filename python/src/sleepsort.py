#!/usr/bin/python

import sys
import threading
import copy

class DelayedPrinter(object):
	"""Print something after a given interval"""
	def __init__(self, what, after):
		super(DelayedPrinter, self).__init__()
		def pr():
			print what
		self.timer = threading.Timer(after, pr)
	
	def start(self):
		self.timer.start()
		

def sleep_sort(seq):
	for x in seq:
		DelayedPrinter(x, x).start()

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("usage: ./sleepsort.py N1 N2...")
		sys.exit(1)
	sleep_sort(map(int, sys.argv[1:]))