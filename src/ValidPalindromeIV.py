"""_summary
2330. Valid Palindrome IV
"""

import math
from typing import List


class Solution:
    def makePalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        opCount = 0

        while l < r:
            # if opCount > 2:
            #     return False
            if s[l] != s[r]:
                opCount += 1
            l += 1
            r -= 1
        return True if opCount < 3 else False
