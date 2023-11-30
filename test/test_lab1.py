import unittest

from src.task_lab1 import plant


class TestPlantingAlgorithm(unittest.TestCase):
    # def test_1(self):
    #     m, n = 5, 5
    #     counts = [[1, 2, 3, 4, 5],
    #               [6, 7, 8, 9, 10],
    #               [11, 12, 13, 14, 15],
    #               [16, 17, 18, 19, 20],
    #               [21, 22, 23, 24, 25]]
    #     expected_result = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
    #     self.assertEqual(plant(m, n, counts), expected_result)
    #
    # def test_2(self):
    #     m, n = 2, 4
    #     counts = [[1, 2, 3, 4],
    #               [5, 6, 7, 8]]
    #     expected_result = [1, 2, 3, 4, 8, 7, 6, 5]
    #     self.assertEqual(plant(m, n, counts), expected_result)
    #
    # def test_3(self):
    #     m, n = 1, 6
    #     counts = [[1, 2, 3, 4, 5, 6]]
    #     expected_result = [1, 2, 3, 4, 5, 6]
    #     self.assertEqual(plant(m, n, counts), expected_result)

    def test_4(self):
        counts = [[11, 3, 7], [4, 5, 2], [1, 0, 6], [4, 4, 1]]

        expected_result = [11, 4, 1, 4, 4, 0, 5, 3, 7, 2, 6, 1]
        self.assertEqual(plant(counts), expected_result)


if __name__ == "__main__":
    unittest.main()
