# See http://programmingpraxis.com/2012/07/31/send-more-money-part-1/

import time
import itertools


def timeit(fn):
    def wrapper():
        start = time.clock()
        ret = fn()
        elapsed = time.clock() - start
        print("%s took %2.fs" % (fn.__name__, elapsed))
        return ret
    return wrapper


@timeit
def solve1():
    for s in xrange(1, 10):
        for e in xrange(0, 10):
            for n in xrange(0, 10):
                for d in xrange(0, 10):
                    for m in xrange(1, 10):
                        for o in xrange(0, 10):
                            for r in xrange(0, 10):
                                for y in xrange(0, 10):
                                    if distinct(s, e, n, d, m, o, r, y):
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
                                        if send + more == money:
                                            return send, more, money


def distinct(*args):
    return len(set(args)) == len(args)


@timeit
def solve2():
    letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y')
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sol['s'] == 0 or sol['m'] == 0:
            continue
        send = 1000 * sol['s'] + 100 * sol['e'] + 10 * sol['n'] + sol['d']
        more = 1000 * sol['m'] + 100 * sol['o'] + 10 * sol['r'] + sol['e']
        money = 10000 * sol['m'] + 1000 * sol['o'] + 100 * sol['n'] + 10 * sol['e'] + sol['y']
        if send + more == money:
            return send, more, money


print(solve1())
print(solve2())
