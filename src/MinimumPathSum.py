from bisect import bisect_left
import math
from typing import List

"""_summary_
Minimum Path Sum
DP
#Leetcode150
Time:O(n^2)
Space:O(1)
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        pre = 0
        for i in range(len(grid[0])):
            grid[0][i] += pre
            pre = grid[0][i]
        pre = 0
        for i in range(len(grid)):
            grid[i][0] += pre
            pre = grid[i][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
