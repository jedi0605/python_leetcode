import unittest
from SpiralMatrix import Solution


class test_SpiralMatrix(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        assert solution.spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    def test_case2(self):
        solution = Solution()
        matrix = [[1, 2, 3, 4]]
        assert solution.spiralOrder(matrix) == [1, 2, 3, 4]


if __name__ == "__main__":
    unittest.main()
