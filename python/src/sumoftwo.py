#!/usr/bin/python


def sum_of_two_ints(L, t):
    L.sort()
    i = 0
    while i < len(L) and L[i] < t:
        j = i + 1
        while j < len(L):
            v = L[i] + L[j]
            if v == t:
                return L[i], L[j]
            elif v > t:
                break
            j += 1
        i += 1
    return None


def sum_of_two_with_hash(L, t):
    D = {}
    for x in L:
        v = D.get(t-x)
        if v:
            return v, x
        D[x] = x
    return None


if __name__ == '__main__':
    L = [3, 5, 1, 8, 2]
    t = 4
    sol = sum_of_two_with_hash(L, t)
    if sol:
        print("Solution: %s" % str(sol))
    else:
        print("No solution")
