import unittest
from RangeSumofBST import Solution
from TreeNode import TreeNode


class RangeSumofBST_test(unittest.TestCase):
    def test_case1(self):
        root = [10, 5, 15, 3, 7, None, 18]
        rootNode = TreeNode.array_to_binary_tree(root)
        sol = Solution()
        res = sol.rangeSumBST(rootNode, 7, 15)
        assert res == 32


def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
