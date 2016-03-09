#!/usr/bin/env python

import unittest

def uniq(alist):
    set = {}
    return [set.setdefault(e,e) for e in alist if e not in set]

def partition(str, size):
    l = []
    for i in range(0, len(str), size):
        l.append(str[i:i+size])
    return l

class PlayfairCipher:
    
    def __init__(self, pass_phrase):
        letters = pass_phrase.upper() + ''.join([chr(x) for x in range(ord('A'), ord('Z')+1) if x != ord('J')])
        self.key = uniq(letters)

    def encrypt(self, text):
        
        words = text.upper().split()
        
        def encrypt_word(word):
            
            def split_digrams(str):
                all = []
                digram = []
                for c in str:
                    if c == 'J': c = 'I'
                    
                    if len(digram) == 1 and digram[0] == c:
                        digram.append('X')
                        all.append(''.join(digram))
                        digram = []
                        digram.append(c)
                    else:
                        digram.append(c)
                        
                    if len(digram) == 2:
                        all.append(''.join(digram))
                        digram = []
                        
                if len(digram) > 0:
                    all.append(''.join(digram))
        
                return all
            
            def encrypt_digram(digram):
                r0, c0 = self._row_col(digram[0])
                r1, c1 = self._row_col(digram[1])
                
                if r0 == r1:
                    c0 = (c0 + 1) % 5
                    c1 = (c1 + 1) % 5
                elif c0 == c1:
                    r0 = (r0 + 1) % 5
                    r1 = (r1 + 1) % 5
                else:
                    c0, c1 = c1, c0
        
                return "%s%s" % (self._letter_at(r0, c0), self._letter_at(r1, c1))
            
            encrypted_digrams = map(encrypt_digram, split_digrams(word))            
            return ''.join(encrypted_digrams)
    
        return ' '.join(map(encrypt_word, words))
    
    def decrypt(self, text):

        words = text.upper().split()
        
        def decrypt_word(word):

            def join_digrams(digrams):
                all = []
                for d in digrams:
                    if len(all) > 0:
                        last = all[-1]
                        if last[1] == 'X' and last[0] == d[0]:
                            all[-1] = last[0]
                    all.append(d)
                return ''.join(all)
            
            def decrypt_digram(digram):
                r0, c0 = self._row_col(digram[0])
                r1, c1 = self._row_col(digram[1])

                if r0 == r1:
                    c0 = (c0 - 1) % 5
                    c1 = (c1 - 1) % 5
                elif c0 == c1:
                    r0 = (r0 - 1) % 5
                    r1 = (r1 - 1) % 5
                else:
                    c0, c1 = c1, c0

                return "%s%s" % (self._letter_at(r0, c0), self._letter_at(r1, c1))
            
            decrypted_digrams = map(decrypt_digram, partition(word, 2))
            return join_digrams(decrypted_digrams)
        
        return ' '.join(map(decrypt_word, words))

    def _row_col(self, letter):
        i = self.key.index(letter)
        return i / 5, i % 5

    def _letter_at(self, row, col):
        return self.key[5 * row + col]
    
class PlayfairCipherTest(unittest.TestCase):
    def setUp(self):
        self.cipher = PlayfairCipher("PLAYFAIR")
    
    def test_encrypt(self):
        self.assertEquals(self.cipher.encrypt("PROGRAMMINGPRAXIS"), "LIVOBLKZEDOELIYWCN") 
    
    def test_decrypt(self):
        self.assertEquals(self.cipher.decrypt("LIVOBLKZEDOELIYWCN"), "PROGRAMMINGPRAXIS")      

if __name__ == "__main__":
    unittest.main()