#!/usr/bin/python

import random

SYMBOLS = {
    0: 'BAR',
    1: 'BELL',
    2: 'ORANGE',
    3: 'LEMON',
    4: 'PLUM',
    5: 'CHERRY'
}


class SlotMachine(object):

    MIN_BET = 1
    MAX_BET = 100

    def __init__(self):
        self.bet = 0
        self.standings = 0

    def pull_arm(self):
        if self.bet < self.MIN_BET:
            print('Minimum bet is %d.' % self.MIN_BET)
        elif self.bet > self.MAX_BET:
            print('House limits are %d.' % self.MAX_BET)
        else:
            x, y, z = [random.randrange(1, 6) for _ in xrange(3)]
            print('%s %s %s' % (SYMBOLS[x], SYMBOLS[y], SYMBOLS[z]))
            if x == y == z == 0:
                print('*** Jackpot ***')
                self.standings += 101 * self.bet
            elif x == y == z:
                print('*** Top Dollar ***')
                self.standings += 11 * self.bet
            elif x == y == 0 or x == z == 0 or y == z == 0:
                print('*** Double Bar ***')
                self.standings += 6 * self.bet
            elif x == y or x == z or y == z:
                print('*** Double ***')
                self.standings += 3 * self.bet
            else:
                print('*** You Lose ***')
                self.standings -= self.bet
        self.bet = 0
        print('Your standings %d.' % self.standings)

    def set_bet(self, amount):
        self.bet = amount

    def cash_out(self):
        if self.standings == 0:
            print('Hey, you broke even !')
        elif self.standings > 0:
            print('Collect your winnings from the cashier.')
        else:
            print('Pay up ! Please leave you money on the terminal.')
        self.standings = 0


def game_loop():
    sm = SlotMachine()
    while True:
        try:
            amount = int(raw_input('Your bet ?\n'))
            sm.set_bet(amount)
            sm.pull_arm()
            if not raw_input('Again ?\n').lower().startswith('y'):
                break
        except ValueError:
            print('Invalid input.')
    sm.cash_out()


if __name__ == '__main__':
    print('''
    You are in the Casino in front of our one armed bandits. Bet from %d to %d.
    To pull the arm punch the return key after making you bet.
    '''
    % (SlotMachine.MIN_BET, SlotMachine.MAX_BET))
    game_loop()
