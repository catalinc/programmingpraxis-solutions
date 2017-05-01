
# https://programmingpraxis.com/2017/04/28/abbreviated-sentences/

import unittest


def abbrev_word(w):
    if len(w) <= 1:
        return w
    return "{}{}{}".format(w[0], len(w) - 2, w[-1])


def abbrev_sentence(s):
    return ' '.join([abbrev_word(w) for w in s.split(' ')])


class Test(unittest.TestCase):

    def test_abbrev_word(self):
        self.assertEqual("", abbrev_word(""))
        self.assertEqual("P", abbrev_word("P"))
        self.assertEqual("P0s", abbrev_word("Ps"))
        self.assertEqual("P9g", abbrev_word("Programming"))

    def test_abbrev_sentence(self):
        self.assertEqual("", abbrev_sentence(""))
        self.assertEqual("I", abbrev_sentence("I"))
        self.assertEqual("P9g P4s", abbrev_sentence("Programming Praxis"))


if __name__ == '__main__':
    unittest.main()
