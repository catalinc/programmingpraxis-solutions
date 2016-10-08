import sys

# Solution to https://programmingpraxis.com/2016/05/10/concatenate-n-n-times/

if __name__ == '__main__':
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        print(str(n) * n)
