from typing import List

"""_summary_
LeetCode 560. Subarray Sum Equals K
Using Maps to count prefix sum.
#Meta Tag
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        maps = {}
        maps[0] = 1

        cur = 0
        for n in nums:
            cur += n
            diff = cur - k

            res += maps.get(diff, 0)
            maps[cur] = 1 + maps.get(cur, 0)
        return res