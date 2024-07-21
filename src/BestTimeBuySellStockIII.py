from bisect import bisect_left
import math
from typing import List

"""_summary_
123. Best Time to Buy and Sell Stock III
#Leetcode150
Time:O(n)
Space:O(1)

hold1[k]:max(0-price[k], hold1[k-1])
sold1[k]:max(hold1[k-1]+p, sold1[k-1])
hold2[k]:max(sold1[k-1]-p, hold2[k-1])
sold2[k]:max(hold2[k-1]+p,sold2[k-1])
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy1, buy2 = float("inf"), float("inf")
        sell1, sell2 = 0, 0
        for p in prices:
            # update buy1
            buy1 = min(buy1, p)
            sell1 = max(p - buy1, sell1)
            # update buy2
            buy2 = min(p - sell1, buy2)
            sell2 = max(p - buy2, sell2)
            print(f"{buy1},{sell1} = {buy2},{sell2}")
        return sell2
