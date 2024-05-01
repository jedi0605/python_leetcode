import unittest
from LowestCommonAncestorOfABinarySearchTree import Solution
from TreeNode import TreeNode


class test_TwoSumII(unittest.TestCase):
    def test_case1(self):
        root = [6,2,8,0,4,7,9,None,None,3,5]
      
        tmp= TreeNode.array_to_binary_tree(root)
        sol = Solution()
        p = TreeNode(2)
        q = TreeNode(8)
        assert sol.lowestCommonAncestor(tmp,p,q).val == 6
    
if __name__ == "__main__":
    unittest.main()
