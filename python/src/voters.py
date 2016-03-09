#!/usr/bin/python

# See http://programmingpraxis.com/2012/04/06/voters/

import random
import sys


def simulate(rows, cols):
    turn = 0
    grid = [[random.choice([0, 1]) for _ in xrange(cols)] for _ in xrange(rows)]
    while not totalitarism(grid):
        show(turn, grid)
        for r in xrange(rows):
            for c in xrange(cols):
                grid[r][c] = random.choice(neighbours(r, c, grid))[2]
        turn += 1
    show(turn, grid)


def totalitarism(grid):
    v = grid[0][0]
    for line in grid:
        for cell in line:
            if cell != v:
                return False
    return True


def neighbours(row, col, grid):
    width = len(grid[0])
    height = len(grid)
    ret = []
    for i in (-1, 0, 1):
        r = (row + i) % height
        for j in (-1, 0, 1):
            c = (col + j) % width
            if r != row and c != col:
                ret.append((r, c, grid[r][c]))
    return tuple(ret)


def show(turn, grid):
    out = ["\n\nturn = %d\n\n" % turn]
    for row in grid:
        out.append(' '.join(map(str, row)))
    print '\n'.join(out)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: %s ROWS COLS" % (sys.argv[0]))
        sys.exit(1)
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    simulate(rows, cols)
