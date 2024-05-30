"""_summary
190. Reverse Bits
#Leetcode150
Time:O(log(m*n))
Space:O(1)
"""

import heapq
from typing import List


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res *= 2
            res += n % 2
            n = n // 2
        return res
