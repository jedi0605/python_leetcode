import unittest
from FindLargestValueInEachTreeRow import Solution
from TreeNode import TreeNode


class FindLargestValueInEachTreeRow_test(unittest.TestCase):
    def test_case1(self):
        root = [1, 3, 2, 5, 3, None, 9]
        node = TreeNode.array_to_binary_tree(root)
        solution = Solution()
        res = solution.largestValues(node)
        ans = [1,3,9]
        self.assertSequenceEqual(res,ans)


if __name__ == "__main__":
    unittest.main()
