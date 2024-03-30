from bisect import bisect_left
from typing import List

"""_summary_
LeetCode 354. Russian Doll Envelopes
Pre Question is Longest increasing Subsequence. (LIC)
Sort nums
Using DP
dp[1]*n. 
#Leetcode150
Time:O(n^2)
Space:O(n)
"""


class Solution:
    # nlogn
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        result = []
        for _, e in envelopes:
            # idx = self.bSearch(result, e)
            idx = bisect_left(result,e)
            if idx == len(result):
                result.append(e)
            else:
                result[idx] = e
        return len(result)

    def bSearch(self, arr, target) -> int:
        l, r = 0, len(arr) - 1
        while r >= l:
            mid = (l + r) >> 1
            if arr[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l

    # envelopes.sort(key=lambda x: (x[0], -x[1]))
    # dp = []
    # for _, h in envelopes:
    #     # l, r = 0, len(dp) - 1
    #     idx = bisect_left(dp, h)
    #     if idx == len(dp):
    #         dp.append(h)
    #     else:
    #         dp[idx] = h

    # return len(dp)

    # N^2
    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #     envelopes.sort()
    #     dp = [1] * len(envelopes)
    #     for i in range(1, len(envelopes)):
    #         for j in range(0, i):
    #             if (
    #                 envelopes[i][0] > envelopes[j][0]
    #                 and envelopes[i][1] > envelopes[j][1]
    #             ):
    #                 dp[i] = max(1 + dp[j], dp[i])
    #     return max(dp)
