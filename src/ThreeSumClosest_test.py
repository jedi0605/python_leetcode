import unittest
from ThreeSumClosest import Solution


class ThreeSumClosest_test(unittest.TestCase):
    def test_case1(self):
        nums = [-1,2,1,-4]
        target = 1
        sol = Solution()
        assert sol.threeSumClosest(nums,target) == 2


if __name__ == "__main__":
    unittest.main()
