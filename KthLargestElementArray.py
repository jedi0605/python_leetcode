from collections import defaultdict
import collections
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # in python only have min heap.
        # base on this idea. put k nums in to the heap
        # if nums > heap[0]. pop heap, push nums into the heap        
        for n in nums:
            if len(heap)<k:
                heapq.heappush(heap,n)
            else:
                if n > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,n)
        return heap[0]
    # T: N * logK, k is size of heap
    # S: O (K)
    # also have quick select. But T: O(N) -> O(N^2), S:O(1)
