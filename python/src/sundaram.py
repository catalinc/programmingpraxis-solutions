#!/usr/bin/env python

import bitarray

def sundaram_sieve(n):
	ba = bitarray.bitarray(n+1)
	ba.setall(True)
	for i in xrange(1, n+1):
		k = i + i + 2*i*i
		while k <= n:
			ba[k] = False
			k += 2*i + 1
	L = [2]
	for i, v in enumerate(ba):
		if v:
			k = 2*i + 1
			if k > 1 and k <= n:
				L.append(k)
	return L

if __name__ == '__main__':
	for x in sundaram_sieve(1000):
		print x
