"""_summary
2340. Minimum Adjacent Swaps to Make a Valid Array
"""

import math
from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        large, small, large_idx, small_idx = -math.inf, math.inf, 0, 0
        for i, n in enumerate(nums):
            if n < small:
                small = n
                small_idx = i
            if n >= large:
                large = n
                large_idx = i
        res = small_idx + (len(nums) - 1 - large_idx)
        # edge case: if small_idx > large_idx, it can save 1 swap
        return res-1 if large_idx < small_idx else res