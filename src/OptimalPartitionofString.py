"""_summary
Leetcode 2405. Optimal Partition of String

#AMZ
Time: O(n)
Space:O(n)
"""

from typing import List, Optional
from ListNode import ListNode


class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        res = 1
        for c in s:
            if c in seen:
                res += 1
                seen = set()            
            seen.add(c)
        return res
