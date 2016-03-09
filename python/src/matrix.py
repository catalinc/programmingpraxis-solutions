#!/usr/bin/env python

import unittest
import numbers

class Matrix(object):
    
    def __init__(self, rows, cols, init=0):
        if rows < 0 or cols < 0:
            raise ValueError("invalid dimensions: rows: %d, cols %d" % (rows, cols))
        self.matrix = [[init for _ in range(0, cols)] for _ in range(0, rows)]
    
    def dimensions(self):
        if self.matrix:
            return (len(self.matrix), len(self.matrix[0]))
        else:
            return (0, 0)

    def get(self, row, col):
        self._check(row, col)
        return self.matrix[row][col] 
    
    def set(self, row, col, val):
        self._check(row, col)
        self.matrix[row][col] = val
    
    def _check(self, row, col):
        rows, cols = self.dimensions()
        if row < 0 or col < 0 or row > rows or col > cols:
            raise IndexError("row: %d, col: %d" % (row, col))

    def transpose(self):
        rows, cols = self.dimensions()
        r = Matrix(cols, rows)
        for i in range(rows):
            for j in range(cols):
                r.set(j, i, self.get(i, j))
        return r

    def __add__(self, other):
        if self.dimensions() != other.dimensions():
            raise ValueError("different dimensions")
        rows, cols = self.dimensions()
        r = Matrix(rows, cols)
        for i in range(rows):
            for j in range(cols):
                v = self.get(i, j) + other.get(i, j)
                r.set(i,j,v)
        return r

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            rows, cols = self.dimensions()
            r = Matrix(rows, cols)
            for i in range(rows):
                for j in range(cols):
                    r.set(i, j, other * self.get(i, j))
            return r
        else:
            rows1, cols1 = self.dimensions()
            rows2, cols2 = other.dimensions()
            if cols1 != rows2:
                raise ValueError("invalid dimensions: %s %s" % (self.dimensions(), other.dimensions()))
            r = Matrix(rows1, cols2)
            for i in range(rows1):
                for j in range(cols2):
                    v = 0
                    for k in range(0, cols1):
                        v += self.get(i, k) * other.get(k, j)
                    r.set(i, j, v)
            return r
        
    def __eq__(self, other):
        if self.dimensions() != other.dimensions():
            return False
        rows, cols = self.dimensions()
        for i in range(rows):
            for j in range(cols):
                if self.get(i, j) != other.get(i, j):
                    return False
        return True
    
    def __str__(self):
        return '\n'.join([' '.join(str(e) for e in row) for row in self.matrix])


class Test(unittest.TestCase):
    
    def test_empty(self):
        m = Matrix(0, 0)
        self.assertEquals((0, 0), m.dimensions())
    
    def test_init(self):
        m = Matrix(5, 4, 1)
        rows, cols = m.dimensions()
        self.assertEquals(5, rows)
        self.assertEquals(4, cols)
    
    def test_get(self):
        m = Matrix(2, 3, 2)
        self.assertEquals(2, m.get(1, 1))
        invalid = [(-1, 2), (3, 1), (1, 4)]
        for x in invalid:
            try:
                m.get(x[0], x[1])
                self.fail("%s should be invalid" % x)
            except IndexError:
                pass

    def test_set(self):
        m = Matrix(5, 5, 5)
        
        m.set(2, 3, 4)
        self.assertEquals(4, m.get(2, 3))
        
        invalid = [(-1, 1), (7, 1), (1, 10)]
        for x in invalid:
            try:
                m.set(x[0], x[1], 10)
                self.fail("%s should be invalid" % x)
            except IndexError:
                pass    
    
    def test_add(self):
        m1 = Matrix(2, 2, 1)
        m2 = Matrix(2, 2, 2)
        
        self.assertEquals(Matrix(2, 2, 3), m1 + m2)

        try:
            m1 + Matrix(2, 3, 2)
            self.fail("matrix add")
        except ValueError:
            pass
    
    def test_multiply(self):
        m1 = Matrix(2, 3, 1)
        m2 = Matrix(3, 4, 1)
        
        m3 = m1 * m2
        self.assertEquals(m3.dimensions()[0], m1.dimensions()[0])
        self.assertEquals(m3.dimensions()[1], m2.dimensions()[1])
        
        expected1 = Matrix(2, 4, 3)
        self.assertEquals(expected1, m3)
        
        m4 = m1 * 11
        expected2 = Matrix(2, 3, 11)
        self.assertEquals(expected2, m4)
        
        try:
            m1 * Matrix(2, 4, 123)
            self.fail("matrix multiply")
        except ValueError:
            pass

    def test_transpose(self):
         m = Matrix(2, 3, 1)
         t = m.transpose()
         
         self.assertEquals(t.dimensions()[0], m.dimensions()[1])
         self.assertEquals(t.dimensions()[1], m.dimensions()[0])
         
         self.assertEquals(1, t.get(1, 1))
    
if __name__ == '__main__':
    unittest.main()
