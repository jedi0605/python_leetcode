"""_summary
1143. Longest Common Subsequence
"""

from typing import List
from TreeNode import TreeNode


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[]] * (len(text1) + 1)
        for i in range(len(dp)):
            dp[i] = [0] * (len(text2) + 1)
        print(dp)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
