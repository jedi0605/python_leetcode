import random
from typing import List

"""_summary_
LeetCode 1428. Leftmost Column with at Least a One 
#Meta Tag
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        r, c = binaryMatrix.dimensions()
        minCol = float("inf")
        for i in range(r):
            left = 0
            right = c - 1
            while left<=right:
                mid = (left+right)//2
                if binaryMatrix.get(i, mid) == 1:
                    minCol = min(minCol,mid)
                    right = mid -1
                else:
                    left = mid+1

        return minCol if minCol != float("inf") else -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
