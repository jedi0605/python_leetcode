from typing import List

"""_summary_
LeetCode 494. Target Sum
T: O(n * t) # t = sum(nums), n = len(nums)
S: O(1)
#Meta Tag
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.res = 0
        dic = {}

        def backtracking(idx, curr):
            if idx == len(nums):
                return 1 if target == curr else 0
            if (idx, curr) in dic:
                return dic[(idx, curr)]
            dic[(idx, curr)] = backtracking(idx + 1, curr + nums[idx]) + backtracking(
                idx + 1, curr - nums[idx]
            )
            return dic[(idx,curr)]
        backtracking(0, 0)
        return dic[(0,0)]
