#!/usr/bin/env python

def solve():
    S = 711
    P = 711 * 1e6
    divs = [i for i in range(1, S+1) if P % i == 0]
    for a in divs:
        for b in divs:
            for c in divs:
                for d in divs:
                    if b <= a and c <= b and d <= c:
                        s = a + b + c + d
                        p = a * b * c * d
                        if s == S and p == P:
                            return a, b, c, d

if __name__ == '__main__':
    print solve()
