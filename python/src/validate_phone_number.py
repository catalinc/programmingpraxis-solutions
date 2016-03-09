#!/usr/bin/env python

# See http://programmingpraxis.com/2011/12/13/validating-telephone-numbers/

import unittest
import re

VALID_PATTERNS = ['^\d{10}$',
                  '^\d{3}-\d{3}-\d{4}$',
                  '^\d{3}\.\d{3}\.\d{4}$',
                  '^\(\d{3}\)\s?\d{3}-\d{4}$',
                  '^\d{3}-\d{4}$']


def is_valid(phone_number):
    for pattern in VALID_PATTERNS:
        if re.match(pattern, phone_number):
            return True
    return False


class Test(unittest.TestCase):

    def test_valid_phone_numbers(self):
        valid_phone_numbers = ['1234567890',
                               '123-456-7890',
                               '123.456.7890',
                               '(123)456-7890',
                               '(123) 456-7890',
                               '456-7890']
        for phone_number in valid_phone_numbers:
            if not is_valid(phone_number):
                self.fail("%s should be a valid" % phone_number)

    def test_invalid_phone_numbers(self):
        invalid_phone_numbers = ['123-45-6789',
                                 '123:4567890',
                                 '123/456-7890',
                                 '1234567890 ']
        for phone_number in invalid_phone_numbers:
            if is_valid(phone_number):
                self.fail("%s should be invalid" % phone_number)
 
if __name__ == '__main__':
    unittest.main()
