import unittest
import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0] # you can pick any pivot long as you ignore it
    smaller = [v for v in arr[1:] if v <= pivot] # it does not matter where the = is
    larger = [v for v in arr[1:] if v > pivot] # [1:] to make sure we dont include the pivot twice
    return quick_sort(smaller) + [pivot] + quick_sort(larger)



class TestQuickSort(unittest.TestCase):
    def test(self):
        for l in range(0, 500):
            huge_array = [random.randint(0, 500000) for _ in range(l)]
            huge_array_copy = huge_array[:]
            self.assertEqual(sorted(huge_array_copy), quick_sort(huge_array))