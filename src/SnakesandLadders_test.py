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

if __name__ == "__main__":
    unittest.main()
