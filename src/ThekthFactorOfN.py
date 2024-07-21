"""_summary
Leetcode 1492. The kth Factor of n

#AMZ
Time: N^2 * logN
Space:O(n)
"""

from typing import List, Optional
from ListNode import ListNode

class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        return -1
