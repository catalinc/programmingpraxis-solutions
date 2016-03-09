import sys
from collections import Counter

# Solution to http://programmingpraxis.com/2014/11/11/favorite-color/

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as infile:
        c = Counter()
        for line in infile:
            line = line.rstrip()
            name, value = line.split(': ')
            if name == 'favoritecolor':
                c[value] += 1
        print(c.most_common(1))