"""_summary_
2268. Minimum Number of Keypresses
#Leetcode150
"""

from collections import Counter
from typing import List


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        d = Counter(s)
        ans = 0
        # sort by value, hight freq nums should be first char of key
        afterSort = sorted(d.values())
        for i, n in enumerate(afterSort[::-1]):
            if i < 9:
                ans += n
            elif i < 18:
                ans += n * 2
            else:
                ans += n * 3
        return ans