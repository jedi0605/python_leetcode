from typing import List

"""_summary_
Using two maps to track word exist or not
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sArr = s.split()
        if len( sArr) != len( pattern):
            return False
                
        patternToS = {}
        sToPattern = {}
        for i in range(len(pattern)):
            if (pattern[i] in patternToS and patternToS[pattern[i]] != sArr[i]) or (
                sArr[i] in sToPattern and sToPattern[sArr[i]] != pattern[i]
            ):
                return False
            patternToS[pattern[i]] = sArr[i]
            sToPattern[sArr[i]] = pattern[i]

        return True
