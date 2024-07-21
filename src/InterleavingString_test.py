import unittest
from InterleavingString import Solution
from TreeNode import TreeNode


class test_InvertBinaryTree(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        assert solution.isInterleave(s1, s2, s3) == True
    def test_case2(self):
        solution = Solution()
        s1 = "db"
        s2 = "b"
        s3 = "cbb"
        assert solution.isInterleave(s1, s2, s3) == False


if __name__ == "__main__":
    unittest.main()
