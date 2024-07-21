"""_summary
137. Single Number II
#Leetcode150
Time:O(n)
Space:O(1)
"""

import heapq
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            lastBit = 0
            for n in nums:
                lastBit += (n >> i) & 1
            lastBit %= 3
            res = res | (lastBit << i)
        if res >= (1 << 31):  # if res > 2^32. res is nagetive
            res = res - (1 << 32)
        return res
