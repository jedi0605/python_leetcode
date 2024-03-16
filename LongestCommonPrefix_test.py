import unittest
from LongestCommonPrefix import Solution


class test_LongestCommonPrefix(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        strs = ["flower","flow","flight"]
        assert solution.longestCommonPrefix(strs) == "fl"

        strs = ["dog","racecar","car"]
        assert solution.longestCommonPrefix(strs) == ""

if __name__ == "__main__":
    unittest.main()
