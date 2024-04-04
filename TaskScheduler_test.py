import unittest
from TaskScheduler import Solution


class TaskScheduler_test(unittest.TestCase):
    def test_case1(self):
        tasks = ["A","A","A","B","B","B"]
        n = 2

        solution = Solution()
        assert solution.leastInterval(tasks,n) == 8


if __name__ == "__main__":
    unittest.main()
