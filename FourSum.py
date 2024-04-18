from typing import List

"""_summary_
Leetcode 18. 4Sum
Returns:
    _type_: _description_
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res, tmp = [], []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    tmp.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    tmp.pop()
                return
            # base case -> TwoSumII
            l, r = start, len(nums) - 1
            while l < r:
                if (nums[l] + nums[r]) < target:
                    l += 1
                elif (nums[l] + nums[r]) > target:
                    r -= 1
                else:
                    res.append(tmp + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        kSum(4, 0, target)
        return res
