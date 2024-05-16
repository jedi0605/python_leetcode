import unittest
from MaximumSumDistinctSubarraysWithLengthK import Solution


class MaximumSumDistinctSubarraysWithLengthK_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [1, 5, 4, 2, 9, 9, 9]
        k = 3
        assert solution.maximumSubarraySum(nums,k) == 15
    def test_case2(self):
        solution = Solution()
        nums = [4,4,4]
        k = 3
        assert solution.maximumSubarraySum(nums,k) == 0
    def test_case3(self):
        solution = Solution()
        nums = [5,1,3]
        k = 1
        assert solution.maximumSubarraySum(nums,k) == 5

    def test_case3(self):
        solution = Solution()
        nums = [5,3,3,1,1]
        k = 3
        assert solution.maximumSubarraySum(nums,k) == 0
if __name__ == "__main__":
    unittest.main()
