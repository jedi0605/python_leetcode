"""
2334. Subarray With Elements Greater Than Varying Threshold
#84
#Leetcode150
Time:O(n), O(n^2)
Space:O(n), O(1) 
"""

from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        for i in range(len(nums)):
            minH = float("inf")
            for j in range(j, len(nums)):
                minH = min(minH, nums[j])
                area = minH * (j - i + 1)
                if area > threshold:
                    return j - i + 1
        return -1

    def validSubarraySize2(self, nums: List[int], threshold: int) -> int:
        stack = []
        for i in range(len(nums)):
            start_idx = i
            while stack and stack[-1][1] > nums[i]:
                idx, h = stack.pop()
                area = (i - idx) * h
                if area > threshold:
                    return i - idx
                start_idx = idx
            stack.append((start_idx, nums[i]))
        for idx, h in stack:
            if (len(nums) - idx) * h > threshold:
                return len(nums) - idx
        return -1
