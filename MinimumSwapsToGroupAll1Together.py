"""_summary
1151. Minimum Swaps to Group All 1's Together
"""

from typing import List
from TreeNode import TreeNode


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        totalOne = data.count(1)  # size of sliding window
        ans = curZero = data[:totalOne].count(0)  # init ans

        for i in range(totalOne, len(data)):
            if data[i] == 0:
                curZero += 1
            if data[i - totalOne] == 0:
                curZero -= 1
            ans = min(ans, curZero)
        return ans
