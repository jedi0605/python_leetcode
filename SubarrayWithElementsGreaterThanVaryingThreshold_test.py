import unittest
from SubarrayWithElementsGreaterThanVaryingThreshold import Solution


class SubarrayWithElementsGreaterThanVaryingThreshold_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [1, 3, 4, 3, 1]
        threshold = 6
        assert solution.validSubarraySize2(nums, threshold) == 3


if __name__ == "__main__":
    unittest.main()
