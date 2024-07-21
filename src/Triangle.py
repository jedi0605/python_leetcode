from bisect import bisect_left
import math
from typing import List

"""_summary_
120. Triangle
Using DP

#Leetcode150
Time:O(n^2)
Space:O(1)
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                if col == 0:
                    triangle[row][col] += triangle[row - 1][0]
                elif col == len(triangle[row]) - 1:
                    triangle[row][col] += triangle[row - 1][-1]
                else:
                    smallVal = min(triangle[row - 1][col - 1], triangle[row - 1][col])
                    triangle[row][col] += smallVal
        return min(triangle[-1])
