import unittest
import TestingTool
from ValidWordAbbreviation import Solution


class WallsAndGates_test(unittest.TestCase):
    def test_case1(self):
        word = "internationalization"
        abbr = "i12iz4n"
        solution = Solution()
        assert solution.validWordAbbreviation(word,abbr)
        

def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
