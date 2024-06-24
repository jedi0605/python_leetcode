from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res
        # add DP version
        # using dp?
        # traking Max of left
        # traking Max of right
        # maxL = [0] * len(height)
        # maxR = [0] * len(height)
        # for i in range(1, len(height)):
        #     maxL[i] = max(maxL[i - 1], height[i - 1])
        # for i in range(len(height) - 2, -1, -1):
        #     maxR[i] = max(maxR[i + 1], height[i + 1])
        # res = 0
        # for i in range(len(height)):
        #     trap = min(maxL[i], maxR[i]) - height[i]
        #     res += trap if trap > 0 else 0
        # return res