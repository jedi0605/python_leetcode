import unittest
from MergeSortedArray import Solution


class MergeSortedArray_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        solution.merge(nums1, m, nums2, n)
        ans = [1, 2, 2, 3, 5, 6]
        assert ans == nums1
    def test_case2(self):
        solution = Solution()
        nums1 = [2,0]
        m = 1
        nums2 = [1]
        n = 1
        solution.merge(nums1, m, nums2, n)
        ans = [1, 2]
        assert ans == nums1

if __name__ == "__main__":
    unittest.main()
