class Solution(object):        
    def majorityElement2(self, nums):
        # Initialize count and majority candidate
        count = 0
        majority = 0

        # Traverse through the list
        for i in range(len(nums)):
            if count == 0 and majority != nums[i]:
                # If count is 0 and majority candidate is different from current element,
                # update the majority candidate and set count to 1
                majority = nums[i]
                count += 1
            elif majority == nums[i]:
                # If current element is the same as the majority candidate,
                # increment the count
                count += 1
            else:
                # If current element is different from the majority candidate,
                # decrement the count
                count -= 1

        return majority    