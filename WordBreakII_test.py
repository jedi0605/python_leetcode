import unittest
from WordBreakII import Solution


class WordBreak_test(unittest.TestCase):
    def test_case1(self):
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        solution = Solution()
        res = solution.wordBreak(s, wordDict)
        ans = ["cat sand dog", "cats and dog"]
        self.assertSequenceEqual(res, ans)


def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
