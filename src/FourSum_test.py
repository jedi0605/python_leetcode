import unittest
from FourSum import Solution
import TestingTool


class FourSum_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [1,0,-1,0,-2,2]
        target = 0
        res = solution.fourSum(nums,target)
        ans = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        assert TestingTool.compare_lists_of_lists(res,ans)
        

def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
