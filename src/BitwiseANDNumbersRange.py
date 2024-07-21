"""_summary
201. Bitwise AND of Numbers Range
#Leetcode150
Time:O(n)
Space:O(1)
"""

import heapq
from typing import List


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 7 | 0111 
        # 8 | 1000
        # 9 | 1001
        #10 | 1010
        #left 7, right 10 => 0
        #left 9, right 10 => 8        
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        return left << i
