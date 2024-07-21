"""_summary
2422. Merge Operations to Turn Array Into a Palindrome
"""

from heapq import heappop, heappush
from typing import List
from TreeNode import TreeNode


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        lP, rP = 0, len(nums) - 1
        res = 0
        while lP <= rP:
            if nums[rP] == nums[lP]:
                rP -= 1
                lP += 1
            else:
                if nums[rP] > nums[lP]:
                    nums[lP + 1] += nums[lP]
                    lP += 1
                    res+=1
                else:
                    nums[rP - 1] += nums[rP]
                    rP -= 1
                    res+=1
        return res
