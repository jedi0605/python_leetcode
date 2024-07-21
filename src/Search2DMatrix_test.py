import unittest
from Search2DMatrix import Solution


class Search2DMatrix_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        assert sol.searchMatrix(matrix, 3)


if __name__ == "__main__":
    unittest.main()
