"""_summary
918. Maximum Sum Circular Subarray
#Leetcode150
Time:O(n)
Space:O(1)
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, curMin = 0, 0
        globalMax, globalMin = nums[0], nums[0]
        total = 0

        for n in nums:
            total += n
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            globalMax = max(globalMax, curMax)
            globalMin = max(globalMin, curMin)

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
