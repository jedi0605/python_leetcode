import unittest
from AverageofLevelsinBinaryTree import Solution
from TreeNode import TreeNode


class test_AverageofLevelsinBinaryTree(unittest.TestCase):
    def test_case1(self):
        root = [3, 9, 20, None, None, 15, 7]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        res = solution.averageOfLevels(node)
        ans = [3.00000,14.50000,11.00000]
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
