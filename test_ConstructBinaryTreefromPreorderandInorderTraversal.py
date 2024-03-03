import unittest
from ConstructBinaryTreefromPreorderandInorderTraversal import Solution
from TreeNode import TreeNode


class test_ConstructBinaryTreefromPreorderandInorderTraversal(unittest.TestCase):
    def test_case1(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]

        solution = Solution()
        res = solution.buildTree(preorder, inorder)
        ansArr = [3, 9, 20, None, None, 15, 7]
        ans = TreeNode.array_to_binary_tree(ansArr)
        assert TreeNode.isSameTree(res, ans)


if __name__ == "__main__":
    unittest.main()
