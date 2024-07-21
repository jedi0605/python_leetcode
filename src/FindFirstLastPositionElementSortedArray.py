"""_summary
34. Find First and Last Position of Element in Sorted Array
#Leetcode150
Time:O(log(m*n))
Space:O(1)
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bSearch(nums, target, "left")
        right = self.bSearch(nums, target, "right")
        return [left, right]

    def bSearch(self, nums, target, boundary):
        i = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if boundary == "left":
                    r = m - 1
                else:
                    l = m + 1
        return i
