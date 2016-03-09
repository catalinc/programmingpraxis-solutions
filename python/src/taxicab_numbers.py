# See http://programmingpraxis.com/2012/11/09/taxicab-numbers/

from math import pow


def cubic_root(x):
    return int(round(pow(x, 1.0 / 3)))


def sum_of_cubes(x):
    result = []
    i = 1
    j = cubic_root(x)
    while i < j:
        s = i ** 3 + j ** 3
        if s == x:
            result.append((i, j))
            i += 1
            j -= 1
        elif s < x:
            i += 1
        else:
            j -= 1
    return result

print(sum_of_cubes(1729))
