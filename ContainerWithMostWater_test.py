import unittest
from ContainerWithMostWater import Solution


class test_TwoSumII(unittest.TestCase):
    def test_case1(self):
        height = [1,8,6,2,5,4,8,3,7]        
        solution = Solution()
        assert solution.maxArea(height) == 49
        


if __name__ == "__main__":
    unittest.main()
