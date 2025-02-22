import unittest

# The Knapsack Problem:
# Given a set of items, each with a weight and value, determine the maximum total value 
# that can be carried in a knapsack of limited capacity.
#
# Variants:
# - 0/1 Knapsack: Each item can either be included or not (no partial selection).
# - Fractional Knapsack: Items can be partially included (e.g., taking part of an item).
# - Unbounded Knapsack: Unlimited quantities of each item can be taken.
#
# Common Solutions:
# - Brute Force: Try all subsets (O(2^n), inefficient).
# - Dynamic Programming: Use a table to optimize subproblems (O(n * W)).
# - Greedy Algorithm: For Fractional Knapsack, take items with the best value-to-weight ratio (O(n log n)).

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def dynamic_top_down(items, bag_size):
    if len(items) == 0:
        return 0 

    def take_item(item, bag_size):
        if bag_size == 0 or item.weight > bag_size:
            result = 0
        else:
            result = item.value + max([take_item(i, bag_size - item.weight) for i in items if i is not item] + [0])
        
        return result
        
    return max([take_item(i, bag_size) for i in items])

def dynamic_bottom_up(items, bag_size):
    if bag_size == 0:
        return 0
    
    if len(items) == 0:
        return 0

    table = [[0] * (bag_size + 1) for _ in items]

    for i in range(len(items)):
        for s in range(bag_size + 1):
            if i == 0: # starting the table, there is only one item
                if items[i].weight <= s:
                    table[i][s] = items[i].value
            else:
                if items[i].weight > s: # if the item does not fit, take the current max from the row above
                    table[i][s] = table[i-1][s]
                else:
                    take = items[i].value + table[i-1][s - items[i].weight] # we do table[i-1] because table[i] would include the item 
                    dont_take = table[i-1][s]
                    table[i][s] = max(take, dont_take) 

    return table[-1][-1]



class TestKnapsack(unittest.TestCase):
    def test_single_item_fits(self):
        items = [Item("A", 5, 10)]
        self.assertEqual(dynamic_top_down(items, 5), 10)
        self.assertEqual(dynamic_bottom_up(items, 5), 10)

    def test_single_item_too_heavy(self):
        items = [Item("A", 5, 10)]
        self.assertEqual(dynamic_top_down(items, 4), 0)
        self.assertEqual(dynamic_bottom_up(items, 4), 0)

    def test_multiple_items_fitting_exactly(self):
        items = [Item("A", 2, 3), Item("B", 3, 4), Item("C", 4, 5)]
        self.assertEqual(dynamic_top_down(items, 5), 7)  # Take A and B (3+4)
        self.assertEqual(dynamic_bottom_up(items, 5), 7)  # Take A and B (3+4)

    def test_multiple_items_partial_fit(self):
        items = [Item("A", 1, 1), Item("B", 3, 4), Item("C", 4, 5)]
        self.assertEqual(dynamic_top_down(items, 4), 5)  # Take C
        self.assertEqual(dynamic_bottom_up(items, 4), 5)  # Take C

    def test_empty_knapsack(self):
        items = []
        self.assertEqual(dynamic_top_down(items, 10), 0)
        self.assertEqual(dynamic_bottom_up(items, 10), 0)

    def test_zero_capacity(self):
        items = [Item("A", 2, 3), Item("B", 3, 4)]
        self.assertEqual(dynamic_top_down(items, 0), 0)
        self.assertEqual(dynamic_bottom_up(items, 0), 0)

    def test_large_capacity(self):
        items = [Item("A", 1, 1), Item("B", 3, 4), Item("C", 4, 5), Item("D", 2, 2)]
        self.assertEqual(dynamic_top_down(items, 7), 9)  # Take B and C (4+5)
        self.assertEqual(dynamic_bottom_up(items, 7), 9)  # Take B and C (4+5)