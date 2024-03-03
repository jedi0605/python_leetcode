import unittest
from InvertBinaryTree import Solution
from TreeNode import TreeNode


class test_InvertBinaryTree(unittest.TestCase):
    def test_case1(self):
        root = [4, 2, 7, 1, 3, 6, 9]
        rootTree = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        resTree = solution.invertTree(rootTree)

        ans = [4, 7, 2, 9, 6, 3, 1]
        ansTree = TreeNode.array_to_binary_tree(ans)
        assert TreeNode.isSameTree(resTree, ansTree)


if __name__ == "__main__":
    unittest.main()
