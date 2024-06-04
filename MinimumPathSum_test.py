import unittest
from MinimumPathSum import Solution


class MinimumPathSum_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        target = 7
        assert solution.minPathSum(grid) == 7


if __name__ == "__main__":
    unittest.main()
