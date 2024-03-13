import unittest
from BinaryTreeZigzagLevelOrderTraversal import Solution
from TreeNode import TreeNode
import TestingTool


class test_BinaryTreeZigzagLevelOrderTraversal(unittest.TestCase):
    def test_case1(self):
        root = [3, 9, 20, None, None, 15, 7]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        res = solution.zigzagLevelOrder(node)
        ans = [[3], [20, 9], [15, 7]]
        assert TestingTool.compare_lists_of_lists(res, ans)


if __name__ == "__main__":
    unittest.main()
