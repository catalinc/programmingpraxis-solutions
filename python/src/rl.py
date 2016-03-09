#!/usr/bin/env python

import unittest

def encode(input):    
    out = []
    last = ''
    count = 0
    for c in input:
        if count == 0:
            last = c
            count = 1
        elif last == c:
            count += 1
            if count == 26:
                out.append('~' + chr(ord('A') + count - 1) + last)
                last = ''
                count = 0
        else:
            if count == 1 and last == '~':
                out.append('~A~')
            elif count >= 4:
                out.append('~' + chr(ord('A') + count - 1) + last)
            else:
                out.append(last*count)
            last = c
            count = 1

    if count >= 4:
        out.append('~' + chr(ord('A') + count - 1) + last)
    else:
        out.append(last*count)
        
    return ''.join(out)

def decode(input):
    out = []
    run = []
    
    for c in input:
        if c == '~' and len(run) == 0:
            run = ['~']
        elif len(run) >= 1:
            run.append(c)
            if len(run) == 3:
                l = ord(run[1]) - ord('A') + 1
                if l == 1:
                    out.append('~')
                else:
                    out.append(run[2]*l)
                run = []
        else:
            out.append(c)
            
    return ''.join(out)

class TestRL(unittest.TestCase):
    
    def test_encode(self):
        self.assertEquals("ABBB~A~C~ED~ZE~DE",
                          encode("ABBB~CDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"))
    
    def test_decode(self):
        self.assertEquals("ABBB~CDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
                          decode("ABBB~A~C~ED~ZE~DE"))

if __name__ == "__main__":
    unittest.main()

