from typing import List

"""_summary_
221. Maximal Square
1. Create dp array (m+1) * (n+1). easy to do array operation
2. if matrix[i][j]=="1". get min + 1 of (i+1,j+1. i+1,j. i,j+1)
#Leetcode150
Time:O(m * n)
Space:O(m * n)
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = [[0] * (COL + 1) for i in range(ROW + 1)]
        maxLen = 0
        for r in range(1, ROW + 1):
            for c in range(1, COL + 1):
                if matrix[r - 1][c - 1] == "1":
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1
                    maxLen = max(maxLen, dp[r][c])
        return maxLen * maxLen
