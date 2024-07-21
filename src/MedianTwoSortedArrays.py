"""_summary
4. Median of Two Sorted Arrays
#Leetcode150
Time:O(log(m*n))
Space:O(1)
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minX = float('inf') if partitionX == m else nums1[partitionX]
            minY = float('inf') if partitionY == n else nums2[partitionY]
            
            if maxX <= minY and maxY <= minX:
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1
                
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        m1, m2 = 0, 0  # m2 is tracking for even nums median.

        for _ in range(0, (m + n) // 2 + 1):
            print(m1)
            m2 = m1
            if i < m and j < n:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < m:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1
        if (m + n) % 2 == 1:
            return m1
        else:
            return (m1 + m2) / 2
    # T: O(m+n) S: O(m+n) brute force            
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     m, n = len(nums1), len(nums2)
    #     merge = []
    #     p1, p2 = 0, 0
    #     while p1 < m and p2 < n:
    #         if nums1[p1] > nums2[p2]:
    #             merge.append(nums2[p2])
    #             p2 += 1
    #         else:
    #             merge.append(nums1[p1])
    #             p1 += 1
    #     if p1 != m:
    #         merge = merge + nums1[p1:m]
    #     else:
    #         merge = merge + nums2[p2:n]
        
    #     if  (m + n) % 2 == 1:
    #         return merge[(m+n)//2]
    #     else:        
    #         return (merge[(m+n)//2] + merge[(m+n)//2-1])/2
