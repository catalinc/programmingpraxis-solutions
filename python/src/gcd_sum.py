import unittest
import sys


# Solution to https://programmingpraxis.com/2016/04/22/gcd-sum/


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def sum_gcd(n):
    r = 0
    for k in xrange(1, n + 1):
        r += gcd(k, n)
    return r


class Test(unittest.TestCase):
    def test_coprime(self):
        self.assertEqual(1, gcd(6, 35))

    def test_gcd(self):
        self.assertEqual(12, gcd(36, 48))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage %s: N1 N2...' % sys.argv[0])
        sys.exit(1)
    for s in sys.argv[1:]:
        n = int(s)
        print('%d %d' % (n, sum_gcd(n)))
