#!/usr/bin/env python

import unittest

def lcs(s1, s2):
    """
    Compute the longest common subsequence between s1 and s2
    """
    mat = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])
    seq = []
    i = len(s1)
    j = len(s2)
    while i and j:
        if mat[i][j] > mat[i-1][j-1]:
            seq.append(s1[i-1])
        if i == j:
            i -= 1
            j -= 1
        elif i > j:
            i -= 1
        else:
            j -= 1
    seq.reverse()
    return seq

class Test(unittest.TestCase):

    def test_lcs(self):
        self.assertEqual(''.join(lcs('programming', 'praxis')), 'prai')

if __name__ == '__main__':
    unittest.main()

