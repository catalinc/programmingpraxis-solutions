# Solution to http://programmingpraxis.com/2014/10/28/number-of-divisors-in-a-range/


def count_divisors_in_range(x, y, n):
    return (y - 1) / n - (x / n)


if __name__ == '__main__':
    print(count_divisors_in_range(1, 10, 3))
    print(count_divisors_in_range(100, 200, 7))