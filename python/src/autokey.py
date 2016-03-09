#!/usr/bin/env python

import unittest


class AutokeyCipher:
    """Implements AutoKey cipher."""

    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        def encrypt_letter(a, b):
            o = ord('A') + (ord(a) + ord(b) - 2 * ord('A')) % 26
            return chr(o)
        return self.__transform_text(encrypt_letter, text)

    def decrypt(self, text):
        def decrypt_letter(a, b):
            o = ord('A') + (ord(a) - ord(b) + 26) % 26
            return chr(o)
        return self.__transform_text(decrypt_letter, text)

    def __transform_text(self, fn, text):
        transformed = []
        for index, item in enumerate(text):
            transformed.append(fn(item.upper(), self.key[index % len(self.key)]))
        return "".join(transformed)


class TestAutokeyCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = AutokeyCipher("PRAXISACOLLECTIONOF")

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt("ACOLLECTIONOFETUDES"), "PTOITWCVWZYSHXBIQSX")

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt("PTOITWCVWZYSHXBIQSX"), "ACOLLECTIONOFETUDES")

if __name__ == "__main__":
    unittest.main()
