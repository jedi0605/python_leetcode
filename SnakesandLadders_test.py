import unittest
from SnakesandLadders import Solution


class SnakesandLadders_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
        assert sol.snakesAndLadders(board) == 4

    def test_case2(self):
        solution = Solution()
        matrix = [[1, 2, 3, 4]]
        assert solution.spiralOrder(matrix) == [1, 2, 3, 4]


if __name__ == "__main__":
    unittest.main()
