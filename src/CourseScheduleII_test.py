import unittest
from CourseScheduleII import Solution


class CourseSchedule_test(unittest.TestCase):
    def test_case1(self):
        numCourse = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        sol = Solution()
        res = sol.findOrder(numCourse, prerequisites)
        ans = [0, 2, 1, 3]
        ans2 = [0, 1, 2, 3]
        assert res == ans or res == ans2


if __name__ == "__main__":
    unittest.main()
