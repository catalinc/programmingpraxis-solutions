#!/usr/bin/env python

"""
Jai Alai game simulator
"""

import random

class Game(object):
    
    def __init__(self):
        self.teams = range(0, 8)
        self.scores = [0 for _ in range(0, 8)]
    
    def play(self):
        """
        Simulate a full game and return winner position
        """
        rounds = 0
        red = self.teams.pop(0)
        blue = self.teams.pop(0)
        while True:
            winner = None
            if random.random() > 0.5:
                winner = red
                self.teams.append(blue)
                blue = self.teams.pop(0)
            else:
                winner = blue
                self.teams.append(red)
                red = self.teams.pop(0)
            points = 1
            if rounds > 7:
                points = 2                    
            self.scores[winner] += points
            if self.scores[winner] >= 7:
                return winner            

def main(n):
    stats = [0 for _ in range(0, 8)]
    for i in range(0, n):
        winner = Game().play()
        stats[winner] += 1
    for i, v in enumerate(stats):
        print "%d -> %f" % (i, (float(v)/n)*100)

if __name__ == '__main__':
    main(1000000)                                     
        
