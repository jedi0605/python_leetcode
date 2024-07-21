import unittest
from ValidPalindromeII import Solution


class ValidPalindromeII_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "aba"
        assert solution.validPalindrome(s) == True

if __name__ == "__main__":
    unittest.main()
