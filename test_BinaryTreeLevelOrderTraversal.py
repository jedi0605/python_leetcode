from typing import List
import unittest
from BinaryTreeLevelOrderTraversal import Solution
from TreeNode import TreeNode
import TestingTool


class test_BinaryTreeLevelOrderTraversal(unittest.TestCase):
    def test_case1(self):
        root = [3, 9, 20, None, None, 15, 7]
        node = TreeNode.array_to_binary_tree(root)
        sol = Solution()
        res = sol.levelOrder(node)
        ans = [[3],[9,20],[15,7]]
        assert TestingTool.compare_lists_of_lists(res,ans) == True
        
if __name__ == "__main__":
    unittest.main()
