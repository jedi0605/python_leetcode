from typing import List

"""_summary_
80. Remove Duplicates from Sorted Array II
#Leetcode150
Time:O(n^2)
Space:O(1)
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if len(nums) < 3:
        #     return len(nums)
        # idx = 2
        # for i in range(2, len(nums)):
        #     print(f"{nums[i]}, {nums[idx - 2]}")
        #     if nums[i] != nums[idx - 2]:
        #         nums[idx] = nums[i]
        #         idx += 1
        # return idx
        
        # Initialize the counter and the array index.
        i, cnt = 1,1
        while i <len(nums):
            if nums[i] == nums[i-1]:
                cnt+=1
                if cnt > 2:
                    nums.pop(i)
                    i-=1
            else:
                cnt=1
            i+=1
        return len(nums)    