from collections import Counter, defaultdict, deque
from typing import List
import math

"""_summary_
LeetCode 875. Koko Eating Bananas
T: O (n * max(pile))# brute force. O(n* log(maxPiles))
S: O(1)
#Meta Tag
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_work(k):
            hour = 0
            for p in piles:
                hour += math.ceil(p / k)
            return hour<=h
                
        l = 1
        r = max(piles)
        # 1 2 3 4 5 6 7 8 9 10 11
        while l < r:
            k = (l + r) // 2  # one time eat number
            
            if k_work(k):
                r = k
            else:
                l = k + 1
        return r

        # brute force
        # speed = 1
        # while True:
        #     hourSpend = 0
        #     for p in piles:
        #         hourSpend += math.ceil(p / speed)
        #     if hourSpend <= h:
        #         return speed
        #     else:
        #         speed+=1
