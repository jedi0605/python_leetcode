import unittest
from MaximumSubarray import Solution


class MaximumSubarray_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        
        assert solution.maxSubArray(nums) == 6
    
if __name__ == "__main__":
    unittest.main()
