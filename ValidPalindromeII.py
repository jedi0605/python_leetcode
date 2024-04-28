from collections import Counter, defaultdict, deque
from typing import List, Optional

from TreeNode import TreeNode

"""_summary_
LeetCode 680. Valid Palindrome II
T: O(N)
S: O(1)
#Meta Tag #TwoPointer
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                cutL = s[l + 1 : r + 1]
                cutR = s[l:r]
                return cutL == cutL[::-1] or cutR == cutR[::-1]
            l += 1
            r -= 1
        return True
