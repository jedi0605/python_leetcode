import unittest
from WordBreak import Solution


class WordBreak_test(unittest.TestCase):
    def test_case1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        solution = Solution()
        assert solution.wordBreak(s, wordDict)


def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
