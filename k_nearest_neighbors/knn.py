import math
import random
import unittest

class Data:
    def __init__(self, key, point):
        self.key = key
        self.point = point

def dist(p1, p2):
    return math.sqrt(sum([(p1[i] + p2[i])**2 for i in range(len(p1))]))

def generate_points_around(key, center, num_points, radius):
    points = []
    for _ in range(num_points):
        new_point = tuple(center[i] + random.uniform(-radius, radius) for i in range(len(center)))
        points.append(Data(key, new_point))
    return points

def knn(k, point, points):
    k_nearest = [] #heap would be better?

    for other_point in points:
        d = dist(point.point, other_point.point)
        k_nearest.append((d, other_point.key))
    
    k_nearest.sort(key=lambda p:p[0], reverse=True)

    key_map = {}
    for key in k_nearest[:k]:
        if key not in key_map:
            key_map[key] = 0
        else:
            key_map[key] += 1
    return max(key_map, key=key_map.get)[1]

class TestKNN(unittest.TestCase):
    def setUp(self):
        group1 = generate_points_around(1, (5,5), 55, 5)
        group2 = generate_points_around(2, (-5,-5), 55, 5)
        test_group1, data_group1 = group1[:6], group1[6:]
        test_group2, data_group2 = group2[:6], group2[6:]
        self.data_points = data_group1 + data_group2
        self.test_points = test_group1 + test_group2

    def test_knn_single_neighbor(self):
        for test_point in self.test_points:
            self.assertEqual(knn(5, test_point, self.data_points), test_point.key)
        
