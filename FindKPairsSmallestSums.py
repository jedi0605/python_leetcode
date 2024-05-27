"""_summary
373. Find K Pairs with Smallest Sums#Leetcode150
Time:O(log(m*n))
Space:O(1)
"""

import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        res = []
        pq = []

        for i in range(len(nums1)):
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))

        while pq and len(res) < k:
            p, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])
            if j < len(nums2) - 1:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
