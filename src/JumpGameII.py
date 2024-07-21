from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        step = 0
        while r < len(nums) - 1:
            farset = 0
            for i in range(l, r + 1):
                farset = max(nums[i] + i, farset)

            l = r + 1
            r = farset
            step += 1
        return step
