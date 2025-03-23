import unittest

def stack_squeze(arr):
    res = []
    stack = []
    for i, v in enumerate(arr):
        while stack and stack[-1][1] > v:
            v = stack.pop()[1]
        res.append(v)
        stack.append([i, v])

    return res

class TestStackSqueze(unittest.TestCase):
    def test_empty_input(self):
        # Test with an empty list
        self.assertEqual(stack_squeze([]), [])

    def test_single_element(self):
        # Test with a single element in the list
        self.assertEqual(stack_squeze([5]), [5])

    def test_multiple_elements(self):
        # Test with multiple elements in the list
        self.assertEqual(stack_squeze([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [3, 3, 4, 4, 5, 9, 9, 9, 9, 9, 9])