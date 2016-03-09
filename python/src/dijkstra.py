#!/usr/bin/python

import unittest
import sys


class Graph(object):

    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, dist):
        self.edges.setdefault(u, {})[v] = dist

    def neighbours(self, u):
        return self.edges.get(u, {}).keys()

    def distance(self, u, v):
        return self.edges.get(u, {}).get(v, sys.maxint)

    def vertices(self):
        vertices = set(self.edges.keys())   # add source vertices
        for d in self.edges.values():
            vertices.update(d.keys())       # add target vertices
        return vertices


def shortest_path(graph, source, target):
    distance = {}
    previous = {}

    vertices = graph.vertices()
    for v in vertices:
        distance[v] = sys.maxint
        previous[v] = None

    distance[source] = 0

    while vertices:
        min_dist = sys.maxint
        u = None
        for v in vertices:
            if distance[v] <= min_dist:
                u = v
                min_dist = distance[v]
        if distance[u] == sys.maxint:
            break  # no path
        vertices.remove(u)
        for v in graph.neighbours(u):
            if v in vertices:
                alt = distance[u] + graph.distance(u, v)
                if alt < distance[v]:
                    distance[v] = alt
                    previous[v] = u
    u = target
    path = []
    while u:
        path.insert(0, u)
        u = previous.get(u, None)

    return path, distance[target]


class Test(unittest.TestCase):

    def test_dijskstra(self):
        g = Graph()
        g.add_edge('a', 'c', 2)
        g.add_edge('a', 'd', 6)
        g.add_edge('b', 'a', 3)
        g.add_edge('b', 'd', 8)
        g.add_edge('c', 'd', 7)
        g.add_edge('c', 'e', 5)
        g.add_edge('d', 'e', 10)

        self.assertEqual((['a', 'c', 'e'], 7), shortest_path(g, 'a', 'e'))

if __name__ == '__main__':
    unittest.main()
