import unittest
from IsSubsequence import Solution


class test_IsSubsequence(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "abc"
        t = "ahbgdc"
        assert solution.isSubsequence(s, t)

    def test_case2(self):
        solution = Solution()
        s = "axc"
        t = "ahbgdc"
        self.assertEqual(solution.isSubsequence(s, t), False)


if __name__ == "__main__":
    unittest.main()
