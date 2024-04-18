"""_summary_
LeetCode 16. 3Sum Closest
Two Pointer
#Leetcode150
Time:O(1)
Space:O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from typing import List, Optional
from ListNode import ListNode


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) < 3:
            return -1
        diff = float("inf")
        res = 0
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]                
                
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                    res = sum
                
                if res == target:
                    return res
                
                if sum > target:
                    right -= 1
                else:
                    left += 1

        return res
