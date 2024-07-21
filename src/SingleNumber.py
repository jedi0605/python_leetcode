"""_summary
136. Single Number
#Leetcode150
Time:O(n)
Space:O(1)
"""

import heapq
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # numsSet = set(nums)
        # return 2 * sum(numsSet) - sum(nums)
        a = 0
        for i in nums:
            a = a ^ i
        return a
