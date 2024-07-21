from typing import List


class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            a = nums.pop()
            nums.insert(0, a)

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k% len(nums)
        # reverse all
        nums.reverse()
        #
        self.reverse_subarray(nums, 0, k - 1)
        self.reverse_subarray(nums, k, len(nums) - 1)

    def reverse_subarray(sefl, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
