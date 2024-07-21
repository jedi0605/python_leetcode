"""_summary
322. Coin Change
#Leetcode150
Time:O(n^2)
Space:O(1)
"""

import collections
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[0] means how many choises can make amount '0'
        # so dp size will be amount+1(include0)
        # check every coins. 
        dp = [amount + 1] * (amount + 1)  # include 0
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:  # choise coin
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
