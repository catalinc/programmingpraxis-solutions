# See http://programmingpraxis.com/2012/07/24/zeckendorf-representation/


def fibs(n):
    fs = [1]
    f = 1
    while f <= n:
        fs.append(f)
        f = fs[-1] + fs[-2]
    return fs


def zeckendorf(n):
    fs = fibs(n)
    fs.reverse()
    result = []
    while n > 0:
        for f in fs:
            if f <= n:
                result.append(f)
                n -= f
    result.reverse()
    return result


def solve(n):
    print("%d = %s" % (n, ' + '.join(map(str, zeckendorf(n)))))


solve(100)
