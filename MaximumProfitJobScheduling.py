"""_summary_
1235. Maximum Profit in Job Scheduling
#Leetcode150
Time:O(n logn)
Space:O(n)
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:

        jobs2 = sorted(zip(startTime, endTime, profit))
        print(jobs2)
        heap = []
        max_profit = 0
        for s, e, p in jobs2:
            while heap and heap[0][0] <= s:
                endTime, profit = heappop(heap)
                max_profit = max(max_profit, profit)
            heappush(heap, (e, max_profit + p))
        for _, p in heap:
            max_profit = max(max_profit, p)
        return max_profit
