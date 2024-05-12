from collections import Counter, defaultdict
import collections
from typing import List

"""_summary
LeetCode 2597. The Number of Beautiful Subsets
DFS , BFS can do in O(n) time.
IF want to less than O(n)
Find sub complete binary tree and using 2^n - 1
#Leetcode150
Time:O(n)
Space:O(n)
"""


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        nums.sort()
        
        def backtracking(i: int):
            if i == len(nums):
                return 1
            res = backtracking(i + 1)
            if nums[i] - k not in freq:
                freq[nums[i]] += 1
                res += backtracking(i + 1)
                print(freq)
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            return res

        return backtracking(0) - 1
