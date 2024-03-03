import unittest
from SymmetricTree import Solution
from TreeNode import TreeNode


class test_SymmetricTree(unittest.TestCase):
    def test_case1(self):
        root = [1,2,2,3,4,4,3]        
        rootNode =  TreeNode.array_to_binary_tree(root)
        solution = Solution()        
        assert solution.isSymmetric(rootNode)


if __name__ == "__main__":
    unittest.main()
