import unittest
from BinaryTreeMaximumPathSum import Solution
from TreeNode import TreeNode


class test_BinaryTreeMaximumPathSum(unittest.TestCase):
    def test_case1(self):
        root = [-10, 9, 20, None, None, 15, 7]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        assert solution.maxPathSum(node) == 42


if __name__ == "__main__":
    unittest.main()
