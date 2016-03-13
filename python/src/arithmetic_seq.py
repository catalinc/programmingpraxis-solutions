# Solution to https://programmingpraxis.com/2016/02/23/arithmetic-sequence/


def is_arithmetic_seq(l):
    if len(l) >= 2:
        l.sort()
        last_diff = l[1] - l[0]
        for i in xrange(2, len(l)):
            diff = l[i] - l[i - 1]
            if diff != last_diff:
                return False
    return True


def is_arithmetic_seq_fast(l):
    m = min(l)
    s = sum(l)
    n = len(l)
    return (s - n * m) % ((n * (n - 1)) / 2) == 0


if __name__ == '__main__':
    test_data = [[1, 2, 3, 4, 5],
                 [3, 2, 5, 1, 4],
                 [1, 2, 4, 8, 16]]
    for l in test_data:
        print(is_arithmetic_seq_fast(l))
