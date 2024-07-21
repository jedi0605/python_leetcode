from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        forward = [1] * length
        backward = [1] * length
        for i in range(1, length):
            forward[i] = nums[i - 1] * forward[i - 1]
        for i in range(length - 2, -1, -1):
            backward[i] = nums[i + 1] * backward[i + 1]
        
        res = [1] * length
        for i in range(length):
            res[i] = forward[i] * backward[i]    
        return res
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        length = len(nums)
        forward = [1] * length
        res = [1] * length
        for i in range(1, length):
            forward[i] = nums[i - 1] * forward[i - 1]
        B = 1
        for i in range(length-1,-1,-1):
           res[i] = B * forward[i]
           B = B * nums[i]         
        return res

    def productExceptSelf3(self, nums:List[int])-> List[int]:
        res = [0] * len(nums)
        preProduct = 1
        
        # Populate result array with prefix product
        for i,v in enumerate(nums):
            res[i] = preProduct
            preProduct *= v

        postProduct = 1
        
        # Multiply result array with postfix product
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postProduct
            postProduct *= nums[i]

        return res