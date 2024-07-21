import unittest
from KthLargestElementArray import Solution

import TestingTool


class KthLargestElementArray_test(unittest.TestCase):
    def test_case1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        solution = Solution()
        assert solution.findKthLargest(nums, k) == 5


if __name__ == "__main__":
    unittest.main()
