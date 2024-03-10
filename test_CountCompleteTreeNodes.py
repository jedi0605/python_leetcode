import unittest
from CountCompleteTreeNodes import Solution
from TreeNode import TreeNode


class test_CountCompleteTreeNodes(unittest.TestCase):
    def test_case1(self):
        root = [1, 2, 3, 4, 5, 6]
        node = TreeNode.array_to_binary_tree(root) 
        solution = Solution()        
        assert solution.countNodes(node) == 6
        

if __name__ == "__main__":
    unittest.main()
