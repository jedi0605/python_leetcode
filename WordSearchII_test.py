import unittest
from WordSearchII import Solution


class WordSearchII_test(unittest.TestCase):
    def test_case1(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]
        sol = Solution()
        res = sol.findWords(board, words)
        res.sort()
        ans = ["eat", "oath"]
        ans.sort()
        self.assertSequenceEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
