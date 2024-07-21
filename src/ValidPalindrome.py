from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        ## newStr[::-1] will revece string
        return newStr == newStr[::-1]

    def isPalindrome2(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l].isalnum() != True:
                l += 1

            while r > l and s[r].isalnum() != True:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
