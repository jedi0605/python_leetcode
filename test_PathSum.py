import unittest
from PathSum import Solution
from TreeNode import TreeNode


class test_PathSum(unittest.TestCase):
    def test_case1(self):
        root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        targetSum = 22
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        res = solution.hasPathSum(node, targetSum)


if __name__ == "__main__":
    unittest.main()
