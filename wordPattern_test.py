import unittest
from WordPattern import Solution


class test_wordPattern(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        pattern = "abba"
        s = "dog cat cat dog"
        assert solution.wordPattern(pattern, s) == True

    def test_case2(self):
        solution = Solution()
        pattern = "aaaa"
        s = "dog cat cat dog"
        assert solution.wordPattern(pattern, s) == False


def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
