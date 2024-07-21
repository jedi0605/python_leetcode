import unittest
import TestingTool
from WallsAndGates import Solution


class WallsAndGates_test(unittest.TestCase):
    def test_case1(self):
        rooms = [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
        solution = Solution()
        solution.wallsAndGates(rooms)
        ans = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
        assert TestingTool.compare_lists_of_lists(rooms,ans)


def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
