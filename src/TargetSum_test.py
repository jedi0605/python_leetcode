import unittest
from TargetSum import Solution


class TargetSum_test(unittest.TestCase):
    def test_case1(self):
        nums = [1,1,1,1,1]
        target = 3

        solution = Solution()
        assert solution.findTargetSumWays(nums,target) == 5


if __name__ == "__main__":
    unittest.main()
