# See http://programmingpraxis.com/2012/08/10/minimum-scalar-product/

import itertools


def product(v1, v2):
    return reduce(lambda acc, t: acc + t[0] * t[1], zip(v1, v2), 0)


def solve(v1, v2):
    min_product = product(v1, v2)
    for p1 in itertools.permutations(v1):
        for p2 in itertools.permutations(v2):
            prod = product(p1, p2)
            if prod < min_product:
                min_product = prod
    return min_product

print(solve((1, 3, -5), (-2, 4, 1)))
print(solve((1, 2, 3, 4, 5),  (1, 0, 1, 0, 1)))