import unittest
from DiameterofBinaryTree import Solution
from TreeNode import TreeNode


class DiameterofBinaryTree_test(unittest.TestCase):
    def test_case1(self):
        
        root = [1,2,3,4,5]
        tree =  TreeNode.array_to_binary_tree(root)
        sol = Solution()
        assert sol.diameterOfBinaryTree(tree) == 3

if __name__ == "__main__":
    unittest.main()
