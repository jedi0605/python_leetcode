"""_summary_
Leetcode 22. Generate Parentheses
Try all index i combination, and move to i+1
Backtracking recursive
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []

        def backtracking(openN, closeN, cur):
            if closeN == n:
                res.append("".join(cur))
            if openN < n:
                cur.append("(")
                backtracking(openN + 1, closeN, cur)
                cur.pop()
            if openN > closeN:
                cur.append(")")
                backtracking(openN, closeN + 1, cur)
                cur.pop()

        backtracking(0, 0, stack)
        return res
