import unittest
from MaximumDepthOfBinaryTree import Solution
from TreeNode import TreeNode


class test_LRUCache(unittest.TestCase):
    def test_case1(self):
        arr = [3, 9, 20, None, None, 15, 7]
        root = TreeNode.array_to_binary_tree(arr)
        solution = Solution()

        assert solution.maxDepth(root) == 3


if __name__ == "__main__":
    unittest.main()
