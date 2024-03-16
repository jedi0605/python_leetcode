import unittest
from SameTree import Solution
from TreeNode import TreeNode


class test_LRUCache(unittest.TestCase):
    def test_case1(self):
        arr = [3, 9, 20]
        arr2 = [3, 9, 20]
        root = TreeNode.array_to_binary_tree(arr)
        root2 = TreeNode.array_to_binary_tree(arr2)
        solution = Solution()
        assert solution.isSameTree(root, root2)

    def test_case2(self):
        arr = [1, 2]
        arr2 = [1, None, 2]
        root = TreeNode.array_to_binary_tree(arr)
        root2 = TreeNode.array_to_binary_tree(arr2)
        solution = Solution()
        assert solution.isSameTree(root, root2) == False


if __name__ == "__main__":
    unittest.main()
