"""_summary
2486. Append Characters to String to Make Subsequence
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque, defaultdict
from typing import List, Optional

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return len(t) - j