def gen_tribonacci():
    a, b, c = 0, 0, 1
    while True:
        yield c
        a, b, c = b, c, a + b + c


def nth_tribonacci(n):
    m = matpow([[1, 1, 0],
                [1, 0, 1],
                [1, 0, 0]], n)
    return m[2][0]


def matpow(m, n):
    if n == 1:
        return m
    if n % 2:
        return matmult(m, matpow(matmult(m, m), n / 2))
    return matpow(matmult(m, m), n / 2)


def matmult(m1, m2):
    return [[dot(row, col) for col in zip(*m2)] for row in m1]


def dot(a, b):
    return sum([x * y for x, y in zip(a, b)])


def tribonacci_const(n):
    ts = take(n, gen_tribonacci())
    return float(ts[-1]) / ts[-2]


def take(n, g):
    result = []
    for _ in xrange(n):
        result.append(g.next())
    return result


if __name__ == '__main__':
    print(take(10, gen_tribonacci()))
    print(nth_tribonacci(8))
    print(tribonacci_const(1000))
