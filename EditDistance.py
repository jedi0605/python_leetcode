from bisect import bisect_left
import math
from typing import List

"""_summary_
72. Edit Distance
#Leetcode150
Time:O()
Space:O(1)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for row in range(len(word1) + 1):
            dp[row][-1] = len(word1) - row
        for col in range(len(word2) + 1):
            dp[-1][col] = len(word2) - col

        for row in range(len(word1) - 1, -1, -1):
            for col in range(len(word2) - 1, -1, -1):
                if word1[row] == word2[col]:
                    dp[row][col] = dp[row + 1][col + 1]
                else:
                    dp[row][col] = 1 + min(
                        dp[row + 1][col + 1], dp[row + 1][col], dp[row][col + 1]
                    )
        return dp[0][0]        
