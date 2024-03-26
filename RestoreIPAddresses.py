"""_summary
93. Restore IP Addresses
1. Brute force
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def works(self, s) -> bool:
        # s == str(int(s)) -> make no 0 in begin except 0,
        if s == "":
            return False
        return s == str(int(s)) and int(s) <= 255

    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        if len(s) > 12:
            return res

        def backtracking(i, dots, curIp):
            if dots == 4 and i == len(s):
                res.append(curIp[:-1])
                return
            if dots >4:
                return 
            # in case out of range
            for j in range(i, min(i + 3, len(s))):
                if self.works(s[i : j + 1]):  # int(s[i : j + 1]) < 255:
                    backtracking(j + 1, dots + 1, curIp + s[i : j + 1] + ".")

        backtracking(0, 0, "")
        return res
        # n = len(s)
        # res = []

        # for i in range(1, 4):
        #     for j in range(i + 1, i + 4):
        #         for k in range(j + 1, j + 4):
        #             a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
        #             if (
        #                 self.works(a)
        #                 and self.works(b)
        #                 and self.works(c)
        #                 and self.works(d)
        #             ):
        #                 print(f"{a}.{b}.{c}.{d}")
        #                 res.append(f"{a}.{b}.{c}.{d}")
        # return res
