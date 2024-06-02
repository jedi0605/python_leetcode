"""_summary
149. Max Points on a Line
#Leetcode150
Time:O(n^2)
Space:O(1)
"""

import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 1
        for i in range(n):
            pointA = points[i]
            maps = collections.defaultdict(int)
            for j in range(n):
                if i == j:
                    continue
                pointB = points[j]
                slope = 0
                if pointA[0] == pointB[0]:
                    slope = float("inf")
                else:
                    slope = (pointB[1] - pointA[1]) / (pointB[0] - pointA[0])
                maps[slope] += 1
                res = max(res, maps[slope] + 1)  # cause 1 slope have 2 points. if have 2 slope, means 3 points
        return res
