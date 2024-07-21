import unittest
from FindPeakElement import Solution
from TreeNode import TreeNode


class FindPeakElement_test(unittest.TestCase):
    def test_case1(self):
        
        solution = Solution()
        nums = [1,2,1,3,5,6,4]
        assert solution.findPeakElement(nums) == 5


if __name__ == "__main__":
    unittest.main()
