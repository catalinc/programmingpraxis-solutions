# Solution to http://programmingpraxis.com/2012/10/09/two-word-games/


def is_sorted(seq):
    last = None
    for x in seq:
        if last is None:
            last = x
        else:
            if x < last:
                return False
            last = x
    return True


def vowels(s):
    return reduce(lambda s, c: s + c if c in 'aeiou' else s, s, '')


def map_file(fn, filename):
    result = []
    with open(filename) as infile:
        for line in infile:
            line = line.strip()
            if fn(line):
                result.append(line)
    return result


def exercise1(filename):
    def fn(line):
        return len(line) > 5 and vowels(line) == 'aeiou'
    return map_file(fn, filename)


def exercise2(filename):
    def fn(line):
        return len(line) > 5 and is_sorted(line)
    return map_file(fn, filename)


from pprint import pprint
pprint(exercise1('words.lst'))
pprint(exercise2('words.lst'))
