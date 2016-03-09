#!/usr/bin/python

import unittest
import bst


KEYPAD = (
        ('ABC', 2),
        ('DEF', 3),
        ('GHI', 4),
        ('JKL', 5),
        ('MNO', 6),
        ('PQRS', 7),
        ('TUV', 8),
        ('WXYZ', 9),
        (' ', 0))


T9 = {}
for s, d in KEYPAD:
    for i, c in enumerate(s):
        T9[c] = ('%d' % d) * (i + 1)


def buy(L, C):
    bt = bst.BinarySearchTree(sort_key=lambda t: t[1])
    for i, v in enumerate(L):
        bt.insert((i, v))
    for i, v in enumerate(L):
        d = C - v
        if d > 0:
            bt.pop(v)
            try:
                j, _ = bt.find(d)
                i += 1
                j += 1
                if i < j:
                    return i, j
                return j, i
            except KeyError:
                bt.insert((i, v))


def reverse_words(s):
    a = list(s)
    reverse_word(a, 0, len(a))
    start = 0
    end = 0
    while start < len(a):
        while end < len(a) and a[end] != ' ':
            end += 1
        reverse_word(a, start, end)
        end += 1
        start = end
    return ''.join(a)


def reverse_word(a, start, end):
    end -= 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1


def t9_spelling(s):
    L = []
    for c in s.upper():
        if L and L[-1][-1] == T9[c][0] and c != ' ':
            L.append(' ')
        L.append(T9[c])
    return ''.join(L)


class Test(unittest.TestCase):

    def test_buy_1(self):
        self.assertEqual((2, 3), buy([5, 75, 25], 100))

    def test_buy_2(self):
        self.assertEqual((1, 4), buy([150, 24, 79, 50, 88, 345, 3], 200))

    def test_buy_3(self):
        self.assertEqual((4, 5), buy([2, 1, 9, 4, 4, 56, 90, 3], 8))

    def test_reverse_words_1(self):
        self.assertEqual("test a is this", reverse_words("this is a test"))

    def test_reverse_words_2(self):
        self.assertEqual("foobar", reverse_words("foobar"))

    def test_t9_spelling_1(self):
        self.assertEqual('2 2', t9_spelling("aa"))
        self.assertEqual("22", t9_spelling('b'))
        self.assertEqual("44 444", t9_spelling('hi'))

    def test_t9_spelling_2(self):
        self.assertEqual('333666 6660022 2777', t9_spelling('foo  bar'))
        self.assertEqual("4433555 555666096667775553",
                        t9_spelling("hello world"))


if __name__ == '__main__':
    unittest.main()
