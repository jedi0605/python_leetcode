import unittest
from LongestPalindromicSubstring import Solution


class LongestPalindromicSubstring_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "cbbd"
        assert solution.longestPalindrome(s) == "bb"

    def test_case2(self):
        solution = Solution()
        s = "babad"
        assert solution.longestPalindrome(s) == "aba"


if __name__ == "__main__":
    unittest.main()
