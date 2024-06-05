from bisect import bisect_left
import math
from typing import List

"""_summary_
63. Unique Paths II
#Leetcode150
Time:O(n^2)
Space:O(1)
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return -1
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        # row [1,0,1,0] turn in to blow
        # row [1,1,0,0]
        obstacleGrid[0][0] = 1
        for i in range(1, col):
            obstacleGrid[0][i] = int(
                obstacleGrid[0][i] == 0 and obstacleGrid[0][i - 1] == 1
            )
        for i in range(1, row):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1
            )
            
        # traverse grid
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    top = obstacleGrid[i - 1][j]
                    left = obstacleGrid[i][j - 1]
                    obstacleGrid[i][j] = top + left
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]
