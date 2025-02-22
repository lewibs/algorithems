import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

def make_graph(node_neighbor_pairs):
    graph = {}
    for node, _ in node_neighbor_pairs:
        graph[node] = Node(node)
    
    for node, neighbors in node_neighbor_pairs:
        for n in neighbors:
            graph[node].neighbors.append(graph[n])

    return graph

def bfs(start, target, graph):
    e = {}
    q = [(graph[start], 0)]

    while len(q):
        n, dist = q.pop(0)

        if n.data == target:
            return dist

        e[n] = True
        for n in n.neighbors:
            if n not in e:
                q.append((n, dist+1))

    return -1


class TestBFS(unittest.TestCase):
    def setUp(self):
        # Create a sample graph
        self.graph = make_graph([
            ('A', ['B', 'C']),
            ('B', ['A', 'D', 'E']),
            ('C', ['A', 'F']),
            ('D', ['B']),
            ('E', ['B', 'F']),
            ('F', ['C', 'E'])
        ])

    def test_bfs_found(self):
        self.assertEqual(bfs('A', 'F', self.graph), 2)  # A → C → F

    def test_bfs_same_node(self):
        self.assertEqual(bfs('A', 'A', self.graph), 0)  # Start and end are the same

    def test_bfs_not_found(self):
        self.assertEqual(bfs('A', 'Z', self.graph), -1)  # Z isn't in the graph

    def test_bfs_single_node(self):
        single_node_graph = make_graph([('X', [])])
        self.assertEqual(bfs('X', 'X', single_node_graph), 0)  # X → X (distance 0)


