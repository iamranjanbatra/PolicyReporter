import unittest
import sys
import os

# Add the parent directory of assignment1 and assignment2 to the Python path
# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from assignment1.test import TestFindBestThreshold
from assignment2.test import TestModThreeFSM

def run_all_tests():
    # Create a test loader
    loader = unittest.TestLoader()

    # Load tests from the test cases in assignment1 and assignment2
    suite1 = loader.loadTestsFromTestCase(TestFindBestThreshold)
    suite2 = loader.loadTestsFromTestCase(TestModThreeFSM)

    # Combine the test suites
    combined_suite = unittest.TestSuite([suite1, suite2])

    # Run the combined test suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(combined_suite)

if __name__ == '__main__':
    run_all_tests()