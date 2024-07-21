"""_summary
191. Number of 1 Bits
#Leetcode150
Time:O(log(m*n))
Space:O(1)
"""

from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        # count = 0
        # while n > 0:
        #     if n % 2:
        #         count += 1
        #     n = n // 2
        # return count
        res = 0
        while n > 0:
            if n & 1 == 1:  # last bit is 1
                res += 1
            n >>= 1  # n right shift one bit
        return res
