import unittest
import sys

# https://programmingpraxis.com/2017/08/04/last-name-comma-first-name/

def convert_name(name):
    last_name, first_name = [s.strip() for s in name.split(',')]
    return '{0}, {1}'.format(first_name, last_name)


class Test(unittest.TestCase):

    def test_convert(self):
        test_data = [("Sr. Matthew, John", "John, Sr. Matthew"),
                     ("Barry , Matt", "Matt, Barry")]
        for name, expected in test_data:
            self.assertEqual(convert_name(name), expected)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
