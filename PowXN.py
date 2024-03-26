"""_summary
50. Pow(x, n)
Divid
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, times):
            if x == 0:
                return 0
            if times == 0:
                return 1

            # take care power of odd
            # x * x^2 * x^2
            res = helper(x, times // 2)
            res = res * res
            return res if times % 2 == 0 else res * x

        times = abs(n)
        res = helper(x, times)
        return res if n > 0 else 1 / res
