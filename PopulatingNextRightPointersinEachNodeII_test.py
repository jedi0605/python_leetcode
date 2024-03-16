import unittest
from PopulatingNextRightPointersinEachNodeII import Node, Solution
from TreeNode import TreeNode


class test_ConstructBinaryTreefromPreorderandInorderTraversal(unittest.TestCase):
    def test_case1(self):
        root = [1, 2, 3, 4, 5, None, 7]
        rootTree = Node.array_to_binary_tree(root)

        solution = Solution()
        res = solution.connect(rootTree)


if __name__ == "__main__":
    unittest.main()
