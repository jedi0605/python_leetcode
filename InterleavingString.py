from bisect import bisect_left
import math
from typing import List

"""_summary_
97. Interleaving String
#Leetcode150
Time:O()
Space:O(1)
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return False
        dp = []
        for i in range(len1 + 1):
            tmp = [False] * (len2 + 1)
            dp.append(tmp)
        dp[0][0] = True

        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # Fill the first column
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                if s3[i + j - 1] == s2[j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        return dp[len1][len2]
        # dp = {}
        # def dfs(i, j):
        #     print(str(i) + "," + str(j))
        #     if i == len(s1) and j == len(s2):
        #         return True
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
        #         return True
        #     if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
        #         return True

        #     dp[(i, j)] = False
        #     return False

        # res = dfs(0, 0)
        # print(dp)
        # return res
