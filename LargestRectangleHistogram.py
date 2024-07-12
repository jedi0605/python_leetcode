"""
like 2334
84. Largest Rectangle in Histogram
#Leetcode150
Time:O(n), O(n^2)
Space:O(n), O(1) 
"""

from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx, hei = stack.pop()
                maxArea = max(maxArea, hei * (i - idx))
                start = idx
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea

    ### brute force n^2
    ### It will TLE
    def largestRectangleArea2(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            minHeight = inf
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                maxArea = max(maxArea, minHeight * (j - i + 1))
        return maxArea
