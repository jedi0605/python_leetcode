"""_summary_
Leetcode 150. Evaluate Reverse Polish Notation
Using stack.
1. for each tokens 
    if token is operator -> pop*2 (val_1, val_2) to calculate -> add result to task
        *careful val_2 - val_1 or val_2 // val_1
        * truncates toward zero -> int(val_2/val1)
    else stack.app(val)
#Leetcode150
Time:O(1)
Space:O(1)
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack.pop()

    def operation(self, operator: str, val_1: int, val_2: int) -> int:
        if operator == "+":
            return val_2 + val_1
        elif operator == "-":
            return val_2 - val_1
        elif operator == "*":
            return val_2 * val_1
        else:
            return val_2 // val_1
