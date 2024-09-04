import unittest
from .binary_classifier import find_best_threshold
class TestFindBestThreshold(unittest.TestCase):

    def test_normal_case(self):
        data = [
            (0.1, 100, 50, 10, 5),   # recall = 0.952, precision = 0.909
            (0.2, 95, 55, 5, 10),    # recall = 0.905, precision = 0.950
            (0.3, 90, 58, 2, 15),    # recall = 0.857, precision = 0.978
            (0.4, 85, 59, 1, 20),    # recall = 0.810, precision = 0.988
        ]
        self.assertEqual(find_best_threshold(data), 0.2)

    def test_no_valid_threshold(self):
        data = [
            (0.1, 80, 50, 10, 25),   # recall = 0.762, precision = 0.889
            (0.2, 75, 55, 5, 30),    # recall = 0.714, precision = 0.938
            (0.3, 70, 58, 2, 35),    # recall = 0.667, precision = 0.972
        ]
        self.assertIsNone(find_best_threshold(data))

    def test_all_valid_thresholds(self):
        data = [
            (0.1, 100, 50, 10, 5),   # recall = 0.952, precision = 0.909
            (0.2, 98, 52, 8, 7),     # recall = 0.933, precision = 0.925
            (0.3, 95, 54, 6, 10),    # recall = 0.905, precision = 0.941
        ]
        self.assertEqual(find_best_threshold(data), 0.3)

    def test_edge_case_zero_denominator(self):
        data = [
            (0.1, 0, 50, 0, 0),      # recall = 0, precision = 0
            (0.2, 10, 55, 0, 0),     # recall = 1, precision = 1
            (0.3, 0, 58, 0, 10),     # recall = 0, precision = 0
        ]
        self.assertEqual(find_best_threshold(data), 0.2)