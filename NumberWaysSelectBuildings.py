"""_summary
Leetcode 2222. Number of Ways to Select Buildings
DP problem
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional


class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = {"1": 0, "10": 0, "101": 0, "0": 0, "01": 0, "010": 0}

        for c in s:
            if c == '0':
                dp["0"] += 1
                dp["01"] += dp["1"]
                dp["010"] += dp["10"]
            else:
                dp["1"] += 1
                dp["10"] += dp["0"]
                dp["101"] += dp["01"]
        return dp["101"] + dp["010"]
