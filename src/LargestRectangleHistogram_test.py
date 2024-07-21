import unittest
from LargestRectangleHistogram import Solution


class LargestRectangleHistogram_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        heights = [2,1,5,6,2,3]
        assert solution.largestRectangleArea2(heights) == 10


if __name__ == "__main__":
    unittest.main()
