# Solution to https://programmingpraxis.com/2017/05/05/calculating-derivatives/


def make_derivative(fn, dx=0.0000001):
    def derivative(x):
        return (fn(x + dx) - fn(x)) / dx
    return derivative


if __name__ == '__main__':
    def cube(x):
        return x * x * x
    d = make_derivative(cube)
    for x in (2, 3, 4):
        print('d(%d) = %f' % (x, d(x)))
