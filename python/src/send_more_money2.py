# See http://programmingpraxis.com/2012/08/03/send-more-money-part-2/

import random
import time


def random_solution(*words):
    solution = list(set(''.join(words)))
    if len(solution) < 10:
        for _ in xrange(len(solution), 10):
            solution.append("_")
    return solution


def number(word, solution):
    n = 0
    for letter in word:
        n = n * 10 + lookup(letter, solution)
    return n


def lookup(letter, solution):
    for i, l in enumerate(solution):
        if letter == l:
            return i


def score(solution, *words):
    nums = [number(word, solution) for word in words]
    return abs(sum(nums[:-1]) - nums[-1])


def alter_solution(solution, first_letters):
    altered = solution[:]
    i = random.randint(0, 9)
    j = random.randint(0, 9)
    altered[i], altered[j] = altered[j], altered[i]
    if altered[0] in first_letters:
        return solution
    return altered


def print_solution(solution, *words):
    nums = [str(number(word, solution)) for word in words]
    print("%s = %s" % (' + '.join(nums[:-1]), nums[-1]))


def solve(*words):
    start = time.clock()
    first_letters = set([word[0] for word in words])
    best_solution = random_solution(*words)
    best_score = score(best_solution, *words)
    while True:
        if best_score == 0:
            break
        alt_sol = alter_solution(best_solution, first_letters)
        alt_score = score(alt_sol, *words)
        if alt_score < best_score or random.randint(1, 100) == 1:
            best_score = alt_score
            best_solution = alt_sol
    print_solution(best_solution, *words)
    print("%.2f" % (time.clock() - start))

solve('send', 'more', 'money')
solve('cross', 'roads', 'danger')
solve('green', 'orange', 'colors')
solve('taurus', 'pisces', 'scorpio')
solve('fifty', 'states', 'america')
solve('this', 'size', 'short')
solve('lynne', 'looks', 'sleepy')
solve('nine', 'fine', 'wives')
solve('ted', 'has', 'good', 'taste')
