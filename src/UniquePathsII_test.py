import unittest
from UniquePathsII import Solution


class UniquePathsII_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        assert solution.uniquePathsWithObstacles(obstacleGrid) == 2


if __name__ == "__main__":
    unittest.main()
