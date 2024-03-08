import unittest
from SumRootToLeafNumbers import Solution
from TreeNode import TreeNode


class test_SumRootToLeafNumbers(unittest.TestCase):
    def test_case1(self):
        root = [0,1]
        targetSum = 1
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        assert solution.sumNumbers(node) == 25


if __name__ == "__main__":
    unittest.main()
