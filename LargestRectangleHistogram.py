"""
like 2334
1235. Maximum Profit in Job Scheduling
#Leetcode150
Time:O(n logn)
Space:O(n)
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        maxArea = 0
        
        for i,h in enumerate(heights):
            start = i
            while stack and h<  stack[-1][1] :
                idx, hei = stack.pop()
                maxArea = max(maxArea, hei * (i - idx) )
                start = idx
            stack.append((start,h))
            
        for i,h in stack:
            maxArea = max(maxArea, (len(heights) - i)*h)
        return maxArea        