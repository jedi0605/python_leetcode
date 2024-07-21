import unittest
from TrappingRainWater import Solution


class test_TrappingRainWater(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        res = solution.trap(height)
        assert res == 6

    def test_case2(self):
        solution = Solution()
        height = [4, 2, 0, 3, 2, 5]
        res = solution.trap(height)
        assert res == 9


if __name__ == "__main__":
    unittest.main()
