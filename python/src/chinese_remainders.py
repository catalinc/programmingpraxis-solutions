#!/usr/bin/python


def solve(numbers, limit):
    n = 0
    sol = []
    while n <= limit:
        n += 1
        ok = True
        for t in numbers:
            if n % t[0] != t[1]:
                ok = False
                break
        if ok:
            sol.append(n)
    return sol

if __name__ == '__main__':
    sol = solve(((11, 10), (12, 4), (13, 12)), 2000)
    if sol:
        print "solutions: %s" % sol
    else:
        print "no solution"
