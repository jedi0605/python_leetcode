from collections import defaultdict
import collections
import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        maxProfits = []
        minCaptital = []
        for i in range(len(capital)):
            c_tmp, p_tmp = capital[i], profits[i]
            heapq.heappush(minCaptital, (c_tmp, p_tmp))

        for i in range(k):
            # find satisfied capital to maxProfit
            while minCaptital and minCaptital[0][0] <= w:
                c, p = heapq.heappop(minCaptital)
                heapq.heappush(maxProfits, -1 * p)
            if not maxProfits:
                break
            w += -1 * heapq.heappop(maxProfits)
        return w
