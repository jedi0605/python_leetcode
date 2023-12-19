from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                res = max(res, r - l + 1)
            charSet.add(s[r])
        res = max(len(charSet), res)
        return res
