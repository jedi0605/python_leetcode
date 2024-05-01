import unittest
from LowestCommonAncestorOfABinaryTreeII import Solution
from TreeNode import TreeNode


class test_TwoSumII(unittest.TestCase):
    def test_case1(self):
        root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        tmp = TreeNode.array_to_binary_tree(root)
        p = TreeNode(5)
        q = TreeNode(1)
        sol = Solution()
        assert sol.lowestCommonAncestor(tmp, p, q).val == 3


if __name__ == "__main__":
    unittest.main()
