from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # V1
        # sets = set(nums)
        # longest = 0
        # for i in nums:
        #     # check is n is the start a seq
        #     if (i - 1) not in sets:
        #         length = 0
        #         while (i + length) in sets:
        #             length += 1
        #         longest = max(length, longest)
        # return longest
        
        # V2
        if len(nums) == 0:
            return 0
        numsSet = set(nums)
        longest = 1

        for n in numsSet:
            if n - 1 not in numsSet:
                length = 1

                while n+length in numsSet:
                    length += 1
                longest = max(length,longest)
        return longest
