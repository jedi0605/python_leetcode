from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        maps = {}

        for i in range(len(nums)):
            if nums[i] in maps:
                if abs(maps[nums[i]] - i) <= k:
                    return True
                else:
                    maps[nums[i]] = i
            else:
                maps[nums[i]] = i
        return False
