import unittest
from CountTheNumberOfKBigIndices import Solution


class CourseSchedule_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        nums = [2, 3, 6, 5, 2, 3]
        k = 2
        assert sol.kBigIndices(nums, k) == 2


if __name__ == "__main__":
    unittest.main()
