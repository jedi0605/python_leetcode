import unittest
from CountSubstringsStartingEndingGivenCharacter import Solution


class CourseSchedule_test(unittest.TestCase):
    def test_case1(self):
        s = "abada"
        c = "a"
        sol = Solution()

        assert sol.countSubstrings(s,c) == 6


if __name__ == "__main__":
    unittest.main()
