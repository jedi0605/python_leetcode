import unittest
from BinaryTreeRightSideView import Solution
from TreeNode import TreeNode


class test_BinaryTreeRightSideView(unittest.TestCase):
    def test_case1(self):
        root = [1, 2, 3, None, 5, None, 4]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        res = solution.rightSideView(node)
        ans = [1, 3, 4]
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
