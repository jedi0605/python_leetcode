"""_summary_
LeetCode 224. Basic Calculator

#Leetcode150
Time:O(1)
Space:O(1)
"""

from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0  # temp result
        sign = 1  # present current 1 or -1
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+" or c == "-":
                res += num * sign
                num = 0
                if c == "+":
                    sign = 1
                else:
                    sign = -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0  # reset
                sign = 1  # reset
            elif c == ")":  # end of subCalcu
                res += num * sign
                res *= stack.pop()  # prev sign
                res += stack.pop()  # prev res
                num = 0
        return res + num * sign

    # This is easy version of calculate, without
    # def calculate(self, s: str) -> int:
    #     res = 0
    #     num = 0  # temp result
    #     sign = 1  # present current 1 or -1
    #     for c in s:
    #         if c.isdigit():
    #             num = num * 10 + int(c)
    #         if c == "+" or c == "-":
    #             res += num * sign
    #             num = 0
    #             if c == "+":
    #                 sign = 1
    #             else:
    #                 sign = -1

    #     return res + num * sign
