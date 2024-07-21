import unittest
from SubarraySumEqualsK import Solution


class SubarraySumEqualsK_test(unittest.TestCase):
    def test_case1(self):
        nums = [1, 1, 1]
        k = 2
        solution = Solution()
        assert solution.subarraySum(nums, k) == 2


if __name__ == "__main__":
    unittest.main()
