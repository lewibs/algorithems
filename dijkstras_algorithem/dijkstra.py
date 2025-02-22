import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = []  # List of (neighbor, cost) pairs


def get_next_unexplored(unexplored, dists):
    unexplored.sort(key=lambda n: dists.get(n, float('inf')), reverse=True)
    return unexplored.pop()

def dijkstra(start, target, graph):
    if target not in graph:
        return -1

    dists = {}
    explored = {}
    unexplored = [graph[start]]
    dists[graph[start]] = 0

    while len(unexplored):
        n = get_next_unexplored(unexplored, dists)
        explored[n] = True

        if n == graph[target]:
            return dists[n]

        for next_n, cost in n.adjacent:
            if next_n in explored:
                continue

            if next_n in dists:
                dist_from_here = dists[n] + cost
                if dist_from_here < dists[next_n]:
                    dists[next_n] = dist_from_here
            else:
                dists[next_n] = dists[n] + cost
            
            
            unexplored.append(next_n)

    return -1


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        # Create a simple graph
        self.graph = {
            'A': Node('A'),
            'B': Node('B'),
            'C': Node('C'),
            'D': Node('D'),
            'E': Node('E')
        }

        # Add edges with weights
        self.graph['A'].adjacent = [(self.graph['B'], 1), (self.graph['C'], 4)]
        self.graph['B'].adjacent = [(self.graph['C'], 2), (self.graph['D'], 5)]
        self.graph['C'].adjacent = [(self.graph['D'], 1)]
        self.graph['D'].adjacent = [(self.graph['E'], 3)]
        self.graph['E'].adjacent = []

    def test_shortest_path(self):
        self.assertEqual(dijkstra('A', 'E', self.graph), 7)  # A → B → C → D → E

    def test_same_node(self):
        self.assertEqual(dijkstra('A', 'A', self.graph), 0)  # Start == Target

    def test_unreachable_node(self):
        self.assertEqual(dijkstra('A', 'Z', self.graph), -1)  # 'Z' isn't in graph

    def test_direct_path(self):
        self.assertEqual(dijkstra('A', 'B', self.graph), 1)  # A → B (direct edge)

    def test_longer_path(self):
        self.assertEqual(dijkstra('B', 'E', self.graph), 6)  # B → C → D → E
