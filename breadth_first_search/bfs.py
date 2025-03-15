import unittest

# reps 5

class Node:
    def __init__(self, data, neighbors):
        self.data = data
        self.neighbors = neighbors

def make_graph(pairs):
    g = {}
    for k, n in pairs:
        g[k] = Node(k, n)
    return g

def bfs(start, target, graph):
    explored = {}
    queue = [(start, 0)]

    while queue:
        key, depth = queue.pop()
        if key == target:
            return depth

        explored[key] = True
        nodes = graph[key].neighbors

        for node in nodes:
            if node not in explored:
                queue.append((node, depth+1))
        
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


