import unittest
from .mod_three_fsm import ModThreeFSM

class TestModThreeFSM(unittest.TestCase):
    def setUp(self):
        self.mod_three = ModThreeFSM()

    def test_mod_three_fsm(self):
        test_cases = [
            ("110", 0),
            ("1010", 1),
            ("1101", 1),
            ("1110", 2),
            ("1111", 0)
        ]

        for input_string, expected_output in test_cases:
            with self.subTest(input_string=input_string):
                result = self.mod_three.compute_remainder(input_string)
                self.assertEqual(result, expected_output, 
                                 f"Failed for input '{input_string}'. "
                                 f"Expected {expected_output}, got {result}")
