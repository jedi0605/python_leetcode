import unittest
from MaximumSumCircularSubarray import Solution


class MaximumSumCircularSubarray_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [1,-2,3,-2]
        assert solution.maxSubarraySumCircular(nums) == 3
if __name__ == "__main__":
    unittest.main()
