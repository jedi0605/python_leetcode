from collections import defaultdict
import collections
from typing import List


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:

        def helperCount(vals):
            n = len(vals)
            take = [1] * n
            notake = [1] * n
            for i in range(1, n):
                if vals[i] - k == vals[i - 1]:  # not take sequence k nums
                    take[i] = notake[i - 1]
                    notake[i] = take[i - 1] + notake[i - 1]
                else:
                    take[i] = take[i - 1] + notake[i - 1]
                    notake[i] = take[i - 1] + notake[i - 1]
            return take[n - 1] + notake[n - 1]

        maps = defaultdict(list)
        for n in nums:
            maps[n % k].append(n)
        res = 1
        for bucket in maps.values():
            res *= helperCount(sorted(bucket))
        return res