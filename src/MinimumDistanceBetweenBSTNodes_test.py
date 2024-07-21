import unittest
from MinimumDistanceBetweenBSTNodes import Solution
from TreeNode import TreeNode


class MinimumDistanceBetweenBSTNodes_test(unittest.TestCase):
    def test_case1(self):

        root = [4, 2, 6, 1, 3]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        assert solution.minDiffInBST(node) == 1   

if __name__ == "__main__":
    unittest.main()
