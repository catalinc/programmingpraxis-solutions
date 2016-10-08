import unittest


# Solution to programmingpraxis.com/2016/04/08/google-interview-question/


def max_len_product_bf(words):
    r = ()
    for i in range(0, len(words) - 1):
        s = words[i]
        for j in range(i + 1, len(words)):
            t = words[j]
            if not share_letters(s, t):
                p = len(s) * len(t)
                if not r:
                    r = (s, t, p)
                elif p > r[2]:
                    r = (s, t, p)
    return r


def share_letters(s, t):
    for c in s:
        if c in t:
            return True
    return False


class Test(unittest.TestCase):

    def test_share_letters(self):
        self.assertTrue(share_letters('ABCW', 'ABCDEF'))

    def test_not_share_letters(self):
        self.assertFalse(share_letters('BAZ', 'XFTN'))

    def test_max_len_product_empty_word_list(self):
        self.assertEqual((), max_len_product_bf([]))

    def test_max_len_product(self):
        r = max_len_product_bf(['ABCW', 'BAZ', 'FOO', 'BAR', 'XTFN'])
        self.assertEqual(('ABCW', 'XTFN', 16), r)


if __name__ == '__main__':
    unittest.main()
