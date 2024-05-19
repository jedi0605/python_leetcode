"""_summary
53. Maximum Subarray
#Leetcode150
Time:O(n)
Space:O(1)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        cur = 0
        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            maxSum = max(cur, maxSum)
        return maxSum
