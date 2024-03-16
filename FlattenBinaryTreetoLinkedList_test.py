import unittest
from FlattenBinaryTreetoLinkedList import Solution
from TreeNode import TreeNode


class test_FlattenBinaryTreetoLinkedList(unittest.TestCase):
    def test_case1(self):
        root = [1,2,5,3,4,None,6]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        solution.flatten(node)


if __name__ == "__main__":
    unittest.main()
