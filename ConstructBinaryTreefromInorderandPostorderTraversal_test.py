import unittest
from ConstructBinaryTreefromInorderandPostorderTraversal import Solution
from TreeNode import TreeNode


class test_ConstructBinaryTreefromInorderandPostorderTraversal(unittest.TestCase):
    def test_case1(self):
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]

        solution = Solution()
        res = solution.buildTree(inorder, postorder)
        ansArr = [3, 9, 20, None, None, 15, 7]
        ans = TreeNode.array_to_binary_tree(ansArr)
        assert TreeNode.isSameTree(res, ans)


if __name__ == "__main__":
    unittest.main()
