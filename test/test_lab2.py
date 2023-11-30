import unittest
from task_lab2 import findThreeNumbers


class TestFind3Numbers(unittest.TestCase):
    def test_valid_input(self):
        A = [1, 4, 6, 8, 20, 500, 501, 700, 1000]
        P = 1501
        self.assertTrue(findThreeNumbers(A, P))

    def test_invalid_size(self):
        A = [5, 1]
        P = 10
        self.assertFalse(findThreeNumbers(A, P))

    def test_invalid_value(self):
        A = [-5, 1, 4]
        P = 10
        self.assertFalse(findThreeNumbers(A, P))

    def test_invalid_large_value(self):
        A = [5, 1, 4]
        P = 4000000000
        self.assertFalse(findThreeNumbers(A, P))

    def test_invalid_P_value(self):
        A = [5, 1, 4]
        P = -10
        self.assertFalse(findThreeNumbers(A, P))


if __name__ == "__main__":
    unittest.main()
