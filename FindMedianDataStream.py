"""_summary
373. Find K Pairs with Smallest Sums
#Leetcode150
Time:O(log(m*n))
Space:O(1)
"""

import heapq
from typing import List


class MedianFinder:

    def __init__(self):
        # two heaps, largeGroup-> minHeap, smallGroup->maxHeap
        # heaps should be same size
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # default push to minHeap
        heapq.heappush(self.minHeap, -1 * num)
        # make sure every num minHeap is <= num in maxHeap
        if self.minHeap and self.maxHeap and ((-1 * self.minHeap[0] )> self.maxHeap[0]):
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)

        # uneven size
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * val)

    def findMedian(self) -> float:
        # odd
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        else:
            return (self.minHeap[0] + self.maxHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
