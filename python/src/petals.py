#!/usr/bin/env python

# Solution for http://programmingpraxis.com/2012/12/18/petals-around-the-rose/

import random


def count_petals(dice):
    if dice % 2:
        return dice - 1
    return 0


def score(dice):
    return reduce(lambda acc, d: acc + count_petals(d), dice, 0)


def play_game():
    print("""
Let's play 'Petals Around The Rose.'
The name of the game is significant.
At each turn I will roll five dice,
then ask you for the score, which
will always be zero or an even number.
After you guess the score, I will tell
you if you are right, or tell you the
correct score if you are wrong. The game
ends when you prove that you know the
secret by guessing the score correctly
six times in a row.
""")
    guesses_in_a_row = 0
    while guesses_in_a_row < 6:
        dice = randints(5, 1, 6)
        print("The five dice are: %s" % (' '.join(map(str, dice))))
        guess = int(raw_input("What is the score? "))
        correct_score = score(dice)
        if guess == correct_score:
            print("Correct")
            guesses_in_a_row += 1
        else:
            print("The correct score is %d" % correct_score)
            guesses_in_a_row = 0
    print("""
Congratulations! You are now a member
of the Fraternity of the Petals Around
The Rose. You must pledge never to
reveal the secret to anyone.
""")


def randints(count, min, max):
    return [random.randint(min, max) for _ in xrange(count)]


if __name__ == '__main__':
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nBye")
