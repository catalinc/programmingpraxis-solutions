# A solution for http://programmingpraxis.com/2012/08/21/two-more-random-exercises/

import math


def rand_middle_square(seed):
    n = seed
    seed_len = int(round(math.log(seed, 10)))
    while True:
        yield n
        n = (n * n) / (10 ** (seed_len / 2)) % (10 ** seed_len)


def randu(seed):
    n = seed
    while True:
        yield n
        n = (65539 * n) % 2147483648


def random(count, seed, rand_fn):
    nums = []
    random_gen = rand_fn(seed)
    for _ in xrange(count):
        nums.append(random_gen.next())
    return nums


print(random(5, 675248, rand_middle_square))
print(random(5, 7, randu))
