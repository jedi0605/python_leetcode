import unittest
from ValidateBinarySearchTree import Solution
from TreeNode import TreeNode


class test_ValidateBinarySearchTree(unittest.TestCase):
    def test_case1(self):
        root = [2, 1, 3]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        assert solution.isValidBST(node)

    def test_case2(self):
        root = [5, 1, 4, None, None, 3, 6]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        assert solution.isValidBST(node) == False

    def test_case3(self):
        root = [2, 2, 2]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        assert solution.isValidBST(node) == False

    def test_case4(self):
        root = [5, 3, 7, None, None, 4, 8]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        assert solution.isValidBST(node) == False


if __name__ == "__main__":
    unittest.main()
