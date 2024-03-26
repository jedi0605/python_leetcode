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

        def backtracking(openN, closeN):
            if closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtracking(openN, closeN + 1)
                stack.pop()

        backtracking(0, 0)
        return res
