from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i = 0

        # for j in range(len(nums)):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1
        # return i
        i, j = 0, len(nums) - 1
        if j == -1:
            return 0
        while i < j:
            if nums[i] == val:
                while i < j and nums[j] == val:
                    j -= 1
                nums[i] = nums[j]
                j -= 1
                continue
            i += 1
        return i + 1 if nums[i] != val else i
