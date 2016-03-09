#!/usr/bin/env python

matrix = """
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
17 18 19 20
"""


def unwrap(m):
    m = [[n for n in line.split()] for line in m.split('\n') if line]
    unwrap = []
    unwrap.extend(m[0])
    m = m[1:]
    while m:
        # rotate matrix ccw
        m = [[n for n in reversed(line)] for line in m]
        m = [[l[i] for l in m] for i in range(0, len(m[0]))]
        unwrap.extend(m[0])
        m = m[1:]
    return unwrap

if __name__ == '__main__':
    print unwrap(matrix)
