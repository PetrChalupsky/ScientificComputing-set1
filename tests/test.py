import unittest
import numpy as np
from scientific_computing.time_dep_diff import initialize_grid

class Test(unittest.TestCase):
    def test_initialize_grid(self):
        """
        Test the initialize_grid function.
        """
        expected_grid = np.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]])
        actual_grid = initialize_grid(3)
        self.assertTrue(np.array_equal(expected_grid, actual_grid))

if __name__ == "__main__":
    unittest.main()
