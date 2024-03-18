import unittest
from CourseSchedule import Solution


class CourseSchedule_test(unittest.TestCase):
    def test_case1(self):
        numCourses = 6
        prerequisites = [[4, 0], [4, 1], [3, 1], [3, 2], [5, 4], [5, 3]]
        sol = Solution()
        assert sol.canFinish(numCourses,prerequisites)


if __name__ == "__main__":
    unittest.main()
