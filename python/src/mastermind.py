#!/usr/bin/python

import random
import sys

SYMBOLS = "123456"


def read_user_input(count=None):
    while True:
        s = raw_input("Your guess (q to quit): ")
        if s == "q":
            sys.exit()
        if count and len(s) != count:
            continue
        return s


def secret_code(count=4):
    L = []
    for _ in xrange(count):
        index = random.randint(0, len(SYMBOLS) - 1)
        L.append(SYMBOLS[index])
    return ''.join(L)


def game_loop():
    code = secret_code()
    print("Secret code set")
    attempts = 0
    while True:
        probe = read_user_input(len(code))
        attempts += 1
        black_hits, white_hits = score(probe, code)
        print("B" * black_hits + "W" * white_hits)
        if black_hits == len(code):
            print("Congratulations, you guess the code after %d attempts" % attempts)
            break


def score(probe, code):
    black_hits = 0
    for i, v in enumerate(probe):
        if probe[i] == code[i]:
            black_hits += 1
    total_hits = 0
    for c in SYMBOLS:
        total_hits += min(_count(c, probe), _count(c, code))
    return black_hits, total_hits - black_hits


def _count(c, s):
    count = 0
    for x in s:
        if x == c:
            count += 1
    return count


def main():
    while True:
        game_loop()
        s = raw_input("Another game ? ([y]/n) ")
        if s.startswith("n"):
            print("Bye")
            sys.exit()


if __name__ == "__main__":
    main()
