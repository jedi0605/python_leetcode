"""_summary
2519. Count the Number of K-Big Indices
"""

from heapq import heappop, heappush
from typing import List
from TreeNode import TreeNode


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        res = 0
        maxHeap = []
        validCon1 = [False] * len(nums)
        # condition1
        for i, n in enumerate(nums):
            if len(maxHeap) == k and -maxHeap[0] < n:
                validCon1[i] = True
            heappush(maxHeap, -n)
            if len(maxHeap) > k:
                heappop(maxHeap)

        # condition2
        maxHeap = []
        for i, n in reversed(list(enumerate(nums))):
            if len(maxHeap) == k and -maxHeap[0] < n and validCon1[i]:
                res += 1
            heappush(maxHeap, -n)
            if len(maxHeap) > k:
                heappop(maxHeap)
        return res
