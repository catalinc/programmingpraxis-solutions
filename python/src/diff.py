#!/usr/bin/env python

import sys

from src import lcs


def diff(file1, file2):
    """
    Returns thes lines that differ between two files.
    This implementation works by computing the longest common subsequence (LCS) 
    between the two files and returning the lines that are part of LCS.
    """
    with open(file1) as f1:
        with open(file2) as f2:
            lines1 = [line.strip() for line in f1.readlines()]
            lines2 = [line.strip() for line in f2.readlines()]
            lcs_lines = lcs.lcs(lines1, lines2)
            diff1 = [line for line in lines1 if not line in lcs_lines]
            diff2 = [line for line in lines2 if not line in lcs_lines]
    return diff1, diff2

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "usage: ./diff.py file1 file2"
        sys.exit(1)
    diff1, diff2 = diff(sys.argv[1], sys.argv[2])
    if not (diff1 and diff2):
        print "files do not differ"
    else:
        for line in diff1:
            print ">%s" % line
        for line in diff2:
            print "<%s" % line
        
