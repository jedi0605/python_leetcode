import unittest
from ValidPalindromeIV import Solution


class ValidPalindromeIV_test(unittest.TestCase):
    def test_case1(self):
        s = "abcdef"
        solution = Solution()
        
        assert solution.makePalindrome(s) == False

if __name__ == "__main__":
    unittest.main()
