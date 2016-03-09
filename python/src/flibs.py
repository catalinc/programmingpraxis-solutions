# See http://programmingpraxis.com/2012/07/13/the-evolution-of-flibs/

import random
import time


def random_flib(states, symbols):
    flib = []
    for _ in xrange(len(states) * len(symbols)):
        flib.append("%s%s" % (random.choice(symbols), random.choice(states)))
    return ''.join(flib)


def random_population(size, states, symbols):
    population = []
    for _ in xrange(size):
        population.append(random_flib(states, symbols))
    return population


def mutate(flib, states, symbols):
    locus = random.randint(0, len(flib) - 1)
    if locus % 2 == 0:
        gene = random.choice(symbols)
    else:
        gene = random.choice(states)
    return flib[0:locus] + gene + flib[locus + 1:]


def crossover(flib1, flib2):
    start = random.randint(0, len(flib1) - 2)
    end = random.randint(start + 1, len(flib1) - 1)
    return flib1[:start] + flib2[start:end] + flib1[end:]


def run_flib(flib, input, states, symbols):
    sm = build_state_machine(flib, states, symbols)
    result = []
    state = 'A'
    for symbol in input:
        state, output = sm[(state, symbol)]
        result.append(output)
    return ''.join(result)


def build_state_machine(flib, states, symbols):
    sm = {}
    for state, outputs in zip(states, chunks(flib, len(states))):
        for input, output in zip(symbols, chunks(outputs, len(symbols))):
            sm[(state, input)] = tuple(reversed(list(output)))
    return sm


def score(input, output):
    matches = 0
    for i in xrange(len(input)):
        if input[i] == output[i]:
            matches += 1
    return int(100 * (matches / len(input)))


def rshift(s, count=1, pad='0'):
    return pad * count + s[0:-count]


def chunks(l, n):
    return [l[i:i + n] for i in xrange(0, len(l), n)]


def evolve(states,
           symbols,
           population_size,
           breed_chance,
           max_generations,
           input):
    population = [{'flib': flib, 'score': 0, 'output': ''}
                  for flib in random_population(population_size, states, symbols)]
    count = 1
    best = {}
    while count <= max_generations:
        for i in xrange(len(population)):
            population[i]['output'] = rshift(run_flib(population[i]['flib'], input, states, symbols))
            population[i]['score'] = score(input, population[i]['output'])
        population.sort(key=lambda d: d['score'], reverse=True)

        best = population[0]
        if best['score'] == 100:
            break
        worst = population[-1]
        if random.random() * 100 < breed_chance:
            offspring = crossover(best['flib'], worst['flib'])
            population.pop()
            population.append({'flib': offspring, 'score': 0, 'output': ''})

        i = random.randint(0, len(population) - 1)
        population[i]['flib'] = mutate(population[i]['flib'], states, symbols)

        count += 1
    return best, count

if __name__ == '__main__':
    start = time.clock()
    best, generations = evolve("ABCD", "01", 10, 30, 100, "010011")
    print("best=%s generations=%d time=%.2fs" % (best, generations, time.clock()-start))
