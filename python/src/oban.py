#!/usr/bin/env python

# See http://programmingpraxis.com/2010/10/01/oban-numbers/

import unittest

MILLION = 1000000
BILLION = 1000000000
TRILLION = 1000000000000
QUADRILLION = 1000000000000000
QUINTILLION = 1000000000000000000


ONES = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
}

TENS = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

GROUPS = {
    100: 'hundred',
    1000: 'thousand',
    MILLION:  'million',
    BILLION:  'billion',
    TRILLION:  'trillion',
    QUADRILLION:  'quadrillion',
    QUINTILLION:  'quintillion'
}


def is_oban(n):
    return not 'o' in number_to_word(n)


def number_to_word(n):
    if n < 20:
        ret = ONES[n]
    elif n < 100:
        ret = TENS[n - (n % 10)] + " " + number_to_word(n % 10)
    else:
        b = _base_unit(n)
        ret = number_to_word(n // b) + " " + GROUPS[b] + " " + number_to_word(n % b)
    return ret.rstrip()


def _base_unit(n):
    if n < 1000:
        return 100
    elif n < MILLION:
        return 1000
    elif n < BILLION:
        return MILLION
    elif n < TRILLION:
        return BILLION
    elif n < QUADRILLION:
        return TRILLION
    elif n < QUINTILLION:
        return QUADRILLION
    else:
        return QUINTILLION


class Test(unittest.TestCase):

    def test_number_to_word(self):
        test_data = ((0, ''),
                     (9, 'nine'),
                     (100, 'one hundred'),
                     (123, 'one hundred twenty three'),
                     (85, 'eighty five'),
                     (121, 'one hundred twenty one'),
                     (4024, 'four thousand twenty four'),
                     (1000123, 'one million one hundred twenty three'),
                     (5534210, 'five million five hundred thirty four thousand two hundred ten'))
        for number, expected_word in test_data:
            self.assertEqual(expected_word, number_to_word(number))

    def test_oban_numbers_between_1_and_1000(self):
        count = 0
        for x in range(1, 1000):
            if is_oban(x):
                count += 1
        self.assertEqual(454, count)


if __name__ == '__main__':
    unittest.main()
