import unittest
from TaskScheduler import Solution


class TaskScheduler_test(unittest.TestCase):
    def test_case1(self):
        tasks = ["A","A","A","B","B","B"]
        n = 2
        solution = Solution()
        assert solution.leastInterval(tasks,n) == 8
        
    def test_case2(self):
        tasks=["A","C","A","B","D","B"]
        n = 1
        solution = Solution()
        solution.leastInterval(tasks,n)


if __name__ == "__main__":
    unittest.main()
