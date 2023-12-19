import unittest
from LongestSubstringWithoutRepeatingCharacters import Solution


class test_TwoSumII(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "abcabcbb"
        assert solution.lengthOfLongestSubstring(s) == 3

    def test_case2(self):
        solution = Solution()
        s = "bbbbb"
        assert solution.lengthOfLongestSubstring(s) == 1
        
    def test_case3(self):
        solution = Solution()
        s = " "
        assert solution.lengthOfLongestSubstring(s) == 1

if __name__ == "__main__":
    unittest.main()
