import unittest
from MinimumNumberOfArrowsToBurstBalloons import Solution


class test_MinimumNumberOfArrowsToBurstBalloons(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [[10,16],[2,8],[1,6],[7,12]]
        assert solution.findMinArrowShots(nums) == 2

if __name__ == "__main__":
    unittest.main()
