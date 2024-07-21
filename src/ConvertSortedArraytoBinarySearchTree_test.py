import unittest
from ConvertSortedArraytoBinarySearchTree import Solution
from TreeNode import TreeNode


class ConvertSortedArraytoBinarySearchTree_test(unittest.TestCase):
    def test_case1(self):
        nums = [-10,-3,0,5,9]
        
        solution = Solution()        
        solution.sortedArrayToBST(nums)
        

if __name__ == "__main__":
    unittest.main()
