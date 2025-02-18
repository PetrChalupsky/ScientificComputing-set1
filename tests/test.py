import unittest
import numpy as np
from scientific_computing.time_dep_diff import initialize_grid
from scientific_computing.add_object_SOR import create_objects

class Test(unittest.TestCase):
    def test_initialize_grid(self):
        expected_grid = np.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]])
        actual_grid = initialize_grid(3)
        self.assertTrue(np.array_equal(expected_grid, actual_grid))

    def test_create_object(self):
        list_objects = np.array([[1,3,1,3]])
        width = 3
        expected_grid = [[0,0,0],[0,1,1],[1,1,1]]
        actual_grid = create_objects(list_objects, width)
        self.assertTrue(np.array_equal(expected_grid, actual_grid))


if __name__ == "__main__":
    unittest.main()
