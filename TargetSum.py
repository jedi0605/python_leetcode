from typing import List

"""_summary_
LeetCode 494. Target Sum
T: O(n * t) # t = sum(nums), n = len(nums)
S: O(1)
#Meta Tag
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cashe = {}

        def backtracking(idx, curr):
            if idx == len(nums):
                return 1 if curr == target else 0
            if (idx, curr) in self.cashe:
                return self.cashe[(idx, curr)]
            pos = backtracking(idx + 1, curr + nums[idx])
            nag = backtracking(idx + 1, curr - nums[idx])
            self.cashe[(idx, curr)] = pos + nag
            return self.cashe[(idx, curr)]
        backtracking(0, 0)
        return self.cashe[(0,0)]

        self.res = 0
        tmp = []

        def backtracking(idx, curr):
            if idx == len(nums) and curr == target:
                self.res += 1
                print(tmp)
                return
            if idx == len(nums):
                return
            tmp.append(nums[idx])
            backtracking(idx + 1, curr + nums[idx])
            tmp.pop()
            tmp.append(-nums[idx])
            backtracking(idx + 1, curr - nums[idx])
            tmp.pop()

        backtracking(0, 0)
        return self.res
        # self.res = 0
        # dic = {}

        # def backtracking(idx, curr):
        #     if idx == len(nums):
        #         return 1 if target == curr else 0
        #     if (idx, curr) in dic:
        #         return dic[(idx, curr)]
        #     dic[(idx, curr)] = backtracking(idx + 1, curr + nums[idx]) + backtracking(
        #         idx + 1, curr - nums[idx]
        #     )
        #     return dic[(idx,curr)]
        # backtracking(0, 0)
        # return dic[(0,0)]
