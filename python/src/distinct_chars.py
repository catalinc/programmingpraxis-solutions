# Solution to https://programmingpraxis.com/2017/05/09/distinct-characters/

import unittest


def has_distinct_chars(s):
    if not s:
        return False
    return len(set(s)) == len(s)


class Test(unittest.TestCase):
    def test_has_distinct_chars(self):
        for s in ('abc', 'Praxis', 'sdf'):
            self.assertTrue(has_distinct_chars(s), 'test failed for %s' % s)

    def test_has_not_distinct_chars(self):
        for s in ('Programming', 'derivatives', 'characters'):
            self.assertFalse(has_distinct_chars(s), 'test failed for %s' % s)

    def test_blank_string(self):
        self.assertFalse(has_distinct_chars(''))
        self.assertFalse(has_distinct_chars(None))


if __name__ == '__main__':
    unittest.main()
