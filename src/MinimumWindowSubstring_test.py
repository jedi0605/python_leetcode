import unittest
from MinimumWindowSubstring import Solution


class test_MinimumWindowSubstring(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "ADOBECODEBANC"
        t = "ABC"
        res = solution.minWindow(s, t)
        ans = "BANC"
        assert res == ans

    def test_case2(self):
        solution = Solution()
        s = "ADOBECODEBANC"
        t = "ABC"
        res = solution.minWindow2(s, t)
        ans = "BANC"
        assert res == ans

    def test_case3(self):
        solution = Solution()
        s = "ADOBECODEBANC"
        t = "ABC"
        res = solution.minWindow4(s, t)
        ans = "BANC"
        assert res == ans


if __name__ == "__main__":
    unittest.main()
