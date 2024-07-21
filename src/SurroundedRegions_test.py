import unittest
from SurroundedRegions import Solution
import TestingTool


class SurroundedRegions_test(unittest.TestCase):
    def test_case1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]

        solution = Solution()
        solution.solve(board)
        ans = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        assert TestingTool.compare_lists_of_lists(board, ans)


if __name__ == "__main__":
    unittest.main()
