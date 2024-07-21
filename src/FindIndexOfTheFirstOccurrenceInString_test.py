import unittest
from FindIndexOfTheFirstOccurrenceInString import Solution


class test_ZigzagConversion(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        assert solution.strStr("sadbutsad", "sad") == 0
        assert solution.strStr("leetcode", "leeto") == -1


if __name__ == "__main__":
    unittest.main()
