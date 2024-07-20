import unittest
from MostCommonWord import Solution


class MostCommonWord_test(unittest.TestCase):
    def test_case1(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        sol = Solution()
        assert sol.mostCommonWord(paragraph,banned) == "ball"


if __name__ == "__main__":
    unittest.main()
