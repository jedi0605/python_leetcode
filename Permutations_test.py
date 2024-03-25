import unittest
from Permutations import Solution
import TestingTool

class test_PathSum(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        nums = [1,2,3]
        res = sol.permute(nums)
        ans = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        res.sort()
        ans.sort()
        assert TestingTool.compare_lists_of_lists(ans,res)

if __name__ == "__main__":
    unittest.main()
