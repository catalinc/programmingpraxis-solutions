#!/usr/bin/env python

# See http://programmingpraxis.com/2011/12/20/hangman/

import random
import sys


HANGMAN = [
"",
"""
 O
""",
"""
 O
 |
""",
"""
_O
 |
""",
"""
_O_
 |
""",
"""
_O_
 |
/
""",
"""
_O_
 |
/ \\
"""
]


def play_game():
    secret_word = random_word().upper()
    guessed_letters = set()
    failed_attempts = 0
    print_matches(secret_word, guessed_letters)
    while True:
        try:
            letter = raw_input("Your guess ? ").upper()
        except KeyboardInterrupt:
            exit_game()
        if letter in secret_word:
            guessed_letters.add(letter)
        else:
            failed_attempts += 1
        print_hangman(failed_attempts)
        if lose(failed_attempts):
            print("Sorry, you lose...")
            print("The word was: %s" % (" ".join(list(secret_word))))
            break
        print_matches(secret_word, guessed_letters)
        if win(secret_word, guessed_letters):
            print("You nail it !")
            break


def random_word(words_file='words.lst'):
    word = None
    n = 0
    with open(words_file) as f:
        for line in f:
            n += 1
            if random.random() < 1.0 / n:
                word = line
    return word


def print_matches(word, letters):
    out = []
    for l in word:
        if l in letters:
            out.append(l)
        else:
            out.append("_")
    print(" ".join(out))


def exit_game():
    print("Bye !")
    sys.exit(0)


def print_hangman(guess_attempts):
    print HANGMAN[guess_attempts]


def win(secret_word, guessed_letters):
    return len(secret_word) == len(guessed_letters)


def lose(failed_attempts):
    return failed_attempts == len(HANGMAN) - 1


if __name__ == '__main__':
    print("Let's play Hangman !")
    while True:
        play_game()
        if raw_input("Play another ? [Y]/N ").upper() == "N":
            exit_game()
