#!/usr/bin/env python

import sys


class Table(object):
    def __init__(self):
        self.colnames = []
        self.rows = []

    def join(self, other):
        """
        Natural join
        """
        result = Table()
        result.colnames = self.colnames + other.colnames[1:]
        result.rows = [r1 + r2[1:] for r1 in self.rows for r2 in other.rows if r1[0] == r2[0]]
        return result

    def show(self):
        for name in self.colnames:
            print "%6s" % name,
        print
        for row in self.rows:
            for value in row:
                print "%6s" % value,
            print


def load_table(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
        table = Table()
        table.colnames = lines[0].split()
        if len(lines) > 1:
            for i in range(1, len(lines)):
                table.rows.append(lines[i].split())
        return table

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "usage: ./natural_join.py file1 file2"
        sys.exit(1)

    table1 = load_table(sys.argv[1])
    table2 = load_table(sys.argv[2])

    print "table 1:"
    table1.show()
    print "table 2:"
    table2.show()

    table3 = table1.join(table2)

    print "join result:"
    if table3:
        table3.show()
