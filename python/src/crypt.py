#!/usr/bin/env python

# See http://programmingpraxis.com/2011/10/28/crypt/

import sys

def crypt(infile, outfile, key):
	with open(infile, 'r') as inf:
		with open(outfile, 'w') as outf:
			i = 0
			for c in inf.read():
				outf.write(chr(ord(c) ^ ord(key[i])))
				i = (i + 1) % len(key)		

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("usage: %s <input-file> <output-file> <key>" % sys.argv[0])
		sys.exit(1)		
	crypt(sys.argv[1], sys.argv[2], sys.argv[3])