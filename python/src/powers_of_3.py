import math

# Solution to https://programmingpraxis.com/2016/03/01/powers-of-3/


def is_power_of_3_div(n):
    if n < 1:
        return False
    while n > 1:
        if n % 3 != 0:
            return False
        n /= 3
    return True


def is_power_of_3_log(n):
    if n < 1:
        return False
    p = math.log(n, 3)
    return not p - math.floor(p)


if __name__ == '__main__':
    test_data = [3, 9, 27, 81, 1, 8, 10, 1111, -3, 0]
    for n in test_data:
        print("%d div: %s log: %s" % (n, is_power_of_3_div(n), is_power_of_3_log(n)))
