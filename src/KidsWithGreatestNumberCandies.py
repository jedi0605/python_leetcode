"""_summary
1431. Kids With the Greatest Number of Candies
"""

import math
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # brute force, calculate all max candies for each chield
        res = []
        basicMax = max(candies)  # 5
        for c in candies:
            if c + extraCandies >= basicMax:
                res.append(True)
            else:
                res.append(False)
        return res
