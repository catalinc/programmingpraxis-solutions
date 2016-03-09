#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import random
from math import sqrt
import psyco

psyco.full()


def compute_pi_monte_carlo(radius=1000.0, num_points=1000000, epsilon=.001):
    points_in_circle = 0
    max_radius = radius + epsilon
    for i in range(0, num_points):
        x = random() * radius
        y = random() * radius
        if sqrt(x **2 + y**2) < max_radius:
            points_in_circle += 1
    return  float(points_in_circle *4) / num_points


def compute_pi_arhimedes(n=6):

    def inside_perimeter(k):
        if k == 2:
            return 4 * (1.0 / sqrt(2))
        else:
            return sqrt(inside_perimeter(k -1) * outside_perimeter(k))

    def outside_perimeter(k):
        if k == 2:
            return 4 * 1.0
        else:
            prev_inside = inside_perimeter(k -1)
            prev_outside = outside_perimeter(k -1)
            return 2 * prev_inside * prev_outside / (prev_inside + prev_outside)

    return inside_perimeter(n), outside_perimeter(n)

if __name__ == "__main__":
    print("PI Monte Carlo: %f" % (compute_pi_monte_carlo()))
    print("PI Arhimedes: %f, %f" % compute_pi_arhimedes(12))
