from typing import List


"""_summary_
Leetcode 452. Minimum Number of Arrows to Burst Balloons
Leetcode - 150
#Intervals
#Sort Array.
O(nlogn)
O(1)
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda i: i[0])  # sort by first element
        pre = points[0]
        total = 1
        for s, e in points[1:]:
            if s > pre[1]:  # not overlapping
                total += 1
                pre = [s,e]
            else:
                # pre[0] = max(s,pre[0]) # don't need update the left side. cuz already sorted
                pre[1] = min(e, pre[1])
        return total