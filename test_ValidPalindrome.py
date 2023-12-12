import unittest
from ValidPalindrome import Solution


class test_ValidPalindrome(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "A man, a plan, a canal: Panama"
        assert solution.isPalindrome(s) == True
        assert solution.isPalindrome2(s) == True

        t = "race a car"
        assert solution.isPalindrome(t) == False
        assert solution.isPalindrome2(t) == False


if __name__ == "__main__":
    unittest.main()
