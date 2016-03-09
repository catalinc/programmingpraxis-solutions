#!/usr/bin/env python

"""
wc.py -- word count

wc.py [-lcw] [-f file]

Wc counts lines, words and characters in the named file,
or in the standard input if no file is specified. A word is a
maximal string of characters delimited by spaces, tabs or
newlines.

If the optional argument is present, just the specified
counts (lines, words, or characters) are selected by the
letters l, w or c.
"""

import sys
import getopt

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def count(input):
    lines, words, chars = 0, 0, 0
    in_word = False
    for line in input:
        lines += 1
        for ch in line:
            chars += 1
            if ch.isalnum():
                in_word = True
            elif in_word:
                words += 1
                in_word = False
    return lines, words, chars

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(sys.argv[1:], "lwcf:h", ["lines","words", "characters", "file=", "help"])
        except getopt.error, msg:
            raise Usage(msg)

        input = sys.stdin
        flags = []
        for o, v in opts:
            if o in ("-h", "--help"):
                print __doc__
                return 0
            if o in ("-l", "--lines"):
                flags.append((0, "line(s)"))
            if o in ("-w", "--words"):
                counters.append((1, "word(s)"))
            if o in ("-c", "--characters"):
                counters.append((2, "character(s)"))
            if o in ("-f", "--file"):
                input = open(v, 'r')

        if not flags:
            flags = [(0, "line(s)"), (1, "word(s)"), (2, "character(s)")]
            
        stats = count(input)
        for flag in flags:
            print "%d %s" % (stats[flag[0]], flag[1])

        return 0
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == '__main__':
    sys.exit(main())
