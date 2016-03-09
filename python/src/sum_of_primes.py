# Solution for
# http://programmingpraxis.com/2012/09/11/the-sum-of-the-first-billion-primes/

import time


def primes():
    yield 2
    yield 3
    stack = [3]
    while True:
        n = stack[-1] + 2
        is_prime = False
        while not is_prime:
            is_prime = True
            for p in stack:
                if p * p > n:
                    break
                if n % p == 0:
                    is_prime = False
                    break
            if is_prime:
                stack.append(n)
            else:
                n += 2
        yield stack[-1]


def sum_primes(n):
    result = 0
    count = 0
    for p in primes():
        result += p
        count += 1
        if count == n:
            break
    return result


if __name__ == '__main__':
    start = time.clock()
    print(sum_primes(1000000))
    print("elapsed %.2fs" % (time.clock() - start))
