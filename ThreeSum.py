from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tmpTarget = 0 - nums[i]

            ## twoSumRes = twoSum(i + 1, len(nums) - 1, nums, tmpTarget)
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == tmpTarget:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                if nums[l] + nums[r] > tmpTarget:
                    r -= 1
                else:
                    l += 1
        return res
