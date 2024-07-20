"""_summary
Leetcode 1481. Least Number of Unique Integers after K Removals
DFS search
#Leetcode150
Time:O(n)
Space:O(1)
"""

from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)

        cnt_val = sorted(cnt.values())
        k_count = 0
        print(cnt_val)
        for i in range(len(cnt_val)):
            k_count += cnt_val[i]
            if k_count > k:
                return len(cnt_val) - i
        return 0
