# See http://programmingpraxis.com/2012/05/25/ackermanns-function/

import sys
import time
from decimal import Decimal


def ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    raise ValueError("invalid arguments m=%d, n=%d" % (m, n))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: %s m n" % sys.argv[0])
        sys.exit(1)

    m = Decimal(sys.argv[1])
    n = Decimal(sys.argv[2])
    try:
        sys.setrecursionlimit(10000)
        start = time.time()
        r = ack(m, n)
        duration = time.time() - start
        print("ack(%d, %d) = %d [%d s]" % (m, n, r, duration))
    except Exception, e:
        print("error: %s" % e)
