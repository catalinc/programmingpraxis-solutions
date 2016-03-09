#!/usr/bin/env python

# See http://programmingpraxis.com/2012/11/27/amazon-interview-question/

import random
import time


def distance_from_origin(x, y):
    return abs(x) + abs(y)  # Manhattan distance


def random_points(num_points, max_x, max_y):
    points = []
    for _ in xrange(num_points):
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        points.append((x, y))
    return points


def closest_to_origin(num_points, points):
    result = []
    for p in points:
        d = distance_from_origin(*p)
        _insert(result, p, d)
        if len(result) > num_points:
            result = result[0:num_points]
    return result


def _insert(points, point, distance):
    if points and distance > points[-1][0]:
        return
    i = 0
    while i < len(points):
        if distance <= points[i][0]:
            break
        i += 1
    points.insert(i, (distance, point))


if __name__ == '__main__':
    start = time.clock()
    points = random_points(1000000, 10000, 10000)
    print("closest to origin:\n%s" %
          '\n'.join(map(str, closest_to_origin(100, points))))
    print("%f s" % (time.clock() - start))
