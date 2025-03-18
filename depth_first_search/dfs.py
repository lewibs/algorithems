import unittest

# reps 3

class Node:
    def __init__(self, data, neighbors):
        self.data = data
        self.neighbors = neighbors

def make_graph(paris):
    g = {}
    for k, n in paris:
        g[k] = Node(k,n)
    return g

def dfs(start, target, graph):
    stack = [(start, 0)]
    explored = {}

    while stack:
        key, depth = stack.pop()
        if key == target:
            return depth
        node = graph[key]
        for n in node.neighbors:
            if n not in explored:
                stack.append((n, depth + 1))

    return -1



class TestDFS(unittest.TestCase):
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

    def test_dfs_found(self):
        self.assertEqual(dfs('A', 'F', self.graph), 2)  # A → C → F

    def test_dfs_same_node(self):
        self.assertEqual(dfs('A', 'A', self.graph), 0)  # Start and end are the same

    def test_dfs_not_found(self):
        self.assertEqual(dfs('A', 'Z', self.graph), -1)  # Z isn't in the graph

    def test_dfs_single_node(self):
        single_node_graph = make_graph([('X', [])])
        self.assertEqual(dfs('X', 'X', single_node_graph), 0)  # X → X (distance 0)


