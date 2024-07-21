import unittest
from KthSmallestElementinaBST import Solution
from TreeNode import TreeNode
import TestingTool


class test_KthSmallestElementinaBST(unittest.TestCase):
    def test_case1(self):
        root = [5,3,6,2,4,None,None,1]
        k = 3
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        assert solution.kthSmallest(node, k) == 3


if __name__ == "__main__":
    unittest.main()
