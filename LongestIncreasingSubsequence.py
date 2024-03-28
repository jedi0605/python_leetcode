from typing import List

"""_summary_
LeetCode 300. Longest Increasing Subsequence
Using DP
dp[1]*n. 
every dp[i] have looking before dp[i] max seq
#Leetcode150
Time:O(n)
Space:O(1)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) # cur index is i, j is looking for big seq nums.
        return max(dp)
