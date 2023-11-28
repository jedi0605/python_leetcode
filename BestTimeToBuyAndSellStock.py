from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # using two pointer
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
