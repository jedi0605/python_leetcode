import unittest
from FindFirstLastPositionElementSortedArray import Solution


class FindFirstLastPositionElementSortedArray_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        assert solution.searchRange(nums, target) == [3, 4]


if __name__ == "__main__":
    unittest.main()
