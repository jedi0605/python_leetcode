from bisect import bisect_left
import collections
import random
from typing import List

"""_summary_
LeetCode 400 Nth Digit

#Leetcode150
Time:O(n^2)
Space:O(n)
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = base = 1  # starting from 1 digit

        while n > 9 * base * digit:  # upper limit of d digits
            n -= 9 * base * digit
            digit += 1
            base *= 10
        # q, r = divmod(n - 1, digit)
        
        q = (n - 1) // digit
        r = (n - 1) % digit
        return int(str(base + q)[r])
