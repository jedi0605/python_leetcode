import unittest
from MinimumSizeSubarraySum import Solution


class test_MinimumSizeSubarraySum(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [2, 3, 1, 2, 4, 3]
        target = 7
        assert solution.minSubArrayLen(target, nums) == 2

    def test_case2(self):
        solution = Solution()
        nums = [1, 4, 4]
        target = 4
        assert solution.minSubArrayLen(target, nums) == 1

    def test_case3(self):
        solution = Solution()
        nums = [1,1,1,1,1,1,1,1]
        target = 11
        assert solution.minSubArrayLen(target, nums) == 1


if __name__ == "__main__":
    unittest.main()
