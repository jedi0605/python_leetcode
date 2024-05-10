"""_summary_
Leetcode 990. Satisfiability of Equality Equations
# Union find
#Leetcode150
"""

from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = list(range(26))  # parnet
        for i in range(26):
            root[i] = i

        def find(x):
            res = x
            while res != root[x]:
                res = root[res]
            return res

        def union(x, y):
            x, y = find(x), find(y)
            root[x] = y

        for equ in equations:
            if equ[1] == "=":
                x = ord(equ[0]) - ord("a")
                y = ord(equ[3]) - ord("a")
                union(x, y)

        for equ in equations:
            if equ[1] == "!":
                x = ord(equ[0]) - ord("a")
                y = ord(equ[3]) - ord("a")
                if find(x) == find(y):
                    return False
        return True
