"""_summary
69. Sqrt(x)
#Leetcode150
Time:O(logn)
Space:O(1)
"""

from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return X
        left, right = 2, x // 2

        while left <= right:
            mid = (left + right) // 2
            nums = mid * mid
            if nums > x:
                right = mid - 1
            elif nums < x:
                left = mid + 1
            else:
                return mid
        return right

