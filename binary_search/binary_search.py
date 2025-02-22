import unittest

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end: #This must be = because you can slightly overshoot it
        mid = (end+start)//2 # this is + because math
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # we move the window to the upper half if the number at the middle is lower then the target
            start = mid + 1 # we explude the middle
        elif arr[mid] > target:
            # we move the window to the lower half
            end = mid - 1 # we exclude the number we guess

    return None

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.list = range(1000)

    def test_contigus(self):
        for v in self.list:
            self.assertEqual(binary_search(self.list, v), self.list.index(v))

    def test_missing(self):
        self.list = [x for x in self.list if x % 7 != 0]
        
        for v in self.list:
           self.assertEqual(binary_search(self.list, v), self.list.index(v))