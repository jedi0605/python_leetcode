"""_summary_
Leetcode 46. Permutations
Backtracking recursive
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtracking( combine):
            if len(nums) == len(combine):
                res.append(combine.copy())
            else:
                for i in nums:
                    if i not in visited:
                        visited.add(i)
                        combine.append(i)
                        backtracking(combine)
                        visited.remove(i)
                        combine.pop()

        backtracking([])
        return res
