from bisect import bisect_left
import math
from typing import List

"""_summary_
5. Longest Palindromic Substring
#Leetcode150
Time:O(n^2)
Space:O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1
        return res
        # brute force
        # def isPalindrome(s:str):
        #     l,r = 0, len(s)-1
        #     while l<=r:
        #         if s[l]!=s[r]:
        #             return False
        #         l+=1
        #         r-=1
        #     return True
        # res = ""
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         subS = s[i:j]
        #         if isPalindrome(subS):
        #             res = subS if len(subS) > len(res) else res
        # return res
