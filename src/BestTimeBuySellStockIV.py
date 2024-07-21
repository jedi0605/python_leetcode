from bisect import bisect_left
import math
from typing import List

"""_summary_
188. Best Time to Buy and Sell Stock IV
#Leetcode150
Time:O(n)
Space:O(1)
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        sold = [float("-inf")] * (k + 1)
        hold = [float("-inf")] * (k + 1)
        sold[0] = 0
        hold[0] = 0
        for p in prices:
            sold_tmp = sold[:]
            hold_tmp = hold[:]
            for ktimes in range(1, k + 1):
                sold[ktimes] = max(sold_tmp[ktimes], hold_tmp[ktimes] + p)
                hold[ktimes] = max(hold_tmp[ktimes], sold_tmp[ktimes - 1] - p)   
        return max(sold)
