import unittest
from CounttheNumberKFreeSubsets import Solution


class CourseSchedule_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        nums = [483,482,486,481,485]
        k = 2
        assert sol.countTheNumOfKFreeSubsets(nums, k) == 20


if __name__ == "__main__":
    unittest.main()
