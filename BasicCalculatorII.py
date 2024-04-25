import math
from typing import List

"""_summary_
Leetcode 227. Basic Calculator II
Returns:
    _type_: _description_
"""


class Solution:
    def calculate(self, s: str) -> int:
        arr = []
        nums = 0
        preSign = "+"
        for c in s + "+":
            if c.isdigit():
                nums = nums * 10 + int(c)
            elif c in "+-*/":

                if preSign == "+":
                    arr.append(nums)
                elif preSign == "-":
                    arr.append(-nums)
                elif preSign == "*":
                    arr.append(arr.pop() * nums)
                elif preSign == "/":
                    arr.append(math.trunc(arr.pop() / nums))
                preSign = c
                nums = 0
        print(arr)
        return sum(arr)
