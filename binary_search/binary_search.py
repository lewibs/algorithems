import unittest

#reps 6

def binary_search(arr, target):
    start = 0
    end = len(arr) -1 

    while start <= end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid +1
        elif arr[mid] > target:
            end = mid -1
        else:
            return mid
        
    return None

 
class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.list = range(100)

    def test_contigus(self):
        for v in self.list:
            self.assertEqual(binary_search(self.list, v), self.list.index(v))

    def test_missing(self):
        self.list = [x for x in self.list if x % 7 != 0]
        
        for v in self.list:
           self.assertEqual(binary_search(self.list, v), self.list.index(v))