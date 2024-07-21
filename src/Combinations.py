"""_summary_
Leetcode 77. Combinations
Backtracking recursive
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(start: int, comb: List[int]):
            if k == len(comb):
                res.append(comb.copy())
            else:
                for i in range(start, n + 1):
                    comb.append(i)
                    backtracking(i + 1, comb)
                    comb.pop()

        backtracking(1, [])
        return res
