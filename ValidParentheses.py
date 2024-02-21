"""_summary_
Leetcode 20. Valid Parentheses
#Leetcode150

Time:O(n)
Space:O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in closeToOpen:
                if stack.count != 0 and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        