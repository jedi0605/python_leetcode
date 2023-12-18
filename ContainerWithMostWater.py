from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxA = 0
        while l < r:
            tmp = (r - l) * min(height[l], height[r])
            maxA = max(maxA, tmp)
            if(l<r):
                l+=1
            else:
                r-=1
                
        return maxA