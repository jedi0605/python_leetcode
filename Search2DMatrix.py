"""_summary
74. Search a 2D Matrix
#Leetcode150
Time:O(log(m*n))
Space:O(1)
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find which Raws

        def searchRow(low, height):
            while low <= height:
                m = (low + height) // 2
                if matrix[m][0] <= target and matrix[m][-1] >= target:
                    return m
                if matrix[m][0] > target:
                    height = m - 1
                else:
                    low = m + 1
            return -1

        def searchCol(left, right, r):
            while left <= right:
                m = (left + right) // 2
                if matrix[r][m] == target:
                    return m
                if matrix[r][m] > target:
                    right = m - 1
                else:
                    left = m + 1
            return -1

        r = searchRow(0, len(matrix) - 1)
        if r == -1:
            return False
        c = searchCol(0, len(matrix[0]) - 1, r)
        return True if c != -1 else False
