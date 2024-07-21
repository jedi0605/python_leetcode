import unittest
from MaximalSquare import Solution
from TreeNode import TreeNode


class MaximalSquare_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]

        assert solution.maximalSquare(matrix) == 4


if __name__ == "__main__":
    unittest.main()
