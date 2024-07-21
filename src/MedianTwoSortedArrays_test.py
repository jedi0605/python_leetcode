import unittest
from MedianTwoSortedArrays import Solution
from ListNode import ListNode


class MaximumSwap_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()       
        nums1 = [1,2]
        nums2 = [3,4,5]
        solution.findMedianSortedArrays2(nums1,nums2)


if __name__ == "__main__":
    unittest.main()
