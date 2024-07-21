from typing import List

"""_summary_
Using two maps to track word exist or not
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            sMap[t[i]] = sMap.get(t[i], 0) - 1
        
        for key, value in sMap.items():
            if value != 0:
                return False
        return True
