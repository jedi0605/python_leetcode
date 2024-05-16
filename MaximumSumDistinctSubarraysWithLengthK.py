"""_summary
2461. Maximum Sum of Distinct Subarrays With Length K
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque, defaultdict
from typing import List, Optional


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        sum = 0
        res = 0
        for i in range(k):
            seen[nums[i]] += 1
            sum += nums[i]
        if len(seen) == k:
            res = sum
        for i in range(k, len(nums)):
            sum = sum - nums[i-k] + nums[i]
            seen[nums[i-k]] -= 1
            if seen[nums[i-k]] == 0:
                del seen[nums[i-k]]
            seen[nums[i]]+=1
            if len(seen) == k:
                res = max(res,sum)
        return res