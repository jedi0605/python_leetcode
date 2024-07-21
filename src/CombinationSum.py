"""_summary_
Leetcode 39. Combination Sum
Try all index i combination, and move to i+1
Backtracking recursive
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(idx, arr, sum):
            if sum == target:
                res.append(arr.copy())
                return
            if idx >= len(candidates) or sum > target:
                return
            arr.append(candidates[idx])
            backtracking(idx, arr, sum + candidates[idx])
            arr.pop()
            backtracking(idx + 1, arr, sum)  # just move to next idx, so sum not change.

        backtracking(0, [], 0)
        return res

        # res = []
        # resSet = set()
        # def backtracking(combo):
        #     if sum(combo) == target and tuple(sorted(combo)) not in resSet:
        #         res.append(combo.copy())  # Append combo to the result list
        #         resSet.add(tuple(sorted(combo)))  # Add sorted combo to the set
        #         return
        #     elif sum(combo) > target:
        #         return
        #     else:
        #         for i in candidates:
        #             combo.append(i)
        #             backtracking(combo)
        #             combo.pop()

        # backtracking([])
        # return res
