from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) == i or str[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
