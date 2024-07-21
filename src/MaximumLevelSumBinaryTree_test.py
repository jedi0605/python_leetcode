import unittest
from MaximumLevelSumBinaryTree import Solution
from TreeNode import TreeNode


class MaximumLevelSumBinaryTree_test(unittest.TestCase):
    def test_case1(self):
        arr = [1,7,0,7,-8,None,None]
        root = TreeNode.array_to_binary_tree(arr)        
        solution = Solution()
        assert solution.maxLevelSum(root) == 2

if __name__ == "__main__":
    unittest.main()
