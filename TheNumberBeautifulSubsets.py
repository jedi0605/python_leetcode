from collections import Counter, defaultdict
import collections
from typing import List

"""_summary
LeetCode 2597. The Number of Beautiful Subsets
#Leetcode150
Time:O(n)
Space:O(n)
"""


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        illegal = defaultdict(int)
        self.count = 0        

        def backtracking(idx):
            if idx == len(nums):
                self.count += 1
                return

            x = nums[idx]
            if illegal[x] == 0:
                illegal[x - k] += 1
                illegal[x + k] += 1
                backtracking(idx + 1)
                illegal[x - k] -= 1
                illegal[x + k] -= 1
            backtracking(idx + 1)

        backtracking(0)
        return self.count - 1
