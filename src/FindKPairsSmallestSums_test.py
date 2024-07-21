import unittest
from FindKPairsSmallestSums import Solution
from TreeNode import TreeNode


class FindKPairsSmallestSums_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        k = 3
        solution.kSmallestPairs(nums1, nums2, k)


if __name__ == "__main__":
    unittest.main()
