import unittest

# Solution to https://programmingpraxis.com/2016/04/12/titlecase/


def title_case(s):
    r = []
    prev = None
    for c in s:
        if c.isspace():
            r.append(c)
        elif prev is None or prev.isspace():
            r.append(c.upper())
        else:
            r.append(c.lower())
        prev = c
    return ''.join(r)


class Test(unittest.TestCase):

    def test_title_case_empty_string(self):
        self.assertEqual('', title_case(''))

    def test_title_case(self):
        self.assertEqual('Programming Praxis', title_case('programming PRAXIS'))


if __name__ == '__main__':
    unittest.main()
