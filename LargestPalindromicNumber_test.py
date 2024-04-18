import unittest
from LargestPalindromicNumber import Solution


class LargestPalindromicNumber_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        num = "444947137"
        assert solution.largestPalindromic(num) == "7449447"
    def test_case2(self):
        solution = Solution()
        num = "6006"
        assert solution.largestPalindromic(num) == "6006"


if __name__ == "__main__":
    unittest.main()
