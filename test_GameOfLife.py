import unittest
from GameOfLife import Solution


class test_GameOfLife(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        solution.gameOfLife(board)
        ans = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        assert are_matrices_equal(board, ans)


def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
