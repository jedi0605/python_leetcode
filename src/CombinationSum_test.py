import unittest
from CombinationSum import Solution
from TreeNode import TreeNode


class CombinationSum_test(unittest.TestCase):
    def test_case1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        sol = Solution()
        res = sol.combinationSum(candidates, target)
        assert len(res) == 2


if __name__ == "__main__":
    unittest.main()
